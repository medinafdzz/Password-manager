# Password Manager :key:

![Python Version](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview :mag_right:

The Password Manager is a simple Python application that allows you to securely store and manage your passwords. It uses a graphical user interface built with the Tkinter library and stores passwords in a PostgreSQL database. You can also encrypt and decrypt passwords using JSON Web Tokens (JWT).

## Features :rocket:

- Save your credentials to your PostgreSQL database.
- Decrypt and reveal stored passwords.
- Load and decrypt tokens from text files.
- User-friendly GUI with password input masking.

## Prerequisites :gear:

- [Python 3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- Python libraries: `tkinter`, `psycopg2`, `jwt`

## Installation :wrench:

1. Clone this repository:
- git clone https://github.com/yourusername/password-manager.git

2. Install the required libraries:
 ```cmd
- pip install psycopg2-binary PyJWT
```
3. Make sure you have a PostgreSQL server set up and running.

4. Replace the following database connection details in the code with your own values:
   
```python
user="postgres",
password=passwordDB,  # Change 'passwordDB' to your PostgreSQL password
host="localhost",
port="5432",
database="Password-Manager"
```
5. queries.sql is the file responsible for storing SQL queries.
```sql
-- Insert user,password and token
INSERT INTO passwords (username, password, token) VALUES (%s, %s, %s);
```
6. The load_queries function in the Python code reads SQL queries from the queries.sql file, making it easy to manage your database operations.
```sql
# Load SQL queries from the file
def load_queries():
  with open("queries.sql", "r") as sql_file:
    return sql_file.read()
```
   
## Usage :computer:
Run the application:
```cmd
phyton password_manager.py
```
- Enter your username and password.
- Click "Save Credentials" to save them as a token.txt.
- Click "Reveal token" to decrypt and reveal a stored token.
- Click "Load Token" to load and decrypt tokens from text files.
- Click "Save to Database" to securely store your credentials in your PostgreSQL database.

## License :page_with_curl:
This project is licensed under the MIT License.

## Acknowledgments :pray:
Thanks to the open-source community for creating and maintaining the libraries used in this project.

Feel free to customize and improve this Password Manager application to meet your specific needs!

Happy password managing! :lock: :key:

## Author: 
[@medinafdzz](https://github.com/medinafdzz)
<br>
<br>



