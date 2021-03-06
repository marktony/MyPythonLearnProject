# -*- coding:utf-8 -*-

# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用本身，这个函数就是递归函数
# 计算阶乘:n!=1x2x3x..xn
# 用递归函数表示
def func(n):
    if n == 1:
        return 1
    return n*func(n - 1)

print func(1)
print func(5)
# 计算过程为
# fact(5)
# 5 * fact(4)
# 5 * (4 * fact(3))
# 5 * (4 * (3 * fact(2)))
# 5 * (4 * (3 * (2 * fact(1))))
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
# 递归函数的优点：定义简单，逻辑清晰，缺点也很明显，耗费内存，容易导致栈溢出
# 解决栈溢出的方法，使用尾递归，但是python解释器并没有做优化，所以，使用递归函数时还是有可能导致栈溢出的
