document.addEventListener("DOMContentLoaded", function() {
    let no = document.querySelector("#no");
    let yes = document.querySelector("#yes");
    let hidden = document.querySelector("#hidden");
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
});
