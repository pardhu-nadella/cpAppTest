import cv2
import streamlit as st

st.title("Video Stream with Streamlit")

# Set up the video capture
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_BUFFERSIZE, 1)

stframe = st.empty()

# Stream the video
while True:
    ret, frame = video.read()
    if not ret:
        break
    # Convert the frame to RGB (Streamlit uses RGB images)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    stframe.image(frame, channels="RGB")

# Release the video capture object
video.release()
