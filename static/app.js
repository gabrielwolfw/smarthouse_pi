function loadLights() {
    fetch('/api/lights').then(res => res.json()).then(data => {
        let html = "<h2>Luces</h2>";
        for (let room in data) {
            let state = data[room];
            html += `${room}: <button onclick="toggleLight('${room}', ${!state})">${state ? "Apagar" : "Encender"}</button><br>`;
        }
        document.getElementById("lights").innerHTML = html;
    });
}

function toggleLight(room, state) {
    fetch('/api/lights', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({room, state})
    }).then(() => loadLights());
}

function loadDoors() {
    fetch('/api/doors').then(res => res.json()).then(data => {
        let html = "<h2>Puertas</h2><ul>";
        for (let door in data) {
            let doorObj = data[door];
            let estado = doorObj.estado; // "abierta" o "cerrada"
            html += `<li>${door}: <span>${estado}</span></li>`;
        }
        html += "</ul>";
        document.getElementById("doors").innerHTML = html;
    });
}

function capturePhoto() {
    fetch('/api/capture')
        .then(res => res.json())
        .then(data => {
            document.getElementById("photo").src = data.image + '?t=' + new Date().getTime();
        });
}

setInterval(() => {
    loadLights();
    loadDoors();
}, 3000);

window.onload = () => {
    loadLights();
    loadDoors();
};
