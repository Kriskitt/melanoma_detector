from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from preprocess import preprocess_image
from model import load_model
import tensorflow as tf
import numpy as np

app = FastAPI()
# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], # Allows all origins
 allow_credentials=True,
 allow_methods=["*"], # Allows all methods
 allow_headers=["*"], # Allows all headers
)

app.state.model=load_model()
@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Detección preventiva de cáncer de piel")
    # $CHA_END

@app.post("/predict")
async def receive_image(img: UploadFile=File(...)):
    contents = await img.read()
    nparr = np.frombuffer(contents, np.uint8)
    preproc_img = preprocess_image(nparr)
    prediction = app.state.model.predict(tf.expand_dims(preproc_img, axis=0))
    return {"fare": float(prediction[0][0])}




   ##contents= await img.read() ##archivo de type:byte
   ##nparr = np.fromstring(contents, np.uint8) ## lo conviert en array
   ####tensor_img = tf.convert_to_tensor(nparr) ## lo convierte en tensor
   ##preproc_img=preprocess_image(nparr)
   ##prediction = app.state.model.predict(tf.expand_dims(preproc_img, axis=0))
   ####risk = "Alto riesgo" if prediction[0][0] > 0.5 else "Bajo riesgo"
   ##return dict(fare=float(prediction[0][0]))
   ####return {"risk": prediction[0][0]}
