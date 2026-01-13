function predict() {
    const energy = parseFloat(document.getElementById("energy").value);
    const water = parseFloat(document.getElementById("water").value);
    const co2 = parseFloat(document.getElementById("co2").value);
    const renewable = parseFloat(document.getElementById("renewable").value);
    const waste = parseFloat(document.getElementById("waste").value);

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({energy, water, co2, renewable, waste})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = "Sustainability Score: " + data.score;
    });
}
