function printTransitionRelation(tr)

for i = 1:length(tr)

	disp(['state: ', num2str(i-1), '    ', rule2str(tr(i,1))]);
	disp(['state: ', num2str(i-1), '    ', rule2str(tr(i,2))]);

end