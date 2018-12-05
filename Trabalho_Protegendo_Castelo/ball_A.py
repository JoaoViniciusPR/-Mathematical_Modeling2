class ball_C():
    def __init__(self,gravity):
        self.x = int(random(115,1200-115))
        self.vetor = PVector(self.x,0)
        self.velvetor = PVector(0,0)
        self.aclvetor = PVector(0,gravity)
        self.aux = 0
        self.s0 = millis()
        self.img = 0
        
        
    def draw_ball(self):
        self.death = 0
        self.count = 0
        self.velvetor.add(self.aclvetor)
        self.vetor.add(self.velvetor)
        fill(0,200,0)
        #ellipse(self.vetor.x,self.vetor.y,30,30)
        image(self.img,self.vetor.x-15,self.vetor.y-15,30,30)
        
        if self.vetor.y >= 700 and millis()-self.s0>2000:
            self.count = 1
            if self.vetor.x > 100 and self.vetor.x < 1200-100:
                self.death = 1
            self.__init__(self.aclvetor.y)
        
    def update_bullet(self,bulletvetor,bulletvelvetor):
        self.bulletvetor = bulletvetor
        self.bulletvelvetor = bulletvelvetor
        self.distance = self.bulletvetor.copy().sub(self.vetor)
        if self.distance.mag() <= 35 and self.aux==0:
            self.aux = 1
            self.collision()
        
    def proj(self,a,b):
        c = b.mult(PVector.dot(a,b)/PVector.dot(b,b))
        return c
    
    def collision(self):
        if self.aux==1:
            self.velang = (2*self.bulletvelvetor.mag())/15
            self.distanceperp = PVector(-self.distance.y,self.distance.x)
            self.projectionx = self.proj(self.bulletvelvetor,self.distance)
            self.projectiony = self.proj(self.bulletvelvetor,self.distanceperp)
            self.bulletvelvetor = self.projectiony
            self.velvetor.x = self.projectionx.x
            self.velvetor.y = self.projectionx.y
            self.aux=2
