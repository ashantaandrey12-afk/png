# Childcare Management System

## Overview
This is a Django-based childcare management system that allows administrators to manage records for children, staff, and other childcare-related data with full CRUD (Create, Read, Update, Delete) functionality. The system includes user authentication, an appealing homepage, and a dashboard with analytics.

## Features

### Authentication
- Authentication is required to access the dashboard.

### Homepage
- A welcoming and appealing homepage with a description of the project.

### Dashboard
- A centralized interface to manage and view analytics for all modules.
- Responsive design with charts, statistics, and navigation to app-specific CRUD operations.

### Apps
- **Children**: Add, edit, view, and delete child profiles.
- **Staff**: Add, edit, view, and delete staff member profiles.
- **Attendance**: Track and manage attendance records.
- **Classroom**: Manage classroom assignments and details.
- **Incident Report**: Record and review incidents involving children.
- **Parents**: Maintain parent or guardian contact information.
- **Schedule**: Organize and view schedules.

### Additional Features
- User-friendly interface with Bootstrap styling for consistency and responsiveness.
- Profiles for children and staff, including support for adding photos.
- Database integration using PostgreSQL.

## Installation and Setup

### Prerequisites
- Python 3.x
- Django 4.x (or compatible version)
- PostgreSQL
- Git
- Virtual environment tool (recommended)

### Steps to Clone and Run the Project Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/childcare-management-system.git
2. Navigate to the project directory
   ```bash
   cd childcare-management-system
3. Create and activate a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
4. Install required packages
    ```bash
    pip install -r requirements.txt
5.Configure the database
- Update the DATABASES settings in **settings.py** to match your PostgreSQL credentials.
6. Run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
7. Run development server
   ```bash
   python manage.py
8. Access the app
    ```bash
   -Visit http://127.0.0.1:8000/ in your web browser.
   -Log in with your admin credentials to manage children, staff, and other records.

## Future enhancements
- Multi-users login functionality.
- Extend the dashboard to integrate more analytics and interactive data visualization.
- Improve search and filtering options for all apps.
- Add notifications and reminders for schedules and incident reports.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
- This project is licensed under the MIT License.


