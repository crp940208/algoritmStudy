# # if문
# weather = input("오늘 날씨는 어때요? : ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" : 
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

# temp = int(input("기온은 어때요? : "))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요!")
# elif 10 <= temp & temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요, 나가지 마세요!")

# for문
# lst = ["100번", "101번", "102번", "103번"]
# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in lst:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "캡틴아메리카"]
# for customer in starbucks:
#     print("{0}, 주문하신 메뉴를 받아가세요".format(customer))


# while문
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True: # 무한루프
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


# continue
# break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 두고옴
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}번은 교무실로 따라와.".format(student))
#         break
#     print("{0}번, 책 읽자".format(student))


# 한 줄 for문
# students = [1, 2, 3, 4, 5]
# students = [i+100 for i in students]
# print(students)

# students = ["아이언맨", "토르", "블랙위도우"]
# students = [len(i) for i in students]
# print(students)

# students = ["iron man", "thor", "hulk"]
# students = [i.upper() for i in students]
# print(students)


# Quiz
from random import *
total_cus = 0
for i in range(1, 51):
    soyo_time = randint(5, 50)
    isCheck = 5 <= soyo_time <= 15
    if isCheck:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, soyo_time))
        total_cus += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, soyo_time))
print("총 탑승 승객 : {0}".format(total_cus))