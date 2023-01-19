let college_select = document.getElementById('college');
let course_select = document.getElementById('course');

college_select.onchange = function () {
    college = college_select.value;

    fetch('/home/add-student/course/' + college).then(function (response) {
        response.json().then(function () {
            alert(data);
        });
    });
}