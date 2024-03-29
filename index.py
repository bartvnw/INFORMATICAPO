from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from backend_eindpunt import backend_programma

# cors is hier gebruikt omdat de server anders geen requests krijgt
app = Flask(__name__)
CORS(app)

#als deze route correct wordt gefetched, dan krijgt de server de afbeelding binnen
@app.route('/front_end/index.html/process_image', methods=['POST'])
def upload_and_process():
    if request.method == 'POST':
        if 'bestand van gebruiker' in request.files:
            #hier wordt het geuploade bestand opgeslagen in 'file'
            file = request.files['bestand van gebruiker']
            #hier zeggen we dat processed_file_resultaat het resultaat van blud wordt, door backend_programma uit backend_eindpunt te gebruiken
            processed_file_resultaat = backend_programma(file)
            #hier wordt het bericht gemaakt die wordt geprint op de website als de afbeelding is gesubmit
            message = {'resultaat':f'Het getal in de afbeelding is {processed_file_resultaat}'}
            #hier wordt het bericht gejsonified, zodat javascript ook echt het bericht snapt
            return jsonify(message)            
        else:
            return jsonify({'resultaat':'No file received'})
    else:
        return jsonify({'resultaat':'TERINGZOOI'})

#hiermee wordt de server gestart als de correcte command wordt aangeroepen in de opdrachtenprompt
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)