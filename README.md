# MRAL
- Our codebase is built upon  [MMDetection](https://github.com/open-mmlab/mmdetection)(2.20.0) and [MMDetection](https://github.com/open-mmlab/mmdetection)(2.20.0) , which can be installed following the offcial instuctions.
## Usage

### Installation
```shell
python setup.py install
```
### Initialize the Model
```shell
/root/miniconda3/bin/python -m torch.distributed.launch  --nproc_per_node=8  --master_port=29500  tools/train.py configs/voc_active_learning/al_train/retinanet_26e.py --work-dir train_num_095ws_init  --launcher pytorch
