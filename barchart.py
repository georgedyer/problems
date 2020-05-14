from pylab import *
import datetime
import random
import matplotlib.pyplot as pl

months = [datetime.date(2020, i+1, 1).strftime('%B') for i in range(12)]

values = [random.randrange(100) for i in range(12)]

print(months)
print(values)

pl.yticks(range(12),months)
pl.barh(range(12),values)
pl.show()