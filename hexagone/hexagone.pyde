size(600,800,P2D)
frame.setLocation(1366-600, 0)
background(255)
noStroke()

def hexagone(taille):
    popMatrix
    translate (taille, taille)
    beginShape()
    stroke(0,0)
    for i in range (6):
        x = cos( i * THIRD_PI ) * taille
        y = sin( i * THIRD_PI ) * taille
        vertex( x, y )
    endShape()
    pushMatrix
    


translate(50, 40)

rouge = color(255, 0, 0)

fill(rouge)
hexagone(100)


