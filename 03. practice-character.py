# ======== 문자열 포맷 ========
# 방법 1
print("나는 %d살입니다." % 20) # d는 정수
print("나는 %s을 좋아해요" % "파이썬") # s는 문자열
print("Apple은 %c로 시작해요." % "A") # c는 캐릭터

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))


# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# ======== 탈출문자 ========
# \n : 줄바꿈
print("백문이 불여일견 \n 백견이 불여일타")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\injin\\")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple")

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))

