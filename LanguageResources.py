class I18N():
    def __init__(self,language):
        if language == 'en':self.resourceLanguageEnglish()
        elif language == 'ko':self.resourceLanguageKorean()
        else: raise NotImplementedError('Unsupported language.')

    def resourceLanguageEnglish(self):
        self.title = "Python Graphical User Interface"

    def resourceLanguageKorean(self):
        self.title = "파이썬 그래픽 사용자 인터페이스"

        self.file = "파일"
        self.new = "새로만들기"
        self.exit = "종류"
        self.help = "도움말"
        self.about = "정보"

        self.WIDGET_LABEL = '위젯 프레임'

        self.disabled = "비활성화"
        self.unChecked = "미체크"
        self.toggle = "토글"

        self.colors = ["파란색","노란색", "빨간색"]
        self.colorsIn = ["내부 파란색","내부 노란색","내부 빨간색"]

        self.labelsFrame = '라벨프레임'
        self.chooseNumber = "숫자를 고르세요:"
        self.label2 = "라벨2"

        self.timeZones = "모든 지역/도시"
        self.localZone = "해당지역"
        self.getTime = "뉴욕"

        self.mgrFiles = "파일 관리"
        self.browseTo = "파일 찾아오기 "
        self.copyTo = "파일 복사하기 : "