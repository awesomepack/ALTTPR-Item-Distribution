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
    data: {}
  }
})

const url = 'http://localhost:5000'

d3.json(url+'/viz1').then(function(data) {
  console.log(data)
  makePins(data)
  drawPlaythrough()
})

function drawPlaythrough() { 
    // var dict = {"Links House": [641,1097], "Hyrule Castle": [1101,1003], "Sahasrahla's Hut": [1107,1625], "Kakariko Tavern": [862,320], "Kakariko Well": [1174,47]
    // }

    // var pointlist = []
    // for(let k in dict){
    //   var v = dict[k]; 
    //   pointlist = pointlist.concat([v])
    // }
    
    // var firstpolyline = L.polyline(pointlist, {
    //   color: 'blue',
    //   weight: 3,
    //   opacity: 0.5,
    //   smoothFactor: 1
    //   })
    //   firstpolyline.addTo(map)
}

function makePins(list) {
  list.forEach(element => {
    if (element.children) {
      makePins(element.children);
    }
    if (element.map_locations) {
      makePin(element)
    }
  });
}

function getCoords(map_locations) {
  var x = map_locations[0].map == 'darkworld' ? map_locations[0].x+2007 : map_locations[0].x
  var y = 2007-map_locations[0].y
  return [y, x]
}

function updateGraph(locations) {
  d3.json(url+'/regions/'+locations[0]).then(locationChart)
}

function makePin(region) {
  console.log(region)
  if (region.map_locations) {
    new customMarker(getCoords(region.map_locations), {
      radius: 6,
      color: 'red',
      data: region
    }).bindPopup(region.region + " : " + region.locations).on('click', function(e) {
      updateGraph(e.target.options.data.locations)
    }).addTo(map)
  }
}

