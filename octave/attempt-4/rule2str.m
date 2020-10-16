function s = rule2str(r)

readstr = num2str(r.read);
writestr = num2str(r.write);
nextstr = num2str(r.next);


if     r.dx == -1  xdirstr = 'L';
elseif r.dx ==  0  xdirstr = '0';
elseif r.dx ==  1  xdirstr = 'R';
else   			   xdirstr = 'X';
end

if     r.dy == -1  ydirstr = 'U';
elseif r.dy ==  0  ydirstr = '0';
elseif r.dy ==  1  ydirstr = 'D';
else   			   ydirstr = 'X';
end


s = ['read: ', readstr, '    write: ', writestr, '    move: ', xdirstr, ydirstr, '    next: ', nextstr];