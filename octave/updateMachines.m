function [machines, env] = updateMachines(machines, env)

for j = 1:length(machines)
	[machines(j), env] = updateMachine(machines(j), env);
end
	