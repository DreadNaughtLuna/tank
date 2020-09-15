from globals import *
from tank import *

def setup():
    global AFV1
    size(HEIGHT, WIDTH)
    AFV1 = Tank(150, 150, 100, 100, 150, 10, 10, 0, color = color(255,0,0)) 

def drawGrid():
    
    # Oh hey I found the text options
    textAlign(LEFT, TOP) # Bottom left corner of text is the specified x,y co ordinate
    textSize(10) 
    
    stroke(0,0,0,30) # Black with transparency (30/255)
    fill(0,0,0,100) # Black with less transparency (100/255)
    
    # draw vertical lines 
    x = 100
    while x < width:
        line(x,0,x,height)
        text(str(x), x + 2, 2) # Leave a border of 2 pixels
        x = x + 100 # Increment x by 100
    
    y = 100
    while y < height:
        line(0,y,width,y)
        text(str(y), 2, y + 2) # Leave a border of 2 pixels
        y = y + 100 # Increment y by 100 


def draw():
    global AFV1
    #background(100)
    
    AFV1.draw()
    drawGrid()
    
    
'''def keyPressed():
    global bPosX, bVelX, bPosY, bVelY, AFV1.elAngle
    if keyCode == 37:
        AFV1.elAngle -= 1
        
    if keyCode == 39:
        AFV1.elAngle += 1
        
    if keyCode == 32:
        
        bPosX.append(width/2)
        bVelX.append(30*cos(elAngle*deg))
        bPosY.append(height/2)
        bVelY.append(30*sin(elAngle*deg))'''
        
