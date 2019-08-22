
import os
# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH = os.path.join('ssd_mobilenet_v1_coco_2018_01_28', 'frozen_inference_graph.pb')

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtx')