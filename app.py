'''
    Python-driven image cloud service.
    Github origin repository: https://www.github.com/pointerboy/picturi/
'''
import os
import sqlite3
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# get app root path 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# assign uploads folder using app root path
PIC_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

# set allowed extensions list
ALLOWED_EXTE = set(['png', 'jpeg', 'jpg', 'gif'])

# set database path
DATABASE = 'database.db'

# assign app param (somewhat like os var)
app.config['PIC_FOLDER'] = PIC_FOLDER

# main appliction's functions class
class application():
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTE
    def file_exists(path):
        try:
            file = open(path, 'r')
        except IOError:
             return False
        return True
    def generate_error_page(text):
        return render_template("public/whoopsie.html", error=text)

# app route's:

@app.route('/')
def index_callback():
    return render_template("public/index.html")

@app.route('/upload', methods=['POST'])
def file_upload():
    picture = request.files['picture']

    if 'picture' not in request.files:
        # file is empty
        return "input empty"

    picture_file = os.path.join(app.config['PIC_FOLDER'], picture.filename) 
    
    if not application.file_exists(picture_file):
        if application.allowed_file(picture_file):
            picture.save(picture_file)
            return render_template("public/index.html")
        else:
            # forbbiden file type
            application.generate_error_page("Forbbiden file type!")
    else:
         # file already exists
         return application.generate_error_page("File already exists on the server!")
@app.route('/library')
def library_origin():
	images_count = 0
	image_source_list = []

	for filename in os.listdir(PIC_FOLDER):
		images_count += 1
		image_source_list.append(filename)

	print(image_source_list)
	return render_template('public/library.html', image_list=image_source_list) # We pass our list to the template.


@app.route('/uploads/<source>', methods=['GET', 'POST'])
def library(source):
    print("attempted to access: " + source)
    # check if exists 
    if not appication.file_exists(PIC_FOLDER+'/'+source):
        application.generate_error_page("File doesn't exist or it's damaged")
    return render_template('public/library.html', image_list=source)
 
if __name__ == '__main__':
    app.run(debug=True, port=5001)
