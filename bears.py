import fastai
from fastai.vision import (
    ImageDataBunch,
    create_cnn,
    open_image,
    get_transforms,
    models,
    imagenet_stats
)
import torch
from pathlib import Path
import flask
import io


fastai.defaults.device = torch.device('cpu')

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None

def load_model():
    # load the pre-trained model 
    global model
    path = Path("data/bears")
    classes = ['black', 'grizzly', 'teddys']
    data = ImageDataBunch.single_from_classes(path, classes, tfms=get_transforms(), size=224).normalize(imagenet_stats)
    model = create_cnn(data, models.resnet34).load('stage-2')


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image 
            image = flask.request.files["image"].read()
            # use open_image from fastai (magic)
            image = open_image(io.BytesIO(image))
            # classify the input image 
            pred_class,pred_idx,outputs = model.predict(image)
            data["prediction"] = pred_class
            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Fast.ai model and Flask starting server..."
		"please wait until server has fully started"))
	load_model()
	app.run(debug=True,host='0.0.0.0')