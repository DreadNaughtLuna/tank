from globals import *


deg = PI/180
'''START REMOVING BITS OF THE DESIGN FEATURE TO SEE WHICH ONE IS CAUSING THE PROBLEM, DRAWING IS WORKING.'''

class Tank:
    def __init__(self, x, y, w, h, health, recharge, barrLength, elAngle, color):
        self.pos = PVector(x,y)
        self.w = w
        self.h = h
        self.color = color
        self.health = health
        self.recharge = recharge
        self.maxRecharge = recharge
        self.barrLength = barrLength
        self.elAngle = elAngle
        self.design = \
        createGraphics(1000, 1000)
        self.design.beginDraw()
        #self.design.rectMode(CENTER)
        self.design.fill(color)
        self.design.line(turretSize/2, turretSize/2, turretSize/2 + cos(elAngle*deg) * barrLength, turretSize/2 + sin (elAngle*deg) * barrLength)
        self.design.line(turretSize/2, turretSize/2, turretSize/2 + 10, turretSize/2)
        self.design.rect(0, 0, turretSize, turretSize)
        #self.design.rect(0, 0, 999, 999)
        self.design.endDraw()
        
    def draw (self):
        image(self.design, self.pos.x, self.pos.y)
        #rect(self.pos.x, self.pos.y, self.w, self. h)
