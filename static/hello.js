document.addEventListener("DOMContentLoaded", function() {
    let no = document.querySelector("#no");
    let yes = document.querySelector("#yes");
    let hidden = document.querySelector("#hidden");
    no.addEventListener("click", function () {
        hidden.type = "text";
    });
    hidden.addEventListener("onsubmit", function () {
        alert("Feedback has been submitted. Thank You!");
    }); 
});
