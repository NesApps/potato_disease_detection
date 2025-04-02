# potato_disease_detection
A cutting-edge machine learning application designed to identify potato crop diseases (blight) early from images with high accuracy. This project leverages deep learning to empower farmers and agronomists with a tool for early disease detection, promoting sustainable agriculture

# Potato Disease Detection App

![Potato Disease Detection](https://img.shields.io/badge/Status-In%20Progress-orange)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-green)

Welcome to the **Potato Disease Detection App**, a machine learning-powered solution to identify diseases in potato crops using image analysis. This project combines deep learning with practical agriculture, aiming to help farmers spot issues like late blight, early blight, or bacterial wilt early—before they ruin harvests. Whether you're a coder, a data scientist, or just curious about AI in farming, this repo has something for you!

## 🌱 Project Vision
Potatoes are a global staple, but diseases can wipe out crops fast. This app uses a convolutional neural network (CNN) trained on potato leaf images to classify diseases accurately. Think of it as a digital plant doctor—snap a photo, upload it, and get a diagnosis. The goal? Early detection, better treatment, and healthier spuds for everyone.

## 🚀 Features
- **Image-Based Detection**: Analyzes potato leaf photos to predict diseases.
- **Deep Learning Model**: Built with TensorFlow and Keras for top-notch accuracy.
- **User-Friendly**: Designed to run in Jupyter Notebook, with plans for a simple app interface.
- **Open Source**: Free to use, tweak, and contribute to under the MIT License.

## 📂 Repository Structure

## 🛠️ Tech Stack
- **Python 3.12**: The backbone of the project.
- **TensorFlow 2.15**: For building and training the CNN model.
- **Jupyter Notebook**: Interactive coding and visualization.
- **Libraries**: NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn for data prep and analysis.
- **Git & GitHub**: Version control and collaboration.

## 📊 Dataset
This project uses the **PlantVillage** dataset, a collection of potato leaf images labeled with diseases like:
- Late Blight
- Early Blight
- Healthy (no disease)
The images are preprocessed—resized to 256x256 pixels, shuffled, and batched—for efficient training.

## ⚙️ How It Works
1. **Preprocessing**: Images are cleaned up—resized, normalized, and batched using TensorFlow’s `image_dataset_from_directory`.
2. **Model Training**: A CNN learns to spot disease patterns from leaf features (e.g., spots, discoloration).
3. **Prediction**: Feed a new potato leaf image, and the model outputs the likely disease.
