// Display the current year in the footer
var today = new Date();

function getYear() {
  var year = today.getFullYear();

  document.getElementById("txtYear").innerHTML = year

};

getYear();

function initMap() {
  var location = {
    lat: 56.51734880123457,
    lng: -4.765033244920148
  }; // Replace with your coordinates
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15, // Adjust the zoom level as needed
    center: location
  });
  var marker = new google.maps.Marker({
    position: location,
    map: map,
    title: 'Bridge of Ochy Pods' // Replace with your location name
  });
}

initMap()

$('.carousel').carousel({
  interval: 7000
})