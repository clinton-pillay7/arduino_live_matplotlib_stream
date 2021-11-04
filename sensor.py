

import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *


pot = []
pressure = []
arduinoData = serial.Serial('COM3', 9800, timeout=1)
plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0  # Counter value for the data points reset after 50 points
val = arduinoData.readline()  # arduino reader variable


def makeFig():  # matplotlib drawing function
    plt.ylim(1, 2.5)
    plt.title("Potentiometer sensor")
    plt.grid(True)
    plt.ylabel("Resistance Value")
    plt.plot(pot, 'ro-')


while True:  # While loop that loops forever
    while (arduinoData.inWaiting() == 0):  # Wait here until there is data
        pass  # do nothing
    # read the line of text from the serial port
    arduinoString = arduinoData.readline()
    # Convert data to floating number and put in Potentiometer
    potvalue = float(arduinoString)
    # Build our Potentiometer array by appending potentiometer readings
    pot.append(potvalue)
    # Call drawnow to update our live graph
    drawnow(makeFig)  
    plt.pause(.0001)
    cnt = cnt + 1
    if(cnt > 50):  # If you have 50 or more points, delete the first one from the array
        pot.pop(0)  # This allows us to just see the last 50 data points
