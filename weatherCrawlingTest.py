# beautifulsoup4 설치
# requests 설치

import requests

from bs4 import  BeautifulSoup
# area = "한남동"
area = input("날씨를 입력하세요: ")

weather_html = requests.get(f"https://search.naver.com/search.naver?&query={area}날씨")

#print(weather_html.text)

weather_soup = BeautifulSoup(weather_html.text, "html.parser")

area_text = weather_soup.find("h2", {"class":"title"}).text #현재 날씨가 보여지고 있는 지역
print(f"---{area_text} 날씨---")

today_temperature = weather_soup.find("div", {"class" : "temperature_text"}).text
today_temperature = today_temperature[6:11]
print(f"* 현재 온도 : {today_temperature}")


a = weather_soup.find("span", {"class":"weather before_slash"}).text
    #weathr_soup.find("태그명", {"class":"클래스명"}).text
print(f"* 오늘 날씨 : {a}")

yesterdaty_weathertest = weather_soup.find("p", {"class":"summary"}).text # 어제 온도와 현재온도의 비교
yesterdaty_weathertest = yesterdaty_weathertest[:13].strip()
# 총 13글자를 가져온 후 strip으로 양쪽의 공백제거 후 저장
print(f"* {yesterdaty_weathertest}")

sense_temperature = weather_soup.find('div',{'class':'weather_info'}).find('dl',{'class':'summary_list'}).find('dd',{'class':'desc'}).text
# <div> 태그 중 클래스가 weather_info 인 div 태그 안에 있는 dl 태그 중 클래스가 summary_list인 dl을 찾음
# dl 태그 안에 있는 dd 태그 중 클래스가 desc 인 태그를 찾아 텍스트 값을 반환
print(f"* 체감온도 : {sense_temperature}")

dust_info = weather_soup.select("ul.today_chart_list>li")
#print(dust_info)
dust1_info = dust_info[0].find("span", {"class":"txt"}).text # 미세먼지 정보
print(f"* 미세 먼지 : {dust1_info}")
dust2_info = dust_info[1].find("span", {"class":"txt"}).text # 초미세먼지 정보
print(f"* 초미세 먼지 : {dust2_info}")

# 지역명, 현재온도, 전일온도차, 날씨, 체감온도, 미세먼지, 초미세먼지