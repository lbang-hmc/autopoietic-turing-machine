function plotMachinePositions(machines, rs, gs, bs)

num_machines = length(machines);

for j = 1:num_machines
	c = [0.8, 1 - j / num_machines / 2, 0.3];
	plot(machines(j).x, machines(j).y, 'ks', 'markerfacecolor', c , 'markersize', 7);
end

axis on;
title(num2str([machines.state]));

pause(0.0);
drawnow;

