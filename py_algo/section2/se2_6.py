import sys
# sys.stdin = open("input.txt", "rt")

# 자릿수의 합
# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
# 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 10,000,000를 넘지 않는다.
# 자릿수의 합이 최대인 자연수를 출력한다.

# ▣ 출력예제 1
# 97

n = int(input())
lst = list(map(int, input().split()))

def digit_sum(x):
    arr = list(map(int, list(str(x))))
    res = 0
    for i in arr:
        res += i
    return res

maxNum = 0
maxNumSum = 0
for i in lst:
    num = digit_sum(i)
    if maxNumSum < num:
        maxNum = i
        maxNumSum = num
print(maxNum)


