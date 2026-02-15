/* ================= MENU TOGGLE ================= */
document.addEventListener("DOMContentLoaded", function () {

    const menuBtn = document.getElementById("menuBtn");
    const sidenav = document.getElementById("sidenav");

    if (!menuBtn || !sidenav) {
        console.error("Menu button or sidenav not found");
        return;
    }

    menuBtn.addEventListener("click", function () {
        sidenav.classList.toggle("open");
    });

});


