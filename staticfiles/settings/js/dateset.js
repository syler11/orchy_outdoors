// Populates the dateset input fields from the month and year selection and saves on database on the settings page
function setDateset() {
    month = document.getElementById("monthSelect")
    month = month.options[month.selectedIndex].text;
    month_no = document.getElementById("monthSelect")
    month_no = month_no.options[month_no.selectedIndex].value;
    if (month_no < 10) {
        month_no = "0" + month_no
    }
    year = document.getElementById("yearSelect")
    year = year.options[year.selectedIndex].text;
    full_date = document.getElementById("full_date")
    month_number = document.getElementById("month_number")
    month_year = document.getElementById("month_year")
    month_number.value = month_no
    month_year.value = month + " " + year
    console.log(month)
    console.log(month_no)
    console.log(year)
    
    function daysInMonth(month_no, year) {
        return new Date(year, month_no, 0).getDate();
    }
    
    full_date.value = year + "-" + month_no + "-" + daysInMonth(month_no, year)
    
}



