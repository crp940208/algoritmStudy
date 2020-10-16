# 리스트

# subway = [10, 20, 30] # 지하철 칸별로 10명, 20명, 30명
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# print(subway.index("조세호")) # 조세호가 몇 번째 칸에 타고 있는가?
# subway.append("하하") # 하하가 다음 정류장에서 다음 칸에 탐
# print(subway)
# subway.insert(1, "정형돈") # 정형돈을 유재석/조세호 사이에 태워봄
# print(subway)

# print(subway.pop()) # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway)

# subway.append("유재석") # 같은 이름의 사람이 몇 명 있는지 확인
# print(subway)
# print(subway.count("유재석"))

# 정렬방법
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# num_list.reverse() # 순서 뒤집기 가능
# print(num_list)

# num_list.clear() # 모두 지우기
# print(num_list)

# 파이썬에서는 배열에서 자료형에 제한이 없다
# mix_list = ["조세호", 20, True]
# num_list = [5, 3, 4, 2, 1]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# 사전
# cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet.get(100))
# # print(cabinet[5]) # 오류 발생!
# print(cabinet.get(5)) # None 출력
# print(cabinet.get(5, "사용 가능")) # '사용 가능' 출력
# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet.get("B-100"))
# print(cabinet)
# cabinet["A-3"] = "김종국" # 수정
# cabinet["C-20"] = "조세호" # 추가
# del cabinet["B-100"] # 삭제
# print(cabinet)

# print(cabinet.keys()) # key 만 출력
# print(cabinet.values()) # values 만 출력
# print(cabinet.items()) # key, values 쌍으로 출력
# cabinet.clear() # 전체삭제
# print(cabinet)


# 튜플
# 변경되지 않는 목록을 사용할 때 - 리스트보다는 속도가 빠름
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# # menu.add("생선까스") # 오류 발생!

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# name, age, hobby = ("김종국", 20, "코딩")
# print(name) # 김종국
# print(name, age, hobby) # 김종국 20 코딩


# 세트
# 중복 불가, 순서 없음
# my_set = {1, 2, 3, 4, 3}
# print(my_set) # {1, 2, 3, 4} # 중복 불가로 값 무시

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합
# print(java & python) # {'유재석'}
# print(java.intersection(python)) # {'유재석'}

# # 합집합
# print(java | python) # {'박명수', '김태호', '유재석', '양세형'}
# print(java.union(python)) # {'박명수', '김태호', '유재석', '양세형'}

# # 차집합 (java만 할 줄 아는 사람)
# print(java - python) # {'김태호', '양세형'}
# print(java.difference(python)) # {'김태호', '양세형'}

# python.add("김태호") # python을 할 줄 아는 사람이 늘어남
# print(python) # {'유재석', '김태호', '박명수'}

# java.remove("김태호") # java를 까먹었음
# print(java) # {'양세형', '유재석'}


# 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # <class 'set'>

# menu = list(menu)
# print(menu, type(menu)) # <class 'list'>

# menu = tuple(menu)
# print(menu, type(menu)) # <class 'tuple'>

# menu = set(menu)
# print(menu, type(menu)) # <class 'set'>


# Quiz
# from random import *
# lst = [1, 2, 3, 4, 5]
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))
# from random import *
# users = range(1, 21) # 1부터 20까지 순서를 생성 # <class 'range'>
# users = list(users)
# # print(type(users)) # <class 'list'>
# shuffle(users)
# winners = sample(users, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")