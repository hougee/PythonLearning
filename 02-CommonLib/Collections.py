#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：内建模块collections'

__author__ = 'HouBin'

from collections import namedtuple
#namedtuple是一个函数，用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
#namedtuple('名称', [属性list])
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

from collections import deque
#deque高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x') #在列表最后添加元素
q.appendleft('y') #在列表最前面添加元素
print(q)
print(q.count('a')) #返回指定元素出现次数
q.extend([3,4,5]) #在列表右边扩展一个列表元素
q.extendleft([3,4,5]) #在列表左边扩展一个列表元素
print(q)
print(q.index('a',0,6)) #查找某个元素的索引位置
q.insert(2,'z') #在列表的指定位置插入元素
print(q)
q.pop() #删除列表末尾元素
q.popleft() #删除列表第一个元素
print(q)
q.remove('z') #删除指定元素
print(q)
q.reverse() #列表翻转
print(q)
q.rotate(2) #把右边元素放在左边
print(q)
q.clear() #清空队列

from collections import defaultdict
#defaultdict可以使引用的key在字典中不存在时返回一个默认值
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

from collections import Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
