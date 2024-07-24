from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options)

Email = os.environ.get('Email')
Pass = os.environ.get('Pass')

driver.get("https://www.iios.me/#/login")
sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/input").send_keys(Email)
sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/input").send_keys(Pass)
sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/button").click()
sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div").click()
sleep(2)

LoginStatus = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/div[3]").text
if LoginStatus == "已完成":
    print("登录任务完成")
    pass
else:
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/div[3]").click()
    print("登录成功")
    sleep(2)

WatchStatus = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[3]").text
if WatchStatus is not "立即观看":
    print("观看完成")
    pass
else:
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[3]").click()
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, "/html/body/div/div/div[6]").click()
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div[3]/textarea").send_keys("禁止分享账号密码，如果别人不看教程导致手机被锁，后果自己承担，邀请好友来注册获取账号，可获得积分奖励")
    sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[2]/div[3]/textarea").send_keys("账号只能在AppStore商店登录，禁止在手机设置里登录，否则导致手机被锁后果自己承担")
    sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/div[3]/textarea").send_keys("登录弹窗提示升级应该选择其他选项>不升级")
    sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[4]/div[3]/textarea").send_keys("付费的游戏应该在家庭购买项目中的下载通道里下载")
    sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/button").click()
    sleep(1)

driver.close()