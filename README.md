# A_G_E_DETECTION_WEB_APP
This project is a Flask web app that performs real-time age, gender, and emotion detection using DeepFace. Users can upload an image, and the app will analyze and display the person's age, gender, and dominant emotion.
# Age, Gender, and Emotion Detection Web App

## Overview
The **Age, Gender, and Emotion Detection Web App** is a Flask-based web application that utilizes DeepFace, a powerful facial recognition and analysis library. This app allows users to upload images and receive predictions about the age, gender, and emotional state of the individuals in the images.

## Features
- **Age Detection:** Estimate the age of individuals in the uploaded images.
- **Gender Detection:** Classify individuals as male or female with a probability score.
- **Emotion Detection:** Identify the predominant emotion from a set of emotions including happiness, sadness, anger, surprise, fear, and neutral.
- **User-Friendly Interface:** Easy-to-navigate web interface for seamless user experience.

## Technologies Used
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** DeepFace for facial recognition and analysis
- **Environment:** Virtual environment for dependency management

## Installation
To set up and run the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AyaanShaheer/A_G_E_DETECTION_WEB_APP.git
   cd A_G_E_DETECTION_WEB_APP
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the Flask application:**
   ```bash
   python app.py
5. **Access the app: Open your web browser and navigate to http://127.0.0.1:5000/.**

**Usage**
Upload an image containing a face.
Click the "Analyze" button.
The app will display the estimated age, gender (with probabilities), and detected emotion.


**Contributing**
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to create an issue or submit a pull request.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Acknowledgments**
DeepFace for providing the facial analysis capabilities.
Flask for the web framework.
