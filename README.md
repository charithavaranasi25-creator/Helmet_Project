🪖 Helmet Detection and Violation Monitoring System

A computer vision-based project developed using Python, YOLO, and OpenCV to detect helmet usage and identify potential helmet violations. The system combines image-based detection with camera monitoring, low-light image enhancement, face recognition, and violation record management to support road safety applications.



📌 Project Overview

Helmet usage plays an important role in reducing the risk of serious head injuries among motorcycle riders. Manually monitoring helmet compliance through traffic cameras can be time-consuming, making automated detection a useful application of computer vision.

This project uses a YOLO-based object detection model to identify helmet and head regions. It also includes a Streamlit interface for image-based detection and a separate monitoring script that processes camera feeds, captures potential violation images, and stores relevant information in a database.



✨ Key Features

* YOLO-Based Detection: Detects helmet and head regions using a trained model.
* Image Detection Interface: Allows users to upload images and view annotated detection results.
* Camera Monitoring: Processes live camera feeds for potential helmet violations.
* Low-Light Enhancement: Uses CLAHE and gamma correction to improve image visibility.
* Face Recognition: Uses DeepFace to compare detected faces with reference images.
* Violation Snapshots: Saves images associated with potential violations.
* Database Management: Stores violation details using SQLite.
* Visual Results: Displays detection outputs with bounding boxes and labels.



🛠️ Technologies Used

* Python – Application development
* YOLO (Ultralytics) – Object detection
* OpenCV – Image processing and camera handling
* DeepFace – Face recognition
* NumPy – Numerical and array operations
* treamlit – Interactive web interface
* SQLite – Violation record storage



📂 Project Structure

Helmet_Project/

│
├── annotated_output1.mp4  
├── enhancemulti.py        
├── final.pt               
├── streamlit-app.py       
└── README.md              



⚙️ Installation and Setup

1. Clone the Repository

```bash
git clone https://github.com/charithavaranasi25-creator/Helmet_Project.git
```

2. Open the Project Directory

```bash
cd Helmet_Project
```

3. Install the Required Libraries

```bash
pip install streamlit ultralytics opencv-python numpy pillow deepface
```

Make sure Python is installed and the `final.pt` model file is present in the project directory.



🚀 Running the Application

Option 1: Image-Based Detection

Start the Streamlit web application using:

```bash
streamlit run streamlit-app.py
```

Steps to use:

1. Open the local URL shown in the terminal.
2. Upload an image in JPG, JPEG, or PNG format.
3. Click Detect Helmet.
4. View the original image alongside the detection result.

Option 2: Camera-Based Monitoring

Run the main monitoring script:

```bash
python enhancemulti.py
```

Steps to use:

1. Connect a camera and configure its camera ID if necessary.
2. Ensure that the YOLO model is available.
3. Create a `faces/` directory containing reference images for face matching.
4. Run the script to process the camera feed.
5. View the detection window and check the saved violation snapshots and database records.

Note: Camera monitoring and image-based detection are implemented separately. The camera monitoring script creates the `violations/` directory and `violations.db` database as needed.



🔍 System Workflow

1. Input Acquisition: Receives an uploaded image or camera feed.
2. Image Enhancement: Applies contrast enhancement and gamma correction to improve visibility in low-light conditions.
3. Object Detection: Uses the YOLO model to locate helmet and head regions.
4. Violation Assessment: Checks the overlap between detected head and helmet regions to identify potential violations.
5. Face Matching: Attempts to match a detected face with available reference images.
6. Snapshot Storage: Saves an image of a potential violation.
7. Database Logging: Records the available details, including timestamp, identity label, image path, and camera ID.
8. Result Display: Shows annotated detections and monitoring results.



📊 Model Information

The project uses the YOLO model weights stored in `final.pt` for object detection.

Model-related details:

* Model format: PyTorch weights (`.pt`)
* Framework: Ultralytics YOLO
* Detection input: Images and camera frames
* Output: Detected regions with bounding boxes and labels

The monitoring script expects the model to detect the classes "helmet" and "head". A head region without sufficient overlap with a detected helmet is treated as a potential violation.

Note: The exact model architecture, training dataset, and measured accuracy should be added only when those details have been verified.



🎯 Applications

* Intelligent traffic monitoring
* Road safety analysis
* Smart city traffic systems
* Helmet compliance monitoring
* Computer vision experimentation
* Academic deep learning projects



🔮 Future Enhancements

* Improve detection accuracy under different lighting and weather conditions.
* Add number plate recognition to associate violations with vehicles.
* Develop a dashboard for viewing and filtering violation records.
* Improve multi-camera processing and object tracking.
* Add violation statistics and downloadable reports.
* Evaluate the system using precision, recall, and mean average precision (mAP).
* Explore secure deployment for practical traffic monitoring environments.



⚠️ Limitations

* Detection performance depends on image quality and model accuracy.
* Face matching requires suitable reference images and may produce incorrect matches.
* A head region without sufficient helmet overlap indicates a potential violation, not necessarily a confirmed violation.
* The current Streamlit interface supports image uploads; camera monitoring is handled by the separate Python script.
* The current camera configuration uses camera ID `0` by default.



🔒 Privacy Considerations

Face images and violation records may contain sensitive personal information. Use the system responsibly, obtain appropriate authorization, and protect stored images and database records.



👩‍💻 Author

Charitha Varanasi

GitHub:https://github.com/charithavaranasi25-creator



📄 License

This project is intended for educational and research purposes. Before redistributing or deploying it, verify the licenses of the model, datasets, and third-party libraries used in the project.
