import cv2
import os
import numpy as np
from mtcnn import MTCNN

# Initialize MTCNN detector
detector = MTCNN()

# Paths
input_folder = "uploads/"  # Folder where uploaded student images are stored
output_folder = "processed_faces/"  # Folder to save cropped faces

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the uploads folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Detect faces
        faces = detector.detect_faces(image)

        if len(faces) > 0:
            for i, face in enumerate(faces):
                x, y, width, height = face["box"]

                # Crop face
                cropped_face = image[y:y+height, x:x+width]

                # Save cropped face
                face_filename = f"{os.path.splitext(filename)[0]}_face{i}.jpg"
                face_path = os.path.join(output_folder, face_filename)
                cv2.imwrite(face_path, cropped_face)

                print(f"Saved: {face_path}")
        else:
            print(f"No face detected in {filename}")

print("Face detection complete!")
