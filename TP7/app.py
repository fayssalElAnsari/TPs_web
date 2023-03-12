from flask import Flask, send_from_directory
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def serve_root():
    return send_from_directory('static', 'index.html')

@app.route('/sing_in')
def serve_sign_in():
    return send_from_directory('static', 'sign_in.html')

@app.route('/browse')
def serve_browse():
    return send_from_directory('static', 'browse.html')

@app.route('/personal_library')
def serve_personal_library():
    return send_from_directory('static', 'personal_library.html')

if __name__ == '__main__':
    app.run(debug=True)

