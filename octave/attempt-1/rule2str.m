function s = rule2str(r)

readstr = num2str(r.read);
writestr = num2str(r.write);
nextstr = num2str(r.next);

d = r.direction;

if d == -1 		dirstr = 'L';
elseif d == 0 	dirstr = 'S';
else 			dirstr = 'R';
end

s = ['read: ', readstr, '    write: ', writestr, '    move: ', dirstr, '    next: ', nextstr];