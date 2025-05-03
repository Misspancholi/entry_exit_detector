# This is a Streamlit app for a people counting application using OpenCV and YOLOv8.
import streamlit as st
import cv2
import time
from people_counter import process_frame

st.set_page_config(page_title="CounterH", layout="centered")
st.title("🏢 CounterH - People Entry/Exit Counter")

# Initialize session states
if "run" not in st.session_state:
    st.session_state.run = False
if "entry" not in st.session_state:
    st.session_state.entry = 0
if "exit" not in st.session_state:
    st.session_state.exit = 0

# Metrics display
col1, col2, col3 = st.columns(3)
col1.metric("🟩 Entry", st.session_state.entry)
col2.metric("🟥 Exit", st.session_state.exit)
col3.metric("🟦 Inside", max(0, st.session_state.entry - st.session_state.exit))

FRAME_WINDOW = st.image([])

# Buttons
col_a, col_b = st.columns(2)
if col_a.button("▶️ Start Camera"):
    st.session_state.run = True
if col_b.button("⏹️ Stop Camera"):
    st.session_state.run = False

# Stream video
if st.session_state.run:
    cap = cv2.VideoCapture(0)

    while st.session_state.run:
        ret, frame = cap.read()
        if not ret:
            st.error("❌ Could not access webcam")
            break

        frame, entry, exit_ = process_frame(frame)
        st.session_state.entry = entry
        st.session_state.exit = exit_

        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        time.sleep(0.05)

    cap.release()
