  <!--./cy4neo.js-->
document.addEventListener("DOMContentLoaded", function () {
  fetch('../cy4neo.json')
        .then(response => response.json())
        .then(data => {
            const dataDisplay = document.getElementById("dataDisplay");

            // Create HTML elements to display the JSON data
            const titleElement = document.createElement("p");
            titleElement.textContent = "Title: " + data.title;

            const statementElement = document.createElement("p");
            statementElement.textContent = "Statement: " + data.statement;

            const descriptionElement = document.createElement("p");
            descriptionElement.textContent = "Description: " + data.description;

            // Append the elements to the "dataDisplay" div
            dataDisplay.appendChild(titleElement);
            dataDisplay.appendChild(statementElement);
            dataDisplay.appendChild(descriptionElement);
        })
        .catch(error => console.error("Error fetching JSON data:", error));
});
