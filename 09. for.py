for wating_no in [0,1,2,3,4]:
    print("대기번호 : {0}" .format(wating_no))

# for waiting_no in range(5):
for waiting_no in range(1, 6):
    print("대기번호 : {0}" .format(waiting_no))

starbucks = ["아이언맨", "토르", "아이앰 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다." .format(customer))

# 튜플로 사용한 for
scores = { "수학":0, "영어":50, "코딩":100 }
for subject, score in scores.items():
    print(subject, score)


# 한 줄 for
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)


# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(s) for s in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [s.upper() for s in students]
print(students)

