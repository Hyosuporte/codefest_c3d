#!git clone https://github.com/ultralytics/yolov5  # clone
#%cd yolov5
#%pip install -qr requirements.txt  # install

#import torch
#import utils
#display = utils.notebook_init()  # checks

# Validate YOLOv5s on COCO val
#Aquí reemplazamos el archivo indicado (.yaml)

# Train YOLOv5s on COCO128 for 3 epochs
#!python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt --cache

# 1. Detect

`detect.py` runs YOLOv5 inference on a variety of sources, downloading models automatically from the [latest YOLOv5 release](https://github.com/ultralytics/yolov5/releases), and saving results to `runs/detect`. Example inference sources are:

```shell
python detect.py --source 0  # webcam
                          img.jpg  # image 
                          vid.mp4  # video
                          screen  # screenshot
                          path/  # directory
                         'path/*.jpg'  # glob
                         'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                         'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```
#!python detect.py --weights run/.pt --img 640 --conf 0.25 --source data/images
# display.Image(filename='runs/detect/exp/zidane.jpg', width=600)
#Se pone el directorio donde se encuentra el dataset

