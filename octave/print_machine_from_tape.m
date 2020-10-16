function print_machine_from_tape(tape)

num_states = size(tape, 1) / 2;
num_transition_bits = size(tape, 2);
num_bits = num_transition_bits - 5;

for i = 1 : 2 : 2 * num_states 

  read_x_dir_0      = tape(i, 1);
  read_y_dir_0      = tape(i, 2);
  read_move_x_0     = tape(i, 3);
  read_move_y_0     = tape(i, 4);
  write_x_dir_0     = tape(i, 5);
  write_y_dir_0     = tape(i, 6);
  write_move_x_0    = tape(i, 7);
  write_move_y_0    = tape(i, 8);
  write_bit_0       = tape(i, 9);
  next_state_bits_0 = tape(i, 10:end);
  next_state_0 = bin2dec(strrep(num2str(next_state_bits_0),' ', ''));

  
  read_x_dir_1      = tape(i + 1, 1);
  read_y_dir_1      = tape(i + 1, 2);
  read_move_x_1     = tape(i + 1, 3);
  read_move_y_1     = tape(i + 1, 4);
  write_x_dir_1     = tape(i + 1, 5);
  write_y_dir_1     = tape(i + 1, 6);
  write_move_x_1    = tape(i + 1, 7);
  write_move_y_1    = tape(i + 1, 8);
  write_bit_1       = tape(i + 1, 9);
  next_state_bits_1 = tape(i + 1, 10:end);
  next_state_1 = bin2dec(strrep(num2str(next_state_bits_1),' ', ''));
  

  read_dir_str_0 = ['(', num2str(read_x_dir_0), ', ', num2str(read_y_dir_0), ')'];
  read_dir_str_1 = ['(', num2str(read_x_dir_1), ', ', num2str( read_y_dir_1), ')'];
  
  read_move_str_0 = ['(', num2str(read_move_x_0), ', ', num2str( read_move_y_0), ')'];
  read_move_str_1 = ['(', num2str(read_move_x_1), ', ', num2str( read_move_y_1), ')'];

  write_dir_str_0 = ['(', num2str(write_x_dir_0), ', ', num2str( write_y_dir_0), ')'];
  write_dir_str_1 = ['(', num2str(write_x_dir_1), ', ', num2str( write_y_dir_1), ')'];

  write_move_str_0 = ['(', num2str(write_move_x_0), ', ', num2str( write_move_y_0), ')'];
  write_move_str_1 = ['(', num2str(write_move_x_1), ', ', num2str( write_move_y_1), ')'];


  disp(['state ', num2str((i-1)/2), ...
        ' read 0 :   write ', num2str(write_bit_0), ...
        ',  r-dir ', read_dir_str_0, ...
        ',  r-move ', read_move_str_0, ... 
        ',  w-dir ', write_dir_str_0, ...
        ',  w-move ', write_move_str_0, ... 
        ',  next ', num2str(next_state_0)])

  disp(['state ', num2str((i-1)/2), ...
        ' read 1 :   write ', num2str(write_bit_1), ...
        ',  r-dir ', read_dir_str_1, ...
        ',  r-move ', read_move_str_1, ... 
        ',  w-dir ', write_dir_str_1, ...
        ',  w-move ', write_move_str_1, ... 
        ',  next ', num2str(next_state_1)])

  % disp(['state ', num2str((i-1)/2), ' read 1 :   write ', num2str(write_bit_1), ',  r-move ', read_dir_str_1, ',  w-move ', write_dir_str_1, ',  next ', num2str(next_state_1)])

end
% function m = bit2move(b)
%   if(b == 0)
%     m = 'L'
%   else 
%     m = 'R'