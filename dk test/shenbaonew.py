# -*- coding:utf-8 -*-

# @Created by PyCharm_python-study_health shenbao.py
# @Author: shmily-ing
# @Data: 2022/5/11 0:31
# selenium version 3.8.0

import requests
import datetime

import os
import smtplib
import pyautogui
from email.mime.text import MIMEText
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with open('C:\\Users\\Administrator\\Desktop\\dk\\myInfo.txt', 'r') as f:
    # 个人账号信息封装在myInfo.txt文件中，其中依次存放账号、密码信息（用空格分开）
    myInfo = f.read()
    myInfo = myInfo.split()
    print()


def write(x):
    f = open("result.txt", "a")
    f.write('\n' + x)
    f.close


def checkIn(i):
    driver = webdriver.Chrome(
        executable_path=r'C:\\Users\\Administrator\\Desktop\\dk\\chromedriver_win32\\chromedriver.exe')
    driver.get("http://ehall.jit.edu.cn/new/index.html")
    print("加载“我的金科院”页面成功！")
    # 打开Chrome浏览器并进入我的金科院首页  注：需下载webdriver（Chrom版）放在Chrom根目录下，MacOS放在Python根目录下

    driver.maximize_window()
    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    try:
        WebDriverWait(driver, 800).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".amp-no-login-zh")))
    finally:
        sleep(2)
    # driver.find_element_by_css_selector("#ampHasNoLogin").click()
    driver.find_element_by_xpath('//*[@id="ampHasNoLogin"]/span[1]').click()
    # 等待首页的登录按钮加载完成后点击登录按钮

    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    print("加载登录页面成功!")

    # driver.find_element_by_id("username").clear()
    # driver.find_element_by_id("password").clear()
    driver.find_element_by_id("username").send_keys(myInfo[2 * i - 2])
    # sleep(1)
    driver.find_element_by_id("password").send_keys(myInfo[2 * i - 1])
    sleep(1)
    driver.find_element_by_css_selector(".ipt_btn_dl").click()
    # 进入登录界面后填写用户名和密码并点击登录
    sleep(1)

    now_handle = driver.current_window_handle
    print("加载“学生桌面”页面成功!")
    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(5)
    ##cardMyFavoriteContent > div > widget-app-item:nth-child(2) > div > div > div.widget-information.style-scope.pc-card-html-4786696181711234-01 > div
    ##cardMyFavoriteContent > div > widget-app-item:nth-child(1) > div > div > div.widget-information.style-scope.pc-card-html-4786696181711234-01 > div
    driver.find_element_by_css_selector(
        "#cardMyFavoriteContent > div > widget-app-item:nth-child(1) > div > div > div.widget-information.style-scope.pc-card-html-4786696181711234-01 > div").click()

    # 成功进入学生桌面后等待“健康信息填报系统”按钮加载完成，加载完成后点击它进入打卡页面
    windos = driver.window_handles
    driver.switch_to.window(windos[-1])
    # 切换到新打开的打卡页面窗口
    print("加载“信息填报”页面成功!")
    now_handle = driver.current_window_handle
    try:

        WebDriverWait(driver, 800).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bh-mb-16 > .bh-btn-primary")))
    finally:
        sleep(1)
    sleep(2)
    # driver.find_element_by_css_selector(".bh-mb-16 > .bh-btn-primary").click()
    driver.find_element_by_css_selector(
        "body > main > article > section > div.bh-mb-16 > div.bh-btn.bh-btn-primary").click()
    # 等待“新增”按钮加载完成，加载完成后点击“新增”按钮
    print("点击“新增”按钮")
    sleep(1)

    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(2)

    # 判断是否已经打卡过

    try:
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[13]/div[1]/div[1]/div[2]/div[1]/div")

        # 如果点击“新增”按钮时弹出已填报的对话框说明已经打卡过了。
        print(myInfo[2 * i - 2] + "今日已打卡！无需再次打卡！")
        write(str(i) + "   :    " + myInfo[2 * i - 2] + "今日已打卡！无需再次打卡！")
        # sentEmail()
        # shutdown()
        driver.quit()
        return
    except:
        print("今日还未打卡！开始打卡!")

    sleep(7)

    driver.find_element_by_css_selector("#buttons > button.bh-btn.bh-btn-primary.bh-pull-right").click()
    sleep(2)

    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(1)
    driver.execute_script('window.scrollBy(0,2000)')
    # 异常

    sleep(0.5)

    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[6]/div[1]/div/div[2]/div/div/div[1]").click()
    sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[22]/div/div/div/div[1]/input').send_keys('无')
    sleep(0.7)

    driver.find_element_by_xpath("/html/body/div[22]/div/div/div/div[2]/div/div[1]/span").click()

    # 江苏
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[1]").click()
    sleep(0.7)
    driver.find_element_by_xpath('/html/body/div[17]/div/div/div/div[1]/input').send_keys('江苏')
    sleep(0.7)
    driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[2]/div/div[1]/span").click()

    # 南京
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div[1]").click()
    sleep(1)

    driver.find_element_by_xpath("/html/body/div[18]/div/div/div/div[2]/div/div[2]/span").click()
    sleep(1)

    # 区域
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div").click()
    sleep(1)

    # 建业

    # driver.find_element_by_xpath("/html/body/div[19]/div/div/div/div[2]/div/div[4]/span").click()

    # 玄武区
    driver.find_element_by_xpath("/html/body/div[19]/div/div/div/div[2]/div/div[2]/span").click()

    # 位置
    sleep(0.5)
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div[1]").click()
    sleep(0.5)

    driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[2]/div/div[5]/span").click()

    # 状态
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[5]/div/div/div[2]/div/div/div[1]").click()
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[21]/div/div/div/div[2]/div/div[5]/span").click()
    # 核酸
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[7]/div/div/div[2]/div/div/div[1]").click()
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[23]/div/div/div/div[2]/div/div[3]/span").click()
    # 疫苗
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[8]/div/div/div[2]/div/div/div[1]").click()
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[24]/div/div/div/div[2]/div/div[2]/span").click()

    # 住址
    sleep(1)
    if driver.find_element_by_xpath('/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[11]/div[1]/div/div[2]/div/div/div[1]/span').text == '请选择...':
        driver.find_element_by_xpath(
            "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[10]/div[1]/div/div[2]/div/div/div[1]").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[26]/div/div/div/div[2]/div/div[1]/div/div/div/span").click()

    # 健康马
    sleep(2)
    driver.find_element_by_xpath(
        "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[9]/div/div/div[2]/div/div/div[1]").click()
    sleep(1)

    driver.find_element_by_xpath("/html/body/div[25]/div/div/div/div[2]/div/div[2]/span").click()
    # 漫游
    sleep(1)
    if driver.find_element_by_xpath('/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[11]/div[1]/div/div[2]/div/div/div[1]/span').text == '请选择...':
        driver.find_element_by_xpath(
            "/html/body/div[13]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[11]/div[1]/div/div[2]/div/div/div[1]").click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[27]/div/div/div/div[1]/input').send_keys('江苏省/南京市/江宁区')
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[27]/div/div/div/div[2]/div/div[1]/div/div/div/span").click()

    # 保存
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[13]/div/div[2]/footer/div").click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[41]/div[1]/div[1]/div[2]/div[2]/a[1]").click()
    # sleep(1)
    # driver.find_element_by_css_selector("body > main > article > section > div.bh-mb-16 > div.bh-btn.bh-btn-primary").click()
    # sleep(2)

    write(str(i) + "   :    " + myInfo[2 * i - 2] + "今日完成打卡！")
    sleep(1)
    driver.quit()


if __name__ == '__main__':
    tim = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    write(str(tim))
    for i in range(int(len(myInfo) / 2)):
        print(i + 1)
        checkIn(i + 1)

    try:
        os.system("taskkill /f /im chromedriver.exe /t")  # 清除占用资源放在卡顿
    except:
        pass





