from graphics import *
from TuringMachine import *
import time
from relay import Relay

class FakeRelay:
    def __init__(self):
        self.relaystate = ""
    def state(self, n, on):
        print("relay " + str(n) + " on = " + str(on))


relay = Relay(idVendor=0x16c0, idProduct=0x05df)
# relay = FakeRelay()

def type_or_move_by_keypress(tm, key):
    if (key == 'h'):
        tm.move('up')
    elif (key == 'j'):
        tm.move('down')
    elif (key == 'k'):
        tm.move('left')
    elif(key == 'l'):
        tm.move('right')
    elif(key == 'd'):
        tm.write(0)
    elif(key == 'f'):
        tm.write(1)
    else:
        print('unknown key: ' + key)


# need function for this graphics initialization
win = GraphWin(width = 1800, height = 950) # create a window
win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (100, 100)
win_color = color_rgb(20,20,20)
win_color = color_rgb(255,255,255)
win.setBackground(win_color)
x = 100
y = 120
win.master.geometry('%dx%d+%d+%d' % (1800, 950, x, y))
mySquare = Rectangle(Point(1, 1), Point(99, 99)) # create a rectangle from (1, 1) to (99, 99)
mySquare.setOutline("white")
mySquare.draw(win) # draw it to the window
# win.getMouse() # pause before closing


text_color = color_rgb(20,20,20)


cursor_x = 4.6
cursor_y = 87.8
cursor_h = 2
cursor_w = 0.75
cursor_box = Rectangle(Point(cursor_x, cursor_y), Point(cursor_x + cursor_w, cursor_y + cursor_h))
cursor_box.setOutline("white")
cursor_box.draw(win)

tm = TuringMachine(5)

fontsize = 15

memstr = "Memory Editor"
mem_header = Text(Point(10,90), memstr)
mem_header.setFace("courier")
mem_header.setSize(fontsize)
mem_header.setTextColor(text_color)    
mem_header.setStyle("bold")
mem_header.draw(win)

prgstr1 = "if in |       if reading 0      |       if reading 1     \n"
prgstr2 = "state | write  move  next_state | write  move  next_state\n"
# prgstr3 = "______|______________|_____________"
prg_header = Text(Point(66,89), prgstr1 + prgstr2)
prg_header.setFace("courier")
prg_header.setSize(fontsize)
prg_header.setTextColor(text_color)    
prg_header.setStyle("bold")
prg_header.draw(win)


# need a function to do all this text initialization
bit_text = Text(Point(10,50), str(tm))
bit_text.setFace("courier")
bit_text.setSize(fontsize)
bit_text.setTextColor(text_color)    
# bit_text.draw(win)

cursor_chars = list(str(tm))
# cursor_chars = list(str(tm).replace('0', ' ').replace('1', ' '))
cursor_chars[(tm.width+1) * tm.y + tm.x] = 'X'
cursor_str = "".join(cursor_chars)
cursor_text = Text(Point(10,50), cursor_str)
cursor_text.setStyle("bold")
cursor_text.setTextColor(text_color)

cursor_text.setFace("courier")
cursor_text.setSize(fontsize)    

cursor_text.draw(win)

instr_text = Text(Point(65.0,51.1), tm.human_readable())
instr_text.setFace("courier")
instr_text.setSize(fontsize)
instr_text.setTextColor(text_color)
instr_text.setStyle("bold")    
instr_text.draw(win)

status_text = Text(Point(30, 25), '')
status_text.setFace("courier")
status_text.setSize(fontsize + 10)
status_text.setTextColor(text_color)
status_text.setStyle("bold")
status_text.draw(win)


def handle_typing(to_type):
    if(to_type):
        relay.state(7, on=True)
        time.sleep(0.05)
        relay.state(7, on=False)
        key = win.checkKey()
    else:
        relay.state(1, on=True)
        time.sleep(0.05)
        relay.state(1, on=False)
        key = win.checkKey()
    # print('pressed ' + key)
    return key

def handle_moving(to_move):
    relay_by_direction = {'up': 3, 'down': 4, 'left': 8, 'right': 6}
    relay_n = relay_by_direction[to_move]
    relay.state(relay_n, on=True)
    time.sleep(0.05)
    relay.state(relay_n, on=False)
    # key = win.getKey()
    key = win.checkKey()
    # print('pressed ' + key)
    return key

max_steps = 1000

done = False

while(True and not done):
    tm = TuringMachine(5)
    i = 0
    done = False
    while (i < max_steps and not done):
        i = i + 1
        current_state = tm.state
        current_read = tm.read()
        todo = tm.what_to_do()
        to_type = todo['type']
        to_move = move_to_unicode(todo['move'])

        state_string = 'state   : ' + str(current_state).rjust(2,' ')
        read_string  = 'reading :  ' + str(current_read) 
        type_string  = 'type    :  ' + str(to_type) 
        # move_string  = ''
        move_string  = 'move    :  ' + to_move[0]

        status_string = '\n'.join([state_string, read_string, type_string, move_string])
        print(status_string)
        
        status_text.setText(status_string)


        # implementation is expecting a write (0/1) then move (u/d/l/r)
        # should make it just wait for arbitrary key press then just 
        # execute that keypress.

        # tell the hand (relay) to push the right button to type a 0 or 1
        type_key = handle_typing(todo['type'])
        if(type_key == 'q'):
            done = True



        type_or_move_by_keypress(tm, type_key)

        # need a text update function that does all this
        bit_text.setText(str(tm))
        instr_text.setText(tm.human_readable())
        # cursor_chars = list(str(tm).replace('0', ' ').replace('1', ' '))
        cursor_chars = list(str(tm))
        cursor_chars[(tm.width+1) * tm.y + tm.x] = '_'
        cursor_str = "".join(cursor_chars)
        cursor_text.setText(cursor_str)



        time.sleep(0.1)

        move_key = handle_moving(todo['move'].strip())
        if(move_key == 'q'):
            done = True
       
       
        type_or_move_by_keypress(tm, move_key)
        
        # need a text update function that does all this
        bit_text.setText(str(tm))
        instr_text.setText(tm.human_readable())
        # cursor_chars = list(str(tm).replace('0', ' ').replace('1', ' '))
        cursor_chars = list(str(tm))
        # cursor_chars[(tm.width+1) * tm.y + tm.x] = '_'
        cursor_str = "".join(cursor_chars)
        cursor_text.setText(cursor_str)
        
        tm.state = todo['next']
        time.sleep(0.1)

        print(i)
    
relay.state(0, on=False)







# def move_by_keypress(tm, key):
#     if (key == 'h'):
#         tm.move('up')
#     elif (key == 'j'):
#         tm.move('down')
#     elif (key == 'k'):
#         tm.move('left')
#     elif(key == 'l'):
#         tm.move('right')
#     else:
#         print('unknown direction, ' + key)

# def type_by_keypress(tm, key):
#     if(key == 'd'):
#         tm.write(0)
#     elif(key == 'f'):
#         tm.write(1)
#     else:
#         print('unknown tape symbol, ' + key)




