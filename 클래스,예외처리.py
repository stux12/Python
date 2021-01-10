# import 해서 다른파일에 있는것을 가져옴
# from mod1 import add mod1에 있는 add함수만 가져옴 * 을하면 싹다 불러옴   
     #..을쓰면 이전폴더로 감              #  __All__  = ['메소드', '메소드2']
# import sys
# sys.path.append("C:\\경로") 만약 파일이 다른곳에 있다면 경로를 설정 해줘야 함


if __name__ == "__main__": # 지금 실행하는 곳이 메인일경우 아래로직 실행
    print("아몰랑") 

# immutable (변할수 없는것)
# 정수, 실수, 문자열, 튜플

# Mutable (변할수 있는것)
# 리스트, 딕셔너리, 집합

# 클래스
# 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
class Calculator : # 클래스명 첫글자 대문자
    def __init__(self) :# __변수__이렇게하면 객체를 생성을하면 이 메소드는 무조건 실행된다!! 
        self.result = 0

    def add(self, num): #self는 자기자신을 넣는다라는 뜻 a.add(2)에 a가 self로감
        self.result += num
        return self.result



cal1 = Calculator() # 객체를 생성
cal2 = Calculator()
# print(cal1._init_()) # 각각의 result를 생성
# print(cal2._init_())
print(cal1.add(3)) # 메소드 호출 + 리턴
print(cal1.add(4))
print(cal2.add(2))
print(cal2.add(7))


# 상속    자식클래스  부모클래스 
# 자식에게도 __init__함수는 동작한다. 변형도 가능
class MoreCalculator(Calculator):
    lastname = "김" # 클래스변수
   
    def pow(self): # 자식클래스에 기능 추가 부모는 자식기능을 못가짐
        print("모르겠다")
    def row(self):
        print("아몰라")
    
    # 부모의 기능을 재정의 오버라이드라고 함
    def __init__(self) : 
        self.result = 1

    def add(self, num): 
        self.result += num
        return self.result
a = MoreCalculator()
print(a.add(3))


# 예외처리
try : 
    a = 3/0
    # 오류가 발생할 수 있는 구문
except Exception as e :
    print(e)
    # 오류 발생하면 e변수에 잡힘
else : # try를 해서 구문오류가 없을때 else를 실행한다
    print("성공")
    # 오류없을시 실행 구문
finally : # 오류가 있든없든 무조건 실행 보통 close처리 할때 사용
    print("무조건이야~")

# 일부로 오류 내기
d = 0
if d == 0 :
    raise NotImplementedError #raise 오류발생시킬것


# 내장함수 파이썬에 기본적으로 포함하고 있는 함수
abs() # 절댓값
print()
all() # 모두 참인지 검사
any() # 하나라도 참이 있는가?
chr() # ascll코드를 입력받음
dir() # 명령어의 모음을 볼 수 있음
divmod() # 몫과 나머지를 튜플형태로 돌려줌
enumerate() # 열거하다
eval() # 
filter() # true인것만 남김 필요한것만 남기는느낌
id () # 주소값
len () # 길이
list() #리스트로 변환
map() # 각 요소가 수행한 결과를 돌려줌
max() # 최댓값
open() # 파일열기

# 외장함수 라이브러리함수, import해서 쓰는것
# time time.sleep
# random
# webbrowser.open

