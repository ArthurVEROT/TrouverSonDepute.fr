//
// JavaScript pour l'autcompletion
//

const requestURL = "https://api-adresse.data.gouv.fr/search/?q=";

const inputAddress = document.querySelector("#inputAddress")
const divAddresses = document.querySelector("#divAddresses");
const outputAddresses = document.querySelector("#outputAddresses")
const searchButton = document.querySelector("#searchButton")
    

document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('keypress', function (e) {
            if (e.keyCode === 13 || e.which === 13) {
                e.preventDefault();
                return false;
            }
            
        });
});


document.addEventListener('DOMContentLoaded', function() {
    inputAddress.onkeyup = findAddress;
});

function findAddress() {
    let inputValue = inputAddress.value;

    if (inputValue) {
        requestAPI = (requestURL + inputValue + "?type=lable&autocomplete=1")
        console.log(requestAPI);
        fetch(requestAPI)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            displayAddresses(data);
        })
    } else {
        divAddresses.style.display = "none";
    }
}

function displayAddresses(response) {
    if (Object.keys(response.features).length > 0) {
        divAddresses.style.display = "block";

        response.features.forEach(function (element) {
            var li = document.createElement("li");
            var addressLine = document.createElement("span");
            var cityLine = document.createTextNode(
                element.properties.postcode + " " + element.properties.city
            );
            addressLine.innerHTML = element.properties.name;
            li.onclick = function () {
                inputAddress.value =
                element.properties.name +
                " " +
                element.properties.postcode +
                " " +
                element.properties.city;
            
                searchButton.click();
                divAddresses.style.display = "none";
            };

            li.appendChild(addressLine);
            li.appendChild(cityLine);
            outputAddresses.appendChild(li);
            if ((outputAddresses.childElementCount) > 4) {
            outputAddresses.removeChild(outputAddresses.firstChild);
            }
            
        });

    } else {
        divAddresses.style.display = "none";
    };
}

inputAddress.addEventListener("focusin", function () {
    if (inputAddress.value.length > 0) {
        divAddresses.style.display = "block";
    }
});

// inputAddress.addEventListener("focusout", function () {
//     setTimeout(function () {
//         divAddresses.style.display = "none"; 
//     }
//     , 100)
// });