from PyQt5.QtGui import QIcon 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from goprocam import GoProCamera, constants

from main import Ui_MainWindow 
from TableView import TableView
from bs4 import BeautifulSoup

import requests 
import webbrowser
import socket
import sys
import threading
import subprocess

class MainApp(Ui_MainWindow):

 
    class StreamingWorker(QObject):
        finished = pyqtSignal()
        progress = pyqtSignal(int)

        def __init__(self, gopro, ip, quality):
            
            super(MainApp.StreamingWorker, self).__init__()
            self.gopro = gopro
            self.ip = ip
            self.quality = quality
            self._stop = False
        
        def stop(self):
            self._stop = True
     
        def run(self):
          

            print("Start thread") 
            self.gopro.livestream("start")
            
           
            while True: 
                if self._stop: 
                    print("Exit worker")
                    return
             
            #self.gopro.stream(self.ip, self.quality)
            #subprocess.Popen("vlc --network-caching=300 --sout-x264-preset=ultrafast --sout-x264-tune=zerolatency --sout-x264-vbv-bufsize 0 --sout-transcode-threads 4 --no-audio udp://@:8554", shell=True)
    
    def __init__(self):
        self.links = []
        self.stream_active = False
        self.thread = QThread() 
        

        webbrowser.register('firefox',
            None,
            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        
        

    
    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    def get_status(self, param, constant):
        if param == "battery" or param == "video_left" or param == "sub_mode":
            return self.goproCamera.parse_value(param,self.goproCamera.getStatus(constants.Status.Status, constant))
        else:
            return self.goproCamera.parse_value(param,self.goproCamera.getStatus(constants.Status.Settings, constant))

    def connect_goPro(self):
        self.goproCamera = GoProCamera.GoPro() 

        self.videosLeft.setText(self.get_status("video_left", constants.Status.STATUS.RemVideoTime))
        self.currentMode.setText(self.get_status("mode", constants.Status.STATUS.Mode) )
        self.currentResolution.setText(self.get_status("video_res", constants.Video.RESOLUTION))
        self.currentFramerate.setText(self.get_status("video_fr", constants.Video.FRAME_RATE) )
        self.currentSubmode.setText(self.get_status("sub_mode", constants.Status.STATUS.SubMode) )
        self.battery.setText(self.get_status("battery", constants.Status.STATUS.BatteryLevel))

        self.connection.setText("Connected") 

        self.ip_to_stream_to.setText(self.get_ip_address())

        self.streamWorker = MainApp.StreamingWorker(self.goproCamera, self.ip_to_stream_to.text(), self.stream_quality.currentText().lower())

        self.streamWorker.moveToThread(self.thread)

        self.thread.started.connect(self.streamWorker.run)
        self.streamWorker.finished.connect(self.thread.quit)
        self.streamWorker.finished.connect(self.streamWorker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)



    def start_streaming(self):
        if not self.stream_active:
            self.thread.start()

            self.goproCamera.livestream("start")
            subprocess.Popen("ffplay  -fflags nobuffer -f:v mpegts -probesize 8192 udp://10.5.5.100:8554", shell=True)
            
            self.stream_active = True
        else:
            self.streamWorker.stop()

            self.goproCamera.livestream("stop")
            self.stream_active = False


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.tableWidget.setRowCount(0)
        MainWindow.setWindowIcon(QIcon('icon.png'))
        MainWindow.setWindowTitle("GoPro Hero WiFi Explorer")  

        self.stream_button.clicked.connect(self.start_streaming)
        
        try:
            self.fetch_media()
        except: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("GoPro Offline")
            msg.setText("GoPro Offline, check WiFi!") 
            msg.setStandardButtons(QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel) 
            msg.exec_()
            sys.exit()

        
        self.connect_goPro()

    def get_url_paths(self,url, ext='', params={}):
        try:
            response = requests.get(url,timeout=1, params=params)
            if response.ok:
                response_text = response.text
            else:
                return response.raise_for_status()
            soup = BeautifulSoup(response_text, 'html.parser')
            files = []
            for node in soup.find_all('tr'):
                for file in node.find_all('a'): 
                    if not node.find_all('th') and ( not node.getText() == "Parent directory -  -"):   
                        row = node.find_all('td')
                        filename = row[0].getText()
                        link = row[0].find_all('a')[0].get('href')
                        date = row[1].getText().strip()
                        size = row[2].getText().strip()
                        file = {"link": link, "name": filename, "date": date, "size": size}
                        files.append(file)
            return files
             
     
        except:
            print("Camera offline or not connected to computer")
    
    def fetch_media(self):
        files = self.get_url_paths("http://10.5.5.9:8080/videos/DCIM/100GOPRO/")
        files = sorted(files, key=lambda item: item["date"], reverse=True)
        
        names = []
        sizes = []
        dates = []
        self.links = []
        
        for file in files:
            names.append(file["name"])
            sizes.append(file["size"])
            dates.append(file["date"])
            self.links.append(file["link"])
        
        data = {"Filename": names,
                "Size": sizes,
                "Date": dates}
                
        cols = 3
        rows = len(names)
        self.tableWidget = TableView(data, rows, cols)
        self.tableWidget.clicked.connect(self.item_callback)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)    
        print(data)
     
        
    def item_callback(self, item):
        link  = "http://10.5.5.9:8080/" + self.links[item.row()]
        try:
            webbrowser.get('firefox').open(link) 
        except:
            webbrowser.open(link) 
            
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv) 
    MainWindow = QMainWindow()
    ui = MainApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())