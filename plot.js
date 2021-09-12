
var test_data = ["Ganon's Tower - Compass Room - Bottom Right", ['BossHeartContainer', 'Bottle', 'TenArrows', 'Flippers', 'TwentyRupees', 'other'], [12, 14, 7, 19, 3, 45]];

function charts(data){
  var name =  data[0];
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

charts(test_data);


// Populate #rows with 7 columns
for (row = 1; row < 8; row++){
  
  // appending a column 7 times
  for (col = 1; col < 8; col++) {

    d3.select(`#row${row}`).append('td').attr('class' , 'class = col-1').text(`${col}`)

  }
}


// To Do
// Populate the first row with 7 columns
// Populate the container div with 7 rows



