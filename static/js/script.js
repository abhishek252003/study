// Search filter
document.getElementById("search-bar").addEventListener("input", function() {
    var filter = this.value.toUpperCase();
    var courseLinks = document.getElementsByClassName("course-link");

    for (var i = 0; i < courseLinks.length; i++) {
        var text = courseLinks[i].textContent || courseLinks[i].innerText;
        courseLinks[i].style.display = text.toUpperCase().includes(filter) ? "" : "none";
    }
});

// Hamburger toggle
const hamburger = document.getElementById("hamburger-icon");
const navbarLinks = document.getElementById("navbar-links");

hamburger.addEventListener("click", () => {
    navbarLinks.classList.toggle("hidden");
});
