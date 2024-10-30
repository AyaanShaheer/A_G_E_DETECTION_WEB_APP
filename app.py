<<<<<<< HEAD
from flask import Flask, render_template, request
from deepface import DeepFace
import os

app = Flask(__name__)

# Function to perform age, gender, and emotion detection
def detect_age_gender_emotion(image_path):
    # Analyze the image using DeepFace
    analysis = DeepFace.analyze(image_path, actions=['age', 'gender', 'emotion'])
    return analysis

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and analysis

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    # Save the uploaded file
    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    # Perform detection on the saved file
    analysis = detect_age_gender_emotion(file_path)

    # Extract results from the analysis
    if isinstance(analysis, list) and len(analysis) > 0:
        result = analysis[0]  # Get the first analysis result
        age = result['age']
        
        # Get gender with the highest probability
        gender_probs = result['gender']
        gender = max(gender_probs, key=gender_probs.get)  # Get the gender with the highest probability

        emotion = result['dominant_emotion']
    else:
        return "No analysis result"

    # Pass just the filename and results to the results page
    return render_template('results.html', file_path=file.filename, age=age, gender=gender, emotion=emotion)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, render_template, request
from deepface import DeepFace
import os

app = Flask(__name__)

# Function to perform age, gender, and emotion detection
def detect_age_gender_emotion(image_path):
    # Analyze the image using DeepFace
    analysis = DeepFace.analyze(image_path, actions=['age', 'gender', 'emotion'])
    return analysis

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and analysis

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    # Save the uploaded file
    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    # Perform detection on the saved file
    analysis = detect_age_gender_emotion(file_path)

    # Extract results from the analysis
    if isinstance(analysis, list) and len(analysis) > 0:
        result = analysis[0]  # Get the first analysis result
        age = result['age']
        
        # Get gender with the highest probability
        gender_probs = result['gender']
        gender = max(gender_probs, key=gender_probs.get)  # Get the gender with the highest probability

        emotion = result['dominant_emotion']
    else:
        return "No analysis result"

    # Pass just the filename and results to the results page
    return render_template('results.html', file_path=file.filename, age=age, gender=gender, emotion=emotion)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> e3476272d6ab6525ac96f924c73c8e6b2d7792d7
