# !!! USE AT YOUR OWN RISK !!!
PLEASE READ BELOW CAREFULLY FOR MORE INFORMATION

FolderEncryptor-NoFileNameEncryption.py is less risky but provides less privacy.

# Folder/File Encryption and Decryption Tool

This Python script uses the AES encryption standard to encrypt and decrypt the contents of files within a specified folder, namely a folder named 'Private' in the same directory as the script. The program also works with any subfolders within the 'Private' folder. It features a simple graphical user interface (GUI) created using the Tkinter library. 

## How to Use

1. Run the Python script.
2. A GUI window will open. You will see two radio buttons labeled 'Encrypt' and 'Decrypt', a field to enter your password, and a 'Run' button.
3. Select either 'Encrypt' or 'Decrypt'.
4. Enter your password in the 'Password' field.
5. Click the 'Run' button to perform the chosen operation.

## Security

This tool uses the AES block cipher in ECB mode, with a key derived from your password through the SHA256 hash function.

While this tool should be secure enough for most casual uses, it's important to note that it has not been extensively audited for security. It's recommended to use well-established encryption tools for any sensitive information.

Also, make sure your password is complex enough not to be easily guessed or brute-forced.

## Possible Uses

- Secure personal files on your computer.
- Protect sensitive data when transferring it to another device or person.
- Maintain a secure backup of important files.

## Limitations and Concerns

The current version of the tool also encrypts filenames by default. While this provides additional privacy, it does come with some potential issues:

1. Filesystem limitations: Encrypted filenames could exceed the maximum length allowed by your filesystem, especially if the original filenames are long. This could lead to errors or failed encryption/decryption.
2. Broken references: If a file within the encrypted folder references another file in the folder (e.g., a HTML file linking to an image), the reference will be broken when the filename is encrypted.
3. Long filenames: The base64 encoding used for filenames can cause issues with filesystems that have a maximum file or path length.

Always ensure that you have a secure backup of your files before using this tool. It's also recommended to thoroughly test this tool and understand its limitations before using it on any important data.
