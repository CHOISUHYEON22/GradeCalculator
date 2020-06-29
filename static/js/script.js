function mouseOverSelf() {
    let img = document.getElementById("changeImg1");
    let m = document.getElementById("changeColor1");
    img.src = "{{ url_for('static', filename='img/edit_w.svg') }}"
    m.style.color = "white";
}

function mouseOutSelf() {
    let img = document.getElementById("changeImg1");
    let m = document.getElementById("changeColor1");
    img.src = "{{ url_for('static', filename='img/edit.svg') }}"
    m.style.color = "black";
}

function mouseOverExcel() {
    let img = document.getElementById("changeImg2");
    let m = document.getElementById("changeColor2");
    img.src = "{{ url_for('static', filename='img/spreadsheet_w.svg') }}"
    m.style.color = "white";
}

function mouseOutExcel() {
    let img = document.getElementById("changeImg2");
    let m = document.getElementById("changeColor2");
    img.src = "{{ url_for('static', filename='img/spreadsheet.svg') }}"
    m.style.color = "black";
}
