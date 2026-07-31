const themeButton = document.querySelector("#theme-button");

themeButton.addEventListener("click", function () {
    document.body.classList.toggle("dark-theme");
});