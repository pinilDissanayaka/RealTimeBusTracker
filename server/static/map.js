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
let isFiltered = false;
let currentCheckpoints=[];

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
        currentCheckpoints.push(newMarker);

        // Update the buses map with the new marker
        checkpoints.set(obj.bus_id, newMarker);

        currentCheckpoints.push({
            "bus_id": obj.bus_id,
            "marker": newMarker
        });
    } else {
        // Add a new marker for the bus
        const marker = L.marker([obj.lon, obj.lat]).addTo(map);
        marker.bindPopup("Route Number :" + obj.bus_id + "").openPopup();
        checkpoints.set(obj.bus_id, marker);
        currentCheckpoints.push({
            "bus_id": obj.bus_id,
            "marker": marker
        });
    }
}, false);


function filter(){
    const filter_id = document.getElementById("filter_id").value.trim();

    if (filter_id && isFiltered) {
        isFiltered = true;
        currentCheckpoints.forEach((currentCheckpoint) => {
            if (currentCheckpoint.bus_id == filter_id) {
                currentCheckpoint.marker.addTo(map);
            }
            else {
                map.removeLayer(currentCheckpoint.marker);
            }
            
        });
    }
    else{
        isFiltered=false;
    }
}


