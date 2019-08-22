from load_pretrained_model import load_label,load_pretrained_graph
import os
from PIL import Image
from utils import utils
from utils import visualization_utils as vis_util
import numpy as np
from tensorflow_detection import run_inference_for_single_image

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


def detect_object(TEST_IMAGE_PATHS):
    detection_graph = load_pretrained_graph()
    category_index = load_label()

    # Size, in inches, of the output images.
    IMAGE_SIZE = (12, 8)

    for image_path in TEST_IMAGE_PATHS:
        image = Image.open(image_path)
        # the array based representation of the image will be used later in order to prepare the
        # result image with boxes and labels on it.
        image_np = utils.load_image_into_numpy_array(image)
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        # Actual detection.
        output_dict = run_inference_for_single_image(image_np_expanded, detection_graph)
        # Visualization of the results of a detection.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            category_index,
            instance_masks=output_dict.get('detection_masks'),
            use_normalized_coordinates=True,
            line_thickness=1)
        # plt.figure(figsize=IMAGE_SIZE)
        # plt.imshow(image_np)
        plt.imsave(os.path.join("output",os.path.basename(image_path)),image_np)



