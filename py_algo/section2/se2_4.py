import sys
# sys.stdin = open("input.txt", "rt")

# 대표값
# N명의 학생의 수학점수가 주어집니다.
# N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
# 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
# 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

# 첫줄에 자연수 N(5<=N<=100)이 주어지고,
# 두 번째 줄에는 각 학생의 수학점수인 N개의 자연수가 주어집니다.
# 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
# 첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
# 평균은 소수 첫째 자리에서 반올림합니다.

# ▣ 출력예제 1
# 74 7

studentNum = int(input())
jumsuLst = list(map(int, input().split()))
aver = round(sum(jumsuLst) / studentNum)
num = float('inf')
for i in range(len(jumsuLst)):
    n = abs(aver - jumsuLst[i])
    if n > abs(aver - num):
        pass
    elif n < abs(aver - num):
        num = jumsuLst[i]
    elif num < jumsuLst[i]:
        num = jumsuLst[i]
print("%s %s"%(aver, jumsuLst.index(num)+1))