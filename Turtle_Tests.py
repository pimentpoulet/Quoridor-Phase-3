import turtle

fen = turtle.Screen()
fen.title("Ma fenêtre de tortues!")
fen.setup(width=800, height=600)
alex = turtle.Turtle()

alex.forward(50) # avancer de 50 pixels
alex.left(90)    # tourner de 90° en sens anti-horaire
alex.forward(30) # avancer de 30 pixels

alex.pensize(10)
alex.pencolor('red')
alex.left(30)
alex.forward(100)

alex.penup()
alex.forward(30)
alex.pendown()
alex.left(60)
alex.pensize(5)
alex.pencolor('blue')
alex.forward(100)

alex.fillcolor('black')
alex.begin_fill()
alex.left(30)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.end_fill()

print(alex.shape())
alex.shape('turtle')

alex.stamp()
alex.forward(50)
alex.stamp()

joe = turtle.Turtle()
joe.shape('turtle')

alex.right(120)
alex.forward(100)
joe.right(90)
joe.forward(100)

poly = ((-20,-20),(0,50),(20,-20),(-20,-20))
turtle.addshape('maforme', poly)
joe.shape('maforme')
joe.pencolor('blue')
joe.fillcolor('white')

joe.left(45)
joe.forward(100)


# Tracer un polygone :

def tracerPolygone(toto, poly):
    ''' À l'aide de la tortue *toto*, tracer un polygone
    défini par une séquence *poly* de coordonnées absolues.'''
    toto.penup()
    toto.goto(poly[0])
    toto.pendown()
    for pos in poly[1:]:
        toto.goto(pos)


tracerPolygone(joe, ((200, 0),(200, 200),(150, 250),
                     (210, 280), (270, 250), (220, 200),
                     (220, 0), (200, 0)))

fen.clearscreen()

fen = turtle.Screen()
fen.title("Ma fenêtre de tortues!")
fen.setup(width=800, height=600)
alex = turtle.Turtle()
alex.forward(250)

fen.clearscreen()


# Appuyer sur espace :

#def tourner():
#    fen.onkeypress(None, 'space')
#    alex.forward(10)
#    alex.left(5)
#    fen.onkeypress(tourner, 'space')


#fen = turtle.Screen()
#fen.setup(width=500, height=500)
#fen.onkeypress(tourner, 'space')
#fen.listen()
#alex = turtle.Turtle()
#fen.mainloop()


# Cliquer sur l'écran :

def tracerClic(x, y):
    fen.onclick(None, btn=1)
    alex.setheading(alex.towards(x, y))
    alex.goto(x, y)
    fen.onclick(tracerClic, btn=1)


def changerModeEcriture():
    fen.onkeypress(None, 'space')
    if alex.isdown():
        alex.penup()
        alex.fillcolor('white')
    else:
        alex.pendown()
        alex.fillcolor('black')
    fen.onkeypress(changerModeEcriture, 'space')


fen = turtle.Screen()
fen.setup(width=500, height=500)
fen.onclick(tracerClic, btn=1)
fen.onkeypress(changerModeEcriture, 'space')
fen.listen()
alex = turtle.Turtle()
fen.mainloop()

class App:
    def __init__(self, largeur, hauteur):
        self.fen = turtle.Screen()
        self.fen.setup(largeur, hauteur)
        self.fen.onclick(self.changerOrientation, btn=1)
        self.fen.onkeypress(self.changerModeEcriture, 'space')
        self.fen.listen()
        self.alex = turtle.Turtle()
        self.alex.speed('fastest')
        self.clic = None

    def changerOrientation(self, x, y):
        self.clic = turtle.Vec2D(x, y)

    def changerModeEcriture(self):
        self.fen.onkeypress(None, 'space')
        if self.alex.isdown():
            self.alex.penup()
            self.alex.fillcolor('white')
        else:
            self.alex.pendown()
            self.alex.fillcolor('black')
        self.fen.onkeypress(self.changerModeEcriture, 'space')

    def go(self):
        if self.clic:
            self.alex.setheading(self.alex.towards(self.clic))
            self.clic = None
        self.alex.forward(2)
        turtle.ontimer(x.go, 0)


x = App(800, 600)
turtle.ontimer(x.go, 0)
turtle.mainloop()