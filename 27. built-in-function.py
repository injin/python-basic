# 내장함수 : import 하지 않고도 바로 사용 가능한 함수 
# 구글에서 "list of python built in"으로 검색

language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())
import pickle
print(dir())
print(dir(random))

