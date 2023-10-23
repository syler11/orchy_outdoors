const currentList = document.getElementById("currentList");
const allList = document.getElementById("allList");
const cancelledList = document.getElementById("cancelledList");
const currentListSelect = document.getElementById("currentListSelect");
const allListSelect = document.getElementById("allListSelect");
const cancelledListSelect = document.getElementById("cancelledListSelect");


function reservationSelect() {
    if (currentListSelect.checked) {
        allList.classList.add("d-none");
        cancelledList.classList.add("d-none");
        currentList.classList.remove("d-none");
    } else if (allListSelect.checked) {
        allList.classList.remove("d-none");
        cancelledList.classList.add("d-none");
        currentList.classList.add("d-none");
    } else {
        allList.classList.add("d-none");
        currentList.classList.add("d-none");
        cancelledList.classList.remove("d-none");
    }
}