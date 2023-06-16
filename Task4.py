import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

alpha=0.05
x1=np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
x2=np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
x3=np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
d = stats.kruskal(x1,x2,x3)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.kruskal(x1,x2,x3)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза '
          'не отвергается, время на дистанцию одинаковое.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую '
          'гипотезу отвергаем, время на дистанцию не одинаковое')