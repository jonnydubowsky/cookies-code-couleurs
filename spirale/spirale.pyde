size(630,724,P2D)
frame.setLocation(1366-630, 0)
background(255)
noStroke()

rouge = color(255, 0, 0)
vert = color(0, 255, 0)
verte = vert


def peinture(rouge, vert, bleu):
    fill(rouge, vert, bleu)
    
def aumilieu():
    resetMatrix()
    translate (width/2, height/2)
    

def remonte ():
    translate (0, -40)
    
def descend ():
    translate (0, 40)
    
def agauche ():
    translate (-40, 0)

def cercle(rayon):
    ellipse(0,0,rayon,rayon)

def carre(largeur):
    rect(0,0,largeur,largeur)
    
def hexagone(taille):
    pushMatrix()
    translate (taille, taille)
    beginShape()
    stroke(0,0)
    for i in range (6):
        x = cos( i * THIRD_PI ) * taille
        y = sin( i * THIRD_PI ) * taille
        vertex( x, y )
    endShape()
    popMatrix()

    
def spirale(forme, fois):
    pushMatrix()
    translate(width/2, height/2)
    for n in range(fois):
        rotate (0.1)
        translate(n/10+5, 0)
        forme(20)
    popMatrix()
     
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# Au dessus ce sont les définitions de nos formes         
             
               
# Copiez les noms de vos formes en dessous de cette ligne        
# v v v v v v v v v v v v v v v v v v v v v v v v v v v v
                    
peinture(0,100,193)
spirale(carre, 250)
remonte()
remonte()

peinture(240, 0, 170)
spirale(carre, 250)


aumilieu()

descend()
agauche()
agauche()
agauche()
agauche()
agauche()
agauche()

peinture(120, 250, 160)
spirale(hexagone, 800)



# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# Ici c'est la fin... 
