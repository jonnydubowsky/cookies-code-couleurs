# Des réglages pour la fenêtre, pour le fond
size(int(displayWidth*0.45),displayHeight-100,P2D)
frame.setLocation(displayWidth-int(displayWidth*0.45), 0)
background(255)
noStroke()

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
    


translate(50, 40)

rouge = color(255, 0, 0)

fill(rouge)
hexagone(100)


