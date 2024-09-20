import sys    
import os    
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox    
from PyQt5.QtGui import QMovie    
from PyQt5.QtCore import Qt    

class SystemControl(QWidget):    
    def __init__(self):    
        super().__init__()    
        self.initUI()    
        
    def initUI(self):    
        self.setWindowTitle("System Control")    
        self.setFixedSize(300, 300)  
   
        self.background_label = QLabel(self)    
        self.background_label.setGeometry(0, 0, 300, 300)    
        

        self.movie = QMovie("C:/Users/Persian Rayaneh/Desktop/VID_20240920_193650+(1).gif")    
        self.background_label.setMovie(self.movie)    
        self.movie.start()  
        self.background_label.setScaledContents(True)  

        layout = QVBoxLayout()    
            
   
        title_label = QLabel("Choose an action:")    
        title_label.setStyleSheet("font-size: 24px; color: #ecf0f1;")    
        title_label.setAlignment(Qt.AlignCenter)    
        layout.addWidget(title_label)    
            
 
        self.btn_shutdown = self.create_button("Shutdown", "#e74c3c", self.shutdown)    
        self.btn_restart = self.create_button("Restart", "#3498db", self.restart)    
        self.btn_cancel = self.create_button("Cancel", "#95a5a6", self.cancel)    

        layout.addWidget(self.btn_shutdown)    
        layout.addWidget(self.btn_restart)    
        layout.addWidget(self.btn_cancel)    
    

        self.setLayout(layout)    
        self.setStyleSheet("background-color: rgba(52, 73, 94, 0.8);")  
    
    def create_button(self, text, color, callback):    
        button = QPushButton(text)    
        button.setStyleSheet(f"""    
            background-color: {color};    
            border-radius: 12px;    
            color: white;    
            padding: 12px;    
            font-size: 18px;    
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);    
            transition: background-color 0.3s ease;    
        """)    
        button.clicked.connect(callback)    
            

        button.setMouseTracking(True)    
        button.enterEvent = lambda event: self.change_button_style(button, bold=True, hover=True)    
        button.leaveEvent = lambda event: self.change_button_style(button, bold=False, hover=False)    
        return button    
    
    def change_button_style(self, button, bold, hover):    
        font = button.font()    
        font.setBold(bold)    
        button.setFont(font)    
        if hover:    
            button.setStyleSheet(button.styleSheet() + " background-color: #c0392b;")  
        else:    
            button.setStyleSheet(button.styleSheet().replace("background-color: #c0392b;", ""))    

    def shutdown(self):    
        QMessageBox.information(self, "Shutdown", "System will shut down in 7 seconds.")    
        os.system("shutdown /s /t 7")    
        
    def restart(self):    
        QMessageBox.information(self, "Restart", "System will restart in 7 seconds.")    
        os.system("shutdown /r /t 7")    
        
    def cancel(self):    
        QMessageBox.information(self, "Cancel", "Operation canceled.")    
        self.close()
 
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = SystemControl() 
    ex.show() 
    sys.exit(app.exec_())
