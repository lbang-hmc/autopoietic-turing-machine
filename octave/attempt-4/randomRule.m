function r = randomRule(num_bits, read_bit)

r.n 		= num_bits;
r.read 		= read_bit;
r.write 	= unidrnd(2) - 1;
r.dx		= unidrnd(3) - 2;
r.dy		= unidrnd(3) - 2;
r.next 		= unidrnd(2^num_bits) - 1;
