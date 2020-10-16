n = 3;

lifespan = 200;
gens = 20;

tm = randomTM(n);
% tape = TM2tape(tm);
tape = TM2tape(tm);
	
for i = 1:gens
	% tape = TM2tape(tm);
	m = makeMachine(tm);
	[m, tape] = runMachine(m, tape, lifespan);
	% tape(unidrnd(length(tape))) = mod(unidrnd(2) ,2);
	tm = tape2tm(tape, n);
end

