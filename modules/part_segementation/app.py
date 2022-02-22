import os
import base64
import io
from PIL import Image


MODEL_PATH = os.path.split(__file__)[0]+'/weights/SCOPS-MSHIP.pth'
from .visualizer import Visualizer
vis = Visualizer(MODEL_PATH)

def base64_to_pil(img_base64: str):
    return Image.open(
        io.BytesIO(
            base64.b64decode(
                img_base64.split(',')[-1]
            )
        )
    )
def pil_to_base64(img: Image.Image):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(
        buffered.getvalue()
    ).decode("utf-8")

def segementation(img_base64: str):
    image_pil = base64_to_pil(img_base64)
    seg_result = vis.visualize(image_pil)
    return pil_to_base64(seg_result)


if __name__ == '__main__':
    path = 'cvn_0002.jpg'
    with open(path, 'rb') as f:
        img_data = base64.b64encode(f.read())
    img_data = img_data.decode('utf-8')
    img_data = 'data:image/jpeg;base64,' + img_data
    s=segementation(img_data)
