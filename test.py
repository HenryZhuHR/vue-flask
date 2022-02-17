"""
for run :

pip3 install requests
pip3 flask requests
"""

from pprint import pprint
import json
from flask.wrappers import Response
import requests

import base64

URL_BASE = 'http://1.116.121.100/api'
URL_BASE = 'http://127.0.0.1:2021/api'



# Test part_seg
url = '%s/part_seg' % URL_BASE
image_path='source/images/cvn_0001.jpg'
data = {
    'image': base64.b64encode(open(image_path, 'rb').read()).decode()
}
response = requests.post(url, data=json.dumps(data))
pprint(response.json())
