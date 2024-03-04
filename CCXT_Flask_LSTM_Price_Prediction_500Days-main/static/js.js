function BtnClick() {
    const num_dates = 3;
    fetch(`http://20.198.93.92:5001/forecast/${num_dates}`)
        .then(response => response.json())
        .then(data => {
            console.log("Data received from server:", data);

            let messages = [];

            Object.entries(data.num_dates).forEach(([date, value]) => {
                const message = `Data: ${date} --> Expected Value: $${value}`;
                messages.push(message);
            });

            const graphDiv = document.getElementById("graphDiv");
            const graphData = JSON.parse(data.graph);
            Plotly.newPlot(graphDiv, graphData);
        })
        .catch(error => {
            console.error("Fetch error:", error);
        });
}

document.addEventListener("DOMContentLoaded", function () {
    
});
