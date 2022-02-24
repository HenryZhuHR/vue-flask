"""
for run :

pip3 install requests
pip3 flask requests
"""

import imp
from pprint import pprint
import json
from flask.wrappers import Response
import requests

import base64

URL_BASE = 'http://1.116.121.100/api'
URL_BASE = 'http://127.0.0.1:5000/api'



# Test part_seg
url = '%s/part_seg' % URL_BASE
image_path='images/cvn_0001.jpg'
data = {
    'image': base64.b64encode(open(image_path, 'rb').read()).decode()
}
response = requests.post(url, data=json.dumps(data))
pprint(response.json())
def base64_to_pil(img_base64: str):
    from PIL import Image
    import io
    return Image.open(
        io.BytesIO(
            base64.b64decode(
                img_base64.split(',')[-1]
            )
        )
    )
base64_to_pil(response.json()['image']).save('return.png')