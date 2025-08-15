const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');

const db = new sqlite3.Database('./childcare.db');

// Create tables
db.serialize(async () => {
  // Users table
  db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);

  // Parents table
  db.run(`CREATE TABLE IF NOT EXISTS parents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT,
    email TEXT UNIQUE,
    address TEXT,
    relationship_to_child TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);

  // Children table
  db.run(`CREATE TABLE IF NOT EXISTS children (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('M', 'F')),
    parent_id INTEGER,
    photo TEXT,
    medical_info TEXT,
    notes TEXT,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES parents (id)
  )`);

  // Staff table
  db.run(`CREATE TABLE IF NOT EXISTS staff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT,
    email TEXT UNIQUE,
    phone_number TEXT,
    photo TEXT,
    employment_date DATE,
    specialty TEXT,
    shift_hours TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);

  // Attendance table
  db.run(`CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    child_id INTEGER,
    date DATE,
    status TEXT CHECK(status IN ('Present', 'Absent')),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (child_id) REFERENCES children (id)
  )`);

  // Incident reports table
  db.run(`CREATE TABLE IF NOT EXISTS incident_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    child_id INTEGER,
    staff_id INTEGER,
    date DATE,
    description TEXT,
    action_taken TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (child_id) REFERENCES children (id),
    FOREIGN KEY (staff_id) REFERENCES staff (id)
  )`);

  // Classrooms table
  db.run(`CREATE TABLE IF NOT EXISTS classrooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    capacity INTEGER,
    teacher_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES staff (id)
  )`);

  // Create default admin user
  const hashedPassword = await bcrypt.hash('admin123', 10);
  db.run(`INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)`, 
    ['admin', hashedPassword]);

  // Insert sample data
  db.run(`INSERT OR IGNORE INTO parents (first_name, last_name, phone_number, email, address, relationship_to_child) 
          VALUES (?, ?, ?, ?, ?, ?)`,
    ['John', 'Doe', '+1234567890', 'john.doe@email.com', '123 Main St', 'Father']);

  db.run(`INSERT OR IGNORE INTO parents (first_name, last_name, phone_number, email, address, relationship_to_child) 
          VALUES (?, ?, ?, ?, ?, ?)`,
    ['Jane', 'Smith', '+1234567891', 'jane.smith@email.com', '456 Oak Ave', 'Mother']);

  db.run(`INSERT OR IGNORE INTO staff (first_name, last_name, position, email, phone_number, employment_date, specialty, shift_hours) 
          VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
    ['Sarah', 'Johnson', 'Teacher', 'sarah.johnson@childcare.com', '+1234567892', '2023-01-15', 'Early Childhood Education', '8:00 AM - 4:00 PM']);

  console.log('Database initialized successfully!');
});

db.close();