import argparse
import os
import sys

import torch
import torchvision.transforms as transforms
import torchvision.datasets as dset

from gradient_descent_network import *


parser = argparse.ArgumentParser()
parser.add_argument('--datadir', required=True, default='data', help='directory to dataset')
parser.add_argument('--outdir', required=False, default='out', help='output dir')
parser.add_argument('--epochs', type=int, default=100, help='Number of epochs', dest='epochs')
parser.add_argument('--blocks', type=int, default=6, help='Number of blocks', dest='blocks')
parser.add_argument('--bs', type=int, default=64, help='Batch size')
parser.add_argument('-lr', type=float, default=1e-3, help='Learning rate', dest='lr')
parser.add_argument('--height', required=False, type=int, default=320, help='the height of the input image to network. Cannot change for now.')
parser.add_argument('--width', required=False, type=int, default=180, help='the width of the input image to network. Cannot change for now.')
parser.add_argument('--load', dest='load', type=int, default=-1, help='Load model from a .pth file by epoch #')
args = parser.parse_args()

if args.datadir is None:
    raise ValueError("`datadir` parameter is required for dataset")

dataset = dset.ImageFolder(root=args.datadir,
                            transform=transforms.Compose([  # to 0~1
                                transforms.Resize((args.height,args.width)),
                                transforms.Grayscale(),
                                transforms.ToTensor(),
#                                 transforms.Normalize((0.5,), (0.5,))
                            ]))
assert dataset
print(f"Dataset contains {len(dataset)} images.")
dataloader = torch.utils.data.DataLoader(dataset, shuffle=True, batch_size=args.bs, num_workers=4)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device {device}.')

try:
    if not os.path.exists(os.path.join(args.outdir, 'ckpt')):
        os.makedirs(os.path.join(args.outdir, 'ckpt'))
        print('Created checkpoint directory')
except OSError:
    pass    

try:
    m = GradientDescentNet(args=args, dataloader=dataloader, device=device)
    m.train()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)