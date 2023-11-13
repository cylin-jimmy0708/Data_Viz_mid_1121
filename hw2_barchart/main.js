
//get csv file
let result;
d3.csv('Avg_monthly_rainfall.csv').then(    //該函數有一傳入值叫做res
    res =>{
        console.log('Local CSV:', res);
        result = res;
        console.log(result);
        plot(result);
    }
);


function trace_establish(name, result){
  
    let trace = [];
    trace.type = "bar";
    trace.name = name;
    trace.x = [];
    trace.y = [];
    for(let i = 0; i<result.length; i++){
        trace.x[i] = result[i]['month'];
        trace.y[i] =parseFloat(result[i][name]);
    }
    return trace;

}

function plot(result){
    let myGraph2 = document.getElementById('myGraph2')

    let data2 = [];
    data2.push(trace_establish("TPE", result));
    data2.push(trace_establish("TXG", result));
    data2.push(trace_establish("TNN", result));


    let layout ={margin:{
        t:50
        },
        //barmode:'stack',
        title:'1998~2022逐月降水量統計',
        xaxis: {
            title: {
              text: 'Month',
              font: {
                size: 18,
              }
            },
          },
          yaxis: {
            title: {
              text: '降水量(mm)',
              font: {
                size: 18,
              }
            }
          }
    };
    Plotly.newPlot(myGraph2, data2, layout);


}

