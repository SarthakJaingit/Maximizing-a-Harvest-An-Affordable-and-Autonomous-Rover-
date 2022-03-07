import cv2
from object_detector import ObjectDetector
from object_detector import ObjectDetectorOptions

import utils

def initialize_model():
    high_options = ObjectDetectorOptions(
        num_threads=4,
        score_threshold=0.5, # This is where I can choose confidence thresholds
        max_results=10,
        enable_edgetpu=False)
    high_detector = ObjectDetector(model_path="models/latestModelCER.tflite" , options=high_options)
    low_options = ObjectDetectorOptions(
        num_threads=4,
        score_threshold=0.2, # This is where I can choose confidence thresholds
        max_results=10,
        enable_edgetpu=False)
    low_detector = ObjectDetector(model_path = "models/Feb_6th_Noise_resistant_2nd.tflite", options=low_options)

    return high_detector, low_detector

def run_model() -> bool:

    high_detector, low_detector = initialize_model()

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    alpha, beta = 1.3, 20
    """ https://docs.opencv.org/3.4/d3/dc1/tutorial_basic_linear_transform.html """
    frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

    frame = cv2.flip(frame, 1)
    area_of_frame = frame.shape[0] * frame.shape[1] # It should always be 1920

    detections = list()
    detections.extend(high_detector.detect(frame))
    detections.extend(low_detector.detect(frame))

    cleaned_detections = list()

    for detection in detections:
        xmin = detection.bounding_box.left
        ymin = detection.bounding_box.top
        xmax = detection.bounding_box.right
        ymax = detection.bounding_box.bottom

        area = (xmax - xmin) * (ymax - ymin)
        box_percent = area / area_of_frame

        if box_percent < 0.2:
            cleaned_detections.append(detection)

    image = utils.visualize(frame, cleaned_detections)
    # cv2.imwrite('flask_images/im8.jpg', image)
    cv2.imshow('object_detector', image)
    cv2.waitKey()


    possible_fruits = ['Apples', 'Strawberry', 'Peaches', 'Tomato']

    detected_labels = list()
    for det in detections:
        detected_labels.append(det.categories[0].label)

    if 'Bad_Spots' in detected_labels:
        for det in detected_labels:
            '''Can add additional checks to see if bad spot bbox coord is within any fruit etc.'''
            if det in possible_fruits:
                return True
    if len(detected_labels):
        return True

    return False




if __name__ == "__main__":
    print(run_model())
