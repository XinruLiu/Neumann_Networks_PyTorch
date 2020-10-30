# Neumann Networks Implementation in PyTorch

Original Tensorflow version: https://github.com/dgilton/neumann_networks_code

Paper: https://arxiv.org/abs/1901.03707

- Unrolled Gradient Descent for CT reconstruction implemented.
- Neumann Network implemented.

Example run command:

```
CUDA_VISIBLE_DEVICES=1,2 python3 main.py \
--bs 32 --outdir out_GD \
--datadir data \
--load -1
```
