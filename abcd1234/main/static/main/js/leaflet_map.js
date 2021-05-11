function map_init_basic (map, option) {
    function onMapClick(e) {
        var LatLng = L.latLng(e.latlng);
        $.ajax({
            headers: {
                'X-CSRFToken': csrftoken,
            },
            type: 'POST',
            data: {
                'lat': LatLng.lat,
                'lng': LatLng.lng,
            },
        });
    }

    map.on('click', onMapClick);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1Ijoic3VucHJpenJhayIsImEiOiJja251OWN5NXEwYWxhMnZvYWQxNHVwN2ZiIn0.VgyND-Z0cCS6NXGwbKMKQw'
    }).addTo(map);
};
