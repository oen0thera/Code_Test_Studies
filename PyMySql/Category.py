'''
Main/Sub Category + 상품 정보 + 상품 코드 + 판매자(제공자) 크롤링
'''

import pymysql
import requests
import re
from bs4 import BeautifulSoup


def get_category(category_link,category_name):
    res = requests.get(category_link,category_name)
    soup = BeautifulSoup(res.content,'html.parser')
    get_items(soup,category_name,'ALL')

    sub_categories =soup.select('div.gbest-cate ul.by-group li> a')
    #li바로 밑에 a가 있는 것만 추출

    for sub_category in sub_categories:
        res = requests.get('http://corners.gmarket.co.kr/'+sub_category['href'])
        soup = BeautifulSoup(res.content,'html.parser')
        get_items(soup,category_name,sub_category.get_text())

def get_items(html,category_name,sub_category_name):
    items_result_list = list()
    best_item = html.select('div.best-list')
    for index, item in enumerate (best_item[1].select('li')):
        data_dict = dict()
        title = item.select_one('a.itemname')
        ranking = index + 1
        ori_price = item.select_one('div.o-price')
        dis_price = item.select_one('div.s-price strong span')
        discount_percent = item.select_one('div s-price em')
        if ori_price == None or ori_price.get_text() == '':
            ori_price = dis_price
        if dis_price == None:
            ori_price, dis_price =0,0
        ori_price = ori_price.get_text().replace('.','').replace('원','')
        dis_price = dis_price.get_text().replace('.','').replace('원','')
        if discount_percent==None or discount_percent.get_text()=='':
            discount_percent=0
        else:
            discount_percent = discount_percent.get_text().replace('%','')

        product_link = item.select_one('div.thumb>a')
        item_code = product_link.attrs['href'].split('=')[1]

        res = requests.get(product_link.attrs['href'])
        soup = BeautifulSoup(res.content,'html.parser')
        provider = soup.select_one('div.item-topinfo_headline>p>a>strong')
        if provider == None:
            provider = ''
        else:
            provider = provider.get_text()
        data_dict['category_name'] = category_name
        data_dict['sub_category_name'] = sub_category_name
        data_dict['ranking'] = ranking
        data_dict['title'] = title.get_text()
        data_dict['ori_price'] = re.sub(r'[^0-9]','',ori_price)
        data_dict['dis_price'] = re.sub(r'[^0-9]','',dis_price)
        data_dict['discount_percent'] = discount_percent
        data_dict['item_code'] = re.sub(r'[^0-9]','',item_code)
        data_dict['provider'] = provider

        save_data(data_dict)
        #print(category_name,sub_category_name,ranking,item_code,provider,title.get_text(),ori_price,dis_price,discount_percent,product_link)

res= requests.get('http://corners.gmarket.co.kr/BestSellers')
soup = BeautifulSoup(res.content,'html.parser')
categories = soup.select('div.gbest-cate ul.by-group li a')


db = pymysql.connect(host='localhost',port=3306,user='oenothera',passwd='mint',db='newdb',charset='utf8')
cursor=db.cursor()
cursor.execute('use mysql')
cursor.execute('use newdb')
cursor.execute('show tables')
dt = cursor.fetchall()
print(dt)

ranking_Table = '''CREATE TABLE ranking(
    num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    main_category VARCHAR(20) NOT NULL,
    sub_category VARCHAR(20) NOT NULL,
    item_ranking INT NOT NULL,
    item_code VARCHAR(100) NOT NULL,
    FOREIGN KEY(item_code) REFERENCES items(item_code)
);'''

item_Table = '''CREATE TABLE items(
    item_code VARCHAR(100) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    ori_price INT NOT NULL,
    dis_price INT NOT NULL,
    discount_percent INT NOT NULL,
    provider VARCHAR(100)
);'''
cursor.execute(item_Table)
cursor.execute(ranking_Table)

cursor.execute('SHOW TABLES')
def save_data(item_info):
    cursor = db.cursor()
    sql = """ SELECT COUNT(*) FROM items WHERE item_code ="""+item_info['item_code']+""";"""
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result[0])
    if result[0]==0:
        sqls = ("INSERT INTO items"
            "(item_code,title,ori_price,dis_price,discount_percent,provider)"" VALUES(%(item_code)s,%(title)s,%(ori_price)s,%(dis_price)s,%(discount_percent)s,%(provider)s)")
        cursor.execute(sqls,item_info)


    sql = """ INSERT INTO ranking (main_category, sub_category,item_ranking, item_code) VALUES('
        """+ item_info['category_name']+"""','"""+item_info['sub_category_name']+"""',
        '"""+str(item_info['ranking'])+"""' ,
        '"""+item_info['item_code']+"""')"""
    cursor.execute(sql)
    print(item_info)
    dt=cursor.fetchall()
    print(dt)
    db.commit()
    print('done')

for category in categories:
    get_category('http://corners.gmarket.co.kr/'+category['href'],category.get_text())

cursor.execute('select*from items')
dt=cursor.fetchall()
print(dt)
db.commit()

###COUNT SQL
'''
-COUNT: 검색결과의 row 수를 가져올 수 있는 SQL문법
-SQL 예제: SELECT COUNT(*) FROM items
'''

'''
-GROUP BY : 그룹을 지어서 데이터를 분석하고자 할 때 사용
-COUNT,SUM,AVG,MAX,MIN 함수와 함께 사용하면 각 그룹별 row수, 합계, 평균, 최댓값, 최솟값등을 알 수 있음
-SQL 예제: SELECT AVG(age) FROM people GROUP BY gender
'''

'''
-DISTINCT
    - 특정 컬럼값 출력시 중복된 값 출력 x
    - SQL 예제: SELECT DISTINCT gender FROM People
'''

'''
AS
- 특정 결과값의 이름을 변경하는 방법
- 예: COUNT("")를 total_count로 이름을 변경
    - SELECT COUNT("") AS total_count
'''

'''
HAVING
- HAVING 절은 집계함수를 가지고 조건비교를 할 때 사용한다.
- HAVING절은 GROUP BY 절과 함께 사용
- 예
    - SELECT provider FROM items GROUP BY provider HAVING COUNT(*) >=100

- HAVING절을 포함한 복합검색
    SELECT provider, COUNT(*)
        FROM items
        WHERE provider != '스마일배송'       --스마일배송 제외
        GROUP BY provider                    --판매처별로 그룹
        HAVING COUNT(*)>100                  --베스트 상품이 100개 이상 등록된 경우만 검색
        ORDER BY COUNT(*) DESC               --베스트 상품 등록개수 순으로 검색
'''

'''
JOIN
- JOIN은 두개 이상의 테이블로부터 필요한 데이터를 연결해 하나의 포괄적인 구조로 결합시키는 연산
- JOIN은 다음과 같이 세분화될 수 있지만 보통은 INNER JOIN을 많이 사용함
    -INNER JOIN(일반적인 JOIN): 두 테이블에 해당 필드값이 매칭되는 (두 테이블의 모든 필드로 구성된) 레코드만 가져옴
    -OUTER JOIN(참고)
        - LEFT OUTER JOIN: 왼쪽 테이블에서 모든 레코드와 함께, 오른쪽 테이블에 왼쪽 테이블 레코드와 매칭되는 레코드를 가져옴
        - RIGHT OUTER JOIN: 오른쪽 테이블에서 모든 레코드와 함께, 왼쪽 테이블에 오른쪽 테이블 레코드와 매칭되는 레코드를 가져옴
'''

'''
INNER JOIN
- INNER JOIN은 조인하는 테이블의 ON절의 조건이 일치하는 결과만 출력
- 사용법: FROM 테이블1 INNER JOIN 테이블2 ON 테이블1과 테이블2의 매칭조건
    SELECT * FROM items: INNER JOIN ranking ON ranking.item_code = items.item_code WHERE ranking.main_category = "ALL"
- 테이블 이름 다음에 한칸 띄고 새로운 이름을 쓰면, SQL 구문안에서 해당 이름으로 해당 테이블을 가리킬 수 있음 (AS 용법과 동일함)
    일반적으로 이와 같이 많이 사용됨
    SELECT * FROM items a INNER JOIN ranking b ON a.item_code = b.item_code WHERE b.main_category="ALL"
'''
