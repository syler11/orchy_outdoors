var opt = document.getElementById('monthSelect');

var opt_text = document.getElementById('monthSelect').innerHTML;
let month_nam = opt_text.split(" ");
let month_name = month_nam[0];


if (month_name == "August") {
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

 function modalClick(elem) {
    var text = elem.innerText;
    console.log(text)
    var firstDate = document.getElementById("firstDate").innerText
    console.log(firstDate)
    var fDate = firstDate.slice(0,8)
    console.log(fDate)
    var newDate = fDate + text
    var dep1 = parseInt(text) + 1;
    var firstNight = "1 night - Departing on " + fDate + dep1;
    console.log(firstNight)
    document.getElementById("dateTest").innerText = newDate;
    document.getElementById("dep1").innerText = firstNight;

}