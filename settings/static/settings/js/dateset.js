

function setDateset() {
    month = document.getElementById("monthSelect")
    month = month.options[month.selectedIndex].text;
    month_no = document.getElementById("monthSelect")
    month_no = month_no.options[month_no.selectedIndex].value;
    year = document.getElementById("yearSelect")
    year = year.options[year.selectedIndex].text;
    month_number = document.getElementById("month_number")
    month_year = document.getElementById("month_year")
    month_number.value = month_no
    month_year.value = month + " " + year
    console.log(month)
    console.log(month_no)
    console.log(year)
}