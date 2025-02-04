<?php
include "db.php";

$date = date("Y-m-d");
$sql = "SELECT students.name, attendance.date, attendance.status FROM attendance
        JOIN students ON students.student_id = attendance.student_id
        WHERE attendance.date = '$date'";

$result = $conn->query($sql);

$attendance_data = [];
while ($row = $result->fetch_assoc()) {
    $attendance_data[] = $row;
}

echo json_encode($attendance_data);

$conn->close();
?>
