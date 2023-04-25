// Store the original value of available_cur when the page is loaded
var originalCurrency = document.getElementById("currency").innerHTML;

// Change input blocks dut to the user's chosen request.
function updateForm() {
    var selectBox = document.getElementsByName("selected_request")[0];
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    var quotationLabel = document.getElementsByName("date_or_period")[0].parentNode.previousSibling.innerHTML;

    if (selectedValue == "0") {
        document.getElementsByName("date_or_period")[0].parentNode.previousSibling.innerHTML = "Enter a date in format YYYY-MM-DD:";
        document.getElementById("currency").innerHTML = originalCurrency;
    } else if (selectedValue == "1") {
        document.getElementsByName("date_or_period")[0].parentNode.previousSibling.innerHTML = "Enter a period between 1 <= N <=255:";
        document.getElementById("currency").innerHTML = originalCurrency;
    } else if (selectedValue == "2") {
        document.getElementsByName("date_or_period")[0].parentNode.previousSibling.innerHTML = "Enter a period between 1 <= N <=255:";
        // Replace the contents of the p element with id "currency" with the desired string
        document.getElementById("currency").innerHTML = "AUD | CAD | CZK | DKK | EUR | HUF | NOK | GBP | SEK | CHF | USD | JPY | XDR";
    }
}

// Call the function on page load to set the initial form state
updateForm();

// Add an event listener to update the form when the select box changes
document.getElementsByName("selected_request")[0].addEventListener("change", updateForm);



