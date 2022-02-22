import base64
import io
from PIL import Image
MODEL_PATH = './weights/SCOPS-MSHIP.pth'

def base64_to_pil(img_base64: str):
    return Image.open(
        io.BytesIO(
            base64.b64decode(
                img_base64.split(',')[-1]
            )
        )
    )


def segementation(img_base64: str):
    image_pil = base64_to_pil(img_base64)


if __name__ == '__main__':
    path = 'cvn_0002.jpg'
    with open(path, 'rb') as f:
        img_data = base64.b64encode(f.read())
    img_data = img_data.decode('utf-8')
    img_data = 'data:image/jpeg;base64,' + img_data