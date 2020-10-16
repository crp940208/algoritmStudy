# import practice_module

# # 모듈
# practice_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# practice_module.price_morning(4) # 4명이서 조조 때 영화 보러 갔을 때 가격
# practice_module.price_soldier(5) # 5명이서 군인할인으로 영화 보러 갔을 때 가격

# import practice_module as md
# md.price(3)
# md.price_morning(4)
# md.price_soldier(5)

# from practice_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from practice_module import price
# price(3)
# # price_morning(4) # 에러! name 'price_morning' is not defined

# from practice_module import price_morning as price
# price(4) # 4명의 조조할인 가격은 24000원입니다.


# # 패키지
# import travel.hongkong # 모듈 or 패키지만 가능, 클래스나 메서드는 불가(from A import B 구문에서는 클래스나 메서드도 사용 가능)
# trip_hp = travel.hongkong.HongkongPackage()
# trip_hp.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# # __all__
# from travel import *
# trip_to = vietnam.VietnamPackage() # name 'vietnam' is not defined
# trip_to.detail()

# init파일 수정 후 # ["vietnam"]
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# # trip_hp = travel.hongkong.HongkongPackage() # name 'travel' is not defined
# # trip_hp.detail()

# init파일 수정 후 # ["vietnam", "hongkong"]
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# trip_hp = hongkong.HongkongPackage()
# trip_hp.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(hongkong))


# # pip install
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# # 내장함수
# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir()) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# import random
# print(dir()) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'random']
# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))
# name = "jim"
# print(dir(name))
# https://docs.python.org/3/library/functions.html


# # 외장함수
# import를 해서 사용해야 하는 함수
# https://docs.python.org/3/py-modindex.html

# # glob : 경로 내의 폴더/파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 표시
# folder = "sample_dir"
# if os.path.exists(folder): # 지정한 폴더 혹은 파일이 존재하는지 여부
#     print('이미 존재하는 폴더입니다.')
#     os.rmdir(folder) # 폴더 삭제
#     print("%s폴더를 삭제하였습니다."%folder)
# else:
#     os.makedirs(folder) # 폴더 생성
#     print("%s폴더를 생성하였습니다."%folder)
# print(os.listdir()) # 현재 경로의 모든 폴더 및 파일 출력

# # time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m_%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 %s"%datetime.date.today())
# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("오늘로부터 100일 뒤는 %s"%(today+td))


# # Quiz
import byme
byme.sign()