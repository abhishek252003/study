document.getElementById("search-bar").addEventListener("input", function() {
    var filter = this.value.toUpperCase();
    var courseLinks = document.getElementsByClassName("course-link");

    for (var i = 0; i < courseLinks.length; i++) {
        var text = courseLinks[i].textContent || courseLinks[i].innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            courseLinks[i].style.display = "";
        } else {
            courseLinks[i].style.display = "none";
        }
    }
});
// Get the hamburger icon and the navbar links
const hamburger = document.getElementById("hamburger-icon");
const navbarLinks = document.getElementById("navbar-links");

// Toggle the "active" class when the hamburger is clicked
hamburger.addEventListener("click", () => {
    navbarLinks.classList.toggle("active");
});
