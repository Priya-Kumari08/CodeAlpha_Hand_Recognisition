import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model("model.h5")

def predict_digit(img_path):

    img = Image.open(img_path).convert('L')
    img = img.resize((28,28))

    img = np.array(img)/255.0
    img = img.reshape(1,28,28,1)

    prediction = model.predict(img)
    return np.argmax(prediction)
