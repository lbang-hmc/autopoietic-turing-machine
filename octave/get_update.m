function u = get_update(tape, state, read_bit)

num_states = size(tape, 1) / 2;
num_transition_bits = size(tape, 2);
num_bits = num_transition_bits - 5;

i = 2 * state + read_bit + 1;

read_move_x = tape(i, 3);
read_move_y = tape(i, 4);

write_move_x = tape(i, 7);
write_move_y = tape(i, 8);

u.read_x_dir  = read_move_x  * (2 * tape(i, 1) - 1);
u.read_y_dir  = read_move_y  * (2 * tape(i, 2) - 1);
u.write_x_dir = write_move_x * (2 * tape(i, 5) - 1);
u.write_y_dir = write_move_y * (2 * tape(i, 6) - 1);
u.write_bit   = 1-tape(i, 9);

next_state_bits = tape(i, 10:end);

u.next_state = bin2dec(strrep(num2str(next_state_bits),' ', ''));


