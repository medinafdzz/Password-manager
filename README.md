# Password Manager🔒

This is a simple password manager developed in Python with a graphical user interface using the tkinter library. The program allows users to securely store their user credentials and retrieve and decrypt the stored passwords.

## Features✨

- Secure storage of passwords in text files.
- Encryption and decryption of passwords using JWT (JSON Web Tokens).
- User-friendly graphical user interface.

## Requirements📋

To run this application, you need to have Python 3 installed on your system. You must also install the following Python libraries:

- tkinter: For the graphical user interface.
- jwt: For encrypting and decrypting passwords.
- re: For handling regular expressions.

You can install these libraries using pip:

```bash
pip install tk
pip install pyjwt
```
## Usage🚀

1. Run the application. 
2. Enter your username and password in the corresponding fields. 
3. Click the "Save Credentials" button to securely save the user credentials to a text file. 
4. To retrieve a password, click the "Load Token" button and select the file containing the password. 
5. If you want to manually decrypt a password, click the "Decrypt Token" button and follow the instructions. 

## Secure Storage🔐

Passwords are stored in encrypted text files using JWT (JSON Web Tokens). Security is based on using a secret key (secret_key) to sign and verify the tokens. Make sure your secret key is strong and secure.

## Contribution🤝

If you'd like to contribute to this project, we welcome suggestions and improvements! You can fork this repository, make your changes, and submit a pull request.

## License📜

This project is under the MIT License.

## Author👨‍💻

- Developed by [@Medinafdzz](https://github.com/medinafdzz)
