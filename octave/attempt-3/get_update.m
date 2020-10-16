function u = get_update(tape, state, read_bit)

num_states = size(tape, 1) / 2;
num_transition_bits = size(tape, 2);
num_bits = num_transition_bits - 5;

i = 2 * state + read_bit + 1;

u.read_x_dir  = 2 * tape(i, 1) - 1;
u.read_y_dir  = 2 * tape(i, 2) - 1;
u.write_x_dir = 2 * tape(i, 3) - 1;
u.write_y_dir = 2 * tape(i, 4) - 1;
u.write_bit   = tape(i, 5);

next_state_bits = tape(i, 6:end);

u.next_state = bin2dec(strrep(num2str(next_state_bits),' ', ''));


