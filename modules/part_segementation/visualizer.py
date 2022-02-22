import os
from .model.model_factory import model_generator
import torch
from torchvision.transforms.functional import to_pil_image, normalize, to_tensor
from einops import rearrange
from PIL import Image
import numpy as np
from .utils import BatchColorize

MODEL_PATH = os.path.split(__file__)[0]+'/weights/SCOPS-MSHIP.pth'


class Visualizer:

    def __init__(self, model_path=MODEL_PATH) -> None:
        class TestArgs:
            pass
        args = TestArgs
        args.model = 'FCN'
        args.seg_pretrained = False
        args.num_parts = 4

        self.model = model_generator(args)  # .cuda()
        self.model.load_state_dict(torch.load(
            model_path, map_location=torch.device('cpu')), strict=True)
        self.colorize = BatchColorize(5)

    def visualize(self, img):
        '''
        Args:
            img: PIL Image.
        Return:
            seg_result: PIL Image.
        '''
        img = img.resize((128, 128))
        img = to_tensor(img)

        img = normalize(img, mean=(0.485, 0.456, 0.406),
                        std=(0.229, 0.224, 0.225))
        img = img.unsqueeze(0)
        img = img  # .cuda()

        pred = self.model(img)['out']
        pred = pred.detach().cpu().float().numpy()
        pred = np.asarray(np.argmax(pred, axis=1), dtype=np.int32)
        pred = self.colorize(pred)

        pred = rearrange(pred, "b c h w -> b h w c")
        pred = pred * 255
        pred = pred.squeeze(0)

        img = normalize(img, mean=(0, 0, 0), std=(1/0.229, 1/0.224, 1/0.225))
        img = normalize(img, mean=(-0.485, -0.456, -0.406), std=(1, 1, 1))
        img = rearrange(img, "b c h w -> b h w c")
        img = img * 255
        img = img.squeeze(0)

        pred_pil = Image.fromarray(pred.astype('uint8')).convert('RGB')
        img_pil = Image.fromarray(
            img.cpu().numpy().astype('uint8')).convert('RGB')

        return Image.blend(img_pil, pred_pil, 0.5)
