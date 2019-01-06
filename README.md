# picturi - NOT READY FOR PRODUCTION
Open source image hosting platform written iny Python. Ugh, will be better in future. At this point it has many bugs and isn't stable enough
but I thought why not upload it to GitHub when I'm already using Git. Feel free to contribute in future.

# Requirements
  * Computer 
  * Python3 - ```sudo apt-get install python3``` and make sure you have pip (https://docs.python.org/3/installing/index.html)
  * Pip - install pip by using: ```sudo apt-get install python3-pip```  
  * Flask (latest version) - ```python3 -m pip install flask``` 
  
# How to run?
If You'd like to run python3 application you must match requirements. If you get stuck Google the problem or make an issue on this GitHub
repository, I'd be happy to take a look at it.

# Run > Configuration
Before you boot up the application you might wanna change following things:
  * Flask port
  * Flask environment (debug mode)

They're both located at this line of code: ```app.run(debug=True port=5000)``` If you're launching Picturi on a production environment please 
turn debug mode off and make sure version of your repository is up-to-date!

# Run the python3 application
Just simply run the application - it doesn't require any additional chunk of crap! 

Example on Linux (my environment): ```python3 app.py``` (make sure you're at path where app.py is)

___


# Changing upload directory

Flask likes to keep track of its resources under 'static' folder, it's where you should keep all of your CSS files, javascript files,
and even the images (in our case). 

You may create folders afterward and name them however you'd like to (e.g 'pictures', 'nudes', 'photos') I refer to the source of images as 'uploads' here.
Simply, find following line in *app.py* file: ```PIC_FOLDER = os.path.join(APP_ROOT, 'static/uploads')``` and change ```/uploads```.

# Allowed types

Why do we limit the extensions that are allowed? You probably don’t want your users to be able to upload everything there if the server is directly sending out the data to the client. That way you can make sure that users are not able to upload HTML files that would cause XSS problems (see Cross-Site Scripting (XSS)). Also make sure to disallow .php files if the server executes them, but who has PHP installed on their server, right? :)
(taken from http://flask.pocoo.org/docs/1.0/patterns/fileuploads/)

# Changing allowed types

 Allowed type list is called ```ALLOWED_EXTE``` - simply follow the pattern that has been already given: 'something', 'something1', ...
