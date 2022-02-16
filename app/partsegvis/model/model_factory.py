from torchvision.models.segmentation import fcn_resnet50, deeplabv3_resnet50

def model_generator(args):
    # create segmentation network
    if args.model == 'FCN':
        model = fcn_resnet50(args.seg_pretrained, num_classes=args.num_parts+1)
    elif args.model == 'DeepLab':
        model = deeplabv3_resnet50(args.seg_pretrained, num_classes=args.num_parts+1)
    else:
        raise NotImplementedError

    return model

def get_1x_lr_params(model):

    for i in model.backbone.modules():
        for j in i.parameters():
            yield j

def get_10x_lr_params(model):

    for i in model.classifier.modules():
        for j in i.parameters():
            yield j

def optim_parameters(model, args):
    return [{'params': get_1x_lr_params(model), 'lr': args.learning_rate},
            {'params': get_10x_lr_params(model), 'lr': 10*args.learning_rate}]