Hello World, In this simple example,
I will show you how to make a python web-app using flask.

1) Install git and pull the project
  - Linux $ sudo apt-get install git
  - Windows: go to > https://git-for-windows.github.io/ and download the exe. 
  - If you want to skip set up, clone the sample project from the link below:
  $ git clone https://github.com/scottyadean/webapp.git
  
2) Install pip (if not installed)
  - Linux $ pip install -U pip setuptools
  - Windows $ python -m pip install -U pip setuptools
  - You can also download this file > https://bootstrap.pypa.io/get-pip.py and then run: python get-pip.py

3) Install flask
 - Linux $ pip install flask
 - Windows $ pip install flask
 
4) Create the project structure
  - The base directory layout for your new app should look like this:
  webapp
  ├── app.py
  ├── __init__.py
  └── templates
      └── index.html
  
5) Create the web server
 Open app.py and paste this code into it:
##############Code########################

from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
  app.debug = True
  app.run(port=4996)

##############Code########################
  
6) Run the App
 - open the console and cd to your project dir. run this command: python app.py
 - The output should look like this:
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 183-840-031
    * Running on http://127.0.0.1:4996/ (Press CTRL+C to quit)
 - Open a web browser and go to the address listed above.

7) Add a html template to your view.
 - open up the file: webapp/templates/index.html
 - add this line: <h1>Hello World</h1>

8) Render the html template in your app.py server.
  - open up the file: webapp/app.py
  - update this line:  return 'Hello, World!'
  - change it to: render_template('index.html')
  - your updated function should look like the code below:

@app.route('/')
def hello_world():
  render_template('index.html')

  - navigate to the server url: http://127.0.0.1:4996/
  - your Html template should display.

9) Add a new html template to your app.
 - under the templates directory create a new file called: about.html
 - add any html you like in the new file and save it.

10) Add the new about_us/ route to your app.
  - open up the file: webapp/app.py add code below:

@app.route('/about_us')
def about_us():
  render_template('about.html')
  
  - save the file and navigate to the server url: http://127.0.0.1:4996/about_us
  - enjoy your web app :) 
