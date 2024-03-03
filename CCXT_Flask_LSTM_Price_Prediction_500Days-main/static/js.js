function BtnClick() { // quando apertado o botão será acionado essa função

    const num_dates = document.getElementById("num_dates").value; // pegar o valor de entrada na página HTML

    if (isNaN(num_dates) || num_dates <= 0) { // se o input for nulo ou <= 0, ele irá retornar uma mensagem de erro na página
        const predictionsDiv = document.getElementById("predictions");
        predictionsDiv.innerHTML = "Add a valid number!";
        return;
    }

    fetch(`http://20.198.93.92:5001/forecast/3`) // faz uma solicitação GET na página

        .then(response => response.json()) // passa os dados da solicitação para JSON
        .then(data => { // pega os dados JSON e passa para a função 'data'
            console.log("Date received from server:", data);

            const predictionsDiv = document.getElementById("predictions"); // div 'predictions' de nossa página HTML

            let messages = [];

            for (const date in data.num_dates) {
                const message = `Data: ${date} --> Expected Value: $${data.num_dates[date]}`;
                messages.push(message);
            } // adicionando os dados do nosso forecast para uma array 'messages'

            predictionsDiv.innerHTML = "Prediction Results:<br><br>" + messages.join("<br>"); // printando na tela nossas 'messages'

            const graphDiv = document.getElementById("graphDiv"); // div onde queremos exibir o gráfico

            const graphData = JSON.parse(data.graph); // dados do gráfico

            Plotly.newPlot(graphDiv, graphData); // plotagem do gráfico
        })
        .catch(error => {
            console.error("Fetch error:", error);
        }); // se der algum erro ele apontará no console
}

document.addEventListener("DOMContentLoaded", function() {
});
