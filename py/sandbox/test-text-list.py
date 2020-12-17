from graphics import *
import time
win = GraphWin(width = 500, height = 500) # create a window
win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
mySquare = Rectangle(Point(1, 1), Point(99, 99)) # create a rectangle from (1, 1) to (9, 9)
mySquare.draw(win) # draw it to the window
# win.getMouse() # pause before closing

# t = Text(Point(5,95), "x")
# # t.setText("x: \n" + key)
# t.setFace("courier")
# t.setSize(20)    
# t.draw(win)


xgridsize = 24
ygridsize = 24

textlist = []

for i in range(xgridsize):
    for j in range(ygridsize):
        textlist += [Text(Point(4*(i+1),4*(j+1)), '.')]

for textObj in textlist:
    textObj.draw(win)

for textObj in textlist:
    textObj.move(1,1)
    time.sleep(0.005)

key = win.getKey()
win.close()