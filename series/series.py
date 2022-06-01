def Fibonacci(n):
    '''
    numeric series starts with integers 0 and 1
    the next integer is determined by summing the previous two.
    :param n: nth index value
    :return (n-1)+(n-2):
    '''
    if n < 0:
        return 'incorrect input'
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def lucas (n):
    '''
    numeric series starts with integers 2 and 1
    the next integer is determined by summing the previous two.
    :param n: nth index value
    :return (n-1)+(n-2):
    '''
    if n < 0:
        return 'incorrect input'
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, x=0, y=1):
    '''
    numeric series starts with integers x and y, the default value for them
    is x=0 , y=1 ,
    the next integer is determined by summing the previous two.
    :param n: nth index value
    :param x: start index value
    :param y: second index value
    :return:(n - 1, x, y)+(n - 2, x, y)
    '''
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)