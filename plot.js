function Charts(sample){
    var name =  "Ganon's Tower - Compass Room - Bottom Right";
    var items = ['BossHeartContainer', 'Bottle', 'TenArrows', 'Flippers', 'TwentyRupees', 'other'];
    var values = [12, 14, 7, 19, 3, 45];

    var bar =[
    {
        y: items,
        x: values,
        type: "bar",
        marker:{
            color: 'rgb(158,202,225)',
            opacity: 1.5,
            line: {
            color: 'rgb(8,48,107)',
            width: 2
    }
}
    }]};

    var barshape = {
        title: "Ganon's Tower",
        margin: { top: 80, left: 200 },
        };

    Plotly.newPlot("bar", bar, barshape);
    