function t = TM2tape(tm)

t = [];

for r = tm
	t(:,end+1) = rule2tape(r);
end 

t = t(:);