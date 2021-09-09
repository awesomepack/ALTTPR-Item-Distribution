
var map = L.map('map', {
  minZoom: -2,
  maxZoom: 2,
  center: [1003, 2006],
  zoom: -2,
  maxBoundsViscosity: 1,
  crs: L.CRS.Simple,
});

var bounds = [[0,0], [2007,2007]]
var image = L.imageOverlay('resources/images/lttp_lightworld.png', bounds)
image.addTo(map)

var bounds2 = [[0,2007], [2007,4014]]
var image2 = L.imageOverlay('resources/images/lttp_darkworld.png', bounds2)
image2.addTo(map)
