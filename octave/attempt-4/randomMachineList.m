function machines = randomMachineList(n, num_machines)

for i = 1:num_machines
	tr = randomTransitionRelation(n);
	m = makeMachine(tr);
	machines(i).state = m.state;
	machines(i).x = m.x;
	machines(i).y = i;
	machines(i).tr = m.tr; 
end
