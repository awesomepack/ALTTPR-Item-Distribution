
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

// Modifying index.html //

// rendering the first row of the grid
d3.select("#grid").html("<div class = 'row' id = 'row1'> Hello There Kenobi </div>")

// appending the row with 7 columns
for (let col = 1; col < 8 ; col++){
  
  d3.select('#row1').html("<div class = 'col-1'> Column 1 </div>")

}

// To Do
// Populate the first row with 7 columns
// Populate the container div with 7 rows



