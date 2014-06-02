size(630,724,P2D)
frame.setLocation(1366-630, 0)
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


