sizex = 1200
sizey = 800
sizes = PVector(sizex,sizey)
gravity = 0.10
velcannon = 10
highscore = 0

way = 1 #1: Scrool do mouse aumenta, canhão para esquerda, -1: inverso
def var(x):
    global aux,bullet,s0,score,playing,deaths,starti
    aux = False
    bullet = []
    s0 = -1500
    score = 0
    deaths = 0
    playing = True
    if x == 1:
        starti = False
    if x == 2:
        starti = True


from cannon_A import cannon_C
from bullet_A import bullet_C
from ball_A import ball_C

cannon = cannon_C(sizex/2,sizey-35,way)
ball = ball_C(gravity)
    
def setup():
    global img,imgc0,imgc1,imgc2,imgc3,imggo,imgba,imgbu,imgcn,imgsc,imghs
    size(sizex,sizey)
    frameRate(105)
    var(1)
    img = loadImage("CapaInicial.jpg")
    imgc0 = loadImage("Castle0.png")
    imgc1 = loadImage("Castle1.png")
    imgc2 = loadImage("Castle2.png")
    imgc3 = loadImage("Castle3.png")
    imggo = loadImage("GameOver.png")
    imgba = loadImage("Ball.png")
    imgbu = loadImage("Bullet.png")
    imgcn = loadImage("Cannon.png")
    imgsc = loadImage("Score.png")
    imghs = loadImage("Scorehigh.png")
    
    background(img)

def draw():
    #translate(0,-35)
    global aux,bullet,score,highscore,playing,deaths,starti,collision,ball
    global imgc0,imgc1,imgc2,imgc3,imggo,imgba,imgbu,imgcn,imgsc,imghs
    if starti:
        if playing:
            plotimg(deaths)
            ball.img = imgba
            ball.draw_ball()
            if aux:
                for bull in bullet:
                    bull.img = imgbu
                    bull.draw_bullet()
                    ball.update_bullet(bull.vetor,bull.velvetor)
            cannon.img = imgcn
            cannon.draw_cannon()
            if ball.death == 1:
                deaths += 1
                score -= 1
            if ball.count == 1:
                score += 1
            if deaths == 3:
                plotimg(deaths)
                playing = False
        else:
            s1 = millis()
            while millis()-s1<500:
                    pass
            fill(200,0,0,100)
            noStroke()
            rect(0,0,1200,800)
            image(imggo,0,0)
            text("{}".format(score),200,100)
            text("{}".format(highscore),1140,100)
            noLoop()
        highscore = max(highscore,score)
        textSize(50)
        image(imgsc,0,33,350,100)
        image(imghs,990,33,950,100)
        text("{}".format(score),200,100)
        text("{}".format(highscore),1140,100)
    
def mouseMoved():
    cannon.x = mouseX
    
def mouseWheel(event):
    e = event.getCount()
    cannon.ang_upd(e)
    
def mouseClicked():
    global aux,sizes,bullet,collision,s0
    if millis()-s0>1000:
        direction = PVector.fromAngle(radians(cannon.ang)-HALF_PI)
        origin = direction.copy().mult(50).add(PVector(cannon.x,cannon.y))
        bullet.append(bullet_C(origin,direction,sizes,velcannon,gravity))
        ball.aux = 0
        aux = True
        s0 = millis()
    
def keyPressed():
    global aux,sizes,bullet,collision,starti,s0
    if key == ' ':
        if starti and millis()-s0>1000:
            direction = PVector.fromAngle(radians(cannon.ang)-HALF_PI)
            origin = direction.copy().mult(50).add(PVector(cannon.x,cannon.y))
            bullet.append(bullet_C(origin,direction,sizes,velcannon,gravity))
            ball.aux = 0
            aux = True
            s0 = millis()
        else:
            starti = True
        
    if key == 'r' or key == 'R':
        loop()
        var(2)
        
    if key == 'm' or key == 'M':
        global img
        loop()
        var(1)
        background(img)
        
def plotimg(x):
    global imgc0,imgc1,imgc2,imgc3
    if x == 0:
        background(imgc0)
    elif x == 1:
        background(imgc1)
    elif x == 2:
        background(imgc2)
    elif x == 3:
        background(imgc3)
