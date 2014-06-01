size(600,800,P2D)
background(255)
noStroke()

rouge = color(255, 0, 0)

def remonte ():
    translate (0, -40)

def cercle(rayon):
    ellipse(0,0,rayon,rayon)

def carre(largeur):
    rect(0,0,largeur,largeur)
    
def spirale(forme, fois):
    pushMatrix()
    translate(width/2, height/2)
    for n in range(fois):
        rotate (0.1)
        translate(n/10+5, 0)
        forme(20)
    popMatrix()
        
                        
fill(0,200,133)
spirale(carre, 250)
remonte()
remonte()
fill(80, 0, 170)
spirale(carre, 250)
