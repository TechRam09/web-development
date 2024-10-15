from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')

def home():
    datas = [
        {"name":"Shreeram","Place":"Mysore","State":"Karnataka"},
        {"name":"Adarsh","Place":"Mysore","State":"Karnataka"},
        {"name":"Nishanth","Place":"Mysore","State":"Karnataka"},
        {"name":"Keerthi","Place":"Mysore","State":"Karnataka"},
        {"name":"Shreeram","Place":"Mysore","State":"Karnataka"},
        {"name":"Adarsh","Place":"Mysore","State":"Karnataka"},
        {"name":"Nishanth","Place":"Mysore","State":"Karnataka"},
        {"name":"Keerthi","Place":"Mysore","State":"Karnataka"},
        {"name":"Shreeram","Place":"Mysore","State":"Karnataka"},
        {"name":"Adarsh","Place":"Mysore","State":"Karnataka"},
        {"name":"Nishanth","Place":"Mysore","State":"Karnataka"},
        {"name":"Keerthi","Place":"Mysore","State":"Karnataka"},
        {"name":"Shreeram","Place":"Mysore","State":"Karnataka"},
        {"name":"Adarsh","Place":"Mysore","State":"Karnataka"},
        {"name":"Nishanth","Place":"Mysore","State":"Karnataka"},
        {"name":"Keerthi","Place":"Mysore","State":"Karnataka"},  
    ]
    return render_template('dynamicData.html',datas=datas)


if __name__ == '__main__':
    app.run(debug=True)