from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Flask secret key for sessions
app.secret_key = os.getenv("SECRET_KEY", "fallbacksecret")

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/services')
def services():
    return render_template('services.html', title='Services')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
