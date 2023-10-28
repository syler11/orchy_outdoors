function sortNumber() {

    faq_choices = document.getElementById("id_faq_choices").value

    accomodation = document.getElementById("accomodation").innerText
    amenities = document.getElementById("amenities").innerText
    miscellanous = document.getElementById("miscellanous").innerText

    console.log(faq_choices)
    console.log(accomodation)
    console.log(amenities)
    console.log(miscellanous)

    if (faq_choices == "ACCOMODATION") {
        sort_number = document.getElementById("sort_number").value = accomodation
    } else if (faq_choices == "AMENITIES") {
        sort_number = document.getElementById("sort_number").value = amenities
    } else {
        sort_number = document.getElementById("sort_number").value = miscellanous
    }
}