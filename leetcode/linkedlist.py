# class Node:
#
#     def __init__(self, data=0, next=None) -> None:
#         self.data = data
#         self.next = next
#
#     def __str__(self) -> str:
#         return f'{self.data} -> {self.next}'
#
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = Node()
#
#     def print_ll(self):
#         tmp = self.head
#         while tmp:
#             print(tmp.data, end=' ')
#             tmp = tmp.next
#
# def list_to_ll(self, lst: list):
#     self.head = Node()
#     tmp = self.head
#     for i in lst:
#         tmp.next = Node(i)
#         tmp = tmp.next
#
#     self.head = self.head.next
#
# def len_ll(self) -> int:
#     counter = 0
#     tmp = self.head
#     while tmp:
#         counter += 1
#         tmp = tmp.next
#     return counter
#
# def last_end_element(self, element:int):
#     last = self.len_ll() - element
#     tmp = self.head
#     for i in range(last):
#         tmp =tmp.next
#     return tmp.data
# def last_head_element(self, element:int):
#     last = (self.len_ll() - self.len_ll()) + element -1
#     tmp = self.head
#     for i in range(last):
#         tmp =tmp.next
#     return tmp.data
# def append(self, n:int):
#     tmp = self.head
#     while tmp.next:
#         tmp = tmp.next
#     tmp.next = Node(n)
#
# def insert(self, n:int):
#     a = Node(n)
#     a.next = self.head
#     self.head = a
# def insertlist(self, n:int):
#     a = Node(n)
#     a.next = self.head
#     self.head = a
#
# a = [2, 3, 4, 5, 6, 7, 8]
# ll = LinkedList()
# ll.list_to_ll(a)
# print(ll.last_end_element(7))
# print(ll.last_head_element(6))
# ll.append(34)
# ll.print_ll()
# print()
# ll.append(87)
# ll.print_ll()
# print()
# ll.insert(45)
# ll.print_ll()
# print()
# ll.insert(25)
# ll.print_ll()
#
#
#
# class Node:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = Node()
#
#     def read_list(self, lis: list):
#         self.head = Node()
#         tmp = self.head
#         for i in lis:
#             tmp.next = Node(i)
#             tmp = tmp.next
#         self.head = self.head.next
#     def print_list(self):
#         lis = []
#         tmp = self.head
#         while tmp:
#             lis.append(tmp.val)
#             tmp = tmp.next
#         print(list(sorted(lis)))
# list1 = [1,2,4]
# list2 = [1,3,4]
# ll = LinkedList()
# ll.read_list(sorted(list1+list2))
# ll.print_list()
#
#
#
# class Node:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = Node()
#
#     def read_list(self, lis: list):
#         self.head = Node()
#         tmp = self.head
#         for i in lis:
#             tmp.next = Node(i)
#             tmp = tmp.next
#         self.head = self.head.next
#     def print_list(self):
#         p1 = head = Node(0)
#         head.next = l1
#         p2 = l2
#
#         while (p1.next and p2):
#             if p1.next.val <= p2.val:
#                 p1 = p1.next
#             else:
#                 tmp = p1.next
#                 p1.next = p2
#                 p1 = p2
#                 p2 = tmp
#         if not p1.next:
#             p1.next = p2
#         return head.next
# head = [1,1,2]
# ll = LinkedList()
# ll.read_list(head)
# ll.print_list()
#
#
#
# class Node:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = Node()
#
#     def read_list(self, lis: list):
#         self.head = Node()
#         tmp = self.head
#         for i in lis:
#             tmp.next = Node(i)
#             tmp = tmp.next
#         self.head = self.head.next
#     def print_list(self):
#         lis = []
#         tmp = self.head
#         if tmp is None or tmp.next is None:
#             print(True)
#         while tmp:
#             lis.append(tmp.val)
#             tmp = tmp.next
#         print(lis == lis[::-1])
#
#
# head = [1,2,2,1]
# ll = LinkedList()
# ll.read_list(head)
# ll.print_list()
#
#
#
# class Node:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next
#
# n1 = Node(4)
# n2 = Node(1)
# n3 = Node(8)
# n4 = Node(4)
# n5 = Node(5)
#
# p1 = Node(5)
# p2 = Node(6)
# p3 = Node(1)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# p1.next = p2
# p2.next = p3
# p3.next = n3
# s = set()
# tmp = p1
# while tmp:
#     s.add(tmp)
#     tmp = tmp.next
#
#
#
# seen = set()
# a = listA
# b = listB
# while a:
#     seen.add(a)
#     a = a.next
# while b:
#     if b in seen:
#         print(b)
#     b = b.next
# print(None)
#
#
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = Node(0)
#
#     def read_list(self, lis: list):
#         tmp = self.head
#         for i in lis:
#             tmp.next = Node(i)
#             tmp = tmp.next
#         self.head = self.head.next
#
#     def print_list(self):
#         lis = []
#         tmp = self.head
#         while tmp:
#             lis.append(tmp.val)
#             tmp = tmp.next
#         print(list(sorted(lis)))
#
# head = [4, 5, 1, 9]
# ll = LinkedList()
# ll.read_list(head)
# ll.print_list()
#
#
# if not head:
#     return
# l = 0
# p = head
# while p.next:
#     l += 1
#     p = p.next
# l += 1
# p.next = head
# i = l - k % l
# while i > 0:
#     p = p.next
#     i -= 1
# head = p.next
# p.next = None
# return head
