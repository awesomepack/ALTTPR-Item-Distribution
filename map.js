// var lightworldlayer = L.tileLayer("map/LTTP-LightWorld.jpg");
// var darkworldlayer = L.tileLayer("map/LTTP-DarkWorld.png");

var map = L.map('map', {
  minZoom: 1,
  maxZoom: 4,
  center: [0, 0],
  zoom: 1,
  maxBoundsViscosity: 1,
  crs: L.CRS.Simple,
});




// var map2 = L.map('map2', {
//   minZoom: 1,
//   maxZoom: 4,
//   center: [0, 0],
//   zoom: 1,
//   maxBoundsViscosity: 1,
//   crs: L.CRS.Simple,
//   layer: [darkworldlayer]
// });

// map1.sync(map2);
// map2.sync(map1);



// document.getElementById('switch-layers').addEventHandler('click', function(ev){
//   if (map.hasLayer(lightworldlayer)) {
//       map.addLayer(darkworldlayer);
//       map.removeLayer(lightworldlayer);} 
//   else {
//       map.addLayer(lightworldlayer);
//       map.removeLayer(darkworldlayer);
//   }
// })
// var overlaymap ={
//   ""
// }
var image = L.imageOverlay("map/LTTP-DarkWorld.png", [
  [0, 0],
  [432, 576]
]);
image.addTo(map);

// var image = L.imageOverlay("map/LTTP-LightWorld.jpg", [
//   [0, 0],
//   [432, 576]
// ]);
// image.addTo(map);
// L.control.layers(linkmap, {
//   collapsed: false
// }).addTo(map);

// map.setMaxBounds(new L.LatLngBounds([0, 0], [432, 576])); 
// L.tileLayer('', {
//   attribution: '&copy; <a href="https://mikesrpgcenter.com">Link to the Past</a>'
// }).addTo(map);
