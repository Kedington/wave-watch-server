import os

from flask import Flask, request, send_from_directory, flash, redirect, url_for
from utils import allowed_file, generate_filename
from db import get_db, query_db, close_db


app = Flask(__name__)
app.config.from_object("config")


@app.route('/')
def hello_world():
    return 'Wave Watch'


@app.route('/db/insert')
def db_test():
    db = get_db()
    db.execute("INSERT INTO IMAGE (NAME, LONGITUDE, LATITUDE) VALUES (?, ?, ?)", [generate_filename("test.jpg"), 15, 25])
    db.commit()
    return 'Insert Successful'


@app.route('/db/select')
def db_get():
    string = ""
    for item in query_db("select * from image"):
        string = string + str(item) + "\n"
    return string


@app.route('/file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        elif file and allowed_file(file.filename):
            filename = generate_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.teardown_appcontext
def close_app(exception):
    print("Closed DB")
    close_db()


if __name__ == '__main__':
    app.run()
