function BtnClick() {
    const num_dates = document.getElementById("num_dates").value;

    if (isNaN(num_dates) || num_dates <= 0) {
        const predictionsDiv = document.getElementById("predictions");
        predictionsDiv.innerHTML = "Add a valid number!";
        return;
    }

    fetch(`http://20.198.93.92:5001/forecast/${num_dates}`)
        .then(response => response.json())
        .then(data => {
            console.log("Data received from server:", data);

            const predictionsDiv = document.getElementById("predictions");
            let messages = [];

            for (const date in data.num_dates) {
                const message = `Date: ${date}, Expected Value: $${data.num_dates[date]}`;
                messages.push(message);
            }

            predictionsDiv.innerHTML = "Prediction Results:<br><br>" + messages.join("<br>");

            const graphDiv = document.getElementById("graphDiv");
            const graphData = JSON.parse(data.graph);

            Plotly.newPlot(graphDiv, graphData.data, graphData.layout);
        })
        .catch(error => {
            console.error("Fetch error:", error);
        });
}

document.addEventListener("DOMContentLoaded", function() {
    // ดึงข้อมูลจาก Flask
    const graphData = JSON.parse("{\"data\":[{\"hovertemplate\":\"index=%{x}\\u003cbr\\u003eclose=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x\":[\"2024-03-03\",\"2024-03-04\",\"2024-03-05\",\"2024-03-06\"],\"xaxis\":\"x\",\"y\":[2917.63037109375,2904.60986328125,2875.52685546875,2837.678466796875],\"yaxis\":\"y\",\"type\":\"scatter\"}],\"layout\":{\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"
