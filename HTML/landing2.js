// Establish base url
const url = "http://127.0.0.1:5000/api/v1.0/"
// Make a function activated by the submit button
let button = d3.select("#submit")
button.on("click", function () {
    // Create variables for each input value field
    let tmax = d3.select("#tmax").property("value");
    let tmin = d3.select("#tmin").property("value");
    let humidity = d3.select("#humidity").property("value");
    let wind = d3.select("#wind").property("value");
    let pressure = d3.select("#pressure").property("value");
    //  Build out API call with the input factors
    let data_call = `${url}${tmin}/${tmax}/${humidity}/${wind}/${pressure}`
    // Return the response from the API as a pop up 
    d3.json(data_call).then(function (data) {
        console.log(data);
        alert(data)

    });
})