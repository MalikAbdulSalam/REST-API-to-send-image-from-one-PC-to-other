from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import os

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # cv2.imshow('image',img)

    path = './'
    cv2.imwrite(os.path.join(path , 'received_file.jpg'), img)
    # cv2.waitKey(0)
    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image recccccccceived. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)