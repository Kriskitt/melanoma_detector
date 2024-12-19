# Desarrollar el load model
import os
from tensorflow import keras
from colorama import Fore, Style
from params import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.metrics import Recall
from keras.layers import LeakyReLU
from keras.models import load_model

# Registra LeakyReLU para que sea reconocido
custom_objects = {"LeakyReLU": LeakyReLU}

def load_model():
    print(Fore.BLUE + f"\nLoad latest model from disk..." + Style.RESET_ALL)
    mela_folder = os.path.dirname(os.path.dirname(__file__))
    model_path = os.path.join(mela_folder, 'model', 'model_3.keras')
    model = keras.models.load_model(model_path, custom_objects=custom_objects) ## Toma lo que definimos en params.py
    print("✅ Model loaded from local disk")
    return model
