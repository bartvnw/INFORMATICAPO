from flask import Flask

app = Flask(__name__)

app.route('/')
def leuke_functie():
    return "ja het werkt"

if __name__ == '__main__':
    app.run(host='localhost', port=5500, debug=True)
