from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd


chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('http://data.eastmoney.com/report/industry.jshtml')

path = '''
        /html/body/div[@class='main']/div[@class='main-content']/div[@class='framecontent']/div[@id='industry_table']/table[@class='table-model']/tbody/tr[{}]/td[{}]
       '''
dic = ['行业名称', '涨跌幅', '报告名称','评级类型', '评级变动', '机构名称']
df = pd.DataFrame([dic])
df.to_csv('eastmoney_info.csv', header=None, index=None,encoding='gbk')

def get_info(i):
    for j in range(1, 51):
        col = [driver.find_element_by_xpath(path.format(j, t)).text for t in [2,3,5,6,7,8]]
        df = pd.DataFrame([col])
        df.to_csv('eastmoney_info.csv', header=None, index=None,mode='a', encoding='gbk')


for i in range(10):
    if i == 0:
        get_info(i)
        driver.find_element_by_xpath("/html/body/div[@class='main']/div[@class='main-content']/div[@class='framecontent']/div[@id='industry_table_pager']/div[@class='pagerbox']/a[8]").click()
    else:
        get_info(i)
        driver.find_element_by_xpath("/html/body/div[@class='main']/div[@class='main-content']/div[@class='framecontent']/div[@id='industry_table_pager']/div[@class='pagerbox']/a[9]").click()

driver.quit()

