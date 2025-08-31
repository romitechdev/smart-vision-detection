import cv2
import os

class FaceDetector:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.face_cascade = cv2.CascadeClassifier(os.path.join(base_path, "../haarcascades/haarcascade_frontalface_default.xml"))
        self.smile_cascade = cv2.CascadeClassifier(os.path.join(base_path, "../haarcascades/haarcascade_smile.xml"))

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            smiles = self.smile_cascade.detectMultiScale(roi_gray, 1.7, 20)

            if len(smiles) > 0:
                cv2.putText(frame, "Smiling :)", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        return frame
