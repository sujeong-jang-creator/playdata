#step04tourCrawler.py

'''
학습 방법
1. http://tour.interpark.com/ 사이트에서 '파리' 검색해 보기
2. 소스 실행 후 분석하기
3. 정규 표현식을 반영해 보기
    C:\0.ITStudy\99.제출폴더\10.crawling\181203_정규표현식으로변환해보기
'''

# pip install BeautifulSoup4
# pip install selenium
import time
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements

#검색 page가 로딩 되는 시간을 대기하기 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

main_url = "http://tour.interpark.com/"
keyword = "파리"

driver = webdriver.Chrome("C:/driver/chromedriver")
driver.get(main_url)
time.sleep(3)  # 절대적 : 무조건 정해진 시간(초) 쉬기
driver.implicitly_wait(10) # seconds

# 입력란 찾기 <input id="SearchGNBText" ... >
elem = driver.find_element_by_id("SearchGNBText")
elem.clear()
elem.send_keys(keyword)

# 동작 불가 왜? : 자바스크립트로 구현되어 있기 때문
# elem.submit() 

# 검색 버튼 찾기 <button class="search-btn" ... >
btn_search = driver.find_element_by_css_selector("button.search-btn")
btn_search.click()

driver.find_element_by_css_selector("div.oTravelBox > ul > li.moreBtnWrap > button").click()


driver.implicitly_wait(10) # seconds

# ? 불필요한 코드 정제해 보기
# boxitem밑에 칸 어떻게든 찾으면 나온다. 찾아라

try:
    for page in range(1, 6):
        print("============================== ", page)

        # <ul>
        #     <li class="active" role="button" tabindex="1">1</li>
        #     <li role="button" tabindex="2" onclick="searchModule.SetCategoryList(2, '')">2</li>
        #     <li role="button" tabindex="3" onclick="searchModule.SetCategoryList(3, '')">3</li>
        #     <li role="button" tabindex="4" onclick="searchModule.SetCategoryList(4, '')">4</li>
        #     <li role="button" tabindex="5" onclick="searchModule.SetCategoryList(5, '')">5</li>
        # </ul>


        # 자바스크립트 실행
        driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
        driver.implicitly_wait(15)
        print("{} 페이지로 이동!!!".format(page))

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 위치를 명확하게 정하려고 >표시를 사용한다.
        boxItems = soup.select(".panelZone > .oTravelBox > .boxList > .boxItem")
        # print(boxItems)
        # 순서대로 되있지는 않으므로 전체적으로 보고 찾아보자.
        for boxItem in boxItems: 
            print(boxItem)
            img_src = boxItem.find("img")['src']
            link = boxItem.find("a")['onclick']
            proTitle = boxItem.find("img")['alt']
            proComment = boxItem.find("p", {"class":"proSub"}).text

            # select 는 하나라도 리스트로 리턴
            proPrice = boxItem.select(".proPrice")[0].text
            proPrice = proPrice.replace(" ", "")
            # \n은 줄바꿈을 의미하는데,보면 가격이 앞뒤로 빈칸도 많고 줄바꿈도 한번 되있어서 앞뒤 공백과 빈칸을 없애기 위해 위에줄과 아래줄 실행한다.
            proPrice = proPrice.replace("\n", "")

            # proinfo가 boxitem아래에 여러 div에 분포되어있는데, 위에서 크게 boxitem으로 묶어서
            # 그 안에 proinfo 값들은 div상관없이 순서대로 0,1,2로 배정된다.
            tag_period = boxItem.select(".proInfo")[0]
            # proinfo 0번째 값을 보면 밑에 <span></span>이 포함되어있는데, 이를 없애기 위해서 아래를 실행한다.
            # span을 찾은다음에 이를 '', 즉 빈칸으로 대체한다는 의미이다.
            tag_period.find('span').replace_with('')  # <span> 태그 없애기
            # tag_period값이 ""도 포함하고 있으므로, 안에 텍스트 값만 뽑아내고자 새로 만든다.
            proPeriod = tag_period.text
            proJumsu = boxItem.select(".proInfo")[2].text

            print("썸네일=", img_src)
            print("링크=", link)
            print("상품명=", proTitle)
            print("코멘트=", proComment)
            print("가격=", proPrice)
            print("여행기간=", proPeriod)
            print("평점=", proJumsu)
            print("=" * 100)

except Exception as e:
    print("페이지 파싱 에러", e)
finally:
    time.sleep(3)
    # driver.close()

