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

var locationMap = {
  "Ganon" : [1200,3010]
}

function init() {
  d3.json(url+'/viz1').then(function(data) {
    makePins(data)
  })
}

function getPlaythrough(seed_guid) {
  d3.json(url+'/playthrough/'+seed_guid).then(function(data) {
    drawPlaythrough(data)
  })
}

function drawPlaythrough(playthrough) {

    var pointlist = []
    
    
    var firstpolyline = L.polyline(pointlist, {
      color: 'blue',
      weight: 3,
      opacity: 0.5,
      smoothFactor: 1
      })
      firstpolyline.addTo(map)
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
  $.ajax({
    url: url+'/regions',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    crossDomain: true,
    data: JSON.stringify(locations),
    headers: {
      accept: "application/json",
      "Access-Control-Allow-Origin":url
    }
  }).done(locationChart).fail(function(jqXHR, textStatus, errorThrown) {
    console.log("fail: ",textStatus, errorThrown);
  })
}

// function to update item graph
function updateItemGraph(item_name) {
  d3.json(url+'/items/' + item_name).then(function(data) {
    ItemChart(data)
  })
}

function makePin(region) {
  if (region.map_locations) {
    locationMap[region.region] = getCoords(region.map_locations)
    new customMarker(getCoords(region.map_locations), {
      radius: 6,
      color: 'red',
      data: region
    }).bindPopup(region.region + " : " + region.locations).on('click', function(e) {
      updateGraph(e.target.options.data.locations)
    }).addTo(map)
  }
}

init()