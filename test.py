
# import cv2
# import face_recognition
# import numpy as np
# import os
# import time
# import requests

# # Path to the folder where face images will be stored
# faces_folder = "known_faces"
# if not os.path.exists(faces_folder):
#     os.makedirs(faces_folder)

# # Load known face encodings and names from the folder
# known_face_encodings = []
# known_face_names = []

# # Load faces from folder
# for filename in os.listdir(faces_folder):
#     if filename.endswith(".jpg") or filename.endswith(".jpeg"):
#         name = os.path.splitext(filename)[0]
#         image = face_recognition.load_image_file(os.path.join(faces_folder, filename))
#         face_encodings_in_image = face_recognition.face_encodings(image)

#         if len(face_encodings_in_image) > 0:
#             face_encoding = face_encodings_in_image[0]
#             known_face_encodings.append(face_encoding)
#             known_face_names.append(name)
#         else:
#             print(f"No faces found in the image: {filename}")

# # Initialize variables for processing video frames
# face_locations = []
# face_encodings = []
# face_names = []
# process_this_frame = True
# face_counts = {name: 0 for name in known_face_names}
# currently_visible = {name: False for name in known_face_names}  # Track face visibility status
# last_seen_time = {name: 0 for name in known_face_names}  # Track last time face was seen
# FRAME_THRESHOLD = 2  # Minimum number of seconds the person must be out of frame before the count increases

# # URL of the ESP32 video stream
# video_stream_url = 'http://<esp32_ip>/video'

# # Capture video from the ESP32 stream
# cap = cv2.VideoCapture(video_stream_url)

# while True:
#     # Read a single frame from the video stream
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame. Check the video stream.")
#         break

#     # Resize frame to 1/4 size for faster processing
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#     # Convert the image from BGR color (OpenCV uses) to RGB color (face_recognition uses)
#     rgb_small_frame = small_frame[:, :, ::-1]

#     # Process every alternate frame to save computational power
#     if process_this_frame:
#         # Find all the faces and face encodings in the current frame
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         face_names = []
#         current_frame_visible = {name: False for name in known_face_names}  # Track faces in the current frame

#         for face_encoding, face_location in zip(face_encodings, face_locations):
#             top, right, bottom, left = face_location
#             face_height = bottom - top

#             # Assuming face width ~ 14 cm, and known focal length of camera
#             distance_to_camera = (14 * 100) / face_height
#             if distance_to_camera > 200:
#                 continue

#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"

#             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)

#             if matches and matches[best_match_index]:
#                 name = known_face_names[best_match_index]
#                 current_frame_visible[name] = True
                
#                 current_time = time.time()
#                 if not currently_visible[name]:
#                     if current_time - last_seen_time[name] > FRAME_THRESHOLD:
#                         face_counts[name] += 1
#                     currently_visible[name] = True
#                 last_seen_time[name] = current_time
#             else:
#                 top, right, bottom, left = face_location
#                 face_image = frame[top*4:bottom*4, left*4:right*4]
#                 new_name = f"person_{len(known_face_names)+1}"
#                 file_path = os.path.join(faces_folder, f"{new_name}.jpg")
#                 cv2.imwrite(file_path, face_image)

#                 known_face_encodings.append(face_encoding)
#                 known_face_names.append(new_name)
#                 face_counts[new_name] = 1
#                 currently_visible[new_name] = True
#                 current_frame_visible[new_name] = True
#                 last_seen_time[new_name] = time.time()
#                 name = new_name

#             face_names.append(name)

#         for name in currently_visible:
#             if not current_frame_visible[name]:
#                 currently_visible[name] = False

#     process_this_frame = not process_this_frame

#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, f"{name}: {face_counts[name]}", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture
# cap.release()
# cv2.destroyAllWindows()
