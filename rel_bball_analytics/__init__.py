from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_pyfile('settings.py')

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')
