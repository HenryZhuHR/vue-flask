import flask
import json
import base64
import flask_cors

app=flask.Flask(__name__)

flask_cors.CORS(app, resources={r"/api/*": {"origins": "*"}})

_RETURN_INVALID_REQUEST_PARAMETER = json.dumps({
    'Error': {
        'Code': 'NotParameterGet',
                'Message': 'Invalid request parameter got, check parameter'
    }
})



from modules.part_segementation.app import segementation
@app.route('/api/part_seg', methods=['post'])
def part():
    """
        Parameter
        ---
            - `image` (base64)
    """

    if not flask.request.data:  # check if valid data
        return _RETURN_INVALID_REQUEST_PARAMETER
    # parase paramter
    data_json = json.loads(flask.request.data.decode('utf-8'))


    if 'image' not in data_json:
        return json.dumps({
            'Error': {
                'Code': 'Part_seg.LossParameter',
                'Message': 'parameter "image" not found in request'
            }
        })
    try:
        # image_data = base64.b64decode(data_json['image'])
        # SELECT_IMAGE = image_data
        return json.dumps({
            'image':'data:image/jpeg;base64,'+segementation(data_json['image'])
        })
    except:
        return json.dumps({
            'Error': {
                'Code': 'UploadImage.DecodeImageError',
                'Message': 'decode image error'
            }
        })


if __name__=='__main__':
    app.run(
        host='127.0.0.1',
        # host='192.168.1.131',
        # port=2021
        )