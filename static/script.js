// 
// JavaScript pour l'autcompletion
// 
var requestURL = 'https://api-adresse.data.gouv.fr/search/?q=';
var select = document.getElementById("selection");
window.onload = function() {
    document.getElementById("address").addEventListener("input", autocompleteAdresse, false);
};
function displaySelection(response) {
    if (Object.keys(response.features).length > 0) {
        select.style.display = "block";
        var ul = document.createElement('ul');
        select.appendChild(ul);
        response.features.forEach(function (element) {
            var li = document.createElement('li');
            var ligneAdresse = document.createElement('span');
            var infosAdresse = document.createTextNode(element.properties.postcode + ' ' + element.properties.city);
            ligneAdresse.innerHTML = element.properties.name;
            li.onclick = function () { selectAdresse(element); };
            li.appendChild(ligneAdresse);
            li.appendChild(infosAdresse);
            ul.appendChild(li);
        });
        // select.removeChild(select.firstChild);
    } else {
        select.style.display = "none";
    }
}
function autocompleteAdresse() {
    var inputValue = document.getElementById("address").value;
    if (inputValue) {
        fetch(setQuery(inputValue))
            .then(function (response) {
                response.json().then(function (data) {
                    displaySelection(data);
                });
            });
    } else {
        select.style.display = "none";
    }
};
function selectAdresse(element) {
    document.getElementById("address").value = element.properties.name + " " + element.properties.postcode + " " + element.properties.city;
    select.style.display = "none";
}

function setQuery(value) {
    return requestURL + value + "?type=housenumber&autocomplete=1";
} 


// Validation Email
// function ValidateEmail(inputText){
//     var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
//     if(inputText.value.match(mailformat)){
//         document.form1.text1.focus();
//         return true;
//     }
//     else{
//         alert("Vous avez inscrit une adresse email invalide!");
//         document.form1.text1.focus();
//         return false;
//     }
// };

// 
// JavaScript pour l'autcompletion
// 

