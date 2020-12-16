# Import Serial & Visualization Library

import serial
from vpython import *

arduinoSerialData = serial.Serial('COM10', 9600)

measuringRod = cylinder(length = 6, color = color.yellow, \
                        radius = 0.1, pos = vector(-3,-2,0))

lengthLabel = label(text = 'Target Distance is: ' , \
                    pos = vector(0,3,0), height = 30, box=0)
                        
target = box(color = color.green, length = 0.2, width = 3, \
             pos = vector(0, -0.5, 0) )

while(1 == 1):
    rate(20)
    if(arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        distance = float(myData)
        print(distance)
        myLabel = 'Target Distance is: ' + str(distance) + 'cm'
        lengthLabel.text = myLabel
        target.pos = vector( -3 + distance, -0.5, 0)
        measuringRod.length = distance
