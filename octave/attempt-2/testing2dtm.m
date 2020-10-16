n = 3;

tape_length = 2 ^ n * (2 * n + 10);

num_machines = 25;
machines = [];

machines = randomMachineList(n, num_machines);

% env = makeEnvironment(num_machines, tape_length);

env = mod(unidrnd(2, num_machines, tape_length),2);

lifespan = 512;

for generation = 1:200
	disp(generation);
	fflush(stdout);
	[machines, env] = runGenerations(machines, env, lifespan);
	% machines = machinesFromEnvironment(machines, (env(:, length(env)/2 + 1 : end)), n);
	% env = [(env(:, length(env)/2 + 1 : end)), ones(num_machines, length(env) /2)];
	machines = machinesFromEnvironment(machines, env, n);
	% env = repmat(env(:, length(env)/2 + 1 : end), 1, 2);
end


% for i = 1:500
% 	showEnvironment(env);
% 	plotMachinePositions(machines, reds, greens, blues);
% 	[machines, env] = updateMachines(machines, env);	
% end

% blues  = 0.5 * rand(1,num_machines);
% reds   = 0.5 * rand(1,num_machines);
% greens = 0.5 + 0.5 * rand(1,num_machines);


% for i = 1:num_machines
% 	tr = randomTransitionRelation(n);
% 	m = makeMachine(tr);
% 	machines(i).state = m.state;
% 	machines(i).x = m.x;
% 	machines(i).y = m.y;
% 	machines(i).tr = m.tr; 
% end
