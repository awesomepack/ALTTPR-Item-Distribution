
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


var maplocations =  {
  "Location": [
    "Master Sword Pedestal", 
    "Lumberjack Cave", 
    "Blind's House", 
    "The Well", 
    "Bottle Vendor", 
    "Chicken House", 
    "Tavern", 
    "Sick Kid", 
    "Magic Bat", 
    "Race Game", 
    "Library", 
    "Lost Woods", 
    "Castle Secret Entrance", 
    "Link's House", 
    "Grove Digging Spot", 
    "Bombos Tablet", 
    "South of Grove", 
    "Witch's Hut", 
    "Waterfall Fairy", 
    "Zora Area", 
    "Sahasrala's Hut", 
    "Bonk Rocks", 
    "King's Tomb", 
    "Graveyard Ledge", 
    "Desert Ledge", 
    "Aginah's Cave", 
    "Dwarven Smiths", 
    "Purple Chest", 
    "Dam", 
    "Mini Moldorm Cave", 
    "Ice Rod Cave", 
    "Lake Hylia Island", 
    "Hobo", 
    "Checkerboard Cave", 
    "Old Man", 
    "Spectacle Rock", 
    "Ether Tablet", 
    "Spiral Cave", 
    "Paradox Cave", 
    "Floating Island", 
    "Hyrule Castle & Sanctuary", 
    "Agahnim", 
    "Eastern Palace", 
    "Desert Palace", 
    "Tower of Hera", 
    "Mimic Cave"
  ], 
  "Map": [
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld", 
    "lightworld"
  ], 
  "x": [
    83, 
    633, 
    307, 
    47, 
    190, 
    197, 
    320, 
    314, 
    650, 
    111, 
    313, 
    320, 
    1196, 
    1097, 
    600, 
    440, 
    552, 
    1607, 
    1806, 
    1920, 
    1625, 
    777, 
    1207, 
    1132, 
    40, 
    400, 
    616, 
    680, 
    942, 
    1309, 
    1795, 
    1450, 
    1390, 
    354, 
    816, 
    980, 
    844, 
    1598, 
    1731, 
    1627, 
    1003, 
    1003, 
    1925, 
    146, 
    1126, 
    1694
  ], 
  "y": [
    101, 
    117, 
    840, 
    833, 
    933, 
    1066, 
    1145, 
    1060, 
    1127, 
    1354, 
    1310, 
    260, 
    834, 
    1366, 
    1350, 
    1845, 
    1693, 
    670, 
    286, 
    273, 
    900, 
    590, 
    598, 
    549, 
    1835, 
    1655, 
    1054, 
    1805, 
    1880, 
    1887, 
    1547, 
    1666, 
    1390, 
    1560, 
    378, 
    178, 
    38, 
    180, 
    434, 
    40, 
    906, 
    807, 
    791, 
    1584, 
    68, 
    190
  ]
}
console.log(maplocations)

// var mark = L.marker(
//   L.latLng(
//     parseFloat(mapLocations["x"]),
//     parseFloat(mapLocations["y"])
//   )
// );

// var mark = L.marker(
//   L.latLng(
//     parseFloat(maplocations.x),
//     parseFloat(maplocations.y)
//   )
// );

// var linkloc = [];

// for (var i = 0; i < maplocations.Location; i++) {
//   marker = new L.marker([maplocations.x[i],maplocations.y[i]])
//     .bindPopup(maplocations.map[i])
// .addTo(map);}


L.marker([83, 102]).addTo(map)
    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
    .openPopup();






