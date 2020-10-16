function visualize(m, tape)

hold off;
imshow(tape);
axis on;
set (gca, "xtick", 0);
hold on;
plot(0.5, m.head, 'r>', 'markerfacecolor', 'r', 'markersize', 10)

drawnow;