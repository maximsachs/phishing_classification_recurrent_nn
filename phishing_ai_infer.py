import os
# Printing only fatal errors from the tensorflow module.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  
import pandas as pd
import numpy as np
import json
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence

class phishing_ai():
    """
    Wrapper class to add custom prediction function to the model.
    """

    def __init__(self, model_name='phishing_detection_model'):
        with open(f'{model_name}_settings.json', "r") as msf:
            self.model_settings = json.load(msf)
        self.char2idx = {u:i for i, u in enumerate(self.model_settings["vocab"])}
        self.model = tf.keras.models.load_model(model_name)

    def text_to_int(self, text):
        return np.array([self.char2idx[c] for c in text])

    def is_phishing(self, url):
        """
        Returns True if phishing, False if not-phishing
        """
        encoded_text = sequence.pad_sequences([self.text_to_int(url)], self.model_settings["max_seq_len"])
        result = self.model.predict(encoded_text)
        return result[0][0] > self.model_settings["threshold"]
        

if __name__ == "__main__":
    # Using CPU for inference, disabling all detected gpus.
    tf.config.set_visible_devices([], 'GPU')

    # Initialising the model:
    phishing_ai = phishing_ai()

    # Showing the summary of the loaded model:
    # phishing_ai.model.summary()

    # Making an example prediction
    url = "mail.google.com"
    print("Prediction on url:", url, phishing_ai.is_phishing(url))    
    url = "paypalp.ontraport.com"
    print("Prediction on url:", url, phishing_ai.is_phishing(url))    