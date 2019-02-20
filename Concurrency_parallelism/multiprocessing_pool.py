# With the Pool class, we can also distribute one function execution across multiple processes for different input values.
from multiprocessing import Pool


def f(x):
    return x*x


if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))
# One process executes f(1), another runs f(2) and another runs f(3).
# Finally the results are again aggregated in a list.
