from quoridor import Quoridor
import turtle

class QuoridorX(Quoridor):
    """
    Classe QuoridorX pour jouer avec une représentation graphique
    """

    def __init__(self, *args):
        """
        Constructeur de QuoridorX
        """
        
        super(QuoridorX, self).__init__(*args)

    def afficher(self):
        """
        Méthode pour afficher l'état de jeu graphiquement
        """

        # Créer un objet screen
        sc = turtle.Screen()
        sc.title('Jeu Quoridor')

        # Créer nos objets turtle

        # Tortues pour le damier
        dbitch1 = turtle.Turtle()
        dbitch2 = turtle.Turtle()
        dbitch3 = turtle.Turtle()
        dbitch4 = turtle.Turtle()

        # Tortue pour le joueur 1
        dbitch5 = turtle.Turtle()

        # Tortue pour le joueur 2
        dbitch6 = turtle.Turtle()

        # Tortue pour les murs horizontaux
        dbitch7 = turtle.Turtle()
        dbitch7.pensize(5)
        dbitch7.pencolor('red')

        # Tortue pour les murs verticaux
        dbitch8 = turtle.Turtle()
        dbitch8.pensize(5)
        dbitch8.pencolor('blue')

        # Créer l'écran
        sc.setup(1000, 1000)
        sc.tracer(n=2)

        # dbitch1 trace les rectangles horizontaux

        for i in range(9):
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

        dbitch1.hideturtle()
        dbitch2.hideturtle()

        # dbitch3 trace les chiffres horizontaux

        dbitch3.left(180)
        dbitch3.forward(50)

        x = 23
        for i in range(9):
            dbitch3.penup()
            dbitch3.goto(x, -25)
            dbitch3.pendown()
            dbitch3.write(i+1)

            x += 50

        dbitch3.hideturtle()

        # dbitch4 trace les chiffres verticaux

        dbitch4.right(90)
        dbitch4.forward(50)

        y = 23

        for i in range(9):
            dbitch4.penup()
            dbitch4.goto(-25, y)
            dbitch4.pendown()
            dbitch4.write(i+1)

            y += 50
        
        dbitch4.hideturtle()

        # Placer le joueur 1

        dbitch5.penup()
        dbitch5.goto((self.état['joueurs'][0]['pos'][0]*50)-27, (self.état['joueurs'][0]['pos'][1]*50)-32)
        dbitch5.pendown()
        dbitch5.write('1')

        dbitch5.hideturtle()

        # Placer le joueur 2

        dbitch6.penup()
        dbitch6.goto((self.état['joueurs'][1]['pos'][0]*50)-27, (self.état['joueurs'][1]['pos'][1]*50)-32)
        dbitch6.pendown()
        dbitch6.write('2')

        dbitch6.hideturtle()

        # Placer les murs horizontaux

        for i in self.état['murs']['horizontaux']:

            dbitch7.penup()
            dbitch7.goto((i[0]*50)-50, (i[1]*50)-50)
            dbitch7.pendown()
            dbitch7.forward(100)
        
        dbitch7.hideturtle()

        # Placer les murs verticaux

        for i in self.état['murs']['verticaux']:

            dbitch8.penup()
            #dbitch8.
            dbitch8.goto((i[0]*50)-50, (i[1]*50)-50)
            dbitch8.pendown()
            dbitch8.left(90)
            dbitch8.forward(100)
            dbitch8.setheading(0)
        
        dbitch8.hideturtle()

        sc.textinput("Quel type de coup voulez-vous jouer?", "(D, MH, MV)")

        turtle.Screen().exitonclick()


x = QuoridorX([{"nom": "Alfred", "murs": 7, "pos": [5, 5]}, {"nom": "Robin", "murs": 3, "pos": [8, 6]}], {"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]})

x.afficher()