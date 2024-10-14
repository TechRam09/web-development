from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

user = {'sumit': 'password'}  # Predefined users

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

# Register module
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user:
            return 'Username already exists. Please choose another username.'
        user[username] = password
        return redirect(url_for('login'))  # Redirect to login after registration

    return render_template('register.html')

# Login module
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user and user[username] == password:
            return redirect(url_for('upload'))
        else:
            return 'Invalid username or password'
    
    return render_template('login.html')

# Upload module
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        file.save('uploads/' + file.filename)
        return '<html><h1>File uploaded successfully</h1><br><a href="/">Return to base page</a></html>'
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
