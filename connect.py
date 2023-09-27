from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import pyperclip
# from selenium.webdriver.support.ui import Select
import time
import datetime

form_class = uic.loadUiType("interpark.ui")[0]

#화면을 띄우는데 사용되는 class선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #QT Designer 객체 연결하기
        self.actioninterpark:QWidgetAction
        self.pushButton:QPushButton
        self.lineEdit:QLineEdit
        self.lineEdit_2:QLineEdit
        self.dateEdit:QDateEdit
        self.pushButton3:QPushButton

        # #메뉴바에 기능을 할당하는 코드
        # self.actioninterpark.triggered.connect(self.move_interpark)

        #버튼에 기능을 할당하는 코드
        self.pushButton.clicked.connect(self.login_btn)
        self.pushButton_3.clicked.connect(self.open_btn)
        # # 공연일자 입력란에 오늘 날짜를 기본으로 입력
        # self.dateEdit.setDate(self,str(datetime.date.today()))

    #크롬 드라이버 열기 함수
    def open_btn(self):
        service = Service()
        global driver
        driver = webdriver.Chrome(service=service)
        driver.set_window_size(1400, 1000)  # (가로, 세로)
        driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login&GPage=https%3A%2F%2Ftickets.interpark.com')

    #인터파크에 로그인 하는 함수
    def login_btn(self):

        id = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        show_num = str(self.lineEdit_3.text())

        #로그인
        driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/iframe"))
        self.userId = driver.find_element(By.ID, 'userId')
        self.userId.send_keys(id) # 로그인 할 계정 id
        self.userPwd = driver.find_element(By.ID, 'userPwd')
        self.userPwd.send_keys(pw) # 로그인 할 계정의 패스워드
        self.userPwd.send_keys(Keys.ENTER)
        time.sleep(0.3)

        #해당 공연으로 이동
        driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + show_num)
        time.sleep(0.2)

        #예매하기 버튼 클릭
        driver.find_element(By.XPATH, "//*[@id=\"productSide\"]/div/div[2]/a[1]").click()

        # 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
        driver.switch_to.window(driver.window_handles[1])
        driver.get_window_position(driver.window_handles[1])

       # 예매안내가 팝업이 뜨면 닫기. ( ticketingInfo_check : True, False )
        ticketingInfo_check = self.check_exists_by_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']")
        if ticketingInfo_check:
            driver.find_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']").click()
    # #예약정보 입력(예매하기)버튼 함수
    # def reservation_btn(self):





if __name__ == "__main__":
    #QApplication 실행 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec()


# service = Service()
# driver = webdriver.Chrome(service=service)
#
# # 사이즈조절
# driver.set_window_size(1400, 1000)  # (가로, 세로)
# driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login&GPage=https%3A%2F%2Ftickets.interpark.com')
#
# #로그인
# driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/iframe"))
# userId = driver.find_element(By.ID, 'userId')
# userId.send_keys('chuncool') # 로그인 할 계정 id
# userPwd = driver.find_element(By.ID, 'userPwd')
# userPwd.send_keys('dildil1129^^') # 로그인 할 계정의 패스워드
# userPwd.send_keys(Keys.ENTER)
# time.sleep(0.2)
#
# #해당 공연으로 이동
# driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '23013281')
# time.sleep(5)
#
# # 예매하기 버튼 클릭
# driver.find_element(By.XPATH, "//div[@class='tk_dt_btn_TArea']/a").click()
