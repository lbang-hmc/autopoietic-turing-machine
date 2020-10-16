function [m, env] = updateMachine(m, env)

readbit = env(m.y, m.x);

rule = m.tr(m.state + 1, readbit + 1);

% disp(['state :  ', num2str(m.state)]);
% disp(['rule  :  ', rule2str(rule)]);

env(m.y, m.x) = rule.write;

% disp([m.x, m.y]);	

m.y = mod1(m.y + rule.dy, size(env, 1));
m.x = mod1(m.x + rule.dx, size(env, 2));

% disp([m.x, m.y]);	

m.state = rule.next;

% p = 0.1;

% if (rand > p )
% 	tape(m.head) = rule.write;
% else
% 	tape(m.head) = mod(unidrnd(2),2);
% end
