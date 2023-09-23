var nights = document.getElementById("nights").value;
var rate_rm1 = document.getElementById("rate_rm1").innerHTML
document.getElementById("rate_total").innerText = rate_rm1
document.getElementById("nights").value = 1;

function changeBooking() {
    var select_nights = document.getElementById("select_nights").value;
    var rate_rm1 = document.getElementById("rate_rm1").innerHTML
    total = parseInt(select_nights) * parseInt(rate_rm1)
    document.getElementById("rate_total").innerText = total
    var test_nights = document.getElementById("select_nights").value
    document.getElementById("nights").value = test_nights;
    var occupancy = document.getElementById("occupancy").value;
    console.log(occupancy)
    document.getElementById("pax").value = occupancy
} 

function checkOccupancy() {
    var occupancy = document.getElementById("occupancy").value;
    let test = document.getElementById("occupancy");
    console.log(occupancy)
    if (occupancy == 0) {
        if (test.checkValidity() === false) {
            test.reportValidity();
            return;
        }

    } else if (occupancy > 2) {
        alert("Max occupancy is 2")

    } else {
        document.getElementById("occButton").setAttribute('data-toggle', "modal")
    }
    // Cost
    var total_cost = document.getElementById("rate_total").innerHTML
    console.log(total_cost)
    document.getElementById("total_cost").value = total_cost
}

// Occupancy
