class cannon_C():
    def __init__(self,cannonx,cannony,way):
        self.x = cannonx
        self.y = cannony
        self.ang = 0
        self.way = way
        self.img = 0
        
    def ang_upd(self,e):
        vari = 10*e*self.way
        if self.ang <= -90 and vari <= -10:
            self.ang = -90
        elif self.ang >= 90 and vari >= 10:
            self.ang = 90
        else:
            self.ang += vari
        
    def draw_cannon(self):
        pushMatrix()
        translate(self.x,self.y)
        rotate(radians(self.ang))
        image(self.img,-35,-100,70,135)
        popMatrix()
