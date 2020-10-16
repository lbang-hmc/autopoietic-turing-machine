from graphics import *
from TuringMachine import *
import time
from relay import Relay

relay = Relay(idVendor=0x16c0, idProduct=0x05df)


def move_by_keypress(tm, key):
    if (key == 'h'):
        tm.move('up')
    elif (key == 'j'):
        tm.move('down')
    elif (key == 'k'):
        tm.move('left')
    elif(key == 'l'):
        tm.move('right')
    else:
        print('unknown direction, ' + key)

def type_by_keypress(tm, key):
    if(key == 'd'):
        tm.write(0)
    elif(key == 'f'):
        tm.write(1)
    else:
        print('unknown tape symbol, ' + key)

win = GraphWin(width = 1800, height = 950) # create a window
win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
x = 50
y = 50
win.master.geometry('%dx%d+%d+%d' % (1800, 950, x, y))
mySquare = Rectangle(Point(1, 1), Point(99, 99)) # create a rectangle from (1, 1) to (9, 9)
mySquare.draw(win) # draw it to the window
# win.getMouse() # pause before closing

tm = TuringMachine(5)

fontsize = 14

bit_text = Text(Point(10,50), str(tm))
bit_text.setFace("courier")
bit_text.setSize(fontsize)    
bit_text.draw(win)

instr_text = Text(Point(55.0,51.1), tm.human_readable())
instr_text.setFace("courier")
instr_text.setSize(fontsize)    
instr_text.draw(win)

todo_text = Text(Point(30, 95), '')
todo_text.setFace("courier")
todo_text.setSize(fontsize)
todo_text.draw(win)

def handle_typing(to_type):
    if(to_type):
        relay.state(2, on=True)
        key = win.getKey()
        relay.state(2, on=False)
    else:
        relay.state(1, on=True)
        key = win.getKey()
        relay.state(1, on=False)
    return key

def handle_moving(to_move):
    relay_by_direction = {'up': 3, 'down': 4, 'left': 5, 'right': 6}
    relay_n = relay_by_direction[to_move]
    relay.state(relay_n, on=True)
    key = win.getKey()
    relay.state(relay_n, on=False)
    return key


i = 0
done = False
while (i < 10 and not done):
    i = i + 1
    # tm.step()
    todo = tm.what_to_do()
    todo_text.setText(str(todo) + ' [' + str(tm.x) + ', ' + str(tm.y) + ']')


    # type_key = win.getKey()
    type_key = handle_typing(todo['type'])
    if(type_key == 'q'):
        done = True
    type_by_keypress(tm, type_key)


    bit_text.setText(str(tm))
    instr_text.setText(tm.human_readable())
    time.sleep(0.5)


    # move_key = win.getKey()
    move_key = handle_moving(todo['move'].strip())
    if(type_key == 'q'):
        done = True
    move_by_keypress(tm, move_key)
    
    
    tm.state = todo['next']
    time.sleep(0.1)
    time.sleep(0.5)
# for i in range(5):
#     key = win.getKey()
#     print(key)
#     t.setText("x: \n" + key)
#     # t.draw(win)
    
win.getKey()
win.close()