# ====== 함수 ======
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다." .format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 콤마로 구분해서 튜플로 반환


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다." .format(commission, balance))


# ====== 기본값 ======
def profile(name, age, main_lang):
    print("이름 : {0}\t 나이:{1}\t 주 사용 언어: {2}" \
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업이라면
def profile2(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이:{1}\t 주 사용 언어: {2}" \
        .format(name, age, main_lang))
profile2("유재석")
profile2("김태호")


# ====== 키워드값 ======
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")


# ====== 가변인자 ======
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ") # end 정의해서 print 끝날 때 줄바꿈 하지 않고 " "로 끝내겠다.
    print(lang1, lang2, lang3, lang4, lang5)

def profile_star(name, age, *languages):
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
    for lang in languages:
        print(lang, end=" ")
    print()

profile_star("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile_star("김태호", 25, "Kotlin", "Swift")