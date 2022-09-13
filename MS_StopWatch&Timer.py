import sys
import os
import winsound
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType, loadUi

from ProgressBar import CrlProgressBar

import time


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi('UI/MiddleWatch.ui', self)
        self.setWindowTitle('MS StopWatch & Timer')

        set_Validator_SecMin = QRegExpValidator(QRegExp('[0-9]+'))
        self.Seconds.setValidator(set_Validator_SecMin)
        self.Minutes.setValidator(set_Validator_SecMin)
        set_Validator_hrs = QRegExpValidator(QRegExp('[0-8]+'))
        self.Hours.setValidator(set_Validator_hrs)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.Seconds.setAlignment(Qt.AlignCenter)
        self.Minutes.setAlignment(Qt.AlignCenter)
        self.Hours.setAlignment(Qt.AlignCenter)
        self.oldPosition = None

        self.progress = CrlProgressBar()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.resumeOpz)
        self.timer.start(995)

        self.ShowRoundProgressBar()
        self.shadow = QGraphicsDropShadowEffect(self)
        self.HighLt = {}

        self.timerStarted = False

        self.Sec_increment = 1
        self.Min_increment = 0
        self.Hrs_increment = 0

        self.TimerHrs = None
        self.TimerMins = None
        self.TimerSecs = None
        self.x1 = 0
        self.y1 = 0
        self.TimeOut_Count = 0

        self.HandleButtons()
        self.HandleEditables()
        self.Set_Shadow()

    def Set_Shadow(self):

        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(1)
        self.shadow.setYOffset(1)
        self.shadow.setColor(QColor(0, 0, 0, 200))
        self.label_MS.setGraphicsEffect(self.shadow)

        self.HighLt[1] = QGraphicsDropShadowEffect(self)
        self.HighLt[1].setBlurRadius(10)
        self.HighLt[1].setXOffset(1)
        self.HighLt[1].setYOffset(1)
        self.HighLt[1].setColor(QColor(0, 0, 0, 200))
        self.label_AppName.setGraphicsEffect(self.HighLt[1])

        self.HighLt[2] = QGraphicsDropShadowEffect(self)
        self.HighLt[2].setBlurRadius(10)
        self.HighLt[2].setXOffset(1)
        self.HighLt[2].setYOffset(1)
        self.HighLt[2].setColor(QColor(0, 0, 0, 200))
        self.Hours.setGraphicsEffect(self.HighLt[2])

        self.HighLt[3] = QGraphicsDropShadowEffect(self)
        self.HighLt[3].setBlurRadius(10)
        self.HighLt[3].setXOffset(1)
        self.HighLt[3].setYOffset(1)
        self.HighLt[3].setColor(QColor(0, 0, 0, 200))
        self.Minutes.setGraphicsEffect(self.HighLt[3])

        self.HighLt[4] = QGraphicsDropShadowEffect(self)
        self.HighLt[4].setBlurRadius(10)
        self.HighLt[4].setXOffset(1)
        self.HighLt[4].setYOffset(1)
        self.HighLt[4].setColor(QColor(0, 0, 0, 200))
        self.Seconds.setGraphicsEffect(self.HighLt[4])

        self.HighLt[5] = QGraphicsDropShadowEffect(self)
        self.HighLt[5].setBlurRadius(10)
        self.HighLt[5].setXOffset(1)
        self.HighLt[5].setYOffset(1)
        self.HighLt[5].setColor(QColor(0, 0, 0, 200))
        self.label_Sep1.setGraphicsEffect(self.HighLt[5])

        self.HighLt[6] = QGraphicsDropShadowEffect(self)
        self.HighLt[6].setBlurRadius(10)
        self.HighLt[6].setXOffset(1)
        self.HighLt[6].setYOffset(1)
        self.HighLt[6].setColor(QColor(0, 0, 0, 200))
        self.label_Sep2.setGraphicsEffect(self.HighLt[6])

        self.HighLt[7] = QGraphicsDropShadowEffect(self)
        self.HighLt[7].setBlurRadius(10)
        self.HighLt[7].setXOffset(1)
        self.HighLt[7].setYOffset(1)
        self.HighLt[7].setColor(QColor(0, 0, 0, 200))
        self.CloseBTN.setGraphicsEffect(self.HighLt[7])

        self.HighLt[8] = QGraphicsDropShadowEffect(self)
        self.HighLt[8].setBlurRadius(4)
        self.HighLt[8].setXOffset(1)
        self.HighLt[8].setYOffset(1)
        self.HighLt[8].setColor(QColor(0, 0, 0, 200))
        self.StartBTN.setGraphicsEffect(self.HighLt[8])

        self.HighLt[9] = QGraphicsDropShadowEffect(self)
        self.HighLt[9].setBlurRadius(4)
        self.HighLt[9].setXOffset(1)
        self.HighLt[9].setYOffset(1)
        self.HighLt[9].setColor(QColor(0, 0, 0, 200))
        self.ResetBTN.setGraphicsEffect(self.HighLt[9])

        self.HighLt[10] = QGraphicsDropShadowEffect(self)
        self.HighLt[10].setBlurRadius(4)
        self.HighLt[10].setXOffset(1)
        self.HighLt[10].setYOffset(1)
        self.HighLt[10].setColor(QColor(0, 0, 0, 200))
        self.StopBTN.setGraphicsEffect(self.HighLt[10])

        self.HighLt[11] = QGraphicsDropShadowEffect(self)
        self.HighLt[11].setBlurRadius(3)
        self.HighLt[11].setXOffset(1)
        self.HighLt[11].setYOffset(1)
        self.HighLt[11].setColor(QColor(0, 0, 0, 200))
        self.StopWatch.setGraphicsEffect(self.HighLt[11])

        self.HighLt[12] = QGraphicsDropShadowEffect(self)
        self.HighLt[12].setBlurRadius(3)
        self.HighLt[12].setXOffset(1)
        self.HighLt[12].setYOffset(1)
        self.HighLt[12].setColor(QColor(0, 0, 0, 200))
        self.Timer.setGraphicsEffect(self.HighLt[12])

    def HandleButtons(self):

        self.StopWatch.clicked.connect(self.SetTimerOpz)
        self.Timer.clicked.connect(self.SetStopWatchOpz)
        self.ResetBTN.clicked.connect(self.ReSet)
        self.StartBTN.clicked.connect(self.StartResume)
        self.StopBTN.clicked.connect(self.Stop)
        self.CloseBTN.clicked.connect(self.CloseApp)

    def HandleEditables(self):
        self.Minutes.setReadOnly(True)
        self.Hours.setReadOnly(True)
        self.Seconds.setReadOnly(True)

        self.StopWatch.setEnabled(False)

    def SetTimerOpz(self):

        if self.StopWatch.isChecked():
            self.Timer.setChecked(False)
            self.timerStarted = False
            self.Minutes.setReadOnly(True)
            self.Hours.setReadOnly(True)
            self.Seconds.setReadOnly(True)

            self.StopWatch.setEnabled(False)
            self.Timer.setEnabled(True)

    def SetStopWatchOpz(self):

        if self.Timer.isChecked():
            self.timerStarted = False
            self.StopWatch.setEnabled(True)
            self.StopWatch.setChecked(False)

            self.Timer.setEnabled(False)

            self.Minutes.setReadOnly(False)
            self.Hours.setReadOnly(False)
            self.Seconds.setReadOnly(False)

    def ShowRoundProgressBar(self):

        self.progress.width = 527
        self.progress.height = 527

        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(12, 12)
        self.progress.setParent(self.centralwidget)
        self.progress.Set_Shadow(True)
        self.progress.lower()
        self.progress.show()

    def resumeOpz(self):
        if self.timerStarted:
            if self.StopWatch.isChecked():
                if self.Sec_increment == 60:

                    self.Seconds.setText('00')

                    self.progress.set_value(self.Sec_increment)
                    self.Sec_increment = 1
                    self.Min_increment += 1

                    if self.Min_increment < 10:
                        self.Minutes.setText(str(f"0{self.Min_increment}"))

                    elif self.Min_increment == 60:

                        self.Min_increment = 0
                        self.Minutes.setText("00")
                        self.Hrs_increment += 1

                        if self.Hrs_increment < 10:
                            self.Hours.setText(str(f"0{self.Hrs_increment}"))
                        else:
                            self.Hours.setText(str(self.Hrs_increment))

                    else:
                        self.Minutes.setText(str(self.Min_increment))
                    self.y1 = time.perf_counter()
                    print(f"Time = {(self.y1 - self.x1)}")
                elif self.Sec_increment <= 59:

                    if self.Sec_increment < 10:
                        self.Seconds.setText(f'0{str(self.Sec_increment)}')
                    else:
                        self.Seconds.setText(str(self.Sec_increment))

                    print(f'{str(self.Sec_increment)}')
                    self.progress.set_value(self.Sec_increment)
                    self.Sec_increment += 1
                    self.x1 = time.perf_counter()
            # Main Timer operations.............................
            elif self.Timer.isChecked():
                self.TimerSecs = int(self.TimerSecs)
                if self.TimerSecs != 0:
                    self.TimerSecs -= 1
                    self.progress.set_value(self.TimerSecs)
                    if self.TimerSecs < 10:
                        self.Seconds.setText(f"0{str(self.TimerSecs)}")
                    else:
                        self.Seconds.setText(str(self.TimerSecs))

                elif self.TimerSecs == 0:
                    self.TimerMins = int(self.Minutes.text())
                    if self.TimerMins != 0:
                        self.TimerSecs = 59
                        self.Seconds.setText("59")
                        self.TimerMins -= 1
                        if self.TimerMins < 10:
                            self.Minutes.setText(f"0{str(self.TimerMins)}")
                        else:
                            self.Minutes.setText(str(self.TimerMins))

                    elif self.TimerMins == 0:
                        self.TimerHrs = int(self.Hours.text())
                        if self.TimerHrs != 0:
                            self.TimerMins = 59
                            self.TimerSecs = 59
                            self.Minutes.setText("59")
                            self.Seconds.setText("59")
                            self.TimerHrs -= 1
                            if self.TimerHrs < 10:
                                self.Hours.setText(f"0{str(self.TimerHrs)}")
                            else:
                                self.Hours.setText(str(self.TimerHrs))
                        elif self.TimerHrs == 0:
                            self.TimeOut()

    def StartResume(self):
        self.timerStarted = True
        self.TimeOut_Count = 1
        self.StartBTN.setEnabled(False)
        self.StopBTN.setEnabled(True)
        # print(f"Empty :P{self.Hours.text()}P")
        if self.Timer.isChecked():
            try:
                self.TimerSecs = int(self.Seconds.text())
                self.TimerMins = int(self.Minutes.text())
                self.TimerHrs = int(self.Hours.text())
            except:  # ValueError
                
                if self.Seconds.text() == "":
                    self.TimerSecs = 0

                if self.Minutes.text() == "":
                    self.TimerMins = 0

                    self.Minutes.setText("00")
                if self.Hours.text() == "":
                    self.TimerHrs = 0
                    self.Hours.setText("00")

            print(f"Timer...{self.TimerSecs}.......{self.TimerMins}........{self.TimerHrs}.....")
            self.progress.set_value(self.TimerSecs)

            self.Minutes.setReadOnly(True)
            self.Hours.setReadOnly(True)
            self.Seconds.setReadOnly(True)

    def Stop(self):
        self.timerStarted = False
        self.StopBTN.setEnabled(False)
        self.StartBTN.setEnabled(True)
        if self.Timer.isChecked():
            self.Minutes.setReadOnly(False)
            self.Hours.setReadOnly(False)
            self.Seconds.setReadOnly(False)

    def ReSet(self):

        self.timerStarted = False
        self.Sec_increment = 1
        self.Min_increment = 0
        self.Hrs_increment = 0

        self.Seconds.setText("00")
        self.Minutes.setText("00")
        self.Hours.setText("00")
        self.progress.set_value(0)
        self.StartBTN.setEnabled(True)
        self.StopBTN.setEnabled(False)

        self.Minutes.setReadOnly(False)
        self.Hours.setReadOnly(False)
        self.Seconds.setReadOnly(False)

    def TimeOut(self):
        if self.TimeOut_Count == 1:

            winsound.PlaySound("Sounds/Alarm.wav", winsound.SND_FILENAME)
            self.TimeOut_Count = 0
            self.StopBTN.setEnabled(False)
            self.StartBTN.setEnabled(True)

    def CloseApp(self):
        end_time = time.perf_counter()
        full_time = end_time - self.x1
        print(f"Time for all : {full_time}")
        print("............... Closing Application ...............")
        QApplication.instance().quit()

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
