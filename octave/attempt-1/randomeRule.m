function r = randomRule(n, readbit)

r.read = readbit;
r.write = unidrnd(2) - 1;
r.direction = unidrnd(3) - 2;
r.next = unidrnd(2^n) - 1;
