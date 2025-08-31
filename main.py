import cv2
from detectors.face import FaceDetector
from detectors.hand import HandDetector
from detectors.object import ObjectDetector

def main():
    cap = cv2.VideoCapture(0)

    # 🔹 Perkecil resolusi kamera → biar ringan
    cap.set(3, 640)
    cap.set(4, 480)

    face_detector = FaceDetector()
    hand_detector = HandDetector()
    object_detector = ObjectDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Deteksi wajah
        frame = face_detector.detect(frame)

        # Deteksi tangan & jari
        frame = hand_detector.detect(frame)

        # Deteksi objek
        frame = object_detector.detect(frame)

        # Tampilkan hasil
        cv2.imshow("Face + Hand + Object Detection", frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
