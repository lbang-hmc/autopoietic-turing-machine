num_bits = 6;
num_states = 2 ^ num_bits;
num_transition_bits = num_bits + 5;

tape = unidrnd(2, 2 * num_states, num_transition_bits) - 1;
% print_machine_from_tape(tape);

read_head_pos  = [unidrnd(num_transition_bits), unidrnd(num_states)];
write_head_pos = [unidrnd(num_transition_bits), unidrnd(num_states)];

current_state = unidrnd(num_states) - 1;

state_history = zeros(1,num_states);

colormap('gray')

tape_history = zeros(2 * num_states, num_transition_bits);

for k = 1:1000

% subplot(1,2,1)
hold off;
%   [state_history', state_history']'(:) / max(state_history+1)
imagesc([tape, 1 - tape_history / max(max(tape_history+1))]);
axis equal;
hold on;
axis off;
plot(read_head_pos(1), read_head_pos(2), 'ro', 'markersize', 10, 'markerfacecolor', 'r');
plot(write_head_pos(1), write_head_pos(2), 'bo', 'markersize', 10, 'markerfacecolor', 'b');
% line([0, num_transition_bits + 1], [current_state, current_state], 'color', 'g', 'linewidth', 5)
title([current_state, k]);

state_history(current_state+1)++;
% subplot(1,2,2)

% if(!mod(k,10))
%   colormap('hot')
%   imagesc(state_history)
% end

% if(mod(k,10))
% 	plot(state_history / sum(state_history));
% end

drawnow;

% pause(0.1);

read_bit = tape(read_head_pos(2), read_head_pos(1));
u = get_update(tape, current_state, read_bit);

tape(write_head_pos(2), write_head_pos(1)) = u.write_bit;

tape_history(read_head_pos(2), read_head_pos(1))++;
tape_history(write_head_pos(2), write_head_pos(1))++;

read_head_pos  = read_head_pos  + [u.read_x_dir , u.read_y_dir];
write_head_pos = write_head_pos + [u.write_x_dir, u.write_y_dir];

read_head_pos(1) = mod1(read_head_pos(1), num_transition_bits);
read_head_pos(2) = mod1(read_head_pos(2), 2 * num_states);

write_head_pos(1) = mod1(write_head_pos(1), num_transition_bits);
write_head_pos(2) = mod1(write_head_pos(2), 2 * num_states);



current_state = u.next_state;

end

% hold off;
% imshow(tape);
% hold on;
% axis on;
% plot(read_head_pos(1), read_head_pos(2), 'ro', 'markersize', 30, 'markerfacecolor', 'r');
% plot(write_head_pos(1), write_head_pos(2), 'bo', 'markersize', 20, 'markerfacecolor', 'b');