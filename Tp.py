import turtle

t = turtle.Turtle()
t.speed(0)  #Vitesse maximale, pour que le dessin se fasse vite
t.pensize(2)    #Le trait fait 2 pixels dépaisseur
turtle.bgcolor("black")   #le backgroundcolor est en noir
couleurs = ["cyan", "magenta", "yellow", "orange", "white", "red"]

def petale(taille):  
    for _ in range(2):
        t.circle(taille, 60)
        t.left(120)
def fleur(taille, nb_petales):
    for i in range(nb_petales):
        t.color(couleurs[i % len(couleurs)])
        petale(taille)
        t.left(360 / nb_petales)

# Mandala : la même fleur répétée en cercle
for i in range(12):
    fleur(60, 8)
    t.forward(80)
    t.left(30)
t.hideturtle()
turtle.done()