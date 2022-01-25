import threading
import Mazes
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

class CUnit:
    size = 10
    def __init__(self):
        self.rect = QRect(20,20,10,10)
        self.color = QColor(0,0,0)

class CPlayer(CUnit):
    def __init__(self):
        super().__init__()
        self.color.setRgb(0,0,255,255)

class CEnemy():
    def __init__(self,x,y,dir):
        self.rect = QRect(x*20,y*20,20,20)
        self.dir = dir

class CWall:
    def __init__(self,x,y):
        self.rect = QRect(x*20,y*20,20,20)

class CExit:
    def __init__(self,x,y):
        self.rect = QRect(x*20,y*20,20,20)

class CMap:
    def __init__(self,parent,maze):
        self.parent = parent
        self.player = CPlayer()
        self.gainlabelpos=[]
        self.success=False
        self.exit = 0
        self.lockE = threading.Lock()
        self.enemy = []
        self.enemyCount=Mazes.enemyCount
        self.maze = maze
        self.wall = []
        self.label = []
        self.gain_heart=0
        self.end=False
        self.initGame()
    def getHeart(self):
        return self.gain_heart

    def initGame(self):
        self.player.rect.setRect(20,20,15,15)

        movingEnemy = threading.Thread(target=self.moveEnemy)

        movingEnemy.start()

    def draw(self,drawer):
        drawer.setBrush(QColor(200,200,200))
        drawer.drawEllipse(self.player.rect.x(),self.player.rect.y(),15,15)
        if len(self.enemy)==self.enemyCount[self.parent.stageCount-1]:
            for e in self.enemy:
                drawer.setBrush(QColor(200,0,0))
                drawer.drawEllipse(e.rect.x(),e.rect.y(),15,15)
        #drawer.drawRect(self.player.rect)
        for i in range(0,len(self.maze)):
            for j in range(0,len(self.maze[i])):

                if self.maze[i][j]==1:
                    wall=CWall(i,j)
                    self.wall.append(wall)
                    drawer.setBrush(QColor(200,200,200))
                    drawer.drawRect(wall.rect.x(),wall.rect.y(),20,20)
                elif self.maze[i][j]==2:
                    if len(self.label)<Mazes.requiredHearts[self.parent.stageCount]:
                        label1 = QLabel(self.parent)
                        label1.move(20*i,20*j)
                        self.label.append(label1)
                        folder = os.getcwd()
                        pixmap = QPixmap(folder+'/heart.png')
                        label1.setPixmap(pixmap.scaled(20,20))
                        label1.show()
                elif self.maze[i][j]==3:
                    exit = CExit(i,j)
                    self.exit=exit
                    drawer.setBrush(QColor(0,200,0))
                    drawer.drawRect(exit.rect.x(),exit.rect.y(),20,20)
                elif self.maze[i][j]==4:
                    if len(self.enemy)<self.enemyCount[self.parent.stageCount-1]:
                        rlenemy=CEnemy(i,j,'right')
                        drawer.setBrush(QColor(200,0,0))
                        drawer.drawEllipse(rlenemy.rect.x(),rlenemy.rect.y(),15,15)
                        self.enemy.append(rlenemy)

                elif self.maze[i][j]==5:
                    if len(self.enemy)<self.enemyCount[self.parent.stageCount-1]:
                        udenemy=CEnemy(i,j,'up')
                        drawer.setBrush(QColor(200,0,0))
                        drawer.drawEllipse(udenemy.rect.x(),udenemy.rect.y(),15,15)
                        self.enemy.append(udenemy)


    def moveEnemy(self):
        while self.end==False:
            speed=5
            self.lockE.acquire()
            for enemy in self.enemy[:]:
                if enemy.rect.intersects(self.player.rect):
                    self.parent.parent.gainCommentsLabel("You Fail! Try again!")
                    self.end=True
                elif enemy.dir=='left':
                    pastPos = (enemy.rect.x(),enemy.rect.y())
                    for wall in self.wall:
                        if enemy.rect.left()-speed<=wall.rect.right() and enemy.rect.right()>wall.rect.left() and enemy.rect.left()>=wall.rect.right():
                            if enemy.rect.y()<=wall.rect.bottom() and enemy.rect.y()>=wall.rect.top():
                                enemy.dir='right'

                    enemy.rect.adjust(-speed,0,-speed,0)

                elif enemy.dir=='right':
                    pastPos = (enemy.rect.x(),enemy.rect.y())
                    for wall in self.wall:
                        if enemy.rect.right()+speed>=wall.rect.left() and enemy.rect.left()<wall.rect.right() and enemy.rect.right()<=wall.rect.left():
                            if enemy.rect.y()<=wall.rect.bottom() and enemy.rect.y()>=wall.rect.top():
                                enemy.dir='left'
                    enemy.rect.adjust(speed,0,speed,0)
                elif enemy.dir=='up':
                    for wall in self.wall:
                        if enemy.rect.top()-speed<=wall.rect.bottom() and enemy.rect.bottom()>wall.rect.top() and enemy.rect.top()>=wall.rect.bottom():
                            if enemy.rect.x()<=wall.rect.right() and enemy.rect.x()>=wall.rect.left():
                                    enemy.dir='down'
                    enemy.rect.adjust(0,-speed,0,-speed)
                elif enemy.dir=='down':
                    for wall in self.wall:
                        if enemy.rect.bottom()+speed>=wall.rect.top() and enemy.rect.top()<wall.rect.bottom() and enemy.rect.bottom()<=wall.rect.top():
                            if enemy.rect.x()<=wall.rect.right() and enemy.rect.x()>=wall.rect.left():
                                    enemy.dir='up'
                    enemy.rect.adjust(0,speed,0,speed)


            self.lockE.release()
            self.parent.update()
            time.sleep(0.1)

    def keyDown(self,key):
        if self.end==False and self.success==False:
            speed=5

            if key==Qt.Key_Left:
                for wall in self.wall:
                    if self.player.rect.left()-speed<=wall.rect.right() and self.player.rect.right()>wall.rect.left() and self.player.rect.left()>=wall.rect.right():
                        if self.player.rect.y()<=wall.rect.bottom() and self.player.rect.y()>=wall.rect.top():
                            return
                self.player.rect.adjust(-speed,0,-speed,0)

            elif key==Qt.Key_Right:
                for wall in self.wall:
                    if self.player.rect.right()+speed>=wall.rect.left() and self.player.rect.left()<wall.rect.right() and self.player.rect.right()<=wall.rect.left():
                        if self.player.rect.y()<=wall.rect.bottom() and self.player.rect.y()>=wall.rect.top():
                            return
                self.player.rect.adjust(speed,0,speed,0)
            elif key==Qt.Key_Up:
                for wall in self.wall:
                    if self.player.rect.top()-speed<=wall.rect.bottom() and self.player.rect.bottom()>wall.rect.top() and self.player.rect.top()>=wall.rect.bottom():
                        if self.player.rect.x()<=wall.rect.right() and self.player.rect.x()>=wall.rect.left():
                                return
                self.player.rect.adjust(0,-speed,0,-speed)
            elif key==Qt.Key_Down:
                for wall in self.wall:
                    if self.player.rect.bottom()+speed>=wall.rect.top() and self.player.rect.top()<wall.rect.bottom() and self.player.rect.bottom()<=wall.rect.top():
                        if self.player.rect.x()<=wall.rect.right() and self.player.rect.x()>=wall.rect.left():
                                return
                self.player.rect.adjust(0,speed,0,speed)

            for label in range(len(self.label)):
                    if self.label[label].x()==self.player.rect.x() and self.label[label].y()==self.player.rect.y() and [self.label[label].x(),self.label[label].y()] not in self.gainlabelpos:
                        self.gainlabelpos.append([self.label[label].x(),self.label[label].y()])
                        self.label[label].clear()
                        self.gain_heart+=1
                        self.parent.parent.gainHeartsLabel()



            if self.gain_heart==self.parent.requiredHearts and self.player.rect.intersects(self.exit.rect):
                self.end=True
                self.parent.stageCount+=1
                if self.parent.stageCount==6:
                    self.parent.stageCount-=1
                    self.parent.parent.gainCommentsLabel("You escaped the maze!\nCongratulation!")
                    self.success=True

                else:
                    next_stage=Mazes.Mazes[self.parent.stageCount]
                    self.parent.map=CMap(self.parent,next_stage)
                    self.parent.parent.gainStageLabel()
                    self.parent.parent.gainCommentsLabel("Escape Success!")
                    self.gain_heart=0
                    self.parent.requiredHearts=Mazes.requiredHearts[self.parent.stageCount]
                    self.parent.parent.gainHeartsLabel()
                    self.gainlabelpos=[]
                    time.sleep(0.1)
                    self.end=False
            elif self.gain_heart>self.parent.requiredHearts:
                self.gain_heart=self.parent.requiredHearts
            elif self.end==True:
                self.parent.parent.gainCommentsLabel("You Fail! Try again!")
            elif self.gain_heart==self.parent.requiredHearts:
                self.parent.parent.gainCommentsLabel("Got all hearts! Go to exit!")

            elif self.gain_heart<self.parent.requiredHearts and self.gain_heart>0:
                self.parent.parent.gainCommentsLabel(f"Got {self.gain_heart} hearts! {self.parent.requiredHearts-self.gain_heart} remains.")
            elif self.gain_heart==0:
                self.parent.parent.gainCommentsLabel("Escape the maze!\nEvade all enemies,\nand if you get all hearts,\nthe exit will open!")

        self.parent.update()

    def exitGame(self):
        self.end=True
