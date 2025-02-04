import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import cv2
import os
import mysql.connector

# Load the pre-trained FaceNet model
model = load_model("facenet_keras.h5")

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="attendance_system"
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS face_embeddings (
        student_id INT PRIMARY KEY,
        name VARCHAR(100),
        embedding TEXT
    )
""")

# Preprocess image for FaceNet
def preprocess_image(image_path):
    image = Image.open(image_path).resize((160, 160))
    image = np.asarray(image)
    image = (image - 127.5) / 128.0  # Normalize
    return np.expand_dims(image, axis=0)

# Extract embeddings and store them
face_folder = "processed_faces/"
for filename in os.listdir(face_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(face_folder, filename)
        student_name = filename.split("_face")[0]

        # Generate embedding
        face_array = preprocess_image(image_path)
        embedding = model.predict(face_array)[0]
        embedding_str = ",".join(map(str, embedding))  # Convert to string for MySQL storage

        # Store in database
        cursor.execute("INSERT INTO face_embeddings (name, embedding) VALUES (%s, %s)", (student_name, embedding_str))
        conn.commit()
        print(f"Stored embedding for: {student_name}")

# Close database connection
cursor.close()
conn.close()
print("Embeddings stored successfully!")
