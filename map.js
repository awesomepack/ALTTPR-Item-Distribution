const corner1 = L.latLng(0, 0)
const corner2 = L.latLng(2007, 4014)
const bounds = L.latLngBounds(corner1, corner2)
var map = L.map('map', {
  minZoom: -2,
  maxZoom: 2,
  center: bounds.getCenter(),
  zoom: -2,
  maxBounds: bounds,
  maxBoundsViscosity: 1,
  crs: L.CRS.Simple,
});

var i1bounds = [[0,0], [2007,2007]]
var image1 = L.imageOverlay('resources/images/lttp_lightworld.png', i1bounds)
image1.addTo(map)

var i2bounds = [[0,2007], [2007,4014]]
var image2 = L.imageOverlay('resources/images/lttp_darkworld.png', i2bounds)
image2.addTo(map)

// d3.json('http://localhost:5000/viz1').then(function(data) {
//   for (var i = 0; i < data.length; i++) {
//     marker = new L.marker(data[i][1])
//       .bindPopup(data[i][0]).addTo(map);}

d3.json('http://localhost:5000/viz1').then(function(data) {
  for (var i = 0; i < data.length; i++) {
    marker = new L.circleMarker(data[i][1])
    .bindPopup(data[i][0]).addTo(map);
marker.setStyle({radius: '6'})


// var circle = L.circleMarker(mapstyleInfo(feature) {
//   return {
//     opacity: 1,
//     fillOpacity: 1,
//     fillColor: "#F002134",
//     color: "#000000",
//     radius: 10,
//     stroke: true,
//     weight: 0.5
//   }
// }
// ).addTo(map)


  




  }})
