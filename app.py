from flask import Flask, render_template, request,jsonify
from keras.models import load_model
import cv2
import numpy as np
import base64
from PIL import Image
import io

import re

img_size=224

app = Flask(__name__) 

model = load_model('model_save.h5')

label_dict={0:'covid negative', 1:'covid positive'}

def preprocess(img):

	img=np.array(img)
	if (img.ndim==3):
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	resized=cv2.resize(img,(img_size,img_size))
	reshaped=resized.reshape(1,img_size,img_size,1)
	print(reshaped.shape)
	img= reshaped/255
	return img

@app.route("/")
def index():
	return(render_template("main.html"))

@app.route("/predict", methods=["POST"])
def predict():
	print('HERE')
	message = request.get_json(force=True)
	encoded = message['image']
	decoded = base64.b64decode(encoded)
	dataBytesIO=io.BytesIO(decoded)
	dataBytesIO.seek(0)
	image = Image.open(dataBytesIO)

	test_image=preprocess(image)

	prediction = model.predict(test_image)
	result=np.argmax(prediction,axis=1)[0]
	accuracy=float(np.max(prediction,axis=1)[0])

	label=label_dict[result]

	print(prediction,result,accuracy)

	response = {'prediction': {'result': label,'accuracy': accuracy}}

	return jsonify(response)

app.run(debug=True)

#<img src="" id="img" crossorigin="anonymous" width="400" alt="Image preview...">