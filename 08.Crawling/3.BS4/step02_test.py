html='''<!DOCTYPE html>
<html lang="ko">
<body>
  <div id="main-goods" role="page">
      <h1>과일과 야채</h1>
      <ul id="fr-list">
        <li class="red green" data-lo="ko">사과</li>
        <li class="purple" data-lo="us">포도</li>
        <li class="yellow" data-lo="us">레몬</li>
        <li class="yellow" data-lo="ko">오렌지</li>
      </ul>
      <ul id="ve-list">
        <li class="white green" data-lo="ko">무</li>
        <li class="red green" data-lo="us">파프리카</li>
        <li class="black" data-lo="ko">가지</li>
        <li class="black" data-lo="us">아보카도</li>
        <li class="white" data-lo="cn">연근</li>
      </ul>
  </div>
<body>
</html>'''

'''
어떻게 하면 동일한 결과로 크롤링 가능한지?
https://www.w3schools.com/cssref/css_selectors.asp

레몬
아보카도
파프리카
아보카도
아보카도
아보카도
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# [<li class="yellow" data-lo="us">레몬</li>, <li class="yellow" data-lo="ko">오렌지</li>]
# print(soup.html.select(".yellow"))

# <li class="yellow" data-lo="us">레몬</li>
# print(soup.html.select(".yellow")[0])

# 레몬
# print(soup.html.select(".yellow")[0].string)
# print(soup.html.select(".black")[1].string)
print(soup.html.select(".red green"))
# print(soup.html.select(".black")[1].string)
# print(soup.html.select(".black")[1].string)
# print(soup.html.select(".black")[1].string)






