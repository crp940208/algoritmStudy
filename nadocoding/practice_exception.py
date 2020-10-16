# # 예외처리
# try:
#     nums = []
#     nums.append(int(input("첫번째 숫자 : ")))
#     nums.append(int(input("두번째 숫자 : ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("%d / %d = %d"%(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값 입력")
# except ZeroDivisionError as err:
#     print(err)
# except as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# # 의도적으로 에러 발생시키기
# try:
#     print("한 자리 숫자만 나눗셈함")
#     num1 = int(input("첫번째 숫자 : "))
#     num2 = int(input("두번째 숫자 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("%d / %d = %d"%(num1, num2, int(num1/num2)))
# except ValueError:
#     print("한 자리 숫자만 입력하세요")

# 사용자 정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자만 나눗셈함")
#     num1 = int(input("첫번째 숫자 : "))
#     num2 = int(input("두번째 숫자 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : %d, %d"%(num1, num2))
#     print("%d / %d = %d"%(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다")
# except BigNumberError as err:
#     print("한 자리 숫자만 입력하세요")
#     print(err)

# # finally
# try:
#     print("한 자리 숫자만 나눗셈함")
#     num1 = int(input("첫번째 숫자 : "))
#     num2 = int(input("두번째 숫자 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("%d / %d = %d"%(num1, num2, int(num1/num2)))
# except ValueError:
#     print("한 자리 숫자만 입력하세요")
# finally:
#     print("계산기를 이용해주셔서 감사합니다")

# Quiz
chicken = 10
waiting = 1 # 현재 홀 만석, 대기번호 1부터 시작
class SoldOutError(Exception):
    def __init__(self):
        pass

while(True):
    print("남은 치킨 : %d마리"%chicken)
    try:
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
        if(order > chicken):
            print("재료가 부족합니다.")
        else:
            print("[대기번호 %d] %d마리 주문이 완료되었습니다."%(waiting, order))
            waiting += 1
            chicken -= order
        if(chicken == 0):
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
