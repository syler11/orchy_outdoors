var opt = document.getElementById('monthSelect');

var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = yyyy + "-"+ mm + '-' + dd;

var  month03 = document.getElementById("month03")
var  month04 = document.getElementById("month04")
var  month05 = document.getElementById("month05")
var  month06 = document.getElementById("month06")
var  month07 = document.getElementById("month07")
var  month08 = document.getElementById("month08")
var  month09 = document.getElementById("month09")
var  month10 = document.getElementById("month10")
var  month11 = document.getElementById("month11")

if (today > month03.value) {
    month9.classList.add("d-none")
}
if (today > month04.value) {
    month9.classList.add("d-none")
}
if (today > month05.value) {
    month9.classList.add("d-none")
}
if (today > month06.value) {
    month9.classList.add("d-none")
}
if (today > month07.value) {
    month9.classList.add("d-none")
}
if (today > month08.value) {
    month9.classList.add("d-none")
}
if (today > month09.value) {
    month9.classList.add("d-none")
}
if (today > month10.value) {
    month10.classList.add("d-none")
}

var opt_text = opt.innerHTML;
let month_nam = opt_text.split(" ");
let month_name = month_nam[0];


if (month_name == "March") {
    no_days = 31;
} else if (month_name == "April") {
    no_days = 30;
} else if (month_name == "May") {
    no_days = 31;
} else if (month_name == "June") {
    no_days = 30;
} else if (month_name == "July") {
    no_days = 31;
} else if (month_name == "August") {
    no_days = 31;
} else if (month_name == "September") {
    no_days = 30;
} else if (month_name == "October") {
    no_days = 31;
} else if (month_name == "November") {
    no_days = 30;
}

if (no_days == 30) {
    document.getElementById("day31").classList.add("d-none")
    document.getElementById("podA_31").classList.add("d-none")
    document.getElementById("podB_31").classList.add("d-none")
}  else if (no_days == 29) {
    document.getElementById("day31").classList.add("d-none")
    document.getElementById("podA_31").classList.add("d-none")
    document.getElementById("podB_31").classList.add("d-none")
    document.getElementById("day30").classList.add("d-none")
    document.getElementById("podA_30").classList.add("d-none")
    document.getElementById("podB_30").classList.add("d-none")
} else {
    document.getElementById("day31").classList.remove("d-none")
    document.getElementById("podA_31").classList.remove("d-none")
    document.getElementById("podB_31").classList.remove("d-none")
}


let firstDay = opt.value
//let firstDay_format = firstDay.slice(9, 10)
//document.getElementById("podA_1").innerText = firstDay_format
//document.getElementById("podB_1").innerText = firstDay_format

//let secondDay = parseInt(firstDay_format) + 1
//document.getElementById("podA_2").innerText = secondDay

var nights = document.getElementById("nights").value;
var rate_rm1 = document.getElementById("rate_rm1").innerHTML
document.getElementById("rate_total").innerText = rate_rm1

function changeBooking() {
    var nights = document.getElementById("nights").value;
    var rate_rm1 = document.getElementById("rate_rm1").innerHTML
    total = parseInt(nights) * parseInt(rate_rm1)
    document.getElementById("rate_total").innerText = total
} 

function display_guestInfo(event) {
    var guest_info = document.getElementById("guest_info")
    var booking_step = document.getElementById("booking_step")
    var booking_submit = document.getElementById("booking_submit")
    booking_step.classList.add("d-none");
    guest_info.classList.remove("d-none");
    booking_submit.classList.remove("d-none");
}

// Code will prevent to close #availablity modal when the booking_step event button is clickedd
$('#booking_step').off('click').click(function(clickEvent){
    clickEvent.preventDefault();
    clickEvent.stopPropagation();
 });