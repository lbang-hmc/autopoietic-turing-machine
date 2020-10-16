function printMachine(m)

disp('');
disp(['state:     ', num2str(m.state)]);
disp(['position:  ', num2str([m.x, m.y])]);
disp('');
printTransitionRelation(m.tr);
disp('');

