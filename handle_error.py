#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 错误处理
# 在程序运行过程中，如果发生了错误，可以实现约定返回一个错误代码
# 这样就可以知道是否出错，以及出错的原因
# 用错误码表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起
# 造成调用者必须用大量的代码判断是否出错
# 在java中，可以使用try...catch...finally语句捕获错误
# 在python中也可以try...catch机制
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
# try...
# except: integer division or modulo by zero
# finally...
# END
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
# 从输出可以看到，当错误发生时，后续语句print 'result:'
# r不会被执行，except由于捕获到ZeroDivisionError，因此被执行
# 最后，finally语句被执行。然后，程序继续按照流程往下走。
# 如果把除数0改成2，则执行结果如下
try:
    print 'try...'
    r = 10 / 2
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
# try...
# result: 5
# finally...
# END
# 由于没有错误发生，所以except语句块不会被执行
# 但是finally如果有，则一定会被执行（可以没有finally语句）
# 可以有多个except来捕获不同类型的错误：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print 'finally...'
print 'END'
# int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError
# 用另一个except捕获ZeroDivisionError
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是
# 它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
# try:
#     foo()
# except StandardError, e:
#     print 'StandardError'
# except ValueError, e:
#     print 'ValueError'
# 第二个except永远也捕获不到ValueError，因为ValueError是StandardError的子类
# 如果有，也被第一个except给捕获了
# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了
# 这样一来，就大大减少了写try...except...finally的麻烦


# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去
# Python内置的logging模块可以非常容易地记录错误信息：
# err.py
# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except StandardError, e:
#         logging.exception(e)
#
# main()
# print 'END'
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
# $ python err.py
# ERROR:root:integer division or modulo by zero
# Traceback (most recent call last):
#   File "err.py", line 12, in main
#     bar('0')
#   File "err.py", line 8, in bar
#     return foo(s) * 2
#   File "err.py", line 5, in foo
#     return 10 / int(s)
# ZeroDivisionError: integer division or modulo by zero
# END
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。


# 抛出错误

# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# err.py
# class FooError(StandardError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
# 执行，可以最后跟踪到我们自己定义的错误：
# $ python err.py
# Traceback (most recent call last):
#   ...
# __main__.FooError: invalid value: 0
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError）
# 尽量使用Python内置的错误类型
# 最后，我们来看另一种错误处理的方式：
# err.py
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main():
    bar('0')

main()
# 捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理
# raise语句如果不带参数，就会把当前错误原样抛出
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError