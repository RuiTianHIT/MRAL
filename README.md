# MRAL
Our codebase is built upon [MMDetection(2.20.0)](https://mmdetection.readthedocs.io/zh-cn/v2.20.0/get_started.html) and [PPAL](https://github.com/ChenhongyiYang/PPAL), which can be installed following the offcial instuctions.

# Usage
## Installation
`python setup.py install`

# Initialize the Model
`/root/miniconda3/bin/python -m torch.distributed.launch  --nproc_per_node=8  --master_port=29500  tools/train.py configs/voc_active_learning/al_train/retinanet_26e.py --work-dir train_num_095ws_init  --launcher pytorch`

