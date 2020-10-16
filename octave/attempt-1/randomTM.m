function tm = randomTM(n)

m = 2^n;
tm = [];
k = 1;

for i = 1:m

	r = randomRule(n, 0);
	tm(k).n = r.n;
	tm(k).read = r.read;
	tm(k).write = r.write;
	tm(k).direction = r.direction;
	tm(k).next = r.next;

	r = randomRule(n, 1);
	tm(k+1).n = r.n;
	tm(k+1).read = r.read;
	tm(k+1).write = r.write;
	tm(k+1).direction = r.direction;
	tm(k+1).next = r.next;

	k = k + 2;
end

