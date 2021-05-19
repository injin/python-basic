# 모듈은 확장자가 .py
# 모듈은 같은 경로에 있거나 파이썬 라이브러리 폴더에 있어야 사용 가능

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people*10000))

# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people*6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people*4000))



