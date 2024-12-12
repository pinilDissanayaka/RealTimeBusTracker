var popup = L.popup();

var map = L.map('map').setView([6.930243972119172, 79.87848236150131], 10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);


const checkpoints = new Map();

var source = new EventSource('http://127.0.0.1:5001/');
source.addEventListener('message', function (e) {
    const obj = JSON.parse(e.data);

    if (checkpoints.has(obj.bus_id)) {
        // Get the existing marker
        const existingMarker = checkpoints.get(obj.bus_id);

        // Remove the old marker from the map
        if (map.hasLayer(existingMarker)) {
            map.removeLayer(existingMarker);
        }

        // Update the map with the new coordinates
        const newMarker = L.marker([obj.lon, obj.lat]).addTo(map);
        newMarker.bindPopup("Route Number :" + obj.bus_id + "").openPopup();

        // Update the buses map with the new marker
        checkpoints.set(obj.bus_id, newMarker);
    } else {
        // Add a new marker for the bus
        const marker = L.marker([obj.lon, obj.lat]).addTo(map);
        marker.bindPopup("Route Number :" + obj.bus_id + "").openPopup();
        checkpoints.set(obj.bus_id, marker);
    }
}, false);


