var myMap = L.map("map", {
    center: [36.77, -119.41],
    zoom: 15,
  });
  url = 'https://api.songkick.com/api/3.0/metro_areas/31422/calendar.json?apikey=WewWUhkws9IU4phb';
  

  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);
  var streetmap = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: API_KEY,
}).addTo(myMap)
var baseURL = "https://api.songkick.com/api/3.0/artists/379603/gigography.json?apikey=WewWUhkws9IU4phb";
var date = "&onTourUntil=2021-01-10'";
//var country = 
// var complaint = "&complaint_type=Rodent";
// var limit = "&$limit=10000";
var url = baseURL;
d3.json(url, function(data){
  console.log(data)
  if(data.onTourUntil === '2021-01-10'){
  var markers = L.markerClusterGroup();
  for(var i = 0; i < data.length; i++) {
    var location = data[i].areaID;
    markers.addLayer(L.marker([data.location.lng, data.location.lat]))
    .bindPopup()
  }
  myMap.addLayer(markers);
  }
});

// function comparison(date){
//   if parseInt(date[0:4]) < 2021 and parseInt(date[6:8] < 1 and  )
// }