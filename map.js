var map;

let lightworldlayer = L.tileLayer("map/LTTP-LightWorld.jpg",{
    maxZoom: 4,
    minZoom: 1, 
    zoom: 1, 
   });

let darkworldlayer = L.tileLayer("map/LTTP-DarkWorld.png",{
    maxZoom: 4,
    minZoom: 1, 
    zoom: 1, });

let linkmap = {
    "DarkWorld": darkworldlayer,
    "LightWorld": lightworldlayer,
};
map = L.map('map', {
  minZoom: 1,
  maxZoom: 4,
  center: [0, 0],
  zoom: 1,
  maxBoundsViscosity: 1,
  crs: L.CRS.Simple,
  layers: [darkworldlayer, lightworldlayer]
});

// var image = L.imageOverlay("map/LTTP-DarkWorld.png", [
//   [0, 0],
//   [432, 576]
// ]);
// image.addTo(map);
L.control.layers(linkmap, {
  collapsed: false
}).addTo(map);

map.setMaxBounds(new L.LatLngBounds([0, 0], [432, 576])); 
L.tileLayer('', {
  attribution: '&copy; <a href="https://mikesrpgcenter.com">Link to the Past</a>'
}).addTo(map);
