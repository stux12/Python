# ctrl + f5 하면 실행

# 정수형 (int)
a = 1

# 실수형 (double)
b = 1.24

print(b)
print(type(a)) # 타입을 알 수 있음

print(a+b)
print(a*b)
print(a/b)
print(a//b) # 나눈 몫
print(a%b) # 나머지를 구할수 있음
print(a**b) # 제곱

# 문자형(String)
c = "hello world" 
c = 'hello\' world' #\를 쓰면 바로뒤에 것을 문자로 인식하겠다라는 뜻이 됨
c = 'hello \n wolrd' # \n 를 쓰면 줄을 바꿈
c = """ hello world """ # 3개쓰면 알아서 잘 인식 됨

print(c*100) # c를 100번 출력해라라는 뜻

# 슬라이싱 문자를 자른다
# [이상:미만:간격]
print(c[4]) # 첫글자가 0부터 시작함
print(c[-1]) # 맨뒷글자가 나옴
print(c[0:4]) # 0이상 4미만이 나옴
print(c[:8:2]) # 처음이 0부터 시작함 2칸간격으로 간다.

number = 10
a = "i ate %d apples" %(number) # %d(정수) %s(문자)로 나중에 값처리 가능
a = "i ate {name} apples" .format(name = "10개") # 이런식으로도 사용 가능
name = "int"
a = f"나의이름은 {int}입니다." # 앞에 f 를 붙임으로서 더 간단하게 사용가능
a = "%0.4f" %3.423232124 # 소수점 4자리까지 자름
a.count('b') # a의 문자에서 b가 몇개인지 카운트
a.find('b') # a의 문자에서 b가 몇번째 인덱스에 있는지 나옴 없으면 -1이 나옴 
a = "," join("abcd") # 문자하나하나에 ,를 넣어준다
a.upper() # a를 대문자로 바꿔줌
a.lower()
a.strip() # 공백을 없애줌
a.replace("life", "your leg") # life라는걸 뒤에걸로 바꾼다
a.split(":") # 띄워쓰기 기준으로 자른다 괄호안에 문자를 넣으면 그 문자로 잘라짐

a = ["이시영","문재성","각기동",1,2,["김재원",1,2]]
print(a[0][1]) # 인덱스 번호로 넣어야함
print(a[0:3]) # 0이상부터 3미만까지 출력
del a [0] # 인덱스0번 삭제
a.append("기모찌") # 추가
a.sort() #순서대로 정렬
a.reverse() # 순서 반대로 돌림
a.index(5) # 5가 있으면 인덱스 번호를 알려줌
a.insert(0,4) # 0번째 인덱스에 4를 추가해라
a.remove(1) # 1이라는 값을 지워라 여러개 있을경우 1개만삭제됨
a.pop() # 마지막꺼 출력하고 삭제한다
a.count(1) # 1이 몇개있는지 세줌
a.extend([2,3]) # 2,3이 추가됨
 




