# <1> 숫자형 자료형
print(5)
print(-10)
print(5+3)

# <2> 문자형 자료형
print("ㅋ"*10)

# <3> boolean 자료형
print(5<10)
print(True)
print(not True)

# <4> 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집" + animal + "의 이름은 " + name + "예요")
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요.")
print(name + "는 어른일까요? " + str(is_adult))


# <5> 연산자
print(2**3) # 2^3=8
print(5%3) # 나머지 구하기 2
print(5//2) # 몫 구하기 1
print(3==3) # True
print(3+4 == 7) # True

print((3 > 0) and  (3 < 5)) # True
print((3 > 0) &  (3 < 5)) # True
print((3 > 0) or  (3 < 5)) # True
print((3 > 0) |  (3 < 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False


# <6> 숫자처리함수
print(abs(-5)) # 5
print(pow(4,2)) # 4^2 = 4*4 = 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.12)) # 3

from math import * # math 라이브러리 사용
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근 4


# <7> 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# <7-1> 문자열 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7]) # 인덱스 0부터 시작
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지 (2,4)
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# <7-2> 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # (1) 소문자
print(python.upper()) # (2) 대문자
print(python[0].isupper()) # (3) 대문자여부
print(len(python)) # (4) 글자수
print(python.replace("Python", "Java")) # (5) 문자열치환

index = python.index("n") # (6) 인덱스
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("Java")) # (7) find. 원하는 값 없으면 -1 반환
#print(python.index("Java")) # 원하는 값 없으면 에러 반환
print(python.count("n")) # (8) count. n이 총 몇번 출현하는지




















