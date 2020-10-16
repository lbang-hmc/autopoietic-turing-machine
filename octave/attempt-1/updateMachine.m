function [m, tape] = updateMachine(m, tape)

readbit = tape(m.head);
rule = m.rules(1 + 2 * m.state + tape(m.head));

% disp(['rule  :  ', rule2str(rule)]);
% disp(['state :  ', num2str(m.state)]);
% disp(['head  :  ', num2str(m.head)]);
% disp(['read  :  ', num2str(readbit)]);
% disp(['write :  ', num2str(rule.write)]);
% disp(['move  : ', num2str(rule.direction)]);


p = 0.1;

if (rand > p )
	tape(m.head) = rule.write;
else
	tape(m.head) = mod(unidrnd(2),2);
end
	
m.head = m.head + rule.direction;

if(m.head == length(tape) + 1)
	m.head = 1;
elseif(m.head <= 0)
	m.head = length(tape);
end
	
m.state = rule.next;
