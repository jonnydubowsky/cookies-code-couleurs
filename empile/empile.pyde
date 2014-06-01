size(640, 360)
noStroke()
depart = 0 

def empile (forme, couches):
    for n in range(couches):
        scale(n+1)
        fill (n)
        translate(n, n)
        # forme
        ellipse(width/2, height/2, 280, 280)
        empile(forme, n)

moncercle = ellipse(width/2, height/2, 280, 280)

empile (forme = moncercle, couches = 5)

# def spirale (forme):

