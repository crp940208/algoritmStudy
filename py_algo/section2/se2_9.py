import sys
# sys.stdin = open("C:\\Users\\crpark\\vscode_py\\py_algo\\input.txt", "rt")

# 주사위 게임
# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
# 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된다. 
# 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
# 3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금으로 받게 된다.
# N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 그 다음 줄부터 N개의 줄에 사람들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.

# ▣ 출력예제 1
# 12000

n = int(input())
maxMoney = 0

def ruleResult(dice):
    equalCnt = 3
    num = 0
    for i in range(0, 3):
        if i < 2 and dice[i] == dice[i+1]:
            num = dice[i]
            equalCnt -= 1
    if equalCnt == 3:
        num = max(dice)
    return equalCnt, num

for i in range(0, n):
    iMoney = 0
    dice = list(map(int, input().split()))
    rRes = ruleResult(dice)
    if rRes[0] == 1:
        iMoney = 10000 + rRes[1]*1000
    elif rRes[0] == 2:
        iMoney = 1000 + rRes[1]*100
    elif rRes[0] == 3:
        iMoney = rRes[1]*100
    
    if maxMoney < iMoney:
        maxMoney = iMoney

print(maxMoney)
