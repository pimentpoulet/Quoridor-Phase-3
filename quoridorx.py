import turtle
import time
from quoridor import Quoridor

class QuoridorX(Quoridor):
    """
    Classe QuoridorX pour jouer avec une représentation graphique
    """

    def __init__(self, *args):
        """
        Constructeur de QuoridorX
        """

        super().__init__(*args)

        self.sc = turtle.Screen()

    def afficher(self):
        """
        Méthode pour afficher l'état de jeu graphiquement
        """


        # Créer un objet screen
        #sc.title('Jeu Quoridor')
        self.sc.title('Jeu Quoridor')
        turtle.bgcolor('light salmon')


        # Tortues pour le damier
        dbitch1 = turtle.Turtle()
        dbitch1.pensize(2)

        dbitch2 = turtle.Turtle()
        dbitch2.pensize(2)


        # Tortue pour les joueurs
        #dbitch3 = turtle.Turtle()        # Joueur 1
        #dbitch4 = turtle.Turtle()        # Joueur 2
        #dbitch3.color('black', 'royal blue')
        #dbitch4.color('black', 'orange red')

        self.dbitch3 = turtle.Turtle()
        self.dbitch3.color('black', 'royal blue')
        self.dbitch3.hideturtle()
        self.dbitch3.penup()
        self.dbitch3.setpos(-225, -275)
        self.dbitch3.goto((self.état['joueurs'][0]['pos'][0]*50)-251,
         (self.état['joueurs'][0]['pos'][1]*50)-314)
        self.dbitch3.pendown()
        self.dbitch3.begin_fill()
        self.dbitch3.circle(15)
        self.dbitch3.end_fill()

        self.dbitch4 = turtle.Turtle()
        self.dbitch4.color('black', 'orange red')
        self.dbitch4.hideturtle()
        self.dbitch4.penup()
        self.dbitch4.setpos(-225, -275)
        self.dbitch4.goto((self.état['joueurs'][1]['pos'][0]*50)-251,
         (self.état['joueurs'][1]['pos'][1]*50)-314)
        self.dbitch4.pendown()
        self.dbitch4.begin_fill()
        self.dbitch4.circle(15)
        self.dbitch4.end_fill()

        # Tortue pour les murs horizontaux
        dbitch5 = turtle.Turtle()
        dbitch5.pensize(5)
        dbitch5.pencolor('black')


        # Tortue pour les murs verticaux
        dbitch6 = turtle.Turtle()
        dbitch6.pensize(5)
        dbitch6.pencolor('black')


        # Tortue pour la légende
        dbitch7 = turtle.Turtle()


        # Créer l'écran
        #sc.setup(700, 850)
        self.sc.setup(700, 850)
        #sc.tracer(n=0)
        self.sc.tracer(n=0)


        # Centrer le dessin dans l'écran et relocaliser les tortues à la nouvelle origine

        dbitch1.hideturtle()
        dbitch2.hideturtle()
        #dbitch3.hideturtle()
        #dbitch4.hideturtle()
        dbitch5.hideturtle()
        dbitch6.hideturtle()
        dbitch7.hideturtle()

        dbitch1.penup()
        dbitch1.setpos(-225, -275)

        dbitch2.penup()
        dbitch2.setpos(-225, -275)

        #dbitch3.penup()
        #dbitch3.setpos(-225, -275)

        #dbitch4.penup()
        #dbitch4.setpos(-225, -275)

        dbitch7.penup()
        dbitch7.setpos(-225, -275)


        # COMMENCEMENT DU DESSIN

        # dbitch1 trace les rectangles horizontaux

        for i in range(9):
            for j in range(2):

                dbitch1.pendown()
                dbitch1.forward(450)
                dbitch1.left(90)

                dbitch1.forward(50)
                dbitch1.left(90)

        # dbitch 1 ajuste sa position horizontale

            dbitch1.left(90)
            dbitch1.forward(50)
            dbitch1.right(90)

        dbitch1.penup()

        # dbitch1 trace les rectangles verticaux

        dbitch1.goto(-225, -275)

        for i in range(9):
            for j in range(2):

                dbitch1.pendown()
                dbitch1.forward(50)
                dbitch1.left(90)

                dbitch1.forward(450)
                dbitch1.left(90)

        # dbitch1 ajuste sa position verticale

            dbitch1.forward(50)


        # dbitch2 trace les chiffres horizontaux

        x = -202

        for i in range(9):
            dbitch2.penup()
            dbitch2.goto(x, -310)
            dbitch2.pendown()
            dbitch2.write(i+1, font=("Arial", 12, "normal"))

            x += 50

        # dbitch2 trace les chiffres verticaux

        y = -258

        for i in range(9):
            dbitch2.penup()
            dbitch2.goto(-255, y)
            dbitch2.pendown()
            dbitch2.write(i+1, font=("Arial", 12, "normal"))

            y += 50


        # dbitch5 place les murs horizontaux

        for i in self.état['murs']['horizontaux']:

            dbitch5.penup()
            dbitch5.goto((i[0]*50)-275, (i[1]*50)-325)
            dbitch5.pendown()
            dbitch5.forward(100)
            dbitch5.penup()


        # Placer les murs verticaux

        for i in self.état['murs']['verticaux']:

            dbitch6.penup()
            dbitch6.goto((i[0]*50)-275, (i[1]*50)-325)
            dbitch6.pendown()
            dbitch6.left(90)
            dbitch6.forward(100)
            dbitch6.setheading(0)
            dbitch6.penup()


        dbitch7.left(180)
        dbitch7.forward(40)
        dbitch7.right(90)
        dbitch7.forward(470)
        dbitch7.pendown()

        #dbitch7.write(self.formater_légende(), font=("Monaco", 18, "normal"))
        dbitch7.write(f"Légende:\n\nRoyal Blue = {self.état['joueurs'][0]['nom']}\n\n"
        f"Orange Red = {self.état['joueurs'][1]['nom']}\n", font=("Monaco", 18, "normal"))

        self.dbitch3.clear()
        self.dbitch4.clear()

        #move = sc.textinput("Quel type de coup voulez-vous jouer?", "(D, MH, MV)")
        #position2 = []
        #if move in ['D', 'MH' 'MV']:

        #    position1 = sc.textinput("À quelle position voulez-vous jouer?", "(x, y)")

        #    position2.append(int(position1[0]))
        #    position2.append(int(position1[2]))



        #return (move, position2)

    def effacer(self):
        """
        Méthode pour afficher l'état de jeu graphiquement
        """
        self.dbitch3.clear()
        self.dbitch4.clear()

    def demander_coup(self):

        move = self.sc.textinput("Quel type de coup voulez-vous jouer?", "(D, MH, MV)")

        position2 = []
        if move in ('D', 'MH', 'MV'):
            position1 = self.sc.textinput("À quelle position voulez-vous jouer?", "(x, y)")

            position2.append(int(position1[0]))
            position2.append(int(position1[2]))

        return (move, position2)

#x = QuoridorX([{"nom": "Alfred", "murs": 6, "pos": [5, 5]}, {"nom": "Robin", "murs": 3, 
# "pos": [8, 6]}], {"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8], [5, 5]], 
# "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]})
#x.afficher()
