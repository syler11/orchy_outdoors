var nights = document.getElementById("nights").value;
var rate_rm1 = document.getElementById("rate_rm1").innerHTML
document.getElementById("rate_total").innerText = rate_rm1

function changeBooking() {
    var nights = document.getElementById("nights").value;
    var rate_rm1 = document.getElementById("rate_rm1").innerHTML
    total = parseInt(nights) * parseInt(rate_rm1)
    document.getElementById("rate_total").innerText = total
} 