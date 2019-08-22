# Object detection using tensorflow

<p> This model is the collection of only the necessary  files for detecting object on image using tensorflow. </p>

![Object detection](https://github.com/mahbubcseju/object_detection_using_tensorflow/blob/master/output/52429027.jpg)

## Installation:

1. Clone the repository first.
2. Now enter this repository.
  
   - cd object_detection_using_tensorflow/
3. Now create virtual environment on this directory.
   
   - virtualenv .
4. Now activate the environement.
  
   - source bin/activate

5. Now install the dependencies.
   
   ``` bash
   # For CPU
   pip install tensorflow
   pip install pillow
   pip install matplotlib
   ```
## Run

- To detect object on a single image, pass the image path.
    ``` bash
     python3 main.py test_imaes/image1.jpg
    ```
- To detect object on multiple images, pass the directory path.
    ``` bash
     python3 main.py test_imaes/
    ```
    
 ## Output
 
 <p> Output will be saved on output directory after detecting object. <p>
 
 ## which objects can be detected?
 
 As in this projects I mainly used the ssd_mobilenet_v1_coco_2018_01_28 pretrained model, this model is based on coco dataset.
 And in coco dataset there are data of 91 types of objects.
 
person, bicycle, car, motorcycle, airplane, bus, train, truck, boat, traffic, light, fire, hydrant, stop, sign, parking, meter, bench, bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee, skis, snowboard, sports, ball, kite, baseball, bat, baseball, glove, skateboard, surfboard, tennis, racket, bottle, wine, glass, cup, fork, knife, spoon, bowl, banana, apple, sandwich, orange, broccoli, carrot, hot, dog, pizza, donut, cake, chair, couch, potted, plant, bed, dining, table, toilet, tv, laptop, mouse, remote, keyboard, cell, phone, microwave, oven, toaster, sink, refrigerator, book, clock, vase, scissors, teddy, bear, hair, drier, toothbrush