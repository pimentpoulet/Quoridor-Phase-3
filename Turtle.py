import turtle


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