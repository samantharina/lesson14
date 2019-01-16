from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	user_name = 'Sam'
	return render_template('index.html', name=user_name)

@app.route('/process', methods=['POST'])
def process():
	your_pick = request.form['your_pick']


	return 'You sent us ' + your_pick

# at the bottom to run the website
app.run(debug=True)