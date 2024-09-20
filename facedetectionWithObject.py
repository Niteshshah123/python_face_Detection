import cv2
import face_recognition
import numpy as np
import os
import time

# Path to the folder where face images will be stored
faces_folder = "known_faces"
if not os.path.exists(faces_folder):
    os.makedirs(faces_folder)

# Load known face encodings and names from the folder
known_face_encodings = []
known_face_names = []

# Load faces from folder
for filename in os.listdir(faces_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        name = os.path.splitext(filename)[0]
        image = face_recognition.load_image_file(os.path.join(faces_folder, filename))
        face_encodings_in_image = face_recognition.face_encodings(image)
        
        if len(face_encodings_in_image) > 0:
            face_encoding = face_encodings_in_image[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)
        else:
            print(f"No faces found in the image: {filename}")

# Initialize variables for processing video frames
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
face_counts = {name: 0 for name in known_face_names}
currently_visible = {name: False for name in known_face_names}
last_seen_time = {name: 0 for name in known_face_names}
FRAME_THRESHOLD = 2

# Load pre-trained MobileNet SSD model for waste detection
net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')

# Capture video from the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame to 1/4 size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (OpenCV uses) to RGB color (face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Process every alternate frame to save computational power
    if process_this_frame:
        # Face detection
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        current_frame_visible = {name: False for name in known_face_names}

        for face_encoding, face_location in zip(face_encodings, face_locations):
            top, right, bottom, left = face_location
            face_height = bottom - top

            distance_to_camera = (14 * 100) / face_height
            if distance_to_camera > 200:
                continue

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches and matches[best_match_index]:
                name = known_face_names[best_match_index]
                current_frame_visible[name] = True
                
                # Waste detection using MobileNet SSD model
                h, w = frame.shape[:2]
                blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                             (300, 300), (104.0, 177.0, 123.0))
                net.setInput(blob)
                detections = net.forward()

                # Loop over detections and check if waste is found
                waste_detected = False
                for i in range(0, detections.shape[2]):
                    confidence = detections[0, 0, i, 2]

                    if confidence > 0.5:  # Confidence threshold
                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                        (startX, startY, endX, endY) = box.astype("int")

                        # Assuming the waste object is detected in the lower part of the frame (in hand)
                        if startY > h // 2:  # If the object is detected in the lower half of the frame
                            waste_detected = True
                            break

                # Increment count if both face and waste are detected
                current_time = time.time()
                if waste_detected and not currently_visible[name]:
                    if current_time - last_seen_time[name] > FRAME_THRESHOLD:
                        face_counts[name] += 1
                    currently_visible[name] = True
                last_seen_time[name] = current_time

            face_names.append(name)

        for name in currently_visible:
            if not current_frame_visible[name]:
                currently_visible[name] = False

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, f"{name}: {face_counts[name]}", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the video feed
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video_capture.release()
cv2.destroyAllWindows()
