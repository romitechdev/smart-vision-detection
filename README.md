# Smart Vision - Face, Hand, and Object Detection 🧠📷

This project uses **OpenCV**, **MediaPipe**, and **YOLOv8** to detect **faces**, **hands/fingers**, and **any objects** in **real-time** through a camera.

---

## **✨ Main Features**
✅ Real-time face and smile detection  
✅ Hand & finger detection with an accurate skeleton  
✅ Detection of various objects using YOLOv8  
✅ Small camera size (**640x480**) → faster performance  
✅ Easy to extend for further AI projects

---

## **🛠️ Technologies Used**
- [Python 3.11](https://www.python.org/)
- [OpenCV](https://opencv.org/) → face detection & image manipulation
- [MediaPipe](https://mediapipe.dev/) → hand & finger detection
- [YOLOv8](https://github.com/ultralytics/ultralytics) → real-time object detection

---

## **📂 Project Structure**
```

smart\_vision/
│── main.py                     # Main program
│── detectors/
│     ├── face.py               # Face & smile detection
│     ├── hand.py               # Hand & finger detection
│     ├── object.py             # Object detection with YOLOv8
│── haarcascades/
│     ├── haarcascade\_frontalface\_default.xml
│     ├── haarcascade\_smile.xml
└── README.md

````

---

## **⚡ Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/username/smart_vision.git
cd smart_vision
````

### **2. Install Dependencies**

Make sure Python **3.11** is installed, then run:

```bash
pip install opencv-python mediapipe ultralytics
```

### **3. Run the Program**

```bash
python main.py
```

---

## **📸 How It Works**

* **Face Detection** → OpenCV Haarcascade detects faces and draws a blue box.
* **Smile Detection** → When a smile is detected, the text **"Smiling :)"** appears.
* **Finger & Hand Detection** → MediaPipe draws the hand skeleton in real-time.
* **Object Detection** → YOLOv8 marks nearby objects with boxes and labels.

---

## **🎯 How to Use**

| Function               | Description                   |
| -------------------- | ---------------------------- |
| Press **q**          | Exit the program          |
| Blue box appears     | Face detected             |
| Green skeleton appears | Hands & fingers detected     |
| Yellow box + label | Object detected by YOLOv8 |

---

## **📌 Optimization Tips**

If performance is slow, you can:

1. Use a smaller YOLOv8 model:

    ```python
    self.model = YOLO("yolov8n.pt")  # nano (lightest)
    ```
2. Reduce the camera resolution:

    ```python
    cap.set(3, 480)
    cap.set(4, 360)
    ```
3. Limit the objects to be detected:

    ```python
    self.model.predict(frame, classes=[0, 67])  # Example: only detect people & phones
    ```

---

## **🧠 Development Roadmap**

* [ ] Integrate **face recognition** → recognize specific faces
* [ ] **Hand gesture** detection → control applications
* [ ] Add **object tracking** for higher FPS
* [ ] Integration with **Flask / Streamlit** for an AI dashboard

---

## **📄 License**

This project was created for educational purposes and Computer Vision technology development.
Free to use and modify.

---

## **👤 Author**

**Romi**
IT Student • Computer Vision & AI Enthusiast

<!-- last-updated -->
_Last updated: 2026-09-05_

