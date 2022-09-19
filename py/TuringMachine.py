# from relay import Relay
from time import sleep
from graphics import *
import random
import numpy as np


# relay = Relay(idVendor=0x16c0, idProduct=0x05df)

def tmEncodingToTextArray(tm):
    return [ [Text(Point(0.7*j+10, 2*i+20), str(tm.encoding[i][j])) 
              for i in range(tm.height)] 
                 for j in range(tm.width) ]


def move_to_unicode(mv):
    m = mv.strip()
    if (m == 'up'):
        return '↑  '
    if (m == 'down'):
        return '↓  '
    if (m == 'left'):
        return '←  '
    if (m == 'right'):
        return '→  '


class TuringMachine:

    def __init__(self, bitwidth):
        self.bitwidth = bitwidth
        self.width = 2 * bitwidth + 6
        self.height = pow(2,bitwidth)
        self.bits = random.choices([0,1], k= self.width * self.height)
        self.encoding = np.array(self.bits).reshape(self.height, self.width)
        self.state = 0
        self.x = 0
        self.y = 0
        self.textEncoding = tmEncodingToTextArray(self)

    def __repr__(self):
        return str(self)

    def __str__(self):
        result = ''
        for line in self.encoding: # in range(len(self.encoding)):
            # row = self.encoding[i]
            for bit in line: #in range(len(row)):
                result += str(bit)
            result += "\n"
        return result
    
    def read(self):
        return self.encoding[self.y][self.x]

    def move(self, direction):
        d = direction.strip()
        if(d == 'up'):
            self.y  = (self.y - 1) % self.height
        elif(d == 'down'):
            self.y  = (self.y + 1) % self.height
        elif(d == 'left'):
            self.x  = (self.x - 1) % self.width
        elif(d == 'right'):
            self.x  = (self.x + 1) % self.width

    def print_position(self):
        print([self.x, self.y])

    def write(self, bit):
        self.encoding[self.y][self.x] = bit
        # if(bit):
        #     relay.state(2, on=True)
        #     sleep(0.5)
        #     relay.state(2, on=False)
        # else:
        #     relay.state(1, on=True)
        #     sleep(0.5)
        #     relay.state(1, on=False)


    # def print_status(self):
    #     status = self.status();
        
    def step_verbose(self):
        print(self.status())
        print(str(self))
        print(self.human_readable())
        self.step()

    def run_verbose(self, steps, delta_t):
        for i in range(steps):
            self.step_verbose()
            sleep(delta_t)

    def run(self, steps):
        for i in range(steps):
            self.step()

    def what_to_do(self):
        read  = self.read()
        line = self.encoding[self.state]
        instructions = self.line_to_instructions(line, self.bitwidth)
        bit_to_write = instructions[read]['type']
        direction_to_move = instructions[read]['move']
        next_state = instructions[read]['next']

        return {'type': bit_to_write , 'move': direction_to_move, 'next':next_state}
        # self.write(bit_to_write)
        # self.move(direction_to_move)
        # self.state = next_state

    def step(self):
        read  = self.read()
        line = self.encoding[self.state]
        instructions = self.line_to_instructions(line, self.bitwidth)
        bit_to_write = instructions[read]['type']
        direction_to_move = instructions[read]['move']
        next_state = instructions[read]['next']

        self.write(bit_to_write)
        self.move(direction_to_move)
        self.state = next_state


    def status(self):
        return {'state':self.state, 'read':self.read(), 'x':self.x, 'y':self.y}

    def human_readable(self):
        return '\n'.join([str(i).rjust(5, ' ') + '       ' + self.human_readable_line_terse(self.encoding[i], self.bitwidth) for i in range(len(self.encoding))])
        # return '\n'.join(['    from state ' + str(i).rjust(3, ' ') + ' ' + self.human_readable_line(self.encoding[i], self.bitwidth) for i in range(len(self.encoding))])

    @staticmethod
    def line_to_instructions(line, bitwidth):
        read_0_type_bits = line[0]
        read_0_move_bits = line[1 : 3]
        read_0_next_bits = line[3 : 3 + bitwidth]
        
        offset = 3 + bitwidth

        read_1_type_bits = line[offset]
        read_1_move_bits = line[offset + 1 : offset + 3]
        read_1_next_bits = line[offset + 3 : offset + 3 + bitwidth]
        read_1_next_bits = line[offset + 3 : offset + 3 + bitwidth]

        read_0_type_instr = read_0_type_bits
        read_0_move_instr = TuringMachine.move_str(list(read_0_move_bits))
        read_0_next_instr = int(''.join([str(b) for b in read_0_next_bits]),2)

        read_1_type_instr = read_1_type_bits
        read_1_move_instr = TuringMachine.move_str(list(read_1_move_bits))
        read_1_next_instr = int(''.join([str(b) for b in read_1_next_bits]),2)

        return [{"type": read_0_type_instr,
                 "move": read_0_move_instr,
                 "next": read_0_next_instr},
                {"type": read_1_type_instr,
                 "move": read_1_move_instr,
                 "next": read_1_next_instr}]


    @staticmethod
    def human_readable_line_terse(line, bitwidth):

        instructions = TuringMachine.line_to_instructions(line, bitwidth)

        read_0_type_instr = str(instructions[0]['type']) + '    '
        read_0_move_instr = move_to_unicode(instructions[0]['move']) + '     '
        # read_0_move_instr = instructions[0]['move']
        read_0_next_instr = str(instructions[0]['next']).rjust(4, ' ') + '       '

        read_1_type_instr = str(instructions[1]['type']) + '    '
        read_1_move_instr = move_to_unicode(instructions[1]['move']) + '    '
        # read_1_move_instr = instructions[1]['move']
        read_1_next_instr = str(instructions[1]['next']).rjust(4, ' ')

        # print('.' + read_0_move_instr + '.')
        
        return ' '.join([read_0_type_instr, read_0_move_instr, read_0_next_instr, read_1_type_instr, read_1_move_instr, read_1_next_instr])


    @staticmethod
    def human_readable_line(line, bitwidth):

        instructions = TuringMachine.line_to_instructions(line, bitwidth)

        read_0_type_instr = 'type '       + str(instructions[0]['type'])
        read_0_move_instr = 'move '       +     instructions[0]['move']
        read_0_next_instr = 'goto state ' + str(instructions[0]['next']).rjust(4, ' ')

        read_1_type_instr = 'type '       + str(instructions[1]['type'])
        read_1_move_instr = 'move '       +     instructions[1]['move']
        read_1_next_instr = 'goto state ' + str(instructions[1]['next']).rjust(4, ' ')
        
        return ' '.join(['   upon reading 0',
                         read_0_type_instr, 
                         read_0_move_instr, 
                         read_0_next_instr,
                         '   upon reading 1',  
                         read_1_type_instr, 
                         read_1_move_instr, 
                         read_1_next_instr])

    @staticmethod    
    def move_str(move_bits):
        if(move_bits == [0,0]):
            return 'up   '
        elif(move_bits == [0,1]):
            return 'down '
        elif(move_bits == [1,0]):
            return 'left '
        else:
            return 'right'

# t = TuringMachine(4)


# bitwidth = 5



# width = 2 * bitwidth + 6
# height = pow(2,bitwidth)

# bits = [0, 1]


# def tm_to_str(tm):
#     result = ''
#     for i in range(len(tm)):
#         row = tm[i]
#         for j in range(len(row)):
#             result += str(row[j])
#         result += "\n"
#     return result

# def transition_to_instruction(tr):


