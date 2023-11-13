//get csv file
let result3;
d3.csv('Avg_monthly_rainfall.csv').then(    //該函數有一傳入值叫做res
    res =>{
        console.log('Local CSV:', res);
        result3 = res;
        console.log(result3);
        plot_pie(result3);
    }
);

//console.log(result);
function plot_pie(data_input){
    let myGraph3 = document.getElementById('myGraph3');
    let trace1 = {};

    

    trace1 = trace_create("台北", data_input, "TPE", 0, 0);
    let trace2 = trace_create("台中", data_input, "TXG", 0, 1);
    let trace3 = trace_create("台南", data_input, "TNN", 1, 0);
    let data = []
    data.push(trace1);
    data.push(trace2);
    data.push(trace3);
    
    let layout = {
        margin:{
            t:10,
            l:10,
        },
        grid:{
            rows:2,
            columns:2
        },        
    }
    Plotly.newPlot(myGraph3, data, layout);
}


function trace_create(title, input_data, site, dom_row, dom_column){
    let trace = []
    trace.type = "pie";
    trace.title = title;
    trace.hole = 0.5;
    trace.labels = [];
    trace.values = [];
    trace.domain = {
        row:dom_row,
        column:dom_column,
    };

    for(let x = 0; x<input_data.length; x++){
        trace.labels[x] = input_data[x]["month"];
        trace.values[x] = input_data[x][site];
    }

    return trace
}



