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