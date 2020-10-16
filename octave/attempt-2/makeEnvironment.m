function e = makeEnvironment(n,m)

% e = [mod(unidrnd(2, n, m),2), ones(n,m)];
e = repmat(mod(unidrnd(2, n, m),2), 1, 2);