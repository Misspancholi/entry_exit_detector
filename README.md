# 🧍‍♂️🧍‍♀️ People Counter using Face Detection (Entry/Exit Tracker)

This project detects faces in a webcam feed and counts the number of people entering and exiting a virtual line (like a mall entrance). It uses OpenCV's Deep Neural Network (DNN) module to track faces and maintain a live count of people inside.

✅ Built as part of a data analysis internship project.

---

📌 Features

- Real-time face detection using OpenCV DNN
- Counts people crossing a virtual line (Entry/Exit)
- Tracks people using unique IDs
- Keeps live count of people currently inside
- Displays stats in a clean Streamlit web UI
- Optionally export data using `pandas`

---

🧰 Tech Stack

- Python 3
- OpenCV (cv2)
- Streamlit
- Pandas

---

## 📁 Project Structure
Detection_sys/ 
├── detector.py # Main script for face detection and tracking
├── app.py
# Streamlit UI app to display results 
├── face_detector/
# Folder with DNN model files
├── deploy.prototxt 
└──res10_300x300_ssd_iter_140000.caffemodel├── people_data.csv # Auto-generated count log

👨🏻‍💻Install dependencies 
pip install opencv-python opencv-python-headless streamlit pandas

##Add the model files:
Create a folder named face_detector/ and download the following files into it:

-deploy.prototxt

-res10_300x300_ssd_iter_140000.caffemodel

🔧How It Works:

A horizontal line is drawn on the screen to represent the "door".
If a person's face (center point) crosses the line from top to bottom, it's considered an Entry.
If they cross from bottom to top, it's counted as an Exit.
A count is maintained and displayed for:
Total Entries
Total Exits
People currently inside

⏳Future Enhancements:

Improve tracking with object detection or multi-object tracking (Deep SORT)
Add a dashboard to analyze peak times
Store data in a database
Add alerts if max capacity is reached

🙋🏻Author
Kanishka Pancholi 
Data Analyst Intern | Python & OpenCV Enthusiast
LinkedIn • GitHub

📄 License
This project is open-source and available under the MIT License.

