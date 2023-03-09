# Qt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverApi import *
import webbrowser # 웹브라우저 모듈
from urllib.request import urlopen

class qtApp(QWidget) :
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyPyQt/naverApiMovie.ui',self)
        self.setWindowIcon(QIcon('./studyPyQt/movie.png'))
        
        # 검색 버튼 클릭시그널 / 슬롯 함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 검색어 입력 후 엔터를 치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def btnSearchClicked(self) :
        search = self.txtSearch.text()
        if search == '' :
            QMessageBox.warning(self, "경고", "영화명을 입력하세요! ")
            return
        else :
            api = NaverApi() # NaverApi 클래스 객체 생성
            node = 'movie' # movie 로 변경하면 영화검색 가능
            display = 100
            result = api.get_naver_search(node, search, 1, display)         
            items = result['items'] # json 결과 중 items 아래 배열만 추출 
            self.makeTable(items)    

    def txtSearchReturned(self) :
        self.btnSearchClicked()

    def tblResultDoubleClicked(self) :
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text() # 단일 선택
        webbrowser.open(url) # 네이버 영화 웹 오픈

    # table widget에 데이터 표시 -- 네이버 영화 결과 변경
    def makeTable(self,items) -> None :
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(7) # 컬럼 갯수 변경
        self.tblResult.setRowCount(len(items)) # 현재 100개행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', ' 배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 60) # 개봉년도
        self.tblResult.setColumnWidth(4, 50) # 평점

        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 데이터 수정금지

        for i, post in enumerate(items) : # 0, 영화 ...
            title = self.replaceHtmlTag(post['title']) # Html 특수문자 변환
            subtitle = post['subtitle']
            title = f'{title}({subtitle})'
            pubDate = post['pubDate']
            director = post['director']
            director = director.replace('|',',')[:-1]
            actor = post['actor']
            actor = actor.replace('|',',')[:-1]
            userRating = post['userRating']
            link = post['link']
            img_url = post['image']                      

            if img_url != '' : # 빈값이면 포스터가 없음
                data = urlopen(img_url).read() # 2진 데이터 - 네이버 영화에 있는 이미지 다운, 텍스트 형태의 데이터
                image = QImage() # 이미지 객체
                image.loadFromData(data)
                # QTableWidget 이미지를 그냥 넣을 수 없음. QLabel() 집어넣은뒤 QLabel -> QTableWidget
                imgLabel = QLabel()
                imgLabel.setPixmap(QPixmap(image))

                # data - poster 를 이미지로 저장가능 
                # f = open(f'./studyPyQt/temp/image_{i+1}.png',mode ='wb') # 파일쓰기
                # f.write(data)
                # f.close()

            # setItem(행, 열, 넣을 데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))

            if img_url != '' :
                self.tblResult.setCellWidget(i,6,imgLabel)
                self.tblResult.setRowHeight(i,110)
            else :
                self.tblResult.setItem(i, 6, QTableWidgetItem('No Poster'))
                
    def replaceHtmlTag(self, sentence) -> str :
        result = sentence.replace('&lt;', '<') # lesser than
        result = result.replace('&gt;', '>') # greater than
        result = result.replace('<b>', '') # bold
        result = result.replace('</b>', '') # bold
        result = result.replace('&apos;', "'") # apostopy
        result = result.replace('&quot;', '"') # quotation
        # 변환 안된 특수문자가 나타나면 여기 추가
        return result

if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())