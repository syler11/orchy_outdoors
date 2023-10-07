var nights = document.getElementById("nights").value;
var rate_rm1 = document.getElementById("rate_rm1").innerHTML
document.getElementById("rate_total").innerText = rate_rm1
document.getElementById("nights").value = 1;
var arrival_range = document.getElementById("arrival_range")

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
    var arrival_date1 =  document.getElementById("arrivalDate1").innerHTML;
    var depDate1 = document.getElementById("depDate1").innerHTML;
    var depDate2 = document.getElementById("depDate2").innerHTML;
    var depDate3 = document.getElementById("depDate3").innerHTML;

    console.log(arrival_date1 + " " + depDate1 + " " + depDate2 + " " + depDate3)
    

    if (select_nights == 2) {
        arrival_range.value = arrival_date1 + " " + depDate1
    } else if (select_nights == 3) {
        arrival_range.value = arrival_date1 + " " + depDate1 + " " + depDate2
    } else  if ( select_nights == 4) {
        arrival_range.value = arrival_date1 + " " + depDate1 + " " + depDate2 + " " + depDate3
    }
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
