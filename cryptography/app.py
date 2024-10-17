from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
app.config['UPLOAD_FOLDER'] = 'uploads'  
app.config['DECRYPTED_FOLDER'] = 'decrypted'  
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DECRYPTED_FOLDER'], exist_ok=True)

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    if 'file' not in request.files:
        flash('No file uploaded for encryption.')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file for encryption.')
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    key = generate_key()  
    fernet = Fernet(key)

    with open(file_path, "rb") as f:  
        original_data = f.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(file_path + ".enc", "wb") as encrypted_file:  
        encrypted_file.write(encrypted_data)

    flash(f"{filename} has been encrypted successfully!")
    return redirect(url_for('index'))

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    if 'file' not in request.files:
        flash('No file uploaded for decryption.')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file for decryption.')
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as encrypted_file:  
            encrypted_data = encrypted_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        decrypted_file_path = os.path.join(app.config['DECRYPTED_FOLDER'], filename.replace(".enc", "_decrypted"))
        with open(decrypted_file_path, "wb") as decrypted_file:  
            decrypted_file.write(decrypted_data)

        flash(f"{filename} has been decrypted successfully!")
    except Exception as e:
        flash(f"Decryption failed: {str(e)}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
