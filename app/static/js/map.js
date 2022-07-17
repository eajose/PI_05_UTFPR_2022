var satellite = L.tileLayer.provider('MapBox', {
        id: 'mapbox.satellite',
        accessToken: 'pk.eyJ1IjoiY2FpcXVlLXN5bmVyZ2lhIiwiYSI6ImNqdmdxMjkxNzBhOTY0OW50ZHZobHE4cDAifQ.YK7zLzFQdi5n6Bew5kXsfQ'
    }),
    streets = L.tileLayer.provider('MapBox', {
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiY2FpcXVlLXN5bmVyZ2lhIiwiYSI6ImNqdmdxMjkxNzBhOTY0OW50ZHZobHE4cDAifQ.YK7zLzFQdi5n6Bew5kXsfQ'
    });

var map = L.map('map', {
    center: [-1.5173293363818698, -48.669914202657196],
    zoom: 3.5,
    layers: [satellite, streets]
});

var baseLayers = {
    "Satélite": satellite,
    "Ruas": streets
};

L.control.layers(baseLayers).addTo(map);