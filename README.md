# Smart Vision - Face, Hand, and Object Detection 🧠📷

Project ini menggunakan **OpenCV**, **MediaPipe**, dan **YOLOv8** untuk mendeteksi **wajah**, **tangan/jari**, dan **objek apa saja** secara **real-time** melalui kamera.

---

## **✨ Fitur Utama**
✅ Deteksi wajah dan senyuman secara real-time  
✅ Deteksi tangan & jari dengan skeleton akurat  
✅ Deteksi berbagai objek menggunakan YOLOv8  
✅ Ukuran kamera kecil (**640x480**) → performa lebih cepat  
✅ Mudah dikembangkan untuk project AI lebih lanjut

---

## **🛠️ Teknologi yang Digunakan**
- [Python 3.11](https://www.python.org/)
- [OpenCV](https://opencv.org/) → deteksi wajah & manipulasi gambar
- [MediaPipe](https://mediapipe.dev/) → deteksi tangan & jari
- [YOLOv8](https://github.com/ultralytics/ultralytics) → deteksi objek real-time

---

## **📂 Struktur Project**
```

smart\_vision/
│── main.py                     # Program utama
│── detectors/
│     ├── face.py               # Deteksi wajah & senyuman
│     ├── hand.py               # Deteksi tangan & jari
│     ├── object.py             # Deteksi objek dengan YOLOv8
│── haarcascades/
│     ├── haarcascade\_frontalface\_default.xml
│     ├── haarcascade\_smile.xml
└── README.md

````

---

## **⚡ Instalasi**

### **1. Clone Repository**
```bash
git clone https://github.com/username/smart_vision.git
cd smart_vision
````

### **2. Install Dependency**

Pastikan Python **3.11** sudah terinstall, lalu jalankan:

```bash
pip install opencv-python mediapipe ultralytics
```

### **3. Jalankan Program**

```bash
python main.py
```

---

## **📸 Cara Kerja**

* **Deteksi Wajah** → OpenCV Haarcascade mendeteksi wajah & menampilkan kotak biru.
* **Deteksi Senyuman** → Jika senyum, muncul tulisan **"Smiling :)"**.
* **Deteksi Jari & Tangan** → MediaPipe menggambar skeleton tangan secara real-time.
* **Deteksi Objek** → YOLOv8 menandai objek di sekitar dengan kotak dan label.

---

## **🎯 Cara Menggunakan**

| Fungsi               | Keterangan                   |
| -------------------- | ---------------------------- |
| Tekan **q**          | Keluar dari program          |
| Lihat kotak biru     | Wajah terdeteksi             |
| Lihat skeleton hijau | Tangan & jari terdeteksi     |
| Kotak kuning + label | Objek terdeteksi oleh YOLOv8 |

---

## **📌 Tips Optimasi**

Kalau performa lambat, kamu bisa:

1. Gunakan model YOLOv8 lebih kecil:

   ```python
   self.model = YOLO("yolov8n.pt")  # nano (paling ringan)
   ```
2. Perkecil ukuran kamera:

   ```python
   cap.set(3, 480)
   cap.set(4, 360)
   ```
3. Batasi objek yang dideteksi:

   ```python
   self.model.predict(frame, classes=[0, 67])  # Contoh: hanya deteksi orang & ponsel
   ```

---

## **🧠 Rencana Pengembangan**

* [ ] Integrasi **face recognition** → kenali wajah spesifik
* [ ] Deteksi **gesture tangan** → kendalikan aplikasi
* [ ] Tambahkan **tracking objek** untuk FPS lebih cepat
* [ ] Integrasi dengan **Flask / Streamlit** untuk dashboard AI

---

## **📄 Lisensi**

Project ini dibuat untuk tujuan pembelajaran dan pengembangan teknologi Computer Vision.
Bebas digunakan dan dimodifikasi.

---

## **👤 Author**

**Romi**
Mahasiswa IT • Computer Vision & AI Enthusiast
