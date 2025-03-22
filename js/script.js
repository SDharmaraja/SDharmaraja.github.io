document.addEventListener("DOMContentLoaded", function () {
    // For testing, we’re fetching sample data from a local JSON file.
    // If you have a dynamic API, replace 'predictions.json' with your API endpoint.
    fetch('predictions.json')
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById("prediction-results");
            resultsDiv.innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
        })
        .catch(error => {
            console.error("Error loading predictions:", error);
            document.getElementById("prediction-results").innerHTML = "Error loading predictions.";
        });
});
