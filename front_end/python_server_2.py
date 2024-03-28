from flask import Flask, request, jsonify, render_template, send_file

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
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
            response_string = f'Image width: {width}, height: {height}'
            # Alternatively, generate another version of the image and send it back
            # Example: Save the processed image to a new file and return the file path
            # processed_image_path = 'path_to_processed_image.jpg'
            # return send_file(processed_image_path, mimetype='image/jpeg')

            return "HET WERKT!!!"  # Return the response string
        else:
            return 'No file received'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)