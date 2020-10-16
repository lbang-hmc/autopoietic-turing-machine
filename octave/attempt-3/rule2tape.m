function t = rule2tape(r)

m = r.n + 4;
t = zeros(m,1);

t(1) = r.read;
t(2) = r.write;
t(3:4) = bitstr2array(dec2bin(r.direction + 2, 2));
t(5:m) = bitstr2array(dec2bin(r.next, r.n));