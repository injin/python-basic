# 다른 사람들이 만든 패키지를 잘 활용할 것
# https://pypi.org/
# 예) 웹 스크래핑 beautifulsoup 라이브러리
#     => pip install beautifulsoup4

# pip list 명령어
#   =>로 현재 설치된 패키지 확인
# pip show [패키지명]
#   => 패키지 정보 확인
# pip install --upgrade [패키지명]
# pip uninstall [패키지명]

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


