import turtle,time,random

Liste=[]
skor=0
maxSkor=0

w = turtle.Screen()
w.title("yılan oyunu")
w.setup(600, 600)
w.bgcolor("yellow")
w.tracer(0)

yn = turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("blue")
yn.penup()
yn.goto(0, 0)
yn.yon = 'dur'


def hareket():
    if yn.yon == "ust":
        y = yn.ycor()
        yn.sety(y + 20)
    if yn.yon == "alt":
        y = yn.ycor()
        yn.sety(y - 20)
    if yn.yon =="sag":
        x = yn.xcor()
        yn.setx(x + 20)
    if yn.yon =="sol":
        x = yn.xcor()
        yn.setx(x - 20)


def yukariGit():
    if yn.yon != "alt":
        yn.yon = "ust"


def asagiGit():
    if yn.yon != "ust":
        yn.yon = "alt"


def sagaGit():
    if yn.yon != "sol":
        yn.yon = "sag"


def solaGit():
    if yn.yon != "sag":
        yn.yon = "sol"


w.listen()
w.onkeypress(yukariGit, "Up")
w.onkeypress(asagiGit, "Down")
w.onkeypress(sagaGit, "Right")
w.onkeypress(solaGit, "Left")


    
   

yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("black")
yem.penup()
yem.goto(0,100)



def ye():
    if yn.distance(yem)<20 :
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        yem.goto(x,y)
        
        kuyruk=turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        Liste.append(kuyruk)
        global skor
        global maxSkor
        skor+=5
        if skor>maxSkor:
            maxSkor=skor
            w.title("Skor:{} En yüksek skor:{}".format(skor,maxSkor))
    uzunluk = len(Liste)
    for indis in range(uzunluk-1,0,-1):
        x = Liste[indis-1].xcor()
        y = Liste[indis-1].ycor()
        Liste[indis].goto(x,y)
    if len (Liste)>0:
        x=yn.xcor()
        y=yn.ycor()
        Liste[0].goto(x,y)

def baslangic():
    time.sleep(0.1)
    yn.goto(0,0)
    yn.yon="dur"    
    for eklem in Liste:
        eklem.goto(1000,1000)
    Liste.clear()
    skor=0
    w.title("skor{} En yüksek puan:{}" .format(skor,maxSkor))



while True:
    w.update()
    ye()
    hareket()
    if yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290:
        baslangic()
    for eklem in Liste:
        if eklem.distance(yn)<20:
            baslangic()
    time.sleep(0.1)
    
    
        
        
    