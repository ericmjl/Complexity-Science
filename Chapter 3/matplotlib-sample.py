import matplotlib.pyplot as pyplot


xs = [1, 2, 3, 4, 5, 6]
ys = [2, 4, 6, 8, 10, 12]

pyplot.plot(xs, ys)
scale = 'log'
pyplot.xscale(scale)
pyplot.yscale(scale)
pyplot.title('Sample y = 2x graph')
pyplot.xlabel('n')
pyplot.ylabel('run time (s)')
pyplot.show()
