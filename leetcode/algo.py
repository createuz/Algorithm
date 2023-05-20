# l = list(map(int, (input().split())))
# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#     print(*matrix, end = ' ')

# Program to multiply two matrices using nested loops
# l = list(map(int, (input().split())))
# n, m = map(int, input().split())
# result = []
# for i in range(len(n)):
#     for j in range(len(m[0])):
#         for k in range(len(m)):
#             result[i][j] += n[i][k] * m[k][j]
#
# for r in result:
#     print(r)
# from operator import contains
# from audioop import max

# 168    from builtins import max
#
# a, b, c = map(float, input().split())
# def func(a, b, c):
#     x = ((max(a, a + b) + max(a, b + c)) / (1 + max(a + b * c, 1.15)))
#     return f"{x:.2f}"
# print(func(a=a,b=b,c=c))

# t, s = map(float, input().split())
#
# def G(a, b):
#     y = ((a ** 2) + (b ** 2)) / ((a ** 2 ) + (2 * a * b) + (3 * b ** 2) + 4)
#     return y
#
#
# g_1 = G(1.2, s)
# g_2 = G(t, s)
# g_3 = G(2 * s - 1, s * t)
#
# print(f"{g_1 + g_2 + g_3:.2f}")
# from builtins import min, max
#
#
# def func1(a, b):
#     u = min(a, b)
#     v = min(a*b,max(a,b))
#     s = min(u + v, 3.14)
#     return f'{u:.2f}',  f'{v:.2f}', f'{s:.2f}'
#
# a, b = map(float, input().split())
# print(func1(a, b))
# summ = 0
# for i in range(10):
#     for j in range(1, 10):
#         print(f'{i**j:<8}', end = ' ')
#     print()
# a, b = map(int,input().split())
# x = a**b
# print(x%10)
# from builtins import max
# from locale import str
#
# a = [
#     'hello world',
#     'p8 group python pdp',
#     'hello',
#     'algo ub tuit uz sayti'
# ]
# n = 0
# for i in a:
#     n = max(len(i.split()), n)
# print(n)

# a = 'algo       ub         tuit                 uz      sayti'
# x = a.split()
# for i in x:
#     print(i, end=' ')


# from builtins import zip, reversed
#
# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# result = []
# for column in zip(*matrix):
#     result.append(sort(column, reversed=True))
# for column in zip(*result):
#     print(*column)

# n = int(input())
# c = 2
# for i in range(2, n//2+1):
#     if n % i == 0:
#         c += 1
# print(c)

# 302

# x, n= map(int, input().split())
#
# for i in range(i, n)

# x, y= map(float, input().split())
# if x==y:
#     print('NO')
# else:
#     print('YES')

# from math import gcd
#
# input()
# l = list(map(int, input().split()))
# print(gcd(*l))

# s = list(map(int, input().split()))
# min_ = min(s)
# #
# if all(not j % min_ for j in s):
#     print(min_)
# else:
#     for i in range(min_ // 2, 2, -1):
#         if all(not j % i for j in s):
#             print(i)
#             break
#     else:
#         print(1)


# from builtins import sorted
#
# n , m = map(int , input().split())
#
# matrix = []
# for i in range(n+1):
#     matrix.append(list(map(int , input().split())))
#
# for i in sorted(matrix , key= lambda x : x[0], reverse=True):
#     print(*i)
# from builtins import sorted
#
# n = [0, 1, 0, 2, 3]
# for i in n:
#     if i==0:
#         print(n.remove())


# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n+1):
#     s +=factorial((x**(n)) * (n+1))/factorial(n)
# print(int(s))


# from math import log
#
# n, x, y = map(int, input().split())
# s = 0
# for i in range(1, n+1):
#     s +=(log(x, y)**(2*i-1))/(2**i)
# print(f'{s:.2f}')


# 308
# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += (x ** i) *(factorial( (i + 1))) / (factorial(i))
#
# print(int(s))

# 307
# from math import sqrt
#
# c = float(input())
# print(f'{c / 2 * (3 + sqrt(3)):.2f}', f'{c * sqrt(3) / 4:.2f}')


# 310
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += i/(x**i)
#
# print(f'{s:.2f}')

# 311
# from math import sin
#
# x, a = map(float, input().split())
# y = (x**(4/3)) + x*sin(x)*a
# print(f'{y:.2f}')


# 312
# a, b = map(int, input().split())
# s = a*b
# t = a+b
# if a>b:
#     b = s
#     a = t
#     print(a, b)
# else:
#     a = s
#     b = t
#     print(a,b)


# 313
# a, b, c = map(int, input().split())
# s = a+b+c
# t = a*b*c
# if a>0 and b>0 and c>0:
#     print(s)
# else:
#     print(t)

# 317 chiqmagan
# from builtins import abs
#
# x, y = map(int, input().split())
# if x != -1:
#     a = ((x + 2*y)/(y**2 + (abs((y**2 + 2))/(x+1)))) + 2*x - y
#     print(f'{a:.2f}')
# else:
#     a = (2*x) - y
#     print(f'{a:.2f}')


# 41
# from builtins import min, max
#
# a, b, c = map(float, input().split())
# mini = min(a, b, c)
# maxi = max(a, b, c)
# print(mini, maxi)
# if ((a <= b and b <= c) or (c <= b and b <= a)):
#     mini = (maxi + b)/2
#     print(maxi, b, mini)
# elif((b <= a and a <= c) or (c <= a and a <= b)):
#     mini = (maxi + a) / 2
#     print(maxi, a, mini)
# else:
#     mini = (maxi + c) / 2
#     print(maxi, c, mini)


# x, y = map(float,input().split())
# if -0.5 <= x <= 0.5 and -1 <= y <= 1:
#     print('yes')
# else:
#     print('no')

#
# from builtins import type
# from math import sqrt
#
# n = int(input())
# if type(n**(1/2)) == int:
#     print('YES')
# else:
#     print('NO')
#
# def func(x, y):
#     if 0 <= x <= 0.5 and 0 <= y < 1:
#         print('Yes')
#     else:
#         print('No')
#
# x, y = map(float, input().split())
# print(func(x, y))
#
#
# from math import cos, log, exp
#
# x, y, c, d = map(int, input().split())
# S = 0
# P = 1
# SP = 0
# for m in range(1, x + 1):
#     S += (3 * (m ** 3)) / ((m ** 3) + (log(exp(m + 3))))
# for k in range(1, y + 1):
#     P *= (3*k)/((k**3 ) + (7*k))
# for i in range(1, c + 1):
#     D = 1
#     for j in range(1, d + 1):
#         D *= log(exp(i) + (j**i))/((j**i) + (i**2))
#     SP += D
# print(f'{S:.2f} {P:.2f} {SP:.2f}')


# 326
# from math import sqrt, sin, cos
#
# x, y, c, d = map(int, input().split())
# S = 0
# P = 1
# SP = 0
# for i in range(1, x + 1):
#     S += sqrt((c * i) + d)
# for k in range(1, y + 1):
#     P *= (sin(c + d) + (3 * c)) / (cos(c * k) + (2.78 * d))
# for i in range(1, c + 1):
#     D = 1
#     for k in range(1, d + 1):
#         D *= ((c * (x**k)) + (i*k))/((d*i) + (c*k))
#     SP += D
# print(f'{S:.2f} {P:.2f} {SP:.2f}')


# n = int(input())
#
# if 1 <= n <= 54:
#     print('2 baho')
# if 55 <= n <= 50:
#     print('3 baho')
# if 71 <= n <= 85:
#     print('4 baho')
# if 86 <= n <= 100:
#     print('5 baho')


#
# from builtins import max, min
#
# n , m = map(int, input().split())
# list1 = []
# for i in range(n):
#     l = list(map(int, input().split()))
#     list1.append(l)
# summ = 0
# a = max(list1)
# b = min(list1)
# for i in list1:
#     for j in range(len(i)):
#         if i[j] == a:
#             summ += a
#         elif i[j] == b:
#             summ += b
# print(summ)


# from math import sqrt
#
# a, b, x = map(int, input().split())
# brt(a+1)+sqrt((a*x*x+2*b)*1./(2*b+a*b))*(a+x*x+2*b*b)
# from builtins import min
# from distutils.command.install import key
#
# nums = [8, 13, 11, 90, -5, 4]
# nums.sort((key = lambda n: ((n and 1), n)))
# print(nums)

# input()
# arr = list(map(int, input().split()))
# mini = min(arr)
# kv = mini**2
# arr1 = []
# for i in arr:
#     if i < 0:
#         arr1.append(kv)
#         print(arr1)

#
# def move(arr):
#     arr.sort()
# arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# move(arr)
# for e in arr:
#     print(e, end=" ")

# n, m = map(int, input().split())
# matrix = []
# a = 0
# b = 0
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# for i in matrix:
#     for j in i:
#         if j > 0:
#             a += j
#         else:
#             b += j
#     s = a / b
#     print(s)
#

# 347
# n, m = map(int, input().split())
# matrix = []
# s = 0
# c = 0
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for row in matrix:
#     for a in row:
#         s +=a
#         c +=1
# print(f'{s/c:.2f}')

# 127
# n = int(input())
# l = list(map(int, input().split()))
# a = min(l)
# b = a*a
# for i in l:
#     if i < 0:
#         print(b,end=' ')
#     else:
#         print(i,end=' ')


# from math import log
#
# n = int(input())
# l = list(map(int, input().split()))
# s = 0
# c = 0
# for i in l:
#     s += i
#     c += 1
# a = log(s/c)
# for j in l:
#     if j<0:
#         print(f'{a:.2f}', end = ' ')
#     else:
#         print(f'{j:.2f}', end = ' ')

# 350
# a, b, c, d = map(int, input().split())
# s = a+c
# t = b+d
# if s == t:
#     print('Yes')
# else:
#     print('No')
#
#
# from builtins import max, min
#
# a, b, c, d = map(float, input().split())
# a2 = a * 2
# b2 = b * 2
# c2 = c * 2
# d2 = d * 2
# u = (a + b + c + d) / 4
# g = (a * b * c * d) ** (1 / 4)
# maxi = max(a, b, c, d)
# mini = min(a, b, c, d)
# if a > 0 and b > 0 and c > 0 and d > 0:
#     a = a2
#     b = b2
#     c = c2
#     d = d2
#     print(f'{a:.3f}', f'{b:.3f}', f'{c:.3f}', f'{d:.3f}')
# if a < 0 or b > 0 and c > 0 and d > 0:
#     a += u
#     b += u
#     c += u
#     d += u
#     print(f'{a:.3f}', f'{b:.3f}', f'{c:.3f}', f'{d:.3f}')
# if a < 0 and b < 0 and c > 0 or d > 0:
#     a += g
#     b += g
#     c += g
#     d += g
#     print(f'{a:.3f}', f'{b:.3f}', f'{c:.3f}', f'{d:.3f}')
# if a < 0 and b < 0 and c < 0 or d > 0:
#     a += maxi
#     b += maxi
#     c += maxi
#     d += maxi
#     print(f'{a:.3f}', f'{b:.3f}', f'{c:.3f}', f'{d:.3f}')
# if a < 0 and b < 0 and c < 0 and d < 0:
#     a -= mini
#     b -= mini
#     c -= mini
#     d -= mini
#     print(f'{a:.3f}', f'{b:.3f}', f'{c:.3f}', f'{d:.3f}')
#
# from math import sin, sqrt
#
# a,b,c = map(float, input().split())
# x = -c
# sin(x) = t
# a*(t**2) + b*t + c = 0
# d = b*b - 4*a*c
# t1 = -((b + sqrt(d))/(2*a))
# t2 = -((b - sqrt(d))/(2*a))
# sin(x)


# 136
# from builtins import zip
#
# n, n = map(int, input().split())
# matritsa = [list(map(int, input().split())) for i in range(n)]
# k = int(input())
# matritsa = list(zip(*matritsa))
# matritsa.remove(matritsa[k-1])
# for i in zip(*matritsa):
#     print(*i)


# 137
# n = int(input())
# matritasa = [list(map(int, input().split())) for i in range(n)]
# x = int(input())
# counn_element = 0
# new_list = []
#
# for i in matritasa:
#     for j in i:
#         if j % x == 0:
#             counn_element += 1
#             new_list.append(j)
#
# print(f"{sum(new_list) / counn_element:.2f}")


# 157     i elementni TATU suziga almashtirib beruvchi dastur
# a = input().split()
# b = int(input())
# x = ""
# y = "TATU"
#
# for i in range(len(a)):
#     if b -1 == i:
#         x += a[i]
# a[(b -1)] = y
# print(*a)


# n = input()
# arr = list(map(int, input().split()))
# list = []
# for i in arr:
#     list.append(i)
