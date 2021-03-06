
// Chart for item distribution per location
function locationChart(data) {
  var name = data[0]
  var items = data[1];
  var values = data[2];

  var bar = [{
    x: items,
    y: values,
    type: "bar",
    marker: {
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


// Selector Grid
d3.json(url + '/resources/items').then(function (data) {
  var counter = 0
  // creating the item selector grid (8x5)
  for (row = 1; row < 9; row++) {

    for (col = 1; col < 6; col++) {

      var str_name = data[counter].name // current item
      var item_name = str_name.substring(6, str_name.length - 4)

      $(`#row${row}`).append(`<td class = col-2><button type = "button" value = ${item_name} onclick = viz2func(this.value) >${item_name}</button> </td>`)
      counter += 1 // incrementing after each column

    }
  }
});

// end data scope
// end item selector

// OnClick function Viz2
function viz2func(value) {
  console.log(value)
  updateItemGraph(value)
}

// Chart for location distribution per item
function ItemChart(data) {
  var name = data[0]
  var locations = data[1];
  var values = data[2];

  var bar = [{
    x: locations,
    y: values,
    type: "bar",
    marker: {
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
