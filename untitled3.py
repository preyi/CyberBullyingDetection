# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oBi4M2h1u2IoTHmLW-5J5boR-5Myul6Y
"""

!pip install flask-ngrok

from google.colab import drive
drive.mount('/content/drive')

from flask_ngrok import run_with_ngrok
from flask import Flask,request,render_template
import pickle
import numpy as np

!pip install pyngrok

!killall ngrok

from pyngrok import ngrok

    # Set your authtoken
ngrok.set_auth_token("2pcX2uAKByMvIeV1aSTz5oPhklX_6gzJpFWmghqFn9BVsJ95v")

    # Now connect
ngrok_tunnel = ngrok.connect(5000)
print(f"Public URL: {ngrok_tunnel.public_url}")

app = Flask(__name__, template_folder='/content/drive/MyDrive/ModelDeployment/templates')
run_with_ngrok(app)
print('before loading pickel file')
model=pickle.load(open('/content/drive/MyDrive/ModelDeployment/templates/weight_pred_model.pkl','rb'))
@app.route('/')
def home():
  print('in home function')
  return render_template('/content/drive/MyDrive/ModelDeployment/templates/index.html')
@app.route('/getprediction',methods=['POST'])
def getprediction():
  input = [float(x) for x in request.form.values()]
  final_input = [np.array(input)]
  print('before predicrion statement')
  prediction = model.predict(final_input)
  print('after printing statement')
  return render_template('index.html', output='Predicted Weight in KGs :{}'.format(prediction))

print('before app run statement')
if __name__ == "__main__":
  print('in main function')
  app.run()