from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    # Run your Python script here
    subprocess.run(['python3', 'run.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
