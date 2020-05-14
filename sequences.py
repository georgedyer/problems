from pylab import *


xs = [x for x in range(100)]
ys = [x**2 for x in xs]
slopes = [ys[x+1]-ys[x] for x in range(99)]


plot(xs, ys)
xlabel('x-axis')
ylabel('y-axis')
title('My chart')
legend("y(x)")
axis(ymin=-100,xmin=-1)
show()
