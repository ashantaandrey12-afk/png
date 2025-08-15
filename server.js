const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const session = require('express-session');
const multer = require('multer');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Database setup
const db = new sqlite3.Database('./childcare.db');

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static('public'));
app.use('/uploads', express.static('uploads'));

// Session configuration
app.use(session({
  secret: 'childcare-secret-key',
  resave: false,
  saveUninitialized: false,
  cookie: { secure: false, maxAge: 24 * 60 * 60 * 1000 } // 24 hours
}));

// Set view engine
app.set('view engine', 'ejs');
app.set('views', './views');

// File upload configuration
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + '-' + file.originalname)
  }
});
const upload = multer({ storage: storage });

// Authentication middleware
const requireAuth = (req, res, next) => {
  if (req.session.userId) {
    next();
  } else {
    res.redirect('/login');
  }
};

// Routes
app.get('/', (req, res) => {
  res.render('home', { user: req.session.user });
});

app.get('/login', (req, res) => {
  res.render('login', { error: null });
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  db.get('SELECT * FROM users WHERE username = ?', [username], async (err, user) => {
    if (err) {
      return res.render('login', { error: 'Database error' });
    }
    
    if (!user || !await bcrypt.compare(password, user.password)) {
      return res.render('login', { error: 'Invalid credentials' });
    }
    
    req.session.userId = user.id;
    req.session.user = { id: user.id, username: user.username };
    res.redirect('/dashboard');
  });
});

app.get('/signup', (req, res) => {
  res.render('signup', { error: null });
});

app.post('/signup', async (req, res) => {
  const { username, password, confirmPassword } = req.body;
  
  if (password !== confirmPassword) {
    return res.render('signup', { error: 'Passwords do not match' });
  }
  
  const hashedPassword = await bcrypt.hash(password, 10);
  
  db.run('INSERT INTO users (username, password) VALUES (?, ?)', 
    [username, hashedPassword], function(err) {
    if (err) {
      return res.render('signup', { error: 'Username already exists' });
    }
    
    req.session.userId = this.lastID;
    req.session.user = { id: this.lastID, username: username };
    res.redirect('/dashboard');
  });
});

app.post('/logout', (req, res) => {
  req.session.destroy();
  res.redirect('/');
});

app.get('/dashboard', requireAuth, (req, res) => {
  // Get counts for dashboard
  const queries = {
    children: 'SELECT COUNT(*) as count FROM children',
    staff: 'SELECT COUNT(*) as count FROM staff',
    attendance: 'SELECT COUNT(*) as count FROM attendance',
    incidents: 'SELECT COUNT(*) as count FROM incident_reports'
  };
  
  const counts = {};
  let completed = 0;
  
  Object.keys(queries).forEach(key => {
    db.get(queries[key], (err, row) => {
      if (!err) counts[key] = row.count;
      completed++;
      
      if (completed === Object.keys(queries).length) {
        res.render('dashboard', { 
          user: req.session.user,
          counts: counts
        });
      }
    });
  });
});

// Children routes
app.get('/children', requireAuth, (req, res) => {
  db.all(`SELECT c.*, p.first_name as parent_first_name, p.last_name as parent_last_name 
          FROM children c 
          LEFT JOIN parents p ON c.parent_id = p.id`, (err, children) => {
    if (err) {
      return res.status(500).send('Database error');
    }
    res.render('children/list', { children, user: req.session.user });
  });
});

app.get('/children/add', requireAuth, (req, res) => {
  db.all('SELECT * FROM parents', (err, parents) => {
    res.render('children/add', { parents, user: req.session.user });
  });
});

app.post('/children/add', requireAuth, upload.single('photo'), (req, res) => {
  const { first_name, last_name, date_of_birth, gender, parent_id, medical_info, notes } = req.body;
  const photo = req.file ? req.file.filename : null;
  
  db.run(`INSERT INTO children (first_name, last_name, date_of_birth, gender, parent_id, photo, medical_info, notes) 
          VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
    [first_name, last_name, date_of_birth, gender, parent_id, photo, medical_info, notes],
    function(err) {
      if (err) {
        return res.status(500).send('Database error');
      }
      res.redirect('/children');
    });
});

app.get('/children/edit/:id', requireAuth, (req, res) => {
  const childId = req.params.id;
  
  db.get('SELECT * FROM children WHERE id = ?', [childId], (err, child) => {
    if (err || !child) {
      return res.status(404).send('Child not found');
    }
    
    db.all('SELECT * FROM parents', (err, parents) => {
      res.render('children/edit', { child, parents, user: req.session.user });
    });
  });
});

app.post('/children/edit/:id', requireAuth, upload.single('photo'), (req, res) => {
  const childId = req.params.id;
  const { first_name, last_name, date_of_birth, gender, parent_id, medical_info, notes } = req.body;
  const photo = req.file ? req.file.filename : null;
  
  let query = `UPDATE children SET first_name = ?, last_name = ?, date_of_birth = ?, 
               gender = ?, parent_id = ?, medical_info = ?, notes = ?`;
  let params = [first_name, last_name, date_of_birth, gender, parent_id, medical_info, notes];
  
  if (photo) {
    query += ', photo = ?';
    params.push(photo);
  }
  
  query += ' WHERE id = ?';
  params.push(childId);
  
  db.run(query, params, function(err) {
    if (err) {
      return res.status(500).send('Database error');
    }
    res.redirect('/children');
  });
});

app.post('/children/delete/:id', requireAuth, (req, res) => {
  const childId = req.params.id;
  
  db.run('DELETE FROM children WHERE id = ?', [childId], function(err) {
    if (err) {
      return res.status(500).send('Database error');
    }
    res.redirect('/children');
  });
});

// Staff routes
app.get('/staff', requireAuth, (req, res) => {
  db.all('SELECT * FROM staff', (err, staff) => {
    if (err) {
      return res.status(500).send('Database error');
    }
    res.render('staff/list', { staff, user: req.session.user });
  });
});

app.get('/staff/add', requireAuth, (req, res) => {
  res.render('staff/add', { user: req.session.user });
});

app.post('/staff/add', requireAuth, upload.single('photo'), (req, res) => {
  const { first_name, last_name, position, email, phone_number, employment_date, specialty, shift_hours } = req.body;
  const photo = req.file ? req.file.filename : null;
  
  db.run(`INSERT INTO staff (first_name, last_name, position, email, phone_number, employment_date, specialty, shift_hours, photo) 
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    [first_name, last_name, position, email, phone_number, employment_date, specialty, shift_hours, photo],
    function(err) {
      if (err) {
        return res.status(500).send('Database error');
      }
      res.redirect('/staff');
    });
});

// Parents routes
app.get('/parents', requireAuth, (req, res) => {
  db.all('SELECT * FROM parents', (err, parents) => {
    if (err) {
      return res.status(500).send('Database error');
    }
    res.render('parents/list', { parents, user: req.session.user });
  });
});

app.get('/parents/add', requireAuth, (req, res) => {
  res.render('parents/add', { user: req.session.user });
});

app.post('/parents/add', requireAuth, (req, res) => {
  const { first_name, last_name, phone_number, email, address, relationship_to_child } = req.body;
  
  db.run(`INSERT INTO parents (first_name, last_name, phone_number, email, address, relationship_to_child) 
          VALUES (?, ?, ?, ?, ?, ?)`,
    [first_name, last_name, phone_number, email, address, relationship_to_child],
    function(err) {
      if (err) {
        return res.status(500).send('Database error');
      }
      res.redirect('/parents');
    });
});

// Attendance routes
app.get('/attendance', requireAuth, (req, res) => {
  db.all(`SELECT a.*, c.first_name, c.last_name 
          FROM attendance a 
          JOIN children c ON a.child_id = c.id 
          ORDER BY a.date DESC`, (err, attendance) => {
    if (err) {
      return res.status(500).send('Database error');
    }
    res.render('attendance/list', { attendance, user: req.session.user });
  });
});

app.get('/attendance/add', requireAuth, (req, res) => {
  db.all('SELECT * FROM children', (err, children) => {
    res.render('attendance/add', { children, user: req.session.user });
  });
});

app.post('/attendance/add', requireAuth, (req, res) => {
  const { child_id, date, status, notes } = req.body;
  
  db.run(`INSERT INTO attendance (child_id, date, status, notes) VALUES (?, ?, ?, ?)`,
    [child_id, date, status, notes],
    function(err) {
      if (err) {
        return res.status(500).send('Database error');
      }
      res.redirect('/attendance');
    });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});