# Django Password Manager

A secure and user-friendly password manager application built with Django. This application allows users to securely store and manage their passwords for different websites.

## Features

- **User Registration and Authentication**: Users can register, log in, and log out.
- **Password Storage**: Securely store passwords for different websites.
- **Encryption**: Passwords are encrypted using the `cryptography` library before being saved to the database.
- **Password Decryption**: Decrypt stored passwords to view them in plain text.
- **User-Specific Data**: Each user has access only to their own passwords.
- **Admin Interface**: Manage users and passwords through the Django admin interface.

## Setup and Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AliGohar2151/password_manager.git
    cd password_manager
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Generate a Fernet Key**

    ```python
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    print(key.decode())
    ```

    Update the settings: Add the generated Fernet key to your settings.py:
    ```python
    # settings.py
    FERNET_KEY = 'YOUR_GENERATED_KEY=='
    ```

4. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

## Encryption Details

Passwords are encrypted using the cryptography library's Fernet symmetric encryption. The encryption key is stored in the Django settings file and should be kept secure.

## Security Considerations

- Ensure the Fernet key is kept secure and is not hard-coded in the source code for production environments.
- Use environment variables to store sensitive information, such as the Fernet key and database credentials.
