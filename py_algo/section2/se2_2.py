import sys
sys.stdin = open("input.txt", "rt")

# K번째 수
# N개의 숫자로 이루어진 숫자열이 주어지면
# 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름차순 정렬했을 때
# k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

# 첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
# 각 케이스별
# 첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
# 두 번째 줄에 N개의 숫자가 차례로 주어진다.
# 각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.

# ▣ 출력예제 1
# #1 7
# #2 6

T = int(input())
for i in range(1, T+1):
    # inpt = list(map(int, input().split()))
    n, s, e, k = map(int, input().split())

    inputArr = input().split()
    arr = list(map(int, inputArr[s-1:e]))
    arr.sort()
    print("#%s %s"%(i, arr[k-1]))



