from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/upload',methods=['GET','POST'])

def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'no file'
        file = request.files['file']
        if file.filename == '':
            return 'no selected file'
        file.save('uploads/' + file.filename)
        
        return 'SUccessful'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)