# password = input()
# l = len(password)
# next = 0
# num = 0
# upper = 0
# lower = 0
# if l <= 20:
#     if l < 6:
#         print(6 - l)
#     elif l >= 6:
#         for i in range(l):
#
#             if password[i].isdigit():
#                 num += 1
#             elif password[i].isupper():
#                 upper += 1
#             elif password[i].islower():
#                 lower += 1
#         for i in range(l - 2):
#             if password[i] == password[i + 1] and password[i] == password[i + 2]:
#                 next += 1
#         if next == 0 and num > 0 and upper > 0 and lower > 0:
#             print(0)


# command = "G()(al)"
# print(command.replace('()', 'o').replace('(al)', 'al'))

# jewels = "aA"
# stones = "aAAbbbb"
# s = 0
# for i in stones:
#     if i in jewels:
#         s +=1
# print(s)
# print(sum(s in jewels for s in stones))
# print(sum(map(jewels.count, stones)))


# a = [1, 1, 1, 2, 3, 3, 3, 3, 1, 1]
# a.sort(reverse=True)
# d = {}
# for k in a:d.update({k: a.count(k)})
# print(d)

# sentences = ["please wait", "continue to fight", "continue to win"]
# lis = []
# for i in sentences:
#     lis.append(len(i.split()))
# print(max(lis))
#
# print(max(len(i.split()) for i in sentences)
#
# num = 2932
# res = ''.join(sorted(str(num)))
# print(int(res[0] + res[3]) + int(res[1] + res[2]))

# s = "is2 sentence4 This1 a3"
# lis = []
# for i in sorted(s[::-1].split()):
#     lis.append(i[1:][::-1])
# print(' '.join(lis))

# names = ["Mary","John","Emma"]
# heights = [180,165,170]
# res = []
# for i in sorted(heights, reverse=True):
#     res.append(names[heights.index(i)])
# print(res)


# nums = [8, 1, 2, 2, 3]
# l = []
# s = 0
# for i in nums:
#     for j in nums:
#         if i > j:
#             s += 1
#     l.append(s)
#     s = 0
# print(l)
#
# print([sum(list(True for j in nums if i>j)) for i in nums])
#
#
# import string
#
# lowercase = string.ascii_lowercase
# coordinates = "a2"
# tip = coordinates[0]
# index = lowercase.find(tip) + 1
# num = int(coordinates[1:])
# print(True if (index % 2 == 1 and num % 2 == 0 ) or (index % 2 == 0 and num % 2 == 1) else False)


# words = ["pay","attention","practice","attend"]
# pref = "at"
# s = 0
# for i in words:
#     if i.startswith(pref):
#         s +=1
# return s


# print(sum(map(lambda  x: x.startswith(pref), words)))
#
# l = len(pref)
# s = 0
# for i in words:
#     if i[:l] == pref:
#         s += 1
# print(s)
#


# command = "G()(al)"
# print(command.replace('()', 'o').replace('(al)', 'al'))
#
# i = 0
# s = ''
# while i < len(command):
#     if command[i] == 'G':
#         s += 'G'
#         i += 1
#     elif command[i] == '(':
#         if command[i + 1] == ')':
#             s += 'o'
#             i += 2
#         else:
#             s += 'al'
#             i += 4
# print(s)


# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# res = [''] * len(s)
# for i, v in enumerate(indices):
#     res[v] = s[i]
# print(''.join(res))


# items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
#
# ruleKey = "type"
# ruleValue = "phone"
# # lis = []
# s = 0
# for i in items:
#     lis.extend(i)
# for j in lis:
#     if j == ruleValue or j == ruleKey:
#         s +=1
# print(s)
# result = 0
# for type, color, name in items:
#     if eval(ruleKey) == ruleValue:
#         result += 1
# print(int(result))
#
#
# import string
#
# a = string.ascii_lowercase
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# print(set(sentence) == set(a))
#

import string

# words = ["abc","car","adas","racecasr","cool"]
# for i in words:
#     if i[::] == i[::-1]:
#         print(i)
#         break
#     else:
#         print("")
# from builtins import reversed


# rim = {}
# rim['I'] = 1
# rim['V'] = 5
# rim['X'] = 10
# rim['L'] = 50
# rim['C'] = 100
# rim['D'] = 500
# rim['M'] = 1000
#
# s ="LVIII"
# prev = 0
# res = 0
# for i in s[::-1]:
#     c = rim[i]
#     if c >= prev:
#         res += c
#     else:
#         res += -1 * c
#     prev = c
# print(res)
# strs = ["ower","flow","flight"]
# for i in strs:
#     if strs[1].startswith(i[0]) and strs[2].startswith(i[0]):
#         print(i[0])
#         break
#     else:
#         print("")

#
# s = "abccbaacz"
# lis = []
# for i in s: lis.append(i) if i not in lis else print(i)
#
# st = set()
# for i in s: st.add(i) if i not in st else print(i)
#
#
# d = {}
# for i in s:
#     if d.get(i):
#         return i
#     d[i] =True
# return ''


# moves = "UD"
#
# ud = 0
# rl = 0
# for i in moves:
#     if i == 'D':
#         ud -= 1
#     elif i == 'U':
#         ud += 1
#     elif i == 'L':
#         rl -= 1
#     elif i == 'R':
#         rl += 1
# if rl == 0 and ud == 0:
#     print(True)
# else:
#     print(False)
#
# print(moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L'))


# nums = [3,2,3]
# target = 6
#
# for i in range(len(nums)):
#     for i + 1, len(nums)j in range():
#         if nums[i] + nums[j] == target:
#             return [i, j]
# return []
#


# lis = [1, 4, 8, 3, 21]
# l = []
# stp = 0
# while lis[stp] < 5:
#     print(lis[stp], end=' ')
#     stp += 1

# a = 'ABCD'
# b = 'xy'
# s = ''
# for i in a:
#     for j in b:
#         s += i + j + ' '
# print(s)


# nums = [('GM', 'Nexia'), ('BMW', 'model-123'), ('GM', 'Gentra'), ('BMW', 'model-657')]
# lis = []
# s = 1
# st = set()
# for i in nums:
#     st.add(i[0])
# for i in st:
#     for j in nums:
#         if i == j:
#             print(i, j)
#         else:
#             print()
#             print(i,j)


# costs = [1, 3, 2, 4, 1]
# coins = 7
# s = 0
# n = 0
# for i in sorted(costs):
#     s += i
#     n += 1
#     if s == coins:
#         print(n)
#     elif s > coins:
#         print(n - 1)


# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         #
#         s = 0
#         n = 0
#         for i in sorted(costs):
#             s += i
#             n += 1
#             if s == coins:
#                 return n
#             elif s > coins:
#                 return n - 1
#         return n
#
#         # 2-method
#         s = costs.sort()
#         for i in range(len(s)):
#             coins -= s[i]
#             if coins < 0:
#                 return i
#         return len(s)


# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# lis = []
# s = (int(''.join(str(i) for i in reversed(l1)))
#      + int(''.join(str(i) for i in reversed(l2))))
#
# for i in reversed(list(int(i) for i in str(s))):
#     lis.append(i)
# print(lis)
#
#
# s1, s2 = '',''
# lis = []
# for i in reversed(l1):
#     s1 += str(i)
# for j in reversed(l2):
#     s2 += str(j)
# for i in str(int(s1) + int(s2)):
#     lis.append(i)
# lis2 = []
# for i in reversed(lis):
#     lis2.append(int(i))
# print(lis2)

# x = 121
# if x[::] == x[::-1]:
#     print(True)
# else:
#     print(False)
#
# return str(x) == str(x)[::-1]
#


# s = "   fly me   to   the moon  "
# return len(s.split()[-1])

# low = 3
# high = 7
# s = 0
# for i in range(past + 1, baland):
#     if i % 2 != 0: s += 1
# return s
# if low % 2 == 0:
#     return (high - low + 1) // 2
# return (high - low) // 2 + 1
#
# return (high + 1) // 2 - low // 2
#
# salary = [4000, 3000, 1000, 2000]
# c = 0
# for i in salary: c += 1
# print(f'{sum(salary) / c:.5f}')

# nums = [1,2,2,3]
# if sorted(nums) == nums:
#     print(True)
# else:
#     print(False)

# s = "()[]{}"
# while '()' in s or '[]' in s or '{}' in s:
#     s = s.replace('()', '').replace('[]', '').replace('{}', '')
# return False if len(s) != 0 else True
