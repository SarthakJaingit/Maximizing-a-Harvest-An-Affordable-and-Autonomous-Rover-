import cv2
from object_detector import ObjectDetector
from object_detector import ObjectDetectorOptions

def initialize_model():
    options = ObjectDetectorOptions(
        num_threads=4,
        score_threshold=0.5, # This is where I can choose confidence thresholds
        max_results=10,
        enable_edgetpu=False)
    detector = ObjectDetector(model_path="models/latestModelCER.tflite" , options=options)

    return detector

def run_model() -> bool:

    detector = initialize_model()

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    detections = detector.detect(frame)

    possible_fruits = ['Apples', 'Strawberry', 'Peaches', 'Tomato']

    detected_labels = list()
    for det in detections:
        detected_labels.append(det.categories[0].label)

    if 'Bad_Spots' in detected_labels:
        for det in detected_labels:
            '''Can add additional checks to see if bad spot bbox coord is within any fruit etc.'''
            if det in possible_fruits:
                return True

    return False




if __name__ == "__main__":
    print(run_model())
