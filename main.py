
import cv2



video_capture = cv2.VideoCapture(0)  # Use 0 for webcam
facedetector = cv2.CascadeClassifier('c:/Users/kanis/Detection_sys/haarcascade_frontalface_default.xml')

frame_count = 0  # List to store previous centers of detected faces
trackers = []  # List of active trackers
entry_count = 0
exit_count = 0
line_position = 250


while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_count += 1
    if frame_count % 10 == 0:  
        # Detect faces in the frame
     faces = facedetector.detectMultiScale(gray, 1.3, 5)

    new_trackers = []
    for tracker, prev_y in trackers:
        success, box = tracker.update(frame)
        if success:
            new_trackers.append((tracker, box))
            x, y, w, h = [int(v) for v in box]
            center_y = y + h // 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (x + w // 2, center_y), 5, (0, 0, 255), -1)

        if prev_y < line_position and center_y >= line_position:
                entry_count += 1
        elif prev_y > line_position and center_y <= line_position:
                exit_count += 1
        new_trackers.append((tracker, center_y))

    trackers = new_trackers
    cv2.line(frame, (0, line_position), (frame.shape[1], line_position), (0, 255, 0), 2)
    cv2.putText(frame, f'Entry: {entry_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Exit: {exit_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('People Counter', frame)
    if cv2.waitKey(10)  == ord('a'):
        break
    
video_capture.release()
cv2.destroyAllWindows()