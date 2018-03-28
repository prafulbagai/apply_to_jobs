# # # def fib(n):
# # #     if n == 0:
# # #         return 0
# # #     if n == 1:
# # #         return 1

# # #     return fib(n - 1) + fib(n - 2)

# # # print fib(9)


# # # def factorial(n):
# # #     if n <= 0:
# # #         return 0
# # #     if n == 1:
# # #         return 1
# # #     return n * factorial(n - 1)


# # # print factorial(5)


# # # def max_loot(arr, i):
# # #     if i < 0:
# # #         return 0

# # #     if i == 0:
# # #         return arr[i]

# # #     if i == 1:
# # #         return max(arr[i], arr[i - 1])

# # #     return max(arr[i] + max_loot(arr, i - 2), max_loot(arr, i - 1))


# # # arr = [6, 7, 1, 3, 8, 2, 9]
# # # i = len(arr) - 1
# # # print max_loot(arr, i)



# # # def maximize_loot(hval, n):
# # #     if n == 0:
# # #         return 0
# # #     if n == 1:
# # #         return hval[0]
# # #     if n == 2:
# # #         return max(hval[0], hval[1])

# # #     # dp[i] represent the maximum value stolen so
# # #     # for after reaching house i.
# # #     dp = [0]*n

# # #     # Initialize the dp[0] and dp[1]
# # #     dp[0] = hval[0]
# # #     dp[1] = max(hval[0], hval[1])

# # #     # Fill remaining positions
# # #     for i in range(2, n):
# # #         dp[i] = max(hval[i]+dp[i-2], dp[i-1])

# # #     return dp[-1]

# # # hval = [6, 7, 1, 3, 8, 2, 9]
# # # # number of houses
# # # n = len(hval)
# # # print maximize_loot(hval, n)


# # e1 = "a>b=1"
# # e2 = "a>b=2"
# # e3 = "a>c>e=3"
# # e4 = "a>c>f=4"
# # e5 = "b>a=5"
# # e6 = "a>b>c=5"
# # e7 = "b=7"
# # e8 = "a>b>c>d=99"
# # e9 = "a>b=99"

# # S = [e1, e2, e3, e4, e5, e6, e7, e8, e9]

# # d = {}

# # def check(dct, key, value):
# #     if key not in dct:
# #         dct.update({key: value})
# #         return dct[key]

# #     if isinstance(dct[key], list) and isinstance(value, int):
# #         dct[key].append(value)
# #         return dct[key]

# #     if type(dct[key]) != type(value):
# #         return dct[key]

# #     if value == {}:
# #         return dct[key]


# # for s in S:
# #     keys = s.split('>')
# #     temp = d
# #     print keys
# #     for key in keys[:-1]:
# #         print key
# #         dct = check(temp, key, {})
# #         d[key] = dct
# #         temp = d[key]
# #     print d



# def func(arr):
#     l = len(arr)

#     if l < 2:
#         return -1

#     diff = arr[1] - arr[0]
#     curr_sum = diff
#     max_sum = curr_sum

#     for i in xrange(1, l - 1):
#         diff = arr[i + 1] - arr[i]

#         if curr_sum > 0:
#             curr_sum += diff
#         else:
#             curr_sum = diff

#         if curr_sum > max_sum:
#             max_sum = curr_sum

#     return max_sum if max_sum > 0 else -1

# print func([80, 12, 6, 3, -100])

# def mycompare(a, b):
#     ab = a.append(b)
#     ba = b.append(a)
#     return True if ab > ba else False


# def printlargest(n, arr):
#     sorted(arr, key=mycompare)
#     for i in xrange(n):
#         print arr[i]

# printlargest(4, [1,2,3,4])


# print(sorted(arr, key=lambda i: i and i/(10**math.ceil(math.log10(i+1))-1), reverse=True))


# a = '11000000111000000010'
# start, end, temp_start, count, temp = 0, 0, 0, 0, 0
# for i in xrange(len(a) - 1):
#     if a[i] == '0' and temp_start > 0:
#         temp += 1
#         continue

#     if temp > count:
#         start = temp_start
#         count = temp
#         temp = 0
#         end = i

#     temp_start = i


# print start, end, count

print [i if i % 2 == 0 else 0 for i in xrange(10)]