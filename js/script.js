document.addEventListener('DOMContentLoaded', function () {
  var checkbox = document.querySelector('input[type="checkbox"]');

  checkbox.addEventListener('change', function () {
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

x.setAttribute("style", "display:none");

}
function affichermanu() {


var y = document.getElementById("automatique");

y.setAttribute("style", "display:block");

}
