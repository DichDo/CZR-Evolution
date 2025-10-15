from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/services')
def services():
    return render_template('services.html', title='Services')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
