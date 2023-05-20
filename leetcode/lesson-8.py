# import os
#
# result = []
# for i in os.listdir():
#     if i.startswith('.'):
#         continue
#     if os.path.isdir(i):
#         result.append((i, 'fayl ' + ('yoq', 'bor')[bool(os.listdir(i))]))
#     else:
#         with open(i) as file:
#             result.append((i, 'malumot ' + ('yoq', 'bor')[bool(file.read())]))
#
# print(result)


#
# import os
#
# result = []
# for i in os.listdir():
#     if i.startswith('.'):
#         continue
#     if os.path.isdir(i):
#         if len(os.listdir(i)):
#             result.append((i, 'fayl bor'))
#         else:
#             result.append((i, 'fayl yoq'))
#     else:
#         with open(i) as file:
#             if file.read():
#                 result.append((i, 'malumot bor'))
#             else:
#                 result.append((i, 'malumot yoq'))
#
# print(result)

# import os
# import shutil
#
# while True:
#     path = os.getcwd() + f'~ % '
#     key = input(path)
#     if key.startswith('mv'):
#         l = key.split()
#         if len(l) == 3:
#             if os.path.isdir(l[2]):
#                 shutil.move(l[1], l[2])
#             else:
#                 os.rename(l[1], l[2])
#         else:
#             print('Error')
#
#     elif key == 'ls -i':
#         result = []
#         for i in os.listdir():
#             if i.startswith('.'):
#                 continue
#             if os.path.isdir(i):
#                 result.append((i, 'fayl ' + ('yoq', 'bor')[bool(os.listdir(i))]))
#             else:
#                 with open(i) as file:
#                     result.append((i, 'malumot ' + ('yoq', 'bor')[bool(file.read())]))
#         print(result)
#     elif key == 'ls':
#         print(*filter(lambda file_or_dir: not file_or_dir.startswith('.'), os.listdir()))
#     elif key.startswith('change'):
#         l = key.split()
#         if len(l) == 3 and os.path.exists(l[1]) and os.path.isfile(l[1]):
#             os.replace(l[1], l[2])
#         else:
#             print('Togri kiriting')
#     elif key.startswith('cd'):
#         l = key.split()
#         if len(l) == 2 and os.path.isdir(l[1]):
#             os.chdir(l[1])
#         else:
#             print('bunaqa papka yoq')
#     elif key.startswith('touch') and len(key.split()) == 2:
#         name = key.split()[1]
#         with open(name, 'w') as file:
#             pass
#     elif key.startswith('mkdir') and len(key.split()) == 2:
#         name = key.split()[1]
#         if os.path.isdir(name):
#             print('bunaqa papka bor')
#         else:
#             os.mkdir(name)
#     elif key == 'clear':
#         os.system('clear')
#     elif key == 'exit':
#         print('dastur tugadi')
#         break
#


#
# '''
# ls -i
#
# (lesson-3.py, 'malumot bor') (lesson-7.py, 'malumot yoq') (test, 'fayl bor')
#
# '''
#
# import os
#
# os.scandir()
#
# s = [('lesson-3.py', 'malumot bor'), ('lesson-7.py', 'malumot yoq'), ('test', 'fayl bor')]
# print(*s)
from pprint import pprint

#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10,11,12],
#     [13,14,15,16],
n = 10

r = [list(range(i, i + n)) for i in range(1, n * n + 1, n)]

# r = list(map(lambda i: list(range(i, i + n)), range(1, n * n + 1, n)))

# for i in r:
#     print(i)
# print(' ---- --- ---- ')
# print(*r[0])
# for i in range(1, len(r) - 1):
#     print('  ' * (len(r) - 1 - i) + str(r[i][len(r) - 1 - i]))
#
# print(*r[-1])

# counter = 1
# result = []
# for _ in range(n):
#     d = []
#     for _ in range(n):
#         d.append(counter)
#         counter += 1
#     result.append(d)

# pprint(result)
# for i in result:
#     print(i)


# 1)
# a = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10,11,12],
#     [13,14,15,16],
# ]


