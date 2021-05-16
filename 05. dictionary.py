# 사전에서는 키 중복 허용되지 않음
# 같은 값의 키로 추가하면 덮어 씌워지는 구조

cabinet = {3:"유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet.get(3))

# print(cabinet[5]) # 프로그램 종료됨 5라는 키 없기 때문에
print(cabinet.get(5)) # 값이 없어도 오류 출력 안함
print(cabinet.get(5, "사용가능")) # 값이 없으면 기본값 출력

print(3 in cabinet) # 3이라는 키가 캐비넷이 있으면 True

# 새 손님
str_cabinet = {"A-3":"유재석", "B-100": "김태호"}
print(str_cabinet)
str_cabinet["A-3"] = "김종국"
str_cabinet["C-20"] = "조세호"
print(str_cabinet)

# 간 손님
del str_cabinet["A-3"]
print(str_cabinet)

# key 들만 출력
print(str_cabinet.keys())
print(str_cabinet.values())
print(str_cabinet.items())

# 목욕탕 폐점
str_cabinet.clear()
print(str_cabinet)
