

function locationChart(data){
  var name = data[0]
  var items = data[1];
  var values = data[2];

  var bar =[{
    x: items,
    y: values,
    type: "bar",
    marker:{
      color: 'rgb(158,202,225)',
      opacity: 1.5,
      line: {
        color: 'rgb(8,48,107)',
        width: 2
      }
    }
  }];

  var barshape = {
        title: name,
        margin: { top: 80, left: 200 },
        };

  Plotly.newPlot("bar", bar, barshape);
};


// reading in items.json
d3.json('resources/items/items.json').then(function(data){
  console.log(data)

var counter = 0


// creating the item selector grid (8x5)
for (row = 1; row < 9; row++){

  for (col = 1; col < 6; col++) {

    var item_name = data[counter].name

    $(`#row${row}`).append(`<td class = col-1><button type = "button" onclick = "viz2func()" value = ${item_name} >${item_name}</button> </td>`)
    counter += 1

  }

}

});
// end data scope


// To Do
// populate each column cell with the item name from items.json
// move the table object next to th map



