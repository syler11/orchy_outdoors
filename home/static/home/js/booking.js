var dates_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31];


const month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function changeContent() {
var opt = document.getElementById('month');

var opt_text = document.getElementById('month').selectedOptions[0].text;
let month_nam = opt_text.split(" ");
let month_name = month_nam[0];


if (month_name == "August") {
    opt.options[0].value = '2023-08-01';
    opt.text = 'August 2023';
    no_days = 31;
} else if (month_name == "September") {
    opt.options[0].value = '2023-09-01';
    opt.text = 'September 2023';
    no_days = 30;
} else if (month_name == "October") {
    opt.options[0].value = '2023-10-01';
    opt.text = 'October 2023';
    no_days = 31;
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

var day1 = new Date(firstDay);
var day2 = new Date(day1.getTime()+1000*60*60*24*1);
var day3 = new Date(day1.getTime()+1000*60*60*24*2);
var day4 = new Date(day1.getTime()+1000*60*60*24*3);
var day5 = new Date(day1.getTime()+1000*60*60*24*4);
var day6 = new Date(day1.getTime()+1000*60*60*24*5);
var day7 = new Date(day1.getTime()+1000*60*60*24*6);
var day8 = new Date(day1.getTime()+1000*60*60*24*7);
var day9 = new Date(day1.getTime()+1000*60*60*24*8);
var day10 = new Date(day1.getTime()+1000*60*60*24*9);
var day11 = new Date(day1.getTime()+1000*60*60*24*10);
var day12 = new Date(day1.getTime()+1000*60*60*24*11);
var day13 = new Date(day1.getTime()+1000*60*60*24*12);
var day14 = new Date(day1.getTime()+1000*60*60*24*13);
var day15 = new Date(day1.getTime()+1000*60*60*24*14);
var day16 = new Date(day1.getTime()+1000*60*60*24*15);
var day17 = new Date(day1.getTime()+1000*60*60*24*16);
var day18 = new Date(day1.getTime()+1000*60*60*24*17);
var day19 = new Date(day1.getTime()+1000*60*60*24*18);
var day20 = new Date(day1.getTime()+1000*60*60*24*19);
var day21 = new Date(day1.getTime()+1000*60*60*24*20);
var day22 = new Date(day1.getTime()+1000*60*60*24*21);
var day23 = new Date(day1.getTime()+1000*60*60*24*22);
var day24 = new Date(day1.getTime()+1000*60*60*24*23);
var day25 = new Date(day1.getTime()+1000*60*60*24*24);
var day26 = new Date(day1.getTime()+1000*60*60*24*25);
var day27 = new Date(day1.getTime()+1000*60*60*24*26);
var day28 = new Date(day1.getTime()+1000*60*60*24*27);
var day29 = new Date(day1.getTime()+1000*60*60*24*28);
var day30 = new Date(day1.getTime()+1000*60*60*24*29);
var day31 = new Date(day1.getTime()+1000*60*60*24*30);

var dayName1 = day1.toString().split(' ')[0].slice(0, 2);
var dayName2 = day2.toString().split(' ')[0].slice(0, 2);
var dayName3 = day3.toString().split(' ')[0].slice(0, 2);
var dayName4 = day4.toString().split(' ')[0].slice(0, 2);
var dayName5 = day5.toString().split(' ')[0].slice(0, 2);
var dayName6 = day6.toString().split(' ')[0].slice(0, 2);
var dayName7 = day7.toString().split(' ')[0].slice(0, 2);
var dayName8 = day8.toString().split(' ')[0].slice(0, 2);
var dayName9 = day9.toString().split(' ')[0].slice(0, 2);
var dayName10 = day10.toString().split(' ')[0].slice(0, 2);
var dayName11 = day11.toString().split(' ')[0].slice(0, 2);
var dayName12 = day12.toString().split(' ')[0].slice(0, 2);
var dayName13 = day13.toString().split(' ')[0].slice(0, 2);
var dayName14 = day14.toString().split(' ')[0].slice(0, 2);
var dayName15 = day15.toString().split(' ')[0].slice(0, 2);
var dayName16 = day16.toString().split(' ')[0].slice(0, 2);
var dayName17 = day17.toString().split(' ')[0].slice(0, 2);
var dayName18 = day18.toString().split(' ')[0].slice(0, 2);
var dayName19 = day19.toString().split(' ')[0].slice(0, 2);
var dayName20 = day20.toString().split(' ')[0].slice(0, 2);
var dayName21 = day21.toString().split(' ')[0].slice(0, 2);
var dayName22 = day22.toString().split(' ')[0].slice(0, 2);
var dayName23 = day23.toString().split(' ')[0].slice(0, 2);
var dayName24 = day24.toString().split(' ')[0].slice(0, 2);
var dayName25 = day25.toString().split(' ')[0].slice(0, 2);
var dayName26 = day26.toString().split(' ')[0].slice(0, 2);
var dayName27 = day27.toString().split(' ')[0].slice(0, 2);
var dayName28 = day28.toString().split(' ')[0].slice(0, 2);
var dayName29 = day29.toString().split(' ')[0].slice(0, 2);
var dayName30 = day30.toString().split(' ')[0].slice(0, 2);
var dayName31 = day31.toString().split(' ')[0].slice(0, 2);

document.getElementById("day1").innerText = dayName1
document.getElementById("day2").innerText = dayName2
document.getElementById("day3").innerText = dayName3
document.getElementById("day4").innerText = dayName4
document.getElementById("day5").innerText = dayName5
document.getElementById("day6").innerText = dayName6
document.getElementById("day7").innerText = dayName7
document.getElementById("day8").innerText = dayName8
document.getElementById("day9").innerText = dayName9
document.getElementById("day10").innerText = dayName10
document.getElementById("day11").innerText = dayName11
document.getElementById("day12").innerText = dayName12
document.getElementById("day13").innerText = dayName13
document.getElementById("day14").innerText = dayName14
document.getElementById("day15").innerText = dayName15
document.getElementById("day16").innerText = dayName16
document.getElementById("day17").innerText = dayName17
document.getElementById("day18").innerText = dayName18
document.getElementById("day19").innerText = dayName19
document.getElementById("day20").innerText = dayName20
document.getElementById("day21").innerText = dayName21
document.getElementById("day22").innerText = dayName22
document.getElementById("day23").innerText = dayName23
document.getElementById("day24").innerText = dayName24
document.getElementById("day25").innerText = dayName25
document.getElementById("day26").innerText = dayName26
document.getElementById("day27").innerText = dayName27
document.getElementById("day28").innerText = dayName28
document.getElementById("day29").innerText = dayName29
document.getElementById("day30").innerText = dayName30
document.getElementById("day31").innerText = dayName31


}

changeContent()

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