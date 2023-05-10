import math
import matplotlib.pyplot as plt


def f(x): return x**2 - 10*math.sin(x)
def df(x): return 2*x - 10*math.cos(x)


def newton(f, df, x, eps):
    while abs(f(x)) > eps:
        x = x - f(x) / df(x)
    return x

roots = []
for x in range(5):
    root = newton(f, df, x, 1e-6)
    if root >= 0:
        roots.append(root)


print("Положительные корни уравнения x^2 - 10*sin(x) = 0:", roots)


x_values = [x/100 for x in range(-2000, 2000)]
y_values = [f(x) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции y = x^2 - 10*sin(x)')

for root in roots:
    plt.scatter(root, f(root), color='red')

plt.show()
