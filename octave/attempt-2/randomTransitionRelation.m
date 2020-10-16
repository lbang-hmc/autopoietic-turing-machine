function tr = randomTransitionRelation(num_bits)

tr = [];

for k = 1:2^num_bits

  r = randomRule(num_bits, 0);
  tr(k, 1).n     = r.n;
  tr(k, 1).read  = r.read;
  tr(k, 1).write = r.write;
  tr(k, 1).dx    = r.dx;
  tr(k, 1).dy    = r.dy;
  tr(k, 1).next  = r.next;

  r = randomRule(num_bits, 1);
  tr(k, 2).n     = r.n;
  tr(k, 2).read  = r.read;
  tr(k, 2).write = r.write;
  tr(k, 2).dx    = r.dx;
  tr(k, 2).dy    = r.dy;
  tr(k, 2).next  = r.next;

end

