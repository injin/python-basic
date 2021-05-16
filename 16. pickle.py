# 피클이란 데이터를 파일 형태로 저장해주는 라이브러리
# 피클에서는 항상 바이너리 타입을 지정해 줘야함 예) wb - 쓰기+바이너리
# 인코딩 따로 지정해 줄 필요 X
import pickle
profile_file = open("profile.pickle", "wb")
profile = { "이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()


# 프로필 파일 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()