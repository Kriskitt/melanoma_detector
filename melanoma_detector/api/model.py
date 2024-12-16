# Desarrollar el load model
import os
from tensorflow import keras
from colorama import Fore, Style
from params import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.metrics import Recall

def load_model():
    print(Fore.BLUE + f"\nLoad latest model from disk..." + Style.RESET_ALL)
    mela_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    model_path = os.path.join(mela_folder, 'model', 'model.h5')
    # model = Sequential()
    model = keras.models.load_model(model_path) ## Toma lo que definimos en params.py
    # model.compile(optimizer="adam",loss='binary_crossentropy', metrics=[Recall()])
    print("✅ Model loaded from local disk")
    return model
