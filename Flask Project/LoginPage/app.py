from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {"nishanth": "nishanth2910"}


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
      
        if  users[username] == password:
            return redirect(url_for('home'))  
        else:
            return "Enter correct credentials"
    
    return render_template('login.html')  


if __name__ == '__main__':
    app.run(debug=True)
