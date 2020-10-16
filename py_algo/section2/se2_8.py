import sys
# sys.stdin = open("C:\\Users\\crpark\\vscode_py\\py_algo\\input.txt", "rt")

# 뒤집은 소수

# N개의 자연수가 입력되면 각 자연수를 뒤집은 후, 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요.
# 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다.
# 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하여 프로그래밍 한다.
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 100,000를 넘지 않는다.
# 첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

# ▣ 출력예제 1
# 37 9811 67 2543 17 397 19

n = int(input())
nArr = list(map(int, input().split()))

def reverse(x):
    xArr = list(str(x))
    xArr.reverse()
    return int(''.join(xArr))

def isPrime(x):
    if x <= 1:
        return False
    isCheck = True
    arr = [True] * (x+1)
    arr[0] = arr[1] = False
    for i in range(2, int(len(arr)/2)):
        if arr[i] == False:
            continue
        elif x % i == 0:
            isCheck = False
            break
        else:
            for j in range(i*2, len(arr), i):
                arr[i] = False
    return isCheck

for i in nArr:
    rNum = reverse(i)
    if isPrime(rNum) == True:
        print("%s"%rNum, end=' ')
