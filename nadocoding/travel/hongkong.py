class HongkongPackage:
    def detail(self):
        print("[홍콩 패키지 3박 5일] 디즈니랜드 포함 야시장 투어")

if __name__ == "__main__": 
    print("hongkong 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
    trip_to = HongkongPackage()
    trip_to.detail()
else:
    print("hongkong 외부에서 모듈 실행")