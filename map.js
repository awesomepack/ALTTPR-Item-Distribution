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

customMarker = L.CircleMarker.extend({
    options: {
      data: {
        location_name: '',
        coords: ''
      }
    }
  })

const url = 'http://localhost:5000'

d3.json(url+'/viz1').then(function(data) {
    for (var i = 0; i < data.length; i++) {
      var location_name = data[i][0]
      var coords = data[i][1]
      marker = new customMarker(coords, {
        radius: 6,
        color: 'red',
        data: {
          location_name: location_name,
          coords: coords
        }
      })
        .bindPopup(location_name)
        .on('click', function(e) {
          updateGraph(e.target.options.data.location_name)
        })
        .addTo(map)
        
    }
  }
);

function updateGraph(location_name) {
  d3.json(url+'/viz2/'+location_name).then(function(data) {
      console.log(data)
      locationChart(data)
    }
  )
}
