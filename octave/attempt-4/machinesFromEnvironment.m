function machines = machinesFromEnvironment(machines, env, n)

tape_length = 2 ^ n * (2 * n + 10);

for i = 1:length(machines)
	tape = env(i, 1:tape_length);
	machines(i).tr = tape2transitionRelation(tape, n);
	machines(i).y = i;
	machines(i).x = 1;
end
