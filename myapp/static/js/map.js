var map;
var marker;
var infowindow;
var gmarkers = [];

var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 39.7285, lng: -121.8375},
    zoom: 6,
    disableDefaultUI: true,
    zoomControl: true,
    scaleControl: true,
  });

  infowindow = new google.maps.InfoWindow({
          content: document.getElementById('form')
        });

  google.maps.event.addListener(map, 'click', function(event) {
    marker = new google.maps.Marker({
      position: event.latLng,
      map: map,
      icon: 'https://cdn2.iconfinder.com/data/icons/circus/512/tents-32.png'
    });

    var latlng = marker.getPosition();
    var lat = latlng.lat();
    var lng = latlng.lng();
    document.getElementById("myText").innerHTML = "Latitude: " + lat + " & Longitude: " + lng;

    gmarkers.push(marker);
    modal.style.display = "block";

    google.maps.event.addListener(marker, 'click', function() {
      infowindow.open(map, marker);
    });
  });

  span.onclick = function() {
    modal.style.display = "none";
    for(i=0; i<gmarkers.length; i++){
        gmarkers[i].setMap(null);
    }
  }

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      var user = new google.maps.Marker({
       position: pos,
       map: map,
       icon: 'https://www.shareicon.net/data/32x32/2015/11/24/676925_man_512x512.png',
       title: 'You',
       animation: google.maps.Animation.DROP
      });

      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}
