from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import subprocess
import pyautogui


# ブラウザを開く。
driver = webdriver.Chrome()
host_url = "https://kabuoji3.com/stock/"#確定のurl

for name in range(4093,10000):
    era_name = 2018
    pyautogui.moveTo(20, 30, 0.5)
    pyautogui.moveTo(10, 20, 0.5)
    while 1:
        url = host_url + str(name) + "/" + str(era_name) + "/"
        driver.get(url)
        element=driver.find_elements_by_xpath('//button[@class="btn_form btn_download"]')#その要素があるか確認する
        if len(element)==0:#要素がなかったら終わり
            if not era_name == 2018:
                cmd = "mkdir ~/Desktop/kabu/" + str(name) + " | mv ~/Downloads/*.csv ~/Desktop/kabu/" + str(name) + "/"
                subprocess.call(cmd, shell=True)
            break
        else:
            driver.find_element_by_xpath('//button[@class="btn_form btn_download"]').click()#ダウンロードページへ移動
            sleep(2)
            driver.find_element_by_xpath('//button[@class="btn_form btn_download"]').click()#クリックしてダウンロード
            sleep(1)
        era_name -=1

# ブラウザを終了する。
driver.close()
