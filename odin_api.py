from flask import Flask, request, send_from_directory

# set the "static" directory as the static folder.
# this will ensure that all the static files are under one folder

app = Flask(__name__, static_url_path='/static')


# serving some static html files
@app.route('/html/path:path')
def send_html(path):
    return send_from_directory('static', path)


@app.route('/upload', methods=['POST'])
def upload_file():
    print request.files
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
    file = request.files['file']
    file.save("static/test.jpg")
    return "file successfully saved"


if __name__ == "__main__":
    app.run()