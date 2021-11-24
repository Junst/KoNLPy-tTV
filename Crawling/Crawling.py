from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36')
options.add_argument('window-size=1920x1080')
options.add_argument('ignore-certificate-errors')


import os
import time
import socket

from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from PIL import Image
from pygame import mixer

from urllib.error import HTTPError, URLError
from selenium import webdriver

chromedriver = 'C://chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
socket.setdefaulttimeout(30)
date = "2021.11.24"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
                print ('Error: Creating directory. ' + directory)


def scroll_down(keyword):
    print(keyword + ' 스크롤 중 .............')
    elem = driver.find_element_by_tag_name("body")
    for i in range(10):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[4]/div[2]/input').click()

        for i in range(10):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
    except:
        pass


def click_and_retrieve(keyword, index, img, img_list_length):
    global crawled_count
    try:
        img.click()
        time.sleep(1.5)
        driver.implicitly_wait(3)
        src = None
        _format = None
        try:
            srces = driver.find_elements_by_class_name("""n3VNCb""")
            for _src in srces:
                src = _src.get_attribute('src')
                _format = src.split('.')[-1]
                if any(map(lambda x: _format == x, ['jpg', 'jpeg', 'png'])):
                    break
                else:
                    continue
            if not any(map(lambda x: _format == x, ['jpg', 'jpeg', 'png'])):
                print('no jpg.... pass.')
                return
        except:
            print('error2')
        # src.split('.')[-1] = 확장자
        if src is None or _format is None:
            return
        urlretrieve(src, f"{keyword}/{date}/{crawled_count + 1}.{_format}")
        driver.implicitly_wait(3)
        print(f"{index + 1} / {img_list_length} 번째 사진 저장 (png)")
        crawled_count += 1

    except HTTPError:
        print("ㅡ HTTPError & 패스 ㅡ")
        pass


def crawling(keyword):
    global crawled_count
    print("ㅡ 크롤링 시작 ㅡ")

    # 크롤링할 이미지 수
    crawled_count = 100

    # 이미지 고급검색 중 이미지 유형 '사진'
    url = f"https://www.google.com/search?as_st=y&tbm=isch&hl=ko&as_q={keyword}&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=itp:photo"
    driver.get(url)
    # driver.maximize_window()
    scroll_down(keyword)

    div = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]')
    # class_name에 공백이 있는 경우 여러 클래스가 있는 것이므로 아래와 같이 css_selector로 찾음
    img_list = div.find_elements_by_css_selector(".rg_i.Q4LuWd")
    os.makedirs(os.path.join(keyword, date), exist_ok=True)
    print(f"ㅡ {keyword}/{date} 생성 ㅡ")

    for index, img in enumerate(img_list):
        try:
            click_and_retrieve(keyword,index, img, len(img_list))

        except ElementClickInterceptedException:
            print("ㅡ ElementClickInterceptedException ㅡ")
            driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
            print("ㅡ 100만큼 스크롤 다운 및 3초 슬립 ㅡ")
            img.click()
            time.sleep(3)
            click_and_retrieve(keyword,index, img, len(img_list))

        except NoSuchElementException:
            print("ㅡ NoSuchElementException ㅡ")
            driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
            print("ㅡ 100만큼 스크롤 다운 및 3초 슬립 ㅡ")
            time.sleep(3)
            img.click()
            click_and_retrieve(keyword,index, img, len(img_list))

        except ConnectionResetError:
            print("ㅡ ConnectionResetError & 패스 ㅡ")
            pass

        except URLError:
            print("ㅡ URLError & 패스 ㅡ")
            pass

        except socket.timeout:
            print("ㅡ socket.timeout & 패스 ㅡ")
            pass

        except socket.gaierror:
            print("ㅡ socket.gaierror & 패스 ㅡ")
            pass

        except ElementNotInteractableException:
            print("ㅡ ElementNotInteractableException ㅡ")
            break

    try:
        print("ㅡ 크롤링 종료 (성공률: %.2f%%) ㅡ" % (crawled_count / len(img_list) * 100.0))

    except ZeroDivisionError:
        print("ㅡ img_list 가 비어있음 ㅡ")

    driver.quit()


def filtering(keyword):
    print("ㅡ 필터링 시작 ㅡ")
    filtered_count = 0
    dir_name = os.path.join(keyword, date)
    for index, file_name in enumerate(os.listdir(dir_name)):
        try:
            file_path = os.path.join(dir_name, file_name)
            img = Image.open(file_path)

            # 이미지 해상도의 가로와 세로가 모두 350이하인 경우
            if img.width < 351 and img.height < 351:
                img.close()
                os.remove(file_path)
                print(f"{index} 번째 사진 삭제")
                filtered_count += 1

        # 이미지 파일이 깨져있는 경우
        except OSError:
            os.remove(file_path)
            filtered_count += 1

    print(f"ㅡ 필터링 종료 (총 갯수: {crawled_count - filtered_count}) ㅡ")


def checking(keyword):
    # 입력 받은 검색어가 이름인 폴더가 존재하면 중복으로 판단
    for dir_name in os.listdir(keyword):
        file_list = os.listdir(os.path.join(keyword, dir_name))
        if keyword in file_list:
            print(f"ㅡ 중복된 검색어: ({dir_name}) ㅡ")
            return True


def playing_mp3(keyword):
    # mp3 = "Mococo_Seed.mp3"
    # mixer.init()
    # mixer.music.load(mp3)
    # mixer.music.play()
    # while mixer.music.get_busy():
    #     pass
    print(f"ㅡ 검색어: {keyword} ㅡ")

#
# crawling()
# filtering()
# playing_mp3()
