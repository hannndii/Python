import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTabWidget, QTimeEdit, QSpinBox, QHBoxLayout, QLCDNumber
from PyQt5.QtCore import QTimer, QTime

class ClockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.tabs = QTabWidget()
        self.tabs.addTab(self.createStopwatchTab(), "Stopwatch")
        self.tabs.addTab(self.createTimerTab(), "Timer")
        self.tabs.addTab(self.createAlarmTab(), "Alarm")
        
        layout.addWidget(self.tabs)
        self.setLayout(layout)
        self.setWindowTitle("Clock App")
        self.setGeometry(100, 100, 300, 200)
    
    def createStopwatchTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.stopwatch_lcd = QLCDNumber()
        self.stopwatch_lcd.display("00:00")
        layout.addWidget(self.stopwatch_lcd)
        
        self.stopwatch_timer = QTimer()
        self.stopwatch_timer.timeout.connect(self.updateStopwatch)
        self.stopwatch_time = 0
        
        btn_layout = QHBoxLayout()
        self.start_stopwatch_btn = QPushButton("Start")
        self.start_stopwatch_btn.clicked.connect(self.startStopwatch)
        btn_layout.addWidget(self.start_stopwatch_btn)
        
        self.reset_stopwatch_btn = QPushButton("Reset")
        self.reset_stopwatch_btn.clicked.connect(self.resetStopwatch)
        btn_layout.addWidget(self.reset_stopwatch_btn)
        
        layout.addLayout(btn_layout)
        tab.setLayout(layout)
        return tab
    
    def startStopwatch(self):
        if not self.stopwatch_timer.isActive():
            self.stopwatch_timer.start(1000)
            self.start_stopwatch_btn.setText("Stop")
        else:
            self.stopwatch_timer.stop()
            self.start_stopwatch_btn.setText("Start")
    
    def resetStopwatch(self):
        self.stopwatch_timer.stop()
        self.stopwatch_time = 0
        self.stopwatch_lcd.display("00:00")
        self.start_stopwatch_btn.setText("Start")
    
    def updateStopwatch(self):
        self.stopwatch_time += 1
        minutes = self.stopwatch_time // 60
        seconds = self.stopwatch_time % 60
        self.stopwatch_lcd.display(f"{minutes:02}:{seconds:02}")
    
    def createTimerTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.timer_input = QSpinBox()
        self.timer_input.setSuffix(" sec")
        self.timer_input.setMaximum(3600)
        layout.addWidget(self.timer_input)
        
        self.timer_lcd = QLCDNumber()
        layout.addWidget(self.timer_lcd)
        
        self.timer_btn = QPushButton("Start Timer")
        self.timer_btn.clicked.connect(self.startTimer)
        layout.addWidget(self.timer_btn)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer_time = 0
        
        tab.setLayout(layout)
        return tab
    
    def startTimer(self):
        if not self.timer.isActive():
            self.timer_time = self.timer_input.value()
            self.timer_lcd.display(self.timer_time)
            self.timer.start(1000)
            self.timer_btn.setText("Stop Timer")
        else:
            self.timer.stop()
            self.timer_btn.setText("Start Timer")
    
    def updateTimer(self):
        if self.timer_time > 0:
            self.timer_time -= 1
            self.timer_lcd.display(self.timer_time)
        else:
            self.timer.stop()
            self.timer_btn.setText("Start Timer")
    
    def createAlarmTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.alarm_time_edit = QTimeEdit()
        self.alarm_time_edit.setTime(QTime.currentTime())
        layout.addWidget(self.alarm_time_edit)
        
        self.alarm_btn = QPushButton("Set Alarm")
        self.alarm_btn.clicked.connect(self.setAlarm)
        layout.addWidget(self.alarm_btn)
        
        self.alarm_label = QLabel("")
        layout.addWidget(self.alarm_label)
        
        self.alarm_timer = QTimer()
        self.alarm_timer.timeout.connect(self.checkAlarm)
        
        tab.setLayout(layout)
        return tab
    
    def setAlarm(self):
        self.alarm_time = self.alarm_time_edit.time()
        self.alarm_label.setText(f"Alarm set for {self.alarm_time.toString('HH:mm:ss')}")
        self.alarm_timer.start(1000)  # Start checking for alarm
    
    def checkAlarm(self):
        current_time = QTime.currentTime()
        if (current_time.hour() == self.alarm_time.hour() and
            current_time.minute() == self.alarm_time.minute() and
            current_time.second() == self.alarm_time.second()):
            self.alarm_label.setText("ALARM! Wake up!")
            self.alarm_timer.stop()  # Stop the timer after the alarm triggers

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClockApp()
    window.show()
    sys.exit(app.exec_())