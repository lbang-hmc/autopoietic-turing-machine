function [machines, env] = runGenerations(machines, env, gens)

for i = 1:gens
	showEnvironment(env);
	xlabel(i);
	plotMachinePositions(machines);
	[machines, env] = updateMachines(machines, env);	
	drawnow;
end
