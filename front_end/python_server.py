# Flask server code

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Assuming the uploaded file is an image
    image_data = file.read()

    # Process the uploaded image
    # result = process_image(image_data)

    # Return the processing result to the frontend
    return jsonify({'message': 'Image uploaded and processed successfully', 'result': image_data}), 200
upload()