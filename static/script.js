const socket = io.connect('http://127.0.0.1:5000');

socket.on("update_tarifa", function(data) {
    document.getElementById('tarifa').textContent = data.tarifa.toFixed(2) + "€";
});

document.addEventListener("DOMContentLoaded", function() {
    fetch('/get_prices')
        .then(response => response.json())
        .then(data => {
            document.getElementById('tarifa-parado').textContent = "Tarifa Parado: " + data.PARADO + "€";
            document.getElementById('tarifa-movimiento').textContent = "Tarifa Movimiento: " + data.MOVIMIENTO + "€";
        });
})

document.getElementById('iniciar-viaje').addEventListener('click', function() {
    fetch('/start', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('estado').textContent = "Estado: " + data.estado;
        })
        .catch(error => console.error("Error al iniciar viaje:", error));
});

document.getElementById('cambiar-estado').addEventListener('click', function() {
    const estadoElemento = document.getElementById('estado');
    const tarifaElemento = document.getElementById('tarifa');

    
    let estadoActual = estadoElemento.textContent.split(": ")[1];
    let nuevoEstado = (estadoActual === "MOVIMIENTO") ? "PARADO" : "MOVIMIENTO";

    fetch('/change_state', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ estado: nuevoEstado })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        estadoElemento.textContent = "Estado: " + data.estado;
        tarifaElemento.textContent = "Tarifa: " + data.tarifa_acumulada.toFixed(2) + "€";
    })
    .catch(error => console.error("Error al cambiar estado:", error));
});

document.getElementById('finalizar-viaje').addEventListener('click', function() {
    fetch('/stop', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('estado').textContent = "Estado: " + data.estado;
            document.getElementById('tarifa').textContent = "Tarifa Total: " + data.tarifa_total.toFixed(2) + "€";
        })
        .catch(error => console.error("Error al finalizar viaje:", error));
});

document.querySelector(".logout-button a").addEventListener("click", function (e) {
    e.preventDefault();
    window.location.href = "/logout";
});
