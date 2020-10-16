n = 3;

tm = randomTM(n);
tape = tm2tape(tm);
m = makeMachine(tm);

[m, tape] = updateMachine(m, tape);

