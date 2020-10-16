# 반복문을 이용한 문제풀이
# 1) 1부터 N까지 홀수 출력하기
# n=int(input("숫자 n 입력 : "))
# for i in range(1, n+1):
#     if i % 2 == 1:
#         print(i)
# 2) 1부터 N까지의 합 구하기
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("1부터 %d까지의 합 : %d"%(n, sum))
# 3) N의 약수 출력하기
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=", ")


# 람다 함수
# def plus_one(x):
#     return x+1
#
# print(plus_one(1))

# plus_two = lambda x: x+2
# print(plus_two(1))

# def plus_one(x):
#     return x+1
# print(list(map(plus_one, a)))

# a = [1, 2, 3]
# print(list(map(lambda x: x+1, a)))

# 파이썬에서 가장 큰 값 = float('inf')