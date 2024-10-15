from flask import Flask

app = Flask(__name__)


@app.route('/user/<name>')

def user(name):
    greet = f'<h1>Hi Welcome, {name}</h1>'
    link = "<p>My name is <a href='user/Shreeram'>Shreeram</a>"
    return greet + link


if __name__ == '__main__':
    app.run(debug=True)