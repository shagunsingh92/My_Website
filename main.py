from flask import Flask,request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)