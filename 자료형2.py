# list & tuple
a = [1,2,3,'a','b'] # 리스트는 값을 바꿀 수 있음 
b = (1,2,3,'a','b') # 튜플은 값을 못바꿈 고정된것

# dictionary 딕셔너리 사전같은것 Hash map object json같은것
# key를 통해서 value를 얻는다

#       key      value
dic = {'name': 'Eric', 'age ': 15}
print(dic['name'])

# key value 추가
a = {1: 'a'}
a['name'] = "익명" 
print(a)

# key value 삭제
del a[1]

# key를 사용해 value얻기
a = {1: 'a', 1: 'b'} #key는 중복되면 안됨 마지막 키와 value만 남음
print(a.keys()) # key만 뽑아올수 있음
print(a.values()) # value들만 뽑아올수 있음
print(a.items()) # key, value 쌍을 담아서 뽑을수 있음

# 반복문을 통해서 key value 전체 출력하는방법
for k,v in a.keys,a.vlaues():
    print(k)
    print(v)

# 딕셔너리 모두 비우기
a.clear

# value얻기
print(a[1]) # 없는게 있으면 에러가나옴
print(a.get(1,'없음')) # 없는게 있을때 none이 나옴
print(4 in a) # 4가 a에 있냐라고 물어보고 true false 나옴

# 집합
# 집합 자료형
# 중복 X , 순서 X, 집합에 관련된것들을 쉽게 처리하기 위해 만들어진 자료형
s1 = set([1,2,3]) #list가 집합으로 변함
s1 = {1,2,3} # 위의 방법이랑 똑같음
print(s1)
# 사용되는 예시
l = [1,2,2,3,3]
newList = list(set(l)) #중복이 제거되고 다시 리스트화가 됨 약간 강제형변환 같은느낌

s = set("abc")
print(s) #순서 X 중복 X 문자가 다 잘려서 나옴

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2) # 겹치는 교집합값만 나옴
print(s1.intersection(s2)) # 위의 결과랑 같음
print(s1 | s2) # 합집합 나옴
print(s1.union(s2))# 위의 결과랑 같음
print(s1 - s2) # 차집합이 나옴
print(s1.difference(s2)) # 위의 결과랑 같음

s1.add(7) # 값을 추가한다.
s1.update([7,8,9,1]) # 여러개 값 추가
s1.remove(1) # 값을 삭제한다.

# 참과 거짓 boolean
a = True
a = False # 대문자로 써야함
"python"    = 참
[1,2,3]     = 참
"",[],(),{} = 거짓
 1          = 참
0           = 거짓
None        = 거짓

# 변수에 값을 넣는것이 아닌 주소를 넣는것임
a = [1,2,3]
b = a
a[1] = 4
print(a is b) # a랑 b가 주소값이 같은지 같으면 true
a = [1,2,3]
b = a[:] # 새로운게 따져서 들어간다 따라서 주소값이 다름
print(id(a)) # a의 주소를 보여줌

#이 방법으로도 값을 복사할수 있음
from copy import copy
a = [1,2,3]
b = copy(a)

# 튜플을 이용해서 각각 넣을 수 있음
a, b = ('python', 'life')
print(a)
print(b)

# 튜플을 이용해서 값을 서로 바꿀수 있음
a = 3
b = 5
a,b = b,a
