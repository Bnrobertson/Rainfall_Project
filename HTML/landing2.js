const url = "http://127.0.0.1:5000/api/v1.0/"
// function inputfunc() {
//     tmax = d3.select("#tmax").text;
//     tmin = d3.select("#tmin").text;
//     humidity = d3.select("#humidity").text;
//     wind = d3.select("#wind").text;
//     pressure = d3.select("#pressure").text;
//     data_call = `${url}${tmin}/${tmax}/${humidity}/${wind}/${pressure}`
//     d3.json(data_call).then(function (data1) {
//         console.log(data1);
//         alert(data1)
//     });
//     console.log(data);
// }
// let features;
// d3.select("#submit").on("click", inputfunc)
let button = d3.select("#submit")
button.on("click", function () {
    let tmax = d3.select("tmax").html;
    let tmin = d3.select("#tmin").html;
    let humidity = d3.select("#humidity").html;
    let wind = d3.select("#wind").html;
    let pressure = d3.select("#pressure").html;
    let data_call = `${url}${tmin}/${tmax}/${humidity}/${wind}/${pressure}`
    d3.json(data_call).then(function (data1) {
        console.log(data1);
        alert(data1)
    });
    console.log(data1);
})