from flask import Flask, render_template, url_for, request, redirect,
from models import *

app = Flask(__name__)

@app.route('/')
def index():
	pass
    #s = Snippet.query.all()
    #return render_template('index.html', s=s)

@app.route('/create', methods=['GET','POST'])
def create_post():
    pass  
#if request.method == 'GET':
#	return render_template('create.html')
#if request.method == 'POST':
#	name = request.form['name']
#	print("I am In")
#	s = Snippet(name=name)
#	db.session.add(s)
#	db.session.commit()

#2\	return redirect(url_for('index'))
	
if __name__ == '__main__':

    app.run(debug=True)
