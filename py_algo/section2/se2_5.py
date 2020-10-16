import sys
# sys.stdin = open("input.txt", "rt")

# 정다면체
# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
# 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

# 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
# 첫 번째 줄에 답을 출력합니다

# ▣ 출력예제 1
# 5 6 7
n, m = map(int, input().split())

sumLst = list()
for i in range(1, n+1):
    for j in range(1, m+1):
        sumLst.append(i+j)
sumLst.sort()
sumDict = {}
for i in sumLst:
    if i in sumDict:
        sumDict[i] += 1
    else:
        sumDict[i] = 0
max = max(sumDict.values())
for k, v in sumDict.items():
    if max == v:
        print("%s"%k, end=' ')
