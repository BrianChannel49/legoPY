from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub() # LEGO


####### BRO TEST HUB

hub.light_matrix.show_image('hello') #--- FUCKING TEST
hub.light_matrix.write(mot)
mot = 'fucking'
x = 49      
y = 50
hub.light_matrix.show_image(x+y)
print(mot)
print('dick')
print('hello')


######### PROGRAM SYMBOL "+ (plus) , - (moin) , * (multiplier) , / (divisé) , % (modele)"


#### LOOPS TEST 

for i in range(10):
    hub.light_matrix.write(i)
    hub.speaker.beep(60,0.2)
    wait_for_seconds(1)












