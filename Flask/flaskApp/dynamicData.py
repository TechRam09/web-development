from flask import Flask,render_template

app = Flask(__name__)


@app.route('/tableData')

def home():
    data = {"name":["Shreeram","Nishanth"],"place":["Nanjangud","Mysore"],"state":["Karnataka","Karnataka"] }
    return render_template('data.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)