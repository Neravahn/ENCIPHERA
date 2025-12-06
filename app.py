from flask import Flask, render_template, request, session, redirect
from auth.signup import save_user
from auth.login import verify_user
from auth.email_service import send_otp
from auth.checkuser import user_exist_username, user_exists_email
from crypto_engine.encryption import encrypt
from crypto_engine.decryption import decrypt
from crypto_engine.keygen import generate_key
from file_manager.save_file import save
from file_manager.fetch_files import fetch



app = Flask(__name__)
app.secret_key = "your_super_secret_key_here"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if user_exists_email(email):
            return render_template('signup.html', error="E-MAIL ALREADY IN USE")
        
        if user_exist_username(username):
            return render_template('signup.html', error = "USERNAME ALREADY IN USE")
        


        otp = send_otp(email)
        if otp is None:
            return render_template("signup.html", error="OTP CANNOT BE SENT")
        
        session['signup_otp']= otp
        session['user_data'] = {
            'name': name,
            'username': username,
            'email': email,
            'password': password
        }

        return redirect('/verify-otp')
            
    return render_template('signup.html')

        
@app.route('/verify-otp', methods =['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        user_otp = request.form['otp']
        real_otp = session.get('signup_otp')

        print(f"USER OTP{user_otp}")
        print(f"REAL OTP{real_otp}")

        if user_otp == real_otp:
            data = session['user_data']
            save_user(**data)
            return redirect('/login')
        else:
            return render_template("verify_otp.html", error="INCORRECT OTP")


    return render_template('verify_otp.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        session['username'] = username

        verified = verify_user(username, password)

        if verified:
            return redirect('/dashboard')
        else:
            return render_template("login.html", error="Incorrect Credentials")

    return render_template('login.html')




@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    username = session.get('username')
    return render_template('dashboard.html', username = f"Hi , {username}")

@app.route('/editor', methods = ['GET', 'POST'])
def editor():
    if request.method == 'GET':
        return render_template('editor.html')
    
    if request.method == 'POST':
        

        #GETTING THE DATA FROM THE FRONT END
        data = request.get_json()
        text = data.get('text')
        file_name = data.get('file_name')
        file_type = '.txt'

        #PREPARING TH DETAILS TO SAVE 
        key = generate_key()
        key_bytes = [ord(c) for c in key]
        encoded_text = text.encode('utf-8')
        username = session.get('username')
        encrypted_text = encrypt(encoded_text, key_bytes)

        #SAVING AND ERROR HANDLING
        isSaved = save(username, file_name, file_type, encrypted_text)

        if isSaved:
            return {"success": True, "message": "Saved Successfully"}

        
        else:
            return {"success": False, "message": "Something went wrong"}

    

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():

    return

@app.route('/file_manager', methods= ['GET', 'POST'])
def file_manager():
    if request.method == 'POST':
        data = request.get_json()
        file_type = data.get('file_type')
        username = session.get('username')

        if file_type == None:
            file_type = '.txt'

        files = fetch(username)



        if files == None:
            return {"message" : f"No {file_type} files found"}
        
        file_names = []
        for i in range(len(files)):
            file_names.append(files[i][0])

        


    return render_template('file_manager.html')


if __name__ == "__main__":
    app.run(debug=True)
