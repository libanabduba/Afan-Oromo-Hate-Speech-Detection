# Afaan Oromo Hate Speech Detection (NLP Project) 🚫🗣️

## Introduction 📝
This project aims to detect hate speech in Afaan Oromo language using Natural Language Processing (NLP) techniques. The code includes a Django web application with a hate speech detection model implemented in Keras. The hate speech detection model is trained on the "Afaan Oromo Hate Speech Dataset" available in the provided CSV file.

## Getting Started 🚀 ( Project Setup )

Follow these steps to set up and run the project:

#### 1. Clone the Repository

Clone this GitHub repository using the following command:

```bash
git clone https://github.com/Sam-Girma/NLP-project.git 
```
#### 2. Create Virtual Environment
Create a virtual environment to run the project and download the project packages to avoid clashes with existing ones. Refer to the details in Python's venv documentation.

#### 3. Install Dependencies
Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

#### 4. Database Setup
Run the following commands to apply migrations to the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Superuser Setup
Set up a superuser for the app. For Django, use the following command and fill in the details when prompted:

```bash
python manage.py createsuperuser
```

#### 6. Run the App
Now, run the app using the below command.

```bash
python manage.py runserver
```

## Text Preprocessing ✨

The `socials/base/utils.py` file contains functions for text preprocessing, including:

- HTML tag removal ✂️
- Symbol and noise removal 🚮
- Stopword removal 🛑
- Non-alphanumeric word removal ❌

## Hate Speech Detection 🚫🗣️

The hate speech detection model predicts whether a given post contains hate speech. The `Post` model in `socials/base/models.py` includes a method `predict_is_hate` that uses the loaded model to make predictions.

## Usage 💡

1. Integrate the provided code into your Django project.
2. Ensure the hate speech detection model is loaded during application startup.
3. Utilize the `predict_is_hate` method in your views to predict hate speech for each post.

```python
for post in all_posts:
    post.predict_is_hate(loaded_model)
```
## Dependencies

- Django
- NLTK
- Keras

🚀
