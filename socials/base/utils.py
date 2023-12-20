# yourapp/utils.py

import re
import pandas as pd
import nltk
from keras.src.utils import pad_sequences
from keras.preprocessing.text import Tokenizer

# Download the 'punkt' resource
nltk.download('punkt')

import keras.backend as K

data = pd.read_csv("C:/Users/Admin/Downloads/Afaan Oromo Hate Speech Dataset.csv")
X_train = data['Posts']
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)

def remove_html_tags(text):
    # Remove HTML tags using regex
    clean_text = re.sub('<.*?>', '', text)
    return clean_text

def recall(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1(y_true, y_pred):
    precisions = precision(y_true, y_pred)
    recalls = recall(y_true, y_pred)
    return 2 * ((precisions * recalls) / (precisions + recalls + K.epsilon()))



def remove_noise_symbols(raw_text):
    text = raw_text.replace('"', '')
    text = text.replace("'", '')
    text = text.replace("!", '')
    text = text.replace("`", '')
    text = text.replace("..", '')

    return text

def remove_non_alphanumeric_words(sentence):
    words = sentence.split()
    pattern = re.compile(r'\W+')
    cleaned_sentence = ' '.join(word for word in words if not pattern.search(word))
    return cleaned_sentence

def remove_stopwords(raw_text):
    tokenize = nltk.word_tokenize(raw_text)
    text = [word for word in tokenize]
    text = " ".join(text)
    return text

def preprocess_text(text):
    # Remove HTML tags
    text = remove_html_tags(text)
    text = remove_noise_symbols(text)
    text = remove_stopwords(text)
    text = remove_non_alphanumeric_words(text)
    return text

def preprocess_text_for_model(text):
    # Additional preprocessing steps specific to the model input
    preprocessed_text = preprocess_text(text)

    # Tokenize and pad the sequence
    text_sequence = tokenizer.texts_to_sequences([preprocessed_text])
    padded_sequence = pad_sequences(text_sequence, maxlen=591)

    return padded_sequence
