import pygame
import sys
from math import sqrt

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255,255,0)
green = (0,255,0)
size = [1200,1200]

def middle(point_A, point_B):
    """
    Retourne le milieu du point A et B
    
    Parameters:
    
    point_A : un tuple de 2 nombres (Xa, Ya)
    point_B : un tuple de 2 nombres (Xb, Yb)
    
    Return:
    le milieu de A et B : un tuple de 2 nombres
    """
    return((point_A[0]+point_B[0])/2,(point_A[1]+point_B[1])/2)
    

def sierpinski(screen, points, level, color = white):
    """
    Fonction qui dessine les triangles de Sierpinski
    
    Parameters:
    
    screen : la surface sur laquelle dessiner
    points : un tuple de 3 points
    level (int) : le niveau
    color : la couleur, un tuple de 3 valeurs entre 0 et 255

    Return:
    None
    """
    if level==1:
        pass
    else:
        ma=middle(points[0],points[1])
        mb=middle(points[1],points[2])
        mc=middle(points[0],points[2])
        pygame.draw.polygon(screen, color, (ma, mb, mc))
        sierpinski(screen,(points[0],ma,mc), level-1,red)
        sierpinski(screen,(points[2],mb,mc), level-1,blue)
        sierpinski(screen,(points[1],ma,mb), level-1,green)
        pygame.display.flip()

pygame.init()
fenetre = pygame.display.set_mode(size)
fenetre.fill(white)

A = (0, 0) # Le point A en haut à gauche
B = (size[0], 0) #Le point B en haut à droite
C = (size[0]/2, size[0]*sqrt(3)/2) # Le 3eme point du triangle équilateral

pygame.draw.polygon(fenetre, yellow, (A, B, C)) # dessin du premier triangle
sierpinski(fenetre, (A, B, C), 9)

 ##Permet d'afficher le dessin

# Boucle infinie qui attend l'événement QUIT pour terminer le programme
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()