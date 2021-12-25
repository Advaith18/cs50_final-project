document.addEventListener("DOMContentLoaded", function() {
    let no = document.querySelector("#no");
    let yes = document.querySelector("#yes");
    let hidden = document.querySelector("#hidden");
    let p = document.querySelector("#yess")
    no.addEventListener("click", function () {
        hidden.type = "text";
        yes.addEventListener("click", function () {
            hidden.type = "hidden";
        });
    });
    hidden.addEventListener("keypress", function (e) {
        if (e.key == "Enter"){
            alert("Feedback has been submitted. Thank You!");
        }    
    }); 
    yes.addEventListener("click", function () {
        alert("Feedback has been submitted. Thank You!");
    });
});
