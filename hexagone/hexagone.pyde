def hexagone(taille, couleur):
    popMatrix
    translate (taille, taille)
    beginShape()
    stroke(0,0)
    fill(couleur)
    for i in range (6):
        x = cos( i * THIRD_PI ) * taille
        y = sin( i * THIRD_PI ) * taille
        vertex( x, y )
    endShape()
    pushMatrix

    
rouge = color(255, 0, 0)

hexagone(20, rouge)
