import streamlit as st
import cv2
import time
from people_counter import process_frame

# Set page layout
st.set_page_config(layout="centered")
st.title("👥 People Counter - Entry / Exit System")

# Initialize counters
entry_total = 0
exit_total = 0
inside_count = 0

# Streamlit placeholders for metrics
col1, col2, col3 = st.columns(3)
entry_display = col1.metric("🟩 Entry Count", entry_total)
exit_display = col2.metric("🟥 Exit Count", exit_total)
inside_display = col3.metric("🟦 People Inside", inside_count)

# Video display
FRAME_WINDOW = st.image([])

# Start button
if st.button("▶️ Start Camera"):
    cap = cv2.VideoCapture(0)
    st.info("Press Ctrl+C in terminal to stop the camera.")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access the camera.")
            break

        # Run detection and tracking
        frame, entry, exit_ = process_frame(frame)

        # Update counts
        entry_total += entry
        exit_total += exit_
        inside_count = max(0, entry_total - exit_total)

        # Update metrics
        entry_display.metric("🟩 Entry Count", entry_total)
        exit_display.metric("🟥 Exit Count", exit_total)
        inside_display.metric("🟦 People Inside", inside_count)

        # Show updated video frame
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        time.sleep(0.05)

    cap.release()
