*ENCIPHERA* is a secure, server-side encrypted file vault built around a fully custom encryption algorithm written by the developer.
It provides safe file storage, easy management, and a unique math-based recovery system — all inside a clean, modern web interface.

Enciphera is ideal for anyone who wants a simple personal vault, a custom crypto demo, or a security-focused utility project.


## FEATURES
### 1. Server-Side Encryption
- All encryption and decryption happen on the server, not in the browser.
- Keeps client-side simple and prevents exposute of keys.

### 2. Custom Encryption Logic (Hand-Written)
- No standard libraries required — Encryption is implemented manually.
- Great for learning, experimenting, or demonstrating cryptography fundamentals.
- Logic can be improved or replaced easily.

### 3. Supports Many File Types
- Images
- PDFs
- Videos / Audio
- ZIP / code files
- Any binary or text files
⚠️ Note: Maximum file-size capacity is not fully tested yet. Large file support will be documented as testing continues.

### 4. Integrated File Manager
- Upload
- Download 
- Delete
- View metadata (size, upload date, encryption status)
Everything stays inside the user's personal vault

### 5. Safe Metadata Storage
- SQLite database
- No plaintext keys stored
- Only encrypted files + hashed refference saved


## HOW IT WORKS
### 1. File Upload
User uploads a file → server reads it → encrypts using custom cipher → stores encrypted blob.

### 2. Key Handling
- User chooses a key
- Server never stores key in plaintext
- Only encrypted output is written to disk

### 3. File Retrieval
User enters key → server decrypts file → sends original file back as a download.


## INSTALLATION
```bash
git clone https://github.com/Neravahn/enciphera.git
cd enciphera
pip install -r requirements.txt
python app.py
```
Open in Browser
```arduino
http://localhost:5000
```

## TESTING NOTES
- Custom encryption is functional but still experiental
- Large file handling has not been fully tested
- Behaviour with large files may depend on:
    - Server RAM
    - Disk I/O speed
    - Buffering strategy in Python
Testing status will be updated as development continues


## WHY ENCIPHERA?

*ENCIPHERA* showcases custom cryptography, server-side encryption design, and secure file handling — all in a clean, user-friendly package.
It is both a practical vault and a technical learning project, demonstrating how encryption systems can be built from scratch.