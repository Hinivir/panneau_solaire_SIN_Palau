document.addEventListener('DOMContentLoaded', function() {
    var checkbox = document.querySelector('input[type="checkbox"]');

    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            // do this
            console.log('Sécurisé');
            document.getElementById("etatSwitch").innerHTML = "Sécurisé";
        } else {
            // do that
            console.log('Non sécurisé');
            document.getElementById("etatSwitch").innerHTML = "Non sécurisé";
        }
    });
});

function cacherauto() {


    var x = document.getElementById("automatique");
    var v = document.getElementById("automatiqueswitch");
    x.setAttribute("style", "display:none");
    v.setAttribute("style", "display:none");
    console.log("auto")
}

function affichermanu() {

    var y = document.getElementById("automatique");
    var z = document.getElementById("automatiqueswitch");
    y.setAttribute("style", "display:block");
    z.setAttribute("style", "display:block");
    console.log("manu")
}

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}