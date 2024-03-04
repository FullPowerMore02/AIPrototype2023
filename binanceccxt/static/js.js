function BtnClick() {
    const num_dates = document.getElementById("numDatesInput").value;

    // Validate if num_dates is a positive integer or handle validation as needed

    fetch(`http://20.198.93.92:5001/forecast/${num_dates}`)
        .then(response => response.json())
        .then(data => {
            console.log("Date received from server:", data);

            let messages = [];

            for (const date in data.num_dates) {
                const message = `Data: ${date} --> Expected Value: $${data.num_dates[date]}`;
                messages.push(message);
            }

            const graphDiv = document.getElementById("graphDiv");
            const graphData = JSON.parse(data.graph);
            Plotly.newPlot(graphDiv, graphData);
        })
        .catch(error => {
            console.error("Fetch error:", error);
        });
}

document.addEventListener("DOMContentLoaded", function () {
    // Additional initialization if needed
});
