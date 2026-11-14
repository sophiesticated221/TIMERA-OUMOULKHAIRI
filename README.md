J’ai réalisé un mandala de fleurs avec Python et la bibliothèque Turtle, qui permet de dessiner à l’écran en donnant des ordres à une petite tortue : avancer, tourner, changer de couleur. 
Mon dessin repose sur une idée simple : construire une grande forme en répétant plusieurs fois une petite forme, un peu comme des poupées russes. 
Tout commence par une fonction appelée petale, qui dessine un pétale à l’aide de deux arcs de cercle de 60 degrés, séparés par un virage de 120 degrés.
Cette fonction reçoit un paramètre, la taille, qui correspond au rayon des arcs et permet donc d’obtenir des pétales plus ou moins grands. 
Ensuite, j’ai créé une deuxième fonction, appelée fleur, qui utilise la première. 
Elle répète le pétale autant de fois que demandé, et entre deux pétales, la tortue tourne de 360 divisé par le nombre de pétales, ce qui garantit que la fleur fait exactement un tour complet et se referme proprement.
Cette fonction change aussi la couleur à chaque pétale en piochant dans une liste de six couleurs.
Pour que les couleurs recommencent au début de la liste quand on arrive à la fin, j’utilise l’opérateur modulo, noté %, qui donne le reste d’une division : c’est la technique que j’ai découverte par moi-même et qui m’a permis d’éviter une erreur de dépassement de liste.
Enfin, le programme principal contient une boucle qui répète douze fois la même séquence : dessiner une fleur de huit pétales, avancer de quatre-vingts pixels, puis tourner de trente degrés. 
Comme douze fois trente degrés font trois cent soixante degrés, les fleurs se placent en cercle et forment le mandala. 
J’ai aussi testé plusieurs modifications pour comprendre le rôle de chaque valeur : en changeant le nombre de pétales, la fleur devient plus simple ou plus dense, et en modifiant la distance ou l’angle entre les fleurs, le cercle s’écarte, se resserre ou ne se referme plus. 
Ce projet m’a appris qu’une fonction permet de réutiliser du code sans le réécrire, qu’une boucle répète une action autant de fois qu’on le souhaite, et qu’en changeant seulement quelques chiffres, on transforme complètement le résultat.
