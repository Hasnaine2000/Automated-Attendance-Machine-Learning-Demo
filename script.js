function addStudent() {
    let name = document.getElementById("studentName").value;
    let photo = document.getElementById("studentPhoto").files[0];

    let formData = new FormData();
    formData.append("name", name);
    formData.append("photo", photo);

    fetch("add_student.php", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => alert(data));
}

function takeAttendance() {
    fetch("take_attendance.php")
    .then(response => response.json())
    .then(data => {
        let table = document.getElementById("attendanceTable");
        table.innerHTML = "";
        data.forEach(record => {
            let row = `<tr>
                <td>${record.name}</td>
                <td>${record.date}</td>
                <td>${record.status}</td>
            </tr>`;
            table.innerHTML += row;
        });
    });
}
