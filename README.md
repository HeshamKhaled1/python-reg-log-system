# Python Registration & Login System

A secure and modern user authentication system built with Python and Tkinter for GUI applications.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

A comprehensive user authentication system that provides secure registration and login functionality with a modern graphical interface. The system includes features like password hashing, input validation, and user session management.

## Features

- **User Registration** - Secure account creation with validation
- **User Login** - Authentication with credential verification
- **Password Hashing** - Secure password storage using hashing algorithms
- **Input Validation** - Comprehensive form validation and error handling
- **Session Management** - User session tracking and management
- **Modern GUI** - Clean and intuitive Tkinter interface
- **Database Integration** - SQLite database for user data storage
- **Security Features** - Protection against common vulnerabilities

## Project Structure

```
python-reg-log-system/
├── src/
│   ├── auth_system.py     # Main authentication system class
│   ├── database.py        # Database connection and operations
│   ├── gui.py            # Graphical user interface
│   └── validators.py     # Input validation utilities
├── data/
│   └── users.db          # SQLite database (auto-generated)
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Tkinter (usually comes with Python installation)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/HeshamKhaled1/python-reg-log-system.git
   cd python-reg-log-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python src/gui.py
   # or
   python src/auth_system.py
   ```

## Usage

1. **Registration**
   - Launch the application
   - Click "Register" button
   - Fill in required fields (username, email, password)
   - Submit to create new account

2. **Login**
   - Enter registered username and password
   - Click "Login" to authenticate
   - Successful login grants access to the main application

3. **Security Features**
   - Passwords are hashed before storage
   - Input validation prevents SQL injection
   - Session management controls access

## Technical Implementation

### Core Components

- **Authentication System** (`auth_system.py`)
  - User registration and login logic
  - Password hashing and verification
  - Session management

- **Database Layer** (`database.py`)
  - SQLite database operations
  - User data persistence
  - Secure query execution

- **GUI Interface** (`gui.py`)
  - Tkinter-based user interface
  - Form validation and user feedback
  - Responsive design

- **Validators** (`validators.py`)
  - Input sanitization
  - Email format validation
  - Password strength checking

### Security Features

- **Password Hashing**: Uses modern hashing algorithms
- **Input Sanitization**: Prevents injection attacks
- **Session Security**: Secure session management
- **Data Validation**: Comprehensive input validation

## Configuration

The system can be configured through:

- Database connection settings
- Password complexity requirements
- Session timeout duration
- UI theme and styling options

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Hesham Khaled**
- GitHub: [@HeshamKhaled1](https://github.com/HeshamKhaled1)

## Acknowledgments

- Python community for excellent documentation
- Tkinter developers for the GUI framework
- Contributors and testers

---

**Note**: This authentication system is designed for educational purposes and can be integrated into larger Python applications requiring user management functionality.
```
