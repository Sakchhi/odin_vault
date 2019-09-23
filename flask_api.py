import flask
from flask import Flask
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from open_tesseract import processing


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
UPLOAD_FOLD = 'project/api_uploaded_files'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
@app.route("/index")
def index():
    print("Loaded index page")
    return flask.render_template('index.html')


@app.route('/output', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        file = request.files['image']
    if not file:
        return render_template('index.html', label="No file")
    print(UPLOAD_FOLDER)
    print(os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], 'test.png')))
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

    return processing(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port, debug=True)
