size(200,500,P2D)
noStroke()

def cercle(rayon):
    ellipse(0,0,rayon,rayon)

def unecouche(couleur):
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

randomSeed(0)
blendMode(BLEND)
background(255)    

#Copiez vos formes en dessous 
#    v    v     v    v    v

unecouche(color(7,131,16))
unecouche(color(116,49,193))

blendMode(EXCLUSION)
fill(255)
for n in range(5):
    pushMatrix()
    translate(random(width),random(height))
    cercle(150)
    popMatrix()

