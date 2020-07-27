from graphics import*

def main():
    win = GraphWin("Alfredo", 500, 500)
    win.setBackground(color_rgb(0,0,0))

    cir = Circle(Point(50,50),40)
    cir.setOutline(color_rgb(0,250,250))
    cir.setFill(color_rgb(250,100,50))
    cir.setWidth(5)
    cir.draw(win)

    rect = Rectangle(Point(100,100), Point(150,150))
    rect.setOutline(color_rgb(0,255,255))
    rect.setFill(color_rgb(255,100,50))
    rect.draw(win)

    poly = Polygon(Point(200,200), Point(240,240), Point(60,300))
    poly.setFill(color_rgb(250,0,250))
    poly.setOutline(color_rgb(250,0,0))
    poly.draw(win)


    win.getMouse()
    win.close()

main()
