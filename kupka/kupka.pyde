size(500,500)
colorMode(HSB, 1.0)

from contextlib import contextmanager
@contextmanager
def rotation(angle):
    pushMatrix()
    rotate(angle)
    yield
    popMatrix()
    
# Des couleurs sympas
blanc = color(0, 0, 100)
rouge = color(0, 100, 100)
vert = color(119, 100, 100)
bleu = color(239, 100, 10)

noStroke()
background(blanc) # la couleur du fond
translate(width/2,height/2)
for b in range(30):
    scale(0.9)
    translate(8,9)
    rotate(0.1)
    for a in range(10):
        with rotation(2*PI*a/10):
            translate(200,0)
            for i in range(6):
                fill(i/6.0, 1.0-b/30.0, a/10.0)
                rect(10*i,0,11,50)

