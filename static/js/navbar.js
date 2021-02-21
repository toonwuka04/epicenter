const navbar = document.getElementById("navbar");

addEventListener("scroll", function() {
    let offset = this.pageYOffset;
    if (offset < 200)
    {
        let opacity = offset / 200;
        navbar.style = "opacity: " + opacity + ";";
    }
    else 
    {
        navbar.style = "opacity: 1;";
    }

})

// function myClick(){
//     console.log("in function");
//     console.log(document.getElementById('gethelp').value);
//     if(document.getElementById('gethelp').clicked == true){
//         // probably link it to a new page but idk what those are atm
//         console.log('button clicked');
//         location.href = url('../templates/helpform.html');
//     }
//     else if(document.getElementById('havehelp').clicked){
//         // filler
//     }
//     else if(document.getElementById('map').clicked){
//         // filler
//     }

// }