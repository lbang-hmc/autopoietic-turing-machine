function printTransitionRelation(tr)

for i = 1:length(tm)

	disp(['state: ', num2str(i-1), '    ', rule2str(tm(i,1))]);
	disp(['state: ', num2str(i-1), '    ', rule2str(tm(i,2))]);

end