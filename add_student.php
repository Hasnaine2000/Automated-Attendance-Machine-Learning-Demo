<?php
include "db.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $photo_path = "uploads/" . basename($_FILES["photo"]["name"]);

    if (move_uploaded_file($_FILES["photo"]["tmp_name"], $photo_path)) {
        $sql = "INSERT INTO students (name, photo_path) VALUES ('$name', '$photo_path')";
        if ($conn->query($sql) === TRUE) {
            echo "Student added successfully";
        } else {
            echo "Error: " . $conn->error;
        }
    } else {
        echo "Error uploading file";
    }
}

$conn->close();
?>
