from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/front_end/gpt_website.html/d')
def pindex():
    message = {'message': "Haiii"}
    return jsonify(message)

@app.route('/d')
def index():
    return jsonify({'message': 'Flask server is running and message is sent'})

if __name__ == '__main__':
    app.run(host='localhost', port=5500, debug=True)
    
