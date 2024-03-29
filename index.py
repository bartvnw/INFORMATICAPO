from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from backend_eindpunt import backend_programma

app = Flask(__name__)
CORS(app)

@app.route('/front_end/index.html/test')
def test():
    message = {'bleh': "Het werkt."}
    return jsonify(message)

@app.route('/front_end/index.html/process_image', methods=['POST'])
def upload_and_process():
    if request.method == 'POST':
        if 'bestand van gebruiker' in request.files:
            file = request.files['bestand van gebruiker']
            processed_file_resultaat = backend_programma(file)
            message = {'resultaat':f'Het getal in de afbeelding is {processed_file_resultaat}'}
            return jsonify(message)            
        else:
            return jsonify({'resultaat':'No file received'})
    else:
        return jsonify({'resultaat':'TERINGZOOI'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)