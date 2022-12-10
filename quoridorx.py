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
        turtle.bgcolor('dim grey')


        # Tortues pour le damier
        dbitch1 = turtle.Turtle()
        dbitch1.pensize(2)

        dbitch2 = turtle.Turtle()
        dbitch2.pensize(2)


        # Tortue pour les joueurs
        dbitch3 = turtle.Turtle()        # Joueur 1
        dbitch4 = turtle.Turtle()        # Joueur 2
        dbitch3.color('black', 'royal blue')
        dbitch4.color('black', 'orange red')

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
        sc.setup(700, 850)
        sc.tracer(n=2)


        # Centrer le dessin dans l'écran et relocaliser les tortues à la nouvelle origine

        dbitch1.hideturtle()
        dbitch2.hideturtle()
        dbitch3.hideturtle()
        dbitch4.hideturtle()
        dbitch5.hideturtle()
        dbitch6.hideturtle()
        dbitch7.hideturtle()

        dbitch1.penup()
        dbitch1.setpos(-225, -275)

        dbitch2.penup()
        dbitch2.setpos(-225, -275)

        dbitch3.penup()
        dbitch3.setpos(-225, -275)

        dbitch4.penup()
        dbitch4.setpos(-225, -275)
        
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


        # dbitch3 place le joueur 1

        dbitch3.penup()
        dbitch3.goto((self.état['joueurs'][0]['pos'][0]*50)-251, (self.état['joueurs'][0]['pos'][1]*50)-314)
        dbitch3.pendown()
        dbitch3.begin_fill()
        dbitch3.circle(15)
        dbitch3.end_fill()

        # dbitch3 place le joueur 2

        dbitch4.penup()
        dbitch4.goto((self.état['joueurs'][1]['pos'][0]*50)-251, (self.état['joueurs'][1]['pos'][1]*50)-314)
        dbitch4.pendown()
        dbitch4.begin_fill()
        dbitch4.circle(15)
        dbitch4.end_fill()


        # dbitch4 place les murs horizontaux

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


        if len(self.état['joueurs'][0]['nom']) >= len(self.état['joueurs'][1]['nom']):
            c_1 = 1
            c_2 = len(self.état['joueurs'][0]['nom']) - len(self.état['joueurs'][1]['nom']) + 1
        else:
            c_1 = len(self.état['joueurs'][1]['nom']) - len(self.état['joueurs'][0]['nom']) + 1
            c_2 = 1

        k_1 = 10-self.état['joueurs'][0]['murs']
        k_2 = 10-self.état['joueurs'][1]['murs']

        dbitch7.left(180)
        dbitch7.forward(40)
        dbitch7.right(90)
        dbitch7.forward(470)
        dbitch7.pendown()
        dbitch7.write(f"Légende:\n\n1={self.état['joueurs'][0]['nom']},{c_1*' '}murs={self.état['joueurs'][0]['murs']*'|'}{(k_1-1)*' '} (royal blue)\n\n2={self.état['joueurs'][1]['nom']},{c_2*' '}murs={self.état['joueurs'][1]['murs']*'|'}{(k_2-1)*' '} (orange red)\n", font=("Monaco", 18, "normal"))

        

        




        #sc.textinput("Quel type de coup voulez-vous jouer?", "(D, MH, MV)")

        turtle.Screen().exitonclick()


x = QuoridorX([{"nom": "Alfred", "murs": 7, "pos": [5, 5]}, {"nom": "Robin", "murs": 3, "pos": [8, 6]}], {"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]})

x.afficher()