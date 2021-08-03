## Python Summary
### #1 출력 관련
* 연결연산자(+) 대신 콤마(,)로도 문자열 연결할 수 있음. 이때는 str()로 자료형 치환하지 않아도 됨. 단, 스페이스 하나씩 붙음
* print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ") end 정의해서 print 끝날 때 줄바꿈 하지 않고 " "로 끝내겠다.
* print(lang1, lang2, lang3, lang4, lang5)
* print("Python", "Java", sep=",")
* 즉, 크게 세가지. 연결연산자(+) / 콤마(,) / .format()

### #2
* 문자열 연결 시 숫자가 있으면 str()로 형변환 하여 맞춰줄 것
* 형변환 => str(), int(), list(), set(), tupe(), type()
			print(variable, type(variable))
	
### #3 Java, JS와 비교
* 변수 지정 시 자료형 써주지 않음. var, let 없음
* 끝에 세미콜론 안붙임
* 다양한 자료형 리스트 안에 함께 사용 가능 (타입 엄격하지 않음)
* 줄바꿈은 역슬러시
    ```python
    print("이름 : {0}\t 나이:{1}\t 주 사용 언어: {2}" \
        .format(name, age, main_lang))
    ```
* 키워드값 이용해서 함수 매개변수 순서 조절 가능. 메소드 오버라이딩 필요 없음
    ```python
    profile(name="유재석", main_lang="파이썬", age=20)
    profile(main_lang="자바", age=25, name="김태호")
    ```
* 파이썬에서는 추가로 객체의 변수를 만들어 쓸 수 있음
* 다중상속 됨

### #4
    (name, age, hobby) = ("김종국", 20, "코딩")  
    print(name, age, hobby)

### #5 자료형 요약
    리스트: []  
	사전: { key1: value1, key2: value2 }
	튜플: ( value1, value2 )
	집합: { value1, value2 }


### #6
if 조건 예시  
* if 0 <= temp <10:
* if temp >= 10 and temp < 30:
* if student in absentArray:
* if weather == "비" or weather == "눈":
* while True:  
    line = score_file.readline()  
    if not line:

for 예시
* for number in range(1,6):
* students = [1, 2, 3, 4]  
    students = [i+100 for i in students]:

### #7
입력받기
```python
weather = input("오늘 날씨는 어때요?")
temp = int(input("기온은 어때요? "))
```
	
튜플로 반환하고 받기
```python
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 콤마로 구분해서 튜플로 반환
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다." .format(commission, balance))
```
	
가변인자
```python
def profile_star(name, age, *languages):
	for lang in languages
```

### #8 print관련
* print에 값을 여러 개 지정하면 한 줄에 모두 출력
* print에 값을 여러 개 지정하며 줄바꿈 하려면 sep="\n" 지정
* 일반 프린트는 자동으로 줄바꿈 됨
* 일반 프린트에서 줄바꿈 안하려면 end="" 지정


### #9 상속
``` python
class AttackUnit(Unit):
def __init__(self, name, hp, damage):
    Unit.__init__(self, name, hp)
    self.damage = damage


# super
# 다중 상속 받고 super 호출하면 마지막 클래스에 대해서만 생성자 호출됨
# BuildingUnit2(Unit1, Unit2) 이면
# Unit2의 생성자만 호출
super().__init__(name, hp, 0)  # self 없이 쓴다.
```

### #10 예외처리
```python
try:
    ~ 어쩌구 저쩌구 ~
    raise ValueError
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except:
    print("알 수 없는 에러가 발생하였습니다.")
```

### #11
	모듈 - 하나의 .py파일
	예) from [모듈] import *
	예) from [모듈] import [필요한 함수]
	예) from [모듈] import [필요한 함수] as [별명]
	예) from [패키지] import [모듈]
	예) import [모듈 또는 패키지] as [별명]
	
	from math import *
	from random import *
	import sys

	패키지 - 모듈들을 하나의 디렉토리에 모아둔 것
	예) import [패키지명].[모듈]
	__init__.py 파일 __all__
	__name__ 변수 사용하여 모듈 실행 위치 파악 (내부/외부)
