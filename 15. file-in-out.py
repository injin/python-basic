# 파일 입출력 방식1
score_file = open("score.txt", "w", encoding="utf8") # w는 쓰기 용도
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 파일 입출력 방식2
score_file = open("score.txt", "a", encoding="utf8") # a는 계속 쓰겠다. append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()


# 파일 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


# 줄별로 파일 읽기. 한 줄 읽고 커서는 다음 줄로 이동
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()


# 줄별로 파일 읽기. 몇 줄 인지 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 리스트에 값을 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")


