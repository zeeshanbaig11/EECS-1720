def setup():         #this is comment, not //
    size(480, 480)

def draw():
    if  mousePressed:
        fill(255)
    #square(mouseX, mouseY, 80, 80) #Similar to Java?
    else:
        fill(255,125,22)
    ellipse(mouseX, mouseY, 80, 80)
    
    #questions I have
    # how to write java code? is that online or in an app
