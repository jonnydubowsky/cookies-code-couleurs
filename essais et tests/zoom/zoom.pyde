size(600,800,P2D)
background(255)
noStroke()

rouge = color(255, 0, 0)

def cercle(rayon):
    ellipse(0,0,rayon,rayon)

def carre(largeur):
    rect(0,0,largeur,largeur)
    
def hexagone(taille):
    pass

def zoom(forme, fois):
    for n in range(fois):
        pushMatrix()
        translate(10*n, 10*n)
        forme(n*10)
        popMatrix()
  
fill(255, 0, 0)    
zoom(cercle, fois = 40)
fill(0,255,133)
translate (100, 100)
zoom(carre, fois = 20)
