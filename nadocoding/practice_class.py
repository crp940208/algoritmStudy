# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("%s 유닛이 생성되었습니다."%self.name)
#         print("체력: %s, 공격력: %s"%(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 멤버 변수 : 클래스 내에서 정의됨
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : %s, 공격력 : %s"%(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking :
#     print("%s는 현재 클루킹 상태입니다."%wraith2.name)

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("%s : %s방향으로 적군을 공격합니다. [공격력: %s]"%(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("%s : %s 데미지를 입었습니다." )

# Quiz
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year): # 매물 초기화
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self): # 매물 정보 표시
        print("%s %s %s %s %s년"%(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

houseArr = [
    {"location":"강남", "house_type":"아파트", "deal_type":"매매", "price":"10억", "completion_year":"2010"},
    {"location": "마포", "house_type": "오피스텔", "deal_type": "전세", "price": "5억", "completion_year": "2007"},
    {"location": "송파", "house_type": "빌라", "deal_type": "월세", "price": "500/50", "completion_year": "2000"}]


print("총 %s개의 매물이 있습니다."%len(houseArr))
for i in range(0, 3):
    h = houseArr[i]
    house = House(h["location"], h["house_type"], h["deal_type"], h["price"], h["completion_year"])
    House.show_detail(house)