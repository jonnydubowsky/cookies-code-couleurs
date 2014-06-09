# Des réglages pour la fenêtre, pour le fond
size(int(displayWidth*0.45),displayHeight-100,P2D)
frame.setLocation(displayWidth-int(displayWidth*0.45), 0)
randomSeed(millis())
blendMode(BLEND)
background(255)
noStroke()

# Des couleurs sympas
blanc = color(255, 255, 255)
rouge = color(255, 0, 0)
vert = color(0, 255, 0)
bleu = color(0, 0, 255)
violet = color(116,49,193)
vertsapin = color(7,131,16)
orange = color(255, 150, 60)


# Des déplacements simples
def aumilieu():
    resetMatrix()
    translate (width/2, height/2)
    
def remonte ():
    translate (0, -40)
    
def monte ():
    remonte()
    
def descend ():
    translate (0, 40)
    
def agauche ():
    translate (-40, 0)
    
def pluspetit():
    scale(0.5)
    
def plusgrand():
    scale(2)
    
def retourne():
    scale(-1, -1)

# Des formes de base
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
    
# Des morceaux de peintures

def kupka(taille):
    tampon = loadImage("kupka.jpg")
    pushMatrix()
    scale(taille)
    image(tampon, 0,0)
    popMatrix()
    
def valensi(taille):
    tampon = loadImage("valensi.jpg")
    pushMatrix()
    scale(taille)
    image(tampon, 0,0)
    popMatrix()
    
def stanton(taille):
    tampon = loadImage("stanton.jpg")
    pushMatrix()
    scale(taille)
    image(tampon, 0,0)
    popMatrix()

# Des opérations magiques

def antonio(couleur):
    for n in range(30):
        pushMatrix()
        scale(1 + (random(10)-5)/20.0)
        translate(random(width), random(height))
        for i in range(110,10,-20):
            fill(couleur)
            cercle(i)
            fill(255)
            cercle(i-12)
        fill(couleur)
        cercle(10)
        popMatrix()
        
        
def splash(forme):
    for n in range(30):
        pushMatrix()
        scale(1 + (random(10)-5)/20.0)
        translate(random(width-n*3), random(height-n*3))
        forme(n*3)
        popMatrix()
    
def zoom(forme, fois):
    for n in range(fois):
        pushMatrix()
        translate(10*n, 10*n)
        forme(n*10)
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


aumilieu()
pluspetit()
pluspetit()
spirale(stanton, 100)

fill(bleu)
aumilieu()
descend()
descend()
descend()
descend()
descend()
descend()
descend()
descend()
descend()
descend()
spirale(cercle, 2300)

resetMatrix()

fill(blanc)
monte()
monte()
agauche()
splash(hexagone)





# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# Ici c'est la fin... 
