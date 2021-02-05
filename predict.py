from werkzeug.wrappers import Request, Response
import io
import numpy
from PIL import Image
import tensorflow as tf
import json

# Store our model
mnistModel = None

def read_input(request):
    # Load the image that was sent
    imageFile = request.files.get('image')
    img = Image.open(imageFile.stream)
    img.load()

    # Resize image to 28x28 and convert to grayscale
    img = img.resize((28, 28)).convert('L')
    img_array = numpy.array(img)

    # We're reshaping as our model is expecting 3 dimensions
    # with the first one describing the number of images
    image_data = numpy.reshape(img_array, (1, 28, 28))

    return image_data

def mypredictor(environ, start_response):
    request = Request(environ)

    global mnistModel
    # TODO: Load model file
    #if not mnistModel:
    #    mnistModel = tf.keras.models.load_model('model.h5')


    image = read_input(request)

    # If read_input didn't find a valid file
    if (image is None):
        response = Response("\nNo image", content_type='text/html')
        return response(environ, start_response)

    prediction = mnistModel.predict_classes(image)
    
    # TODO: Print Valohai prediction
    # The following line allows Valohai to track endpoint predictions
    # while the model is deployed. Here we remove the full predictions
    # details as we are only interested in tracking the rest of the results.
    
    #json_response = json.dumps({
    #    'vh_metadata': { 
    #        "prediction": str(prediction[0])
    #        }
    #    })
    #print(json_response)

    # Send a response back with the prediction
    response = Response(json_response, content_type='application/json')
    return response(environ, start_response)

# When running locally
if __name__ == "__main__":
    from werkzeug.serving import run_simple

    # Run a local server on port 5000.
    run_simple("localhost", 8000, mypredictor)