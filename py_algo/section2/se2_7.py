import sys
# sys.stdin = open("C:\\Users\\crpark\\vscode_py\\py_algo\\input.txt", "rt")

# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다.
# 첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
# 첫 줄에 소수의 개수를 출력합니다.
#
# ▣ 출력예제 1
# 8

n = int(input())
arr = [True] * (n+1)
arr[0] = arr[1] = False
check = int(n/2)

for i in range(2, check+1):
    if arr[i] == True:
        for j in range(i*2, len(arr), i):
            arr[j] = False

cnt = 0
for i in arr:
    if i == True:
        cnt += 1

print(cnt)