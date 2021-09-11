d3.json('http://localhost:5000/viz1').then(function(data) {
  console.log(data)
});
// Delete the above code when done debugging the app.py


var test_data = ["Ganon's Tower - Compass Room - Bottom Right", ['BossHeartContainer', 'Bottle', 'TenArrows', 'Flippers', 'TwentyRupees', 'other'], [12, 14, 7, 19, 3, 45]];

function charts(sample){
  var name =  sample[0];
  var items = sample[1];
  var values = sample[2];

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