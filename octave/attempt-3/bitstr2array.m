function a = bitstr2array(bs)

a = zeros(1, length(bs));

for i = 1:length(bs)
	a(i) = str2num(bs(i));
end