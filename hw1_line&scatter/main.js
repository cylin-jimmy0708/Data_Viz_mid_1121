let myGraph = document.getElementById('myGraph')
let trace1 = {};
trace1.mode = "lines+markers";
trace1.type = "scatter";
trace1.name = "台北";
trace1.visible = true;
trace1.x = [];
trace1.y = [];
trace1.text = [];
trace1.textposition = "bottom center";
trace1.textfront = {
    family:"Raleway, sans-serif",
    size:10
}

let trace2 = {};
trace2.mode = "lines+markers";
trace2.type = "scatter";
trace2.name = "台中";
trace2.visible = false;
trace2.line = {
    color:'red'
};
trace2.x = [];
trace2.y = [];
trace2.text = [];

let trace3 = {};
trace3.mode = "lines+markers";
trace3.type = "scatter";
trace3.name = "台南";
trace3.visible = false;
trace3.line = {
    color:'green',
    //shape:'spline',
}
trace3.x = [];
trace3.y = [];
trace3.text = [];

for(let i=0;i<set1.length;i++){
    trace1.x[i] = set1[i][0];
    trace1.y[i] =set1[i][1];
    trace1.text[i] = set1[i][2];
}

for(let i=0;i<set2.length;i++){
    trace2.x[i] = set2[i][0];
    trace2.y[i] =set2[i][1];
    trace2.text[i] = set2[i][2];
}

for(let i=0;i<set3.length;i++){
    trace3.x[i] = set3[i][0];
    trace3.y[i] =set3[i][1];
    trace3.text[i] = set3[i][2];
}

let data = [];
data.push(trace1);
data.push(trace2);
data.push(trace3)

let layout = {
    margin:{
        t:50
    },
    xaxis:{
        range:[1997,2023],
        text:"時間"
    },
    yaxis:{
        range:[22.5,25.0]
    },
    title:'1998~2022年平均溫度變化圖',
    updatemenus:[
        {
            y:1.2,
            x:0.3,
            yanchor:'top',
            buttons:[
                {
                    method:'restyle',
                    args:['visible',[true, false, false]],
                    label:'台北'
                },
                {
                    method:'restyle',
                    args:['visible',[false, true, false]],
                    label:'台中'
                },
                {
                    method:'restyle',
                    args:['visible',[false, false, true]],
                    label:'台南'
                },
                {
                    method:'restyle',
                    args:['visible',[true, true, true]],
                    label:'Display All'
                },
            ]
        },
        
    ],
    xaxis: {
        title: {
          text: 'Year',
          font: {
            size: 18,
          }
        },
      },
      yaxis: {
        title: {
          text: 'Temperature(degree C)',
          font: {
            size: 18,
          }
        }
      }
};

Plotly.newPlot(myGraph, data, layout);  /* margin為圖與邊界間距離*/

