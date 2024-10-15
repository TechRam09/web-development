from flask import Flask,render_template

app = Flask(__name__)


@app.route('/table')

def home():
    return render_template('table.html',name="Shreeram N S",c_name="vviet",gender="male",age=20,address="Nanjangud")


if __name__ == '__main__':
    app.run(debug=True)