'''
    Python-driven image cloud service.
    Github origin repository: https://www.github.com/pointerboy/picturi/
'''
import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
PIC_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['PIC_FOLDER'] = PIC_FOLDER

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/upload', methods=['POST'])
def file_upload():
	picture = request.files['picture'] # We fetch the request (the picture from HTML submited form)
	picture_file = os.path.join(app.config['PIC_FOLDER'], picture.filename) # We init a real file object and give it a name 
	picture.save(picture_file) # We save the file object
	return render_template("public/index.html")
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
    try:
        file = open(PIC_FOLDER+'/'+source, 'r')
    except IOError:
        return "Could not find the picture / picture is damaged"
    return render_template('public/library.html', image_list=source)
 
if __name__ == '__main__':
    app.run(debug=True, port=4001)
