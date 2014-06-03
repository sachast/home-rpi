#coding=utf8

import serial
import os
import threading

from bottle import Bottle

import subprocess
from bottle import route, request, response, redirect, template, run

#os.system('gpio mode 0 out') #On
#os.system("gpio write 0 1")
os.system('gpio mode 0 in')
os.system('gpio mode 7 in')



app = Bottle()


#-------------------------

# On va lancer un thread qui lit la temperature a cote du serveur web

senseurs = {}


def connect_arduino():
    for path in ('/dev/ttyACM0',
                 '/dev/ttyACM1',
                 '/dev/tty.usbserial-A8008KAi'):
        try:
            return serial.Serial(path, 9600)
        except serial.serialutil.SerialException:
            pass # Only accept that exception class
    raise serial.serialutil.SerialException(
        "could not open any predefined port")

global arduino
arduino = connect_arduino()

def lance_thread(arduino):
    print('lance_thread')
    while True:
        temperature = arduino.readline().strip()
        senseurs['temperature'] = temperature
        print('temperature', temperature)


lecture_serial = threading.Thread(target=lance_thread, args=tuple(arduino))
lecture_serial.start()


@app.route('/api/temp')
def temp():
    return senseurs['temperature']

#------------------------

#@app.route('/api/temp')
#def temp():
#    sensor = ser.readline().strip()
#    #sensor = "Arduino débranché !!!";
#    return sensor

@app.route("/")
def index():
    redirect("/hello")

@app.route('/hello')
def hello():  
    return template('template.html')


@app.route('/api/relay1/on')
def relay():
    os.system("gpio mode 0 out")    
    return "OK"

@app.route('/api/relay1/off')
def relay():
    os.system("gpio mode 0 in")    
    return "OK"

@app.route('/api/relay2/on')
def relay():
    os.system("gpio mode 7 out")
    return "OK"

@app.route('/api/relay2/off')
def relay():
    os.system("gpio mode 7 in")
    return "OK"
 
@app.route('/api/relay/status')
def relay_status():
#    status = subprocess.check_output(["gpio", "read", "7"])

    data2 = subprocess.check_output(["gpio", "read", "7"]) 
    coin = data2 
    if(coin == b'1\n'): 
        status = 'on' 
    elif(coin == b'0\n'): 
        status = 'off' 
    return status
 

@app.route('/api/relay/status1')
def relay_status1():

    data2 = subprocess.check_output(["gpio", "read", "0"])
    coin = data2
    if(coin == b'1\n'):
        status = 'on'
    elif(coin == b'0\n'):
        status = 'off'
    return status

@app.route('/api/relay/status2')
def relay_status2():
    
    etat = open("etat.txt", "r")
    status2 = etat.read()
    return status2


@app.route('/api/temp2')
def temp():   
    sensor2 = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
    sensor2 = sensor2.decode(encoding='UTF-8')
    sensor2 = sensor2.split("temp=")[1].split("'C")[0]
    sensor2 = sensor2.split("temp=")[0].split("'C")[0]
    return sensor2


@app.route('/api/rideaux/ouvrir')
def ouvrir():
    os.system("python open.py")
    return "OK"

@app.route('/api/rideaux/fermer')
def fermer():
    os.system("python close.py")
    return "OK"

@app.route('/api/rideaux/stop')
def fermer():
    os.system("python stop.py")
    return "OK"
@app.route('/script.js')
def index():
    # rb pour lire en mode 'binaire' (nécessaire pour les images etc)
    return open('script.js', 'rb').read()

@app.route('/jquery-2.1.0.min.js')
def index():
    # rb pour lire en mode 'binaire' (nécessaire pour les images etc)
    return open('jquery-2.1.0.min.js', 'rb').read()

@app.route('/bootstrap.min.js')
def index():
    # rb pour lire en mode 'binaire' (nécessaire pour les images etc)
    return open('bootstrap.min.js', 'rb').read()


@app.route('/bootstrap-theme.min.css')
def index():
    # rb pour lire en mode 'binaire' (nécessaire pour les images etc)
    return open('bootstrap-theme.min.css', 'rb').read()

@app.route('/bootstrap.min.css')
def index():
    # rb pour lire en mode 'binaire' (nécessaire pour les images etc)
    return open('bootstrap.min.css', 'rb').read()

app.run(host='', port=8088, reloader=True)

