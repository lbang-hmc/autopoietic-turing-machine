
h = n + 4;
w = length(tape) / h;

tape_ = reshape(tape, h, w);

tm_ = [];

for i = 1:length(tape_)	
	rulebits = tape_(:,i);
	r.n = n;
	r.read = mod(i + 1, 2);
	r.write = rulebits(2);
	r.direction = bin2dec([num2str(rulebits(3)),num2str(rulebits(4))]) - 2;
	r.next = bin2dec(strrep(num2str(rulebits(5:end)'), ' ', ''));

	disp(rule2str(r));
	
	tm_(i).n = r.n;
	tm_(i).read = r.read;
	tm_(i).write = r.write;
	tm_(i).direction = r.direction;
	tm_(i).next = r.next;

end