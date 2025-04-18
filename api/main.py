import numpy as np
from fastapi import FastAPI, File, UploadFile
import uvicorn
from io import BytesIO
from PIL import Image #This is used to read image in python
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model
@app.get("/ping")
async def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.get("/predict")
async def predict(
    file: UploadFile = File(...)

):
    image = read_file_as_image(await file.read())
    return

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)