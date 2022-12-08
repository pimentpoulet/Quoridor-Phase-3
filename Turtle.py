import turtle

fen = turtle.Screen()
fen.title('Jeu Quoridor')
fen.setup(width=800, height=800)
drawbitch = turtle.Turtle()


# Faire une première ligne horizontale de 600 pixels :

drawbitch.forward(250)
drawbitch.left(180)
drawbitch.forward(500)


# Faire une ligne verticale de 600 pixels :

drawbitch.right(90)
drawbitch.forward(250)
drawbitch.right(180)
drawbitch.forward(500)


# Faire les lignes horizontales du damier :

# Ligne du bas

drawbitch.left(90)
drawbitch.forward(500)

drawbitch.left(90)
drawbitch.forward(50)

drawbitch.left(90)

# Deuxième ligne

drawbitch.forward(500)

drawbitch.right(90)
drawbitch.forward(50)

drawbitch.right(90)

# Troisième ligne

drawbitch.forward(500)

drawbitch.left(90)
drawbitch.forward(50)

drawbitch.left(90)

# Quatrième ligne

drawbitch.forward(500)

drawbitch.right(90)
drawbitch.forward(50)

drawbitch.right(90)

# Cinquième ligne

drawbitch.forward(500)

drawbitch.left(90)
drawbitch.forward(50)

drawbitch.left(90)

# Sixième ligne

drawbitch.forward(500)

drawbitch.right(90)
drawbitch.forward(50)

drawbitch.right(90)

# Septième ligne

drawbitch.forward(500)

drawbitch.left(90)
drawbitch.forward(50)

drawbitch.left(90)

# Huitième ligne

drawbitch.forward(500)

drawbitch.right(90)
drawbitch.forward(50)

drawbitch.right(90)

# Neuvième ligne

drawbitch.forward(500)

drawbitch.left(90)
drawbitch.forward(50)

drawbitch.left(90)

# Dixième ligne

drawbitch.forward(500)

drawbitch.right(90)
drawbitch.forward(50)

drawbitch.right(90)

# Onzième ligne

drawbitch.forward(500)
drawbitch.right(90)
drawbitch.forward(50)


# Faire les lignes verticales du damier :

# Faire la première colonne

drawbitch.forward(400)
drawbitch.right(90)
drawbitch.forward(50)
drawbitch.right(90)
drawbitch.forward(450)

# Deuxième colonne

drawbitch.left(90)
drawbitch.forward(50)
drawbitch.left(90)
drawbitch.forward(450)

# Faire la première colonne

drawbitch.right(90)
drawbitch.forward(50)
drawbitch.right(90)
drawbitch.forward(450)

# Deuxième colonne

drawbitch.left(90)
drawbitch.forward(50)
drawbitch.left(90)
drawbitch.forward(450)

# Troisième colonne

drawbitch.right(90)
drawbitch.forward(50)
drawbitch.right(90)
drawbitch.forward(450)

# Quatrième colonne

drawbitch.left(90)
drawbitch.forward(50)
drawbitch.left(90)
drawbitch.forward(450)

# Cinquième colonne

drawbitch.right(90)
drawbitch.forward(50)
drawbitch.right(90)
drawbitch.forward(450)

# Sixième colonne

drawbitch.left(90)
drawbitch.forward(50)
drawbitch.left(90)
drawbitch.forward(450)

# Septième colonne

drawbitch.right(90)
drawbitch.forward(50)
drawbitch.right(90)
drawbitch.forward(450)

# Huitième colonne

drawbitch.left(90)
drawbitch.forward(50)
drawbitch.left(90)
drawbitch.forward(450)
