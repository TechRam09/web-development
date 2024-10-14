from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

@app.route('/api/<string:name>',methods=['GET'])
def greet(name):
    return jsonify(name =f"{name}")




if __name__ == '__main__':
    app.run(debug=True)