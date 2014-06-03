var relay_button = document.getElementById('relay_button')
var relay_button1 = document.getElementById('relay_button1')
var Temp = document.getElementById('temp')
var TempRPI = document.getElementById('temp2')
var Rideaux = document.getElementById('rideaux')


// Lit l'état du relai sur le Raspi et actualise l'affichage en fonction:
var updateRelayState = function () {
    $.ajax('/api/relay/status').done( function(status) {
        if (status == 'on') {
            relay_button.innerHTML = 'Lampe éteinte !';
        }
        else if (status == 'off') {
            relay_button.innerHTML = 'Lampe allumée !';
        }
        else {
            alert('weird');
        }
    })
}



// Lit l'état du relai sur le Raspi et actualise l'affichage en fonction:
var updateRelayState1 = function () {
    $.ajax('/api/relay/status1').done( function(status) {
        if (status == 'on') {
            relay_button1.innerHTML = 'Lampe éteinte !';
        }
        else if (status == 'off') {
            relay_button1.innerHTML = 'Lampe allumée !';
        }
        else {
            alert('weird');
        }
    })
}



var updateRideauxState = function () {
    $.ajax('/api/relay/status2').done( function(status2) {
         Rideaux.innerHTML = status2;
    })
}
                                      
                                      
var updateTemp = function () {
    $.ajax('/api/temp').done( function(sensor) {
           Temp.innerHTML = sensor;         
    })
}

var updateTemp2 = function () {
    $.ajax('/api/temp2').done( function(sensor2) {
          TempRPI.innerHTML = sensor2;
   })
}

var recurrentCheck = function() {
    updateRelayState();
    updateRelayState1();
    updateRideauxState();
    updateTemp();
    updateTemp2();
    
    setTimeout(recurrentCheck, 500);
}


recurrentCheck();

