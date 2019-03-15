from flask import Flask, render_template,request, redirect, Response
import random, json
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/submit')
def submit():
	return render_template('work.html')
def worker():
	# read json + reply
	data = request.get_json()
	print(data)
 
if __name__ == '__main__':
  app.run(debug=True)