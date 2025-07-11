# Automatic-Number-Plate-Recognition-OCR
This project implements an Automatic Number Plate Recognition (ANPR) system using OpenCV for image processing and Tesseract OCR for character recognition. It detects and extracts license plate information from vehicle images, demonstrating a practical application of computer vision and Optical Character Recognition (OCR)technologies.

# What is OCR and How It Relates to ANPR?

Optical Character Recognition (OCR) is the process of converting printed or handwritten characters in images into machine-readable text. In the context of ANPR, OCR is used to read the alphanumeric characters on a vehicle’s license plate after isolating and extracting the plate from the image.

According to the [JETIR paper on OCR (2021)](https://www.jetir.org/papers/JETIR2104193.pdf) OCR systems typically follow a modular pipeline:

<pre>
Image Acquisition → Preprocessing → Segmentation → Feature Extraction → Classification (Neural Networks)
→ Postprocessing</pre>
This project mirrors those steps in the context of vehicle number plate recognition.

# Technologies Used

Python<br>
OpenCV<br>
Pytesseract (Tesseract OCR)<br>

# How the Code Maps to the OCR Pipeline

| **OCR Module**        | **Project Step Description**                                      |
|------------------------|-------------------------------------------------------------------|
| Image Acquisition      | Load vehicle image using OpenCV                                  |
| Preprocessing          | Grayscale, noise reduction, edge detection                       |
| Segmentation           | Contour detection, top-30 filtering, quadrilateral detection     |
| Feature Extraction     | Cropping the license plate region                                |
| Classification (OCR)   | Use of Tesseract OCR to extract alphanumeric text                |
| Postprocessing         | Display recognized plate optional: format cleanup)                           |

 # Project Structure

<pre>ANPR_OCR
├── car1.jpg              # Input image of a car (MUST be added after cloning)
├── 7.png                 # Cropped license plate (generated at runtime)
├── anpr_ocr.py           # Python script
├── README.md             # Project documentation
└── LICENSE               # MIT License</pre>

 # Getting Started

1. Clone the Repository

   <pre>git clone https://github.com/paimagham/Automatic-Number-Plate-Recognition-OCR
   cd anpr-ocr</pre>
   
3. Add the Test Image<br>
   Download the image file "car1.jpg" from the shared location (provided in the repo) and place it in the ANPR_OCR/ directory.<br>

4. Update Image Path in Code (if needed)<br>
If your file path differs, open anpr_ocr.py and update the image path: img = cv2.imread('./car1.jpg')<br>

4. Install Dependencies<br>
pip install opencv-python pytesseract<br>

Ensure Tesseract OCR is installed and added to your system PATH.

# Sample Output

<pre>Original Image ➝ Vehicle with number plate
Preprocessed Image ➝ Smoothed grayscale image
Edged Image ➝ Detected edges for contour analysis
Contours ➝ Plate contour detected
Cropped Image ➝ Plate area extracted and saved
OCR Result ➝ Extracted text from number plate: Number plate is: MH12DE1XXX</pre>

# Real-World Applications

Vehicle tracking systems<br>
Smart parking systems<br>
Law enforcement and traffic monitoring<br>
Toll booth automation<br>

As noted in the OCR paper, ANPR is a leading practical application of OCR technology, alongside uses like document scanning, passport reading, and signature verification.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

