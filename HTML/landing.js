let features;
document.getElementById("submit").onclick = function () {
    tmax = document.getElementById("tmax").value;
    tmin = document.getElementById("tmin").value;
    humidity = document.getElementById("humidity").value;
    wind = document.getElementById("wind").value;
    pressure = document.getElementById("pressure").value;
    data = {"tmax":tmax, "tmin":tmin, "humidity":humidity, "wind":wind, "pressure":pressure};
    console.log(data);
}