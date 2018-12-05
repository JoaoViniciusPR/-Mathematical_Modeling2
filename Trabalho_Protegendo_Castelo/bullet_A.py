class bullet_C():
    def __init__(self,origin,direction,sizes,velcannon,gravity):
        self.vetor = origin
        self.velvetor = direction.mult(velcannon)
        self.aclvetor = PVector(0,gravity)
        self.sizes = sizes
        self.img = 0
    
    def draw_bullet(self):
        self.velvetor.add(self.aclvetor)
        self.vetor.add(self.velvetor)
        fill(200,0,0)
        image(self.img,self.vetor.x-15,self.vetor.y-15,30,30)
