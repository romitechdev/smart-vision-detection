import cv2
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self):
        # Download YOLOv8n (model ringan)
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model.predict(frame, conf=0.5, verbose=False)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = box.conf[0]
                cls = int(box.cls[0])
                label = self.model.names[cls]

                # Gambar bounding box
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)
                cv2.putText(frame, f"{label} {conf:.2f}",
                            (int(x1), int(y1)-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 255, 255), 2)
        return frame
