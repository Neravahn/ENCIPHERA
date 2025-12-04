from flask import Flask, render_template, request, session, redirect
from auth.signup import save_user
from auth.login import verify_user
from auth.email_service import send_otp




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
        
        otp = send_otp(email)
        
        if otp is None:
            return {"error": "OTP cannont be sent"}
        
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
            return {"error": "INCORRECT OTP"}

    return render_template('verify_otp.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        verified = verify_user(username, password)

        if verified:
            return redirect('/dashboard')
        else:
            return {"error": "Incorrect Credentials"}

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
