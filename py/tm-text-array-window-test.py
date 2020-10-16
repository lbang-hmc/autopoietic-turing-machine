from graphics import *
from TuringMachine import *
import time

win = GraphWin(width = 1800, height = 950) # create a window
win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
x = 50
y = 50
win.master.geometry('%dx%d+%d+%d' % (1800, 950, x, y))
mySquare = Rectangle(Point(1, 1), Point(99, 99)) # create a rectangle from (1, 1) to (9, 9)
mySquare.draw(win) # draw it to the window
# win.getMouse() # pause before closing

tm = TuringMachine(5)

# for row in tm.textEncoding:
# 	for txt in row:
# 		txt.draw(win)

r = Rectangle(Point(49.7,49.1), Point(50.35,50.8))
r.setFill('gray')
r.draw(win)

t = Text(Point(50, 50), "X")
t.draw(win)
t.setTextColor('white')

for i in range(tm.height):
	for j in range(tm.width):
		tm.textEncoding[j][i].setFace("courier")
		if tm.x == i and tm.y == j:
			tm.textEncoding[j][i].setTextColor('red')
			tm.textEncoding[j][i].setFill('red')
		else:
			tm.textEncoding[j][i].setTextColor('black')
			tm.textEncoding[j][i].setFill('black')
		tm.textEncoding[j][i].draw(win)

win.getKey()
win.close()