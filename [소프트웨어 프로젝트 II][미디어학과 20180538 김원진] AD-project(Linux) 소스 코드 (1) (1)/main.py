from PyQt5.Qt import *
import sys
from CObject import *
import Mazes

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
class CMain(QWidget):
    def __init__(self):
        super().__init__()
        self.main=''
        self.hlabel=''
        self.heart=''
        self.slabel=''
        self.stage=''
        self.clabel=''
        self.comments=''

        self.initUI()


    def initUI(self):
        main = QGridLayout()
        self.setWindowTitle("미로 찾기 게임")
        self.main=main
        self.game = CWidget(self)
        label=QLabel("Remaining hearts")
        self.hlabel=label
        heart =QLabel(f"♥:{self.game.map.getHeart()}/{self.game.requiredHearts}")
        self.heart=heart
        heart.setFixedSize(200,20)
        #text.setReadOnly(True)

        label2=QLabel("Remaining Stages")
        self.slabel=label2
        stage = QLabel(f"{self.game.stageCount}/5")
        self.stage=stage
        label2.setFixedSize(200,20)

        label3=QLabel("Comments")
        self.clabel=label3
        comments=QLabel()
        self.comments=comments

        game = QGridLayout()

        game.addWidget(self.game,0,0,0,0)
        main.addWidget(self.game,0,0,0,0)

        main.addWidget(label,0,3,1,2)
        main.addWidget(heart,0,3,2,2)
        main.addWidget(label2,0,3,3,2)
        main.addWidget(stage,0,3,4,2)
        main.addWidget(label3,0,3,5,2)
        main.addWidget(comments,0,3,6,2)

        self.setLayout(main)
        self.show()

    def gainHeartsLabel(self):
        self.heart.setText(f"♥:{self.game.map.getHeart()}/{self.game.requiredHearts}")
        return

    def gainStageLabel(self):
        self.stage.setText(f"{self.game.stageCount}/5" )

    def gainCommentsLabel(self,comments):
        self.comments.setText(comments)

    def keyPressEvent(self, e):
        self.game.map.keyDown(e.key())

    def closeEvent(self,e):
         self.game.map.exitGame()

class CWidget(QWidget):

    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.initUI()


    def initUI(self):
        self.setGeometry(200,200,600,400)
        self.setFixedSize(self.rect().size())
        self.stageCount=1
        self.mazeLength=len(Mazes.Mazes[self.stageCount])
        self.requiredHearts=Mazes.requiredHearts[self.stageCount]
        self.map = CMap(self,Mazes.Mazes[self.stageCount])


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.map.draw(qp)
        qp.end()


    def keyPressEvent(self, e):
        self.map.keyDown(e.key())


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    # sys.exit(1)

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__=='__main__':
    app = QApplication(sys.argv)
    w=CMain()
    w.show()
    sys.exit(app.exec_())
