function [m, tape] = runMachine(m, tape, steps)

for i = 1:steps
	[m, tape] = updateMachine(m, tape);
	visualize(m, tape);
	title([num2str(i), '  ', num2str(m.state)]);
	pause(0);
end