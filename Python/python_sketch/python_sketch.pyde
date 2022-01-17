def setup():
    size(480, 120)

def draw():
    if  mousePressed:
        fill(0)
    else:
        fill(255,125,22)
    ellipse(mouseX, mouseY, 80, 80)
