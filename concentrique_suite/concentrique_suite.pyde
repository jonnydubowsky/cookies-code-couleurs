size(400,500,P2D)
noStroke()

# Des couleurs sympas
blanc = color(255, 255, 255)
rouge = color(255, 0, 0)
vert = color(0, 255, 0)
bleu = color(0, 0, 255)
violet = color(116,49,193)
vertsapin = color(7,131,16)

def aumilieu():
    translate (width/2, height/2)
    
def remonte ():
    translate (0, -40)
    
def descend ():
    translate (0, 40)

def cercle(rayon):
    ellipse(0,0,rayon,rayon)

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
        
        
def splash(forme, couleur):
    for n in range(30):
        pushMatrix()
        scale(1 + (random(10)-5)/20.0)
        translate(random(width-n*3), random(height-n*3))
        fill(couleur)
        forme(n*3)
        popMatrix()
    

randomSeed(millis())
blendMode(BLEND)
background(255)    

#Copiez vos formes en dessous 
#    v    v     v    v    v


antonio (violet)

antonio (color(7,131,16)) #les chiffres sont le rouge, le vert et le bleu.
 
splash(cercle, rouge)

aumilieu()
descend()
descend()
fill(vert)
ellipse(0,0,120,120)

fill(blanc)
ellipse(0,0,100,100)

fill(violet)
ellipse(0,0,70,70)

fill(blanc)
ellipse(0,0,40,40)



# blendMode(EXCLUSION)
# fill(255)
# for n in range(5):
#     pushMatrix()
#     translate(random(width),random(height))
#     cercle(150)
#     popMatrix()

