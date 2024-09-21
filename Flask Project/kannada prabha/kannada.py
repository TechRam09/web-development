from flask import Flask, render_template,request,url_for,redirect

app = Flask(__name__)


users={'Nishanth':'nishu2910'}

@app.route('/')
def Landing():
    return render_template('kannada.html')

@app.route('/home')
def home():
    return render_template('kannadaHome.html')

@app.route('/rajya')
def rajya():
    return render_template('rajya.html')

@app.route('/desha')
def desha():
    return render_template('desha.html')


@app.route('/rajyakeeya')
def rajyakeeya():
    return render_template('rajyakeeya.html')
    

@app.route('/kreeda')
def kreeda():
    return render_template('kreeda.html')

@app.route('/videsha')
def videsha():
    return render_template('videsha.html')

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