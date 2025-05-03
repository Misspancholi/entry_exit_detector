# This script uses OpenCV to count the number of people entering and exiting a specified area in a video stream.
import cv2
import numpy as np

# Load face detector DNN model
prototxt_path = "face_detector/deploy.prototxt"
weights_path = "face_detector/res10_300x300_ssd_iter_140000.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt_path, weights_path)

line_position = 250
entry_total = 0
exit_total = 0
trackers = {}
id_counter = 0
prev_centers = {}

def process_frame(frame):
    global entry_total, exit_total, trackers, id_counter, prev_centers

    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    boxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.6:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")
            boxes.append((x1, y1, x2 - x1, y2 - y1))

    current_trackers = {}
    for (x, y, w_box, h_box) in boxes:
        center = (x + w_box // 2, y + h_box // 2)
        assigned_id = None

        for id_, prev_center in prev_centers.items():
            dist = np.linalg.norm(np.array(center) - np.array(prev_center))
            if dist < 50:
                assigned_id = id_
                break

        if assigned_id is None:
            assigned_id = id_counter
            id_counter += 1

        prev_center_y = prev_centers.get(assigned_id, (0, 0))[1]
        if prev_center_y < line_position and center[1] >= line_position:
            entry_total += 1
        elif prev_center_y > line_position and center[1] <= line_position:
            exit_total += 1

        current_trackers[assigned_id] = center
        cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
        cv2.putText(frame, f"ID: {assigned_id}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    prev_centers = current_trackers

    # Draw virtual line
    cv2.line(frame, (0, line_position), (frame.shape[1], line_position), (0, 255, 255), 2)
    return frame, entry_total, exit_total
