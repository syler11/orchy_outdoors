// Display the current year in the footer
var today = new Date();

function getYear() {
  var year = today.getFullYear();

  document.getElementById("txtYear").innerHTML = year

};

getYear();

