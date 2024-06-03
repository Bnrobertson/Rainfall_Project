const url = "http://127.0.0.1:5000/api/v1.0/"

let features;
document.getElementById("submit").onclick = function () {
    tmax = document.getElementById("tmax").value;
    tmin = document.getElementById("tmin").value;
    humidity = document.getElementById("humidity").value;
    wind = document.getElementById("wind").value;
    pressure = document.getElementById("pressure").value;
    data = {"tmax":tmax, "tmin":tmin, "humidity":humidity, "wind":wind, "pressure":pressure};
    console.log(data);
    data_call = `${url}/${tmin}/${tmax}/${humidity}/${wind}/${pressure}`
    d3.json(data_call).then(function(data){
        alert(data)
    });

  
}