from flask import Flask, request, render_template, Markup
import torch
from torchvision import transforms, models
from PIL import Image
import os
from model import predict_image
import diseases

app = Flask(__name__, template_folder='../templates')

# Serve the React app
@app.route("/")
def home():
    return render_template("home.html")





# Define a route to serve predictions
@app.route("/predict", methods=["POST"])
def predict():  # sourcery skip: inline-immediately-returned-variable
    file = request.files["file"]
    prediction = predict_image(file)
    print(prediction)
    res = Markup(diseases.disease_dic[prediction])
    return render_template('display.html', status=200, result=res)



# Run the app
if __name__ == "__main__":
    app.run(debug=True)