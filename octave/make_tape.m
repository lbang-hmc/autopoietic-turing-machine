function tape = make_tape(num_bits)

num_states = 2 ^ num_bits;
num_transition_bits = num_bits + 9;

tape = unidrnd(2, 2 * num_states, num_transition_bits) - 1;
