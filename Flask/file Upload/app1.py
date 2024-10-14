from flask import *

app = Flask(__name__)

@app.route('/upload',methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        file.save('uploads/'+file.filename)

        return 'File uploaded successfully'
    return render_template('upload.html')

if __name__ == '__main__':
 app.run(debug=True)

 