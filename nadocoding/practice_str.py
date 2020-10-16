# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """테스트
# 나는 소년이고,
# 파이썬은 쉬워요
# 하하하"""
# print(sentence3)

# jumin = "940208-1234567"
# print("성별 : " + jumin[7])
# # jumin[7] = "2" # 이건 불가능
# print("연 : " + jumin[0:2]) # 0번째 인덱스부터 2번째 인덱스 전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower()) # 소문자로
# print(python.upper()) # 대문자로
# print(python[0].isupper()) # python의 0번째 문자가 대문자인지? # True
# print(python[0].islower()) # python의 0번째 문자가 소문자인지? # False
# print(len(python)) # 문자열의 전체 길이 # 17
# print(python.replace("Python", "Java"))

# index = python.index("n") # 지정한 문자가 있는 인덱스
# print(index) # 5
# index = python.index("n", index + 1)
# print(index) # 15

# print(python.find("n")) # index와 비슷하지만
# print(python.find("Java")) # -1
# #print(python.index("Java")) # 오류 발생!!

# print(python.count("n")) # python 변수 안에 'n'이 얼마나 포함되어 있는지 그 개수 반환


# 문자열 포맷 - 방법1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")
# print("나는 %s살입니다." % 20)

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# print("나는 %d살이고 %s을 좋아해요. 내 이름은 %c로 시작합니다." %(20, "파이썬", "P"))

# 문자열 포맷 - 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 문자열 포맷 - 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age = 20))

# 문자열 포맷 - 방법 4 (단, python 버전 3.6 이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자
# \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# print("PS C:\\Users\\crpark\\vscode_py>")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")


# Quiz
url = "http://naver.com"
url = url.replace("http://", "")
url = url[:url.find(".")]
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print("생성된 비밀번호 : %s" % password)







