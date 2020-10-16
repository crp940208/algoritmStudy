# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":20, "영어":50, "코딩": 100}
# for subject, score in scores.items(): # subject : key, score : value
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer)) # <class 'str'>
# print("입력하신 값은 %s입니다."%answer)


# # 다양한 출력 포맷
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<10}".format(500))

# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000000000))

# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(1000000000000000))
# print("{0:+,}".format(-1000000000000000))

# # 3자리 마다 콤마를 찍어주기, +- 부호 붙이기, 자릿수 확보하기, 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))

# # 소수점을 지정한 자리수까지만 표시
# print("{0:.2f}".format(5/3))


# # 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # 파일명, 쓰기, 인코딩 정보
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close() # file open 후에는 반드시 닫아(close)줘야 함

# score_file = open("score.txt", "a", encoding="utf8") # 파일명, 수정, 인코딩 정보
# score_file.write("과학: 80\n")
# score_file.write("코딩: 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 파일명, 읽기, 인코딩 정보
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 파일명, 읽기, 인코딩 정보
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 파일명, 읽기, 인코딩 정보
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 파일명, 읽기, 인코딩 정보
# lines = score_file.readlines() # list형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


# # pickle
# import pickle
# profile_file = open("profile.pickle", "wb") # b : 바이너리
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# # with
# import pickle
# with open("profile.pickle", "rb") as profile_file: # close()가 필요 없다
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부중입니다")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# # Quiz
for i in range(1, 51):
    weekly_report = open(str(i)+"주차.txt", "w", encoding="utf8")
    weekly_report.write("- %d주차 주간보고-\n"%i)
    weekly_report.write("부서 : \n")
    weekly_report.write("이름 : \n")
    weekly_report.write("업무 요약 : \n")
    weekly_report.close()
