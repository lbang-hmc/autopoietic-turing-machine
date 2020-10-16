function tm_ = tape2tm(tape, n)

h = 2 * n + 10;
w = length(tape) / h;

tape_ = reshape(tape, h, w);

tm_ = [];

k = 1;

for i = 1:length(tape_)	
	rulebits = tape_(i,:);
	r.n      = n;
	r.read   = mod(i + 1, 2);
	r.write  = rulebits(1);
	r.dx     = bin2dec(strrep(num2str(rulebits(2:3)')  , ' ', ''));
	r.dy     = bin2dec(strrep(num2str(rulebits(4:5)')  , ' ', ''));
	r.next   = bin2dec(strrep(num2str(rulebits(6:end)'), ' ', ''));

	% disp(rule2str(r));
	
	tm_(k, r.read + 1).n     = r.n;
	tm_(k, r.read + 1).read  = r.read;
	tm_(k, r.read + 1).write = r.write;
	tm_(k, r.read + 1).dy    = r.dy;
	tm_(k, r.read + 1).dx    = r.dx;
	tm_(k, r.read + 1).next  = r.next;

end