# -*- coding:utf-8 -*-

# 切片
# 取一个list或者tuple的部分元素是一种很常见的操作
li = [1, 2, 3, 4, 5]
# 如果要取前3个元素，应该怎么做？
# 一种方法是：
print li[0], li[1], li[2]
# 这样的方法，如果要取前n个元素，就没辙了
# 当然也可以用循环，但是循环的操作也太复杂了，python提供了一种切片的操作，可以大大简化这种操作
# 取前3个元素
print li[0:3]
# li[0:3]表示，从索引0开始取，直到索引3为止，但是不包括索引3，也就是0，1，2，正好3个元素
# 如果第一个索引是0，还可以省略
print li[:3]
# 也可以指定起始索引，例如
print li[1:3]
# 类似的，既然python支持倒序取元素，自然也支持倒序切片了
li2 = [1, 2, 3, 4, 5]
print li2[-3:]
# 如果什么都不写，li2[:]，就可以原样复制一个list
# tuple也可以进行切片操作，得到的仍然是一个tuple
tu = (1, 2, 3, 4)[:3]
print tu

# 字符串'xxx'或Unicode字符串u'xxx'也可以看成一种list，一个元素就是一个字符
# 因此，字符串也可以进行切片，得到的结果仍然是字符串
print 'ABCDEF'[:4]
print u'你好世界'[:2]