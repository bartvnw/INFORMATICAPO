from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Flask server is running and message is sent'})

if __name__ == '__main__':
    app.run(host='localhost', port=5500, debug=True)
