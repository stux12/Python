# 파이썬 함수의 구조
# def 함수명 (매개변수) :
#     <수행할 문장 1>
#     <수행할 문장 2>
#     return 리턴값
def sum(a,b) :
    result = a +b
    return result
print(sum(1,2))

def say():
    print("say")
    return 'Hi'
print(say())

def sum_many(*args) :# 입력받은 인자들로 다받음, **kwargs key balue를 아무거나 입력받을수 있음
    sum2 = 0
    for i in args:
        sum2 = sum2 + i
    return sum2
print(sum_many(1,2,3))   

# 함수의 결과값은 언제나 하나이다 return을 여러개하면 튜플형태로 나옴!!
def sum_and_mul(a,b):
    return a+b, a*b, a-b
print(sum_and_mul(1,2)[0])

# 기본값 설정
def says(a,b,man=True): # c에대한 기본값은 True를 준다 인자 a,b만 줘도 사용가능함
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

# 함수안의 변수의 범위
a = 1 # 전역함수 어디서든 사용가능
def vartest(a): # 지역변수 밖에 빠져나가면 없어짐
    global a # 전역함수로 처리로 할수있게됨
    a = a + 1
    return a
a = vartest(a)
print(a)


# Lamda
def add(a,b):
    return a+b

add = lambda a, b : a+b # 위의식이랑 같음 :뒤에 리턴값
print(add(1,2))
myList = [lambda a,b: a+b, lambda a, b : a*b]
print(myList[0](1,2)) # 앞에것을 가져옴 [1]을할시 뒤에것을 가져옴


a = input() # 내장함수
# 값을 입력받을 수 있음 Scanner 같은녀석

number = input("숫자를 입력하세요: ")
#, 를 넣으면 띄워쓰기가 됨
#그냥 붙여쓸경우 +처리가 됨
#, end =" " 하나가 끝나면 처리함


# 파일 읽고쓰기
f = open("새파일.txt", 'w')   # w = write 쓰기, r = read 읽기, a = 추가
f.close()

f = open("새파일.txt", 'w', encoding = "UTF-8") 
for i in range(1,11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close


# 파일 읽기
# read()함수 통째로 가져옴
f = open("새파일.txt", 'r', encoding="UTF-8")
data = f.read()
print(data)


# 한줄 리스트형태로 가져옴
f = open("새파일.txt", 'r', encoding="UTF-8")
line = f.readline()
print(line)
f.close()

# 여러줄
f = open("새파일.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()

# lines로 여러줄
f = open("새파일.txt", 'r', encoding="UTF-8")
while True:
    lines = f.readlines() # 
    for line in lines :
        print(line.strip("\n"))
f.close()


# 추가 add의 의미
f = open("새파일.txt", 'a', encoding="UTF-8")
for i in range(11,20):
    data = "%d번째 줄입니다 \n" % i
    f.write(data)
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

# 파이썬은 줄을 지키는게 중요하다