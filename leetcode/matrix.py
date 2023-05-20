# from pprint import pprint
#
# # T
# n = int(input())
# m = list(map(lambda _: ['*'] * n, range(n)))
# print(*m[0])
# for i in m[1:-1]: print('  ' * (n // 2) + '*')
# print(*m[-1])
#
# n = int(input())
# m = list(map(lambda _: ['*  '] * n, range(n)))
# for i in range(n - 1): print('*\n')
# print(*m[-1])
#
# n = int(input())
# m = list(map(lambda _: ['* '] * n, range(n)))
# for i, v in enumerate(range(n)): print(*m[i]) if i == n // 2 else print('*', "   " * (n - 2), '*')
#
# n = int(input())
# a = 1
# for i in range(n):
#     b = []
#     for j in range(n):
#         b.append(a)
#         a += 1
#     print(b)
# a = 1
# # H
# for i in range(n):
#     b = []
#     for j in range(n):
#         if i == n or j == 0 or n // 2 == i or j == n - 1:
#             b.append(a)
#         else:
#             b.append('  ')
#         a += 1
#     print(*b)
# print()
#
# # I
# for i in range(n):
#     b = []
#     for j in range(n):
#         if j == n or i == 0 or n // 2 == j or i == n - 1:
#             b.append(a)
#         else:
#             b.append(' ')
#         a += 1
#     print(*b)
# print()
#
# #  T
# for i in range(n):
#     b = []
#     for j in range(n):
#         if j == n or i == 0 or n // 2 == j:
#             b.append(a)
#         else:
#             b.append(' ')
#         a += 1
#     print(*b)
# print()
# # L
# for i in range(n):
#     b = []
#     for j in range(n):
#         if i == n or j == 0 or i == n - 1:
#             b.append(a)
#         a += 1
#     print(*b)
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# ln = len(matrix)
# a = 1
# for i in range(ln):
#     b = []
#     for j in range(ln):
#         b.append(matrix[i][a])
#         a += 1
#     print(*b)
#
# nums = [1, 2, 3]
#
# k = 0
# for i, l in enumerate(nums):
#     for j, val in enumerate(nums[i + 1:]):
#         if (l == val):
#             k += 1
# print(k)
#
# d = {}
# res = 0
# for i in nums:
#     d[i] = d.get(i, 0) + 1
#     res += d.get(i) - 1
# print(res)
#
# nums = [1, 3, 5, 6]
# target = 5
# s = 0
# for i in nums:
#     if i < target:
#         s += 1
# print(s)
#
# nums.append(target)
# nums.sort()
# print(nums.index(target))
#
# digits = [1, 2, 3]
# s = ''.join(str(i) for i in digits)
# lis = []
# for i in str(int(s) + 1):
#     lis.append(int(i))
# print(lis)
#
# s = ""
# for i in range(len(digits)):
#     s += str(digits[i])
# s = str(int(s) + 1)
# lis = []
# for i in range(len(s)):
#     lis.append(int(s[i]))
# print(lis)
#
# tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
# from collections import Counter
#
# sum = 0
# for i in Counter(tasks).values():
#     if i < 2:
#         print(-1)
#         break
#     if i % 3 == 0:
#         sum += i // 3
#     elif i % 3 == 1:
#         sum += (i - 4) + i // 3 + 2
#     elif i % 3 == 2:
#         sum += i // 3 + 1
# print(sum)
#
# nums1 = [1, 1, 3, 2]
# nums2 = [2, 3]
# nums3 = [3]
# lis = set()
# for i in set(nums1):
#     if i in nums2 or i in nums3:
#         lis.add(i)
# for j in set(nums2):
#     if j in nums1 or j in nums3:
#         lis.add(j)
# for s in set(nums3):
#     if s in nums2 or s in nums1:
#         lis.add(s)
# print(list(lis))
#
# from collections import Counter
#
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# paragraph.lower()
# paragraph = paragraph.lower()
# paragraph = paragraph.replace('.', '').replace("'", '')
# paragraph = paragraph.replace('?', '').replace('!', '').replace(',', ' ').replace(';', '')
# d = Counter(paragraph.split())
# for i in banned:
#     if d.get(i):
#         d.pop(i)
# print(d.most_common(1)[0][0])
#
# nums = [1, 8, 9, 11, 12]
# for i in range(1, sorted(nums)[0]):
#     if i not in nums:
#         print(i)
# for v in range(1, len(nums)):
#     if v not in nums:
#         print(v)
# print(v + 1)
