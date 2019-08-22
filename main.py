import sys
from pathlib import Path
from object_detection import detect_object
import os,fnmatch

if(len(sys.argv)==2):
    action = sys.argv[1]
    test_image_path = []
    my_file = Path(action)
    if my_file.is_file():
        test_image_path.append(action)
        detect_object(test_image_path)
    else:
        test_image_path = []
        for file in os.listdir(action):
            if fnmatch.fnmatch(file, '*.jpg'):
                test_image_path.append(os.path.join(action,str(file)))
        detect_object(test_image_path)
else:
    print("Send test image directory or image path")