#*************조건문**********************
a = 'a'
if False or a :
    print("true")
else :
    print("false")


if 1 in[1,2,3]:
    print("true")
else :
    print("false")
    pass # 그냥 넘어감
# 불 자료형
# <, >, <=, >= ==, !=, and, or(|), not 뒤에거가 바뀜
# in, not in
# else if = elif
# 조건부 표현식 (3항 연산자)
# true일때 내용 if 조건식 else 내용
score = 90
message = "success" if score>=60 else "none"



# *******************반복문*************************
# while <조건문> : 
#     <수행할 문장1>
#     <수행할 문장2>
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    # a++ 불가능 a+=1까진 가능
    print("나무를 %d번 찍었습니다" % treeHit)
    continue
    if treeHit == 10:
        print("나무 넘어갑니다")
        break 

# for 변수 in 리스트(또는 튜플, 문자열) :
#  수행할 문장 1
#  수행할 문장 2
test_list = ['one', 'two','three']
for i in test_list :
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a :
    print(first + last)

marks = [90, 25, 67, 34, 21]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다."% number)

sum = 0 
for i in range(1,11) : #1~10까지 하나씩 빼서 담음
    print(i)
print(sum)


for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ") # end는 마지막에 end가 이어져서 나옴
    print(" ")


# 제어문을 이런식으로도 쓸수가 있음 생성과 동시에
line = [1,2,3,4]
result = [text*3 for text in line if text%2==0]
print(result)
# 위에것에과 같음
result = []
for text in line:
    if text%2==0:
        result.append(text%3)
print(result)