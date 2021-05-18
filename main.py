from flask import Flask


app = Flask(__name__)

@app.route('/info')
def print_info():
    return('/info.json')

def main():
    app.run('127.0.0.1', '5000')