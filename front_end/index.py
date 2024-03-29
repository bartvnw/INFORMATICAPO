from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS

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
            # Process the image file here
            # Example: Get width and height of the image
            width = 0
            height = 0
            # Example: Calculate width and height (replace this with your actual processing)
            # For demonstration purposes, we are just assuming width and height as 100
            # Replace the below code with your actual processing logic
            # width, height = process_image_function(file)
            width = 100
            height = 100
            # Generate a string response
            resultaat = {'resultaat':"Hij geeft eindelijk iets terug"}
            # Alternatively, generate another version of the image and send it back
            # Example: Save the processed image to a new file and return the file path
            # processed_image_path = 'path_to_processed_image.jpg'
            # return send_file(processed_image_path, mimetype='image/jpeg')

            return jsonify(resultaat)  # Return the response string
        else:
            return jsonify({'resultaat':'No file received'})
    else:
        return jsonify({'resultaat':'TERINGZOOI'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)