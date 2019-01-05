'''
    Python-driven image cloud service.
    Github origin repository: https://www.github.com/pointerboy/picturi/
'''
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
PIC_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
ALLOWED_EXTE = set(['png', 'jpeg', 'jpg', 'gif'])

app.config['PIC_FOLDER'] = PIC_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTE

def file_exists(path):
    try:
        file = open(path, 'r')
    except IOError:
        return False
    return True

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/upload', methods=['POST'])
def file_upload():
    picture = request.files['picture'] 
    picture_file = os.path.join(app.config['PIC_FOLDER'], picture.filename) 
    if not file_exists(picture_file):
        if allowed_file(picture_file):
            picture.save(picture_file)
            return render_template("public/index.html")
        else:
            # forbbiden file type
            return "forbbiden file type"
    else:
         # file already exists
         return "already exists"
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
    if not file_exists(PIC_FOLDER+'/'+source):
        return "Could not find the picture / picture is damaged"
    return render_template('public/library.html', image_list=source)
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)
