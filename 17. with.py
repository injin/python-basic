# with를 사용하여 close 안함

import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # 자동으로 close해줌


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


# (퀴즈) 주간보고서 자동 생성
for week in range(1, 4):
    with open(str(week) + "주차.txt", "w", encoding="utf8") as week_file:
        week_file.write("- {0} 주차 주간보고 -" .format(week))
        week_file.write("\n부서 : ")
        week_file.write("\n이름 : ")
        week_file.write("\n업무 요약 : ")