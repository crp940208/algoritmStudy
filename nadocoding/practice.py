#연산자
# print(1+1)
# print(2-1)
# print(2*2)
# print(7/2)

# print(2**4) # 제곱
# print(5%3) # 나머지
# print(5//3) # 몫

# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True
# print(3 == 3) # True
# print(5 == 6) # False

# print(1 != 3) # True
# print(not(1 != 3)) # False
# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True
# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True
# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False

# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 20
# number = 2 + 3 * 4
# print(number) # 14
# number = number + 2
# print(number) # 16
# number += 2
# print(number) # 18
# number *= 2
# print(number) # 36
# number /= 3
# print(number) # 12.0
# number -= 3
# print(number) # 9.0
# number %= 2
# print(number) # 1.0

# print(abs(-5)) # 절댓값 # 5
# print(pow(4, 2)) # 제곱 # 4^2 = 4*4 = 16
# print(max(5, 12)) # 최댓값 # 12
# print(min(5, 12)) # 최솟값 # 5
# print(round(3.14)) # 반올림 # 3
# print(round(4.89)) # 반올림 # 5

# from math import *
# print(floor(4.99)) # 내림 # 4
# print(ceil(3.14)) # 올림 # 4
# print(sqrt(16)) # 제곱근 # 4.0

# from random import *
# print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 0 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# Quiz
from random import *
offlineStudyDay = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월 ' + str(offlineStudyDay) + '일로 선정되었습니다.')