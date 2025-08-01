from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # Display login form

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    return f"Username: {username}, Password: {password}"

if __name__ == "__main__":
    app.run(debug=True)
