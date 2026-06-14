# -*- coding: utf-8 -*-
'''
@IDE : PyCharm
@version : 3.9
@Auth : 恍惚
@time : 2026/3/20 14:39
@Description: Null
'''


# print("1".rjust(20,' '))

# print(format(-123, "=+20.3f")) #语法结构：[fill][align][sign][width][.precision][type
# print(format(123.4567, "*^+10.2f"))# ]***+123.46
# print(format(-0.5678, "0>+10.2f"))
# print(dict([]))
# print(list(filter(None,["123",'',(1,2,3),5,"",None])))
# print("".join(filter(None,"235")))
# print('\n\r\t\s\\\"\'\ddd\x12')
# print('1\n')
# print('2\t')
# print('3\r')

# def hcf(x, y):
#     """该函数返回两个数的最大公约数"""
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller + 1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf
#
# def lcm(a, b):
#     """该函数返回两个数的最小公倍数"""
#     if a < b:
#         a, b = b, a
#     if a % b == 0:
#         return a
#     mul = 2
#     while a * mul % b != 0:
#         mul += 1
#     return a * mul

# def main():
#     sum = 4    # 1位奇数
#     s = 4      # 当前位奇数计数
#     for j in range(2, 9):  # 处理2~8位
#         if j == 2:
#             s *= 7  # 2位：首位7种选择
#         else:
#             s *= 8  # ≥3位：中间位8种选择
#         sum += s
#     print('sum = %d' % sum)
#
# if __name__ == '__main__':
#     main()
# def func():
#     n = float(input("请输入一个正整数"))
#     m = 9
#     i = 1
#     L = "1"
#     while i != 0:
#         m = int(m)
#         if m % n == 0.0:
#             print(m/n)
#             print(m,'/',int(n),'=0')
#             print("%s个9能整除%d" % (L, n))
#             return
#         else:
#             m = str(m)
#             m = m+str(9)
#             L = str(len(m))
#
# def main():
#     func()
#
# if __name__ == '__main__':
#     main()
# def outer():
#     x = 1
#     def inner(y):
#         # nonlocal x
#         y += x
#         return y
#     return inner
#
# f = outer()
# print(f(2))

# print('123'.find('8'))
# print(['123',1].index(1))
print(":".join('abc'))