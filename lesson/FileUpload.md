## Serve Flask server
```
flask run --debug
```

## Database 
```
#install package
pip install mysql-connector-python
pip install SQLAlchemy
```
## File Upload 
```
# header
app = Flask(__name__)
# Directory to save images
IMAGE_DIR = 'uploaded_images'
os.makedirs(IMAGE_DIR, exist_ok=True)
------------------------------------

# rout
@app.post('/upload')
def upload():
    try:
        # Get the Base64 image from the request
        data = request.json['image']

        # Separate the header from the base64 data
        header, base64_data = data.split(',')

        # Decode the base64 image data
        image_data = base64.b64decode(base64_data)

        # Define the path to save the image
        image_path = os.path.join(IMAGE_DIR, 'uploaded_image.png')

        # Write the image data to a file
        with open(image_path, 'wb') as file:
            file.write(image_data)

        return jsonify({"message": "Image uploaded successfully", "image_path": image_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
```
