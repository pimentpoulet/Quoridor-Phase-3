import turtle

# Créer un objet screen
sc = turtle.Screen()
sc.title('Jeu Quoridor')


# Créer nos objets turtle
dbitch1 = turtle.Turtle()
dbitch2 = turtle.Turtle()
dbitch3 = turtle.Turtle()
dbitch4 = turtle.Turtle()

# Créer l'écran
sc.setup(1000, 1000)

# Paramétriser la vitesse de dessin
dbitch1.speed(15)
dbitch2.speed(15)
dbitch3.speed(5)
dbitch4.speed(5)

def draw_damier(d=9):

# dbitch1 trace les rectangles horizontaux

    for i in range(d):
        for j in range(2):

            dbitch1.forward(450)
            dbitch1.left(90)

            dbitch1.forward(50)
            dbitch1.left(90)

# dbitch2 trace les rectangles verticaux

            dbitch2.forward(50)
            dbitch2.left(90)

            dbitch2.forward(450)
            dbitch2.left(90)

# dbitch 1 ajuste sa position horizontale

        dbitch1.left(90)
        dbitch1.forward(50)
        dbitch1.right(90)

# dbitch2 ajuste sa position verticale

        dbitch2.forward(50)

# dbitch 3 trace les chiffres horizontaux

    dbitch3.left(180)
    dbitch3.forward(50)

    x = 23
    for i in range(9):
        dbitch3.penup()
        dbitch3.goto(x, -25)
        dbitch3.pendown()
        dbitch3.write(i)

        x += 50

# dbitch4 trace les chiffres verticaux

    dbitch4.right(90)
    dbitch4.forward(50)

    y = 23

    for i in range(9):
        dbitch4.penup()
        dbitch4.goto(-25, y)
        dbitch4.pendown()
        dbitch4.write(i)

        y += 50

draw_damier()