from flask import Flask # import Flask class object from flask library
from flask import render_template

# render_template accesses an html file in python application in python files and then displays that html of the requested url

app = Flask(__name__) # instantiating object
# __name__ is a special variable that will get as value of the name of the python script
# when you execute a python script, python assigns the name main to this string to the file

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about/')
def about():
	return render_template('about.html') # the output that this function produces will be mapped to '/' url

if __name__ == '__main__':
	app.run(debug=True)