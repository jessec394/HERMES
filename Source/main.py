import subprocess
import sys

class libraries:
    def Pip(self):
        try: subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        except subprocess.CalledProcessError: subprocess.run([sys.executable, '-m', 'ensurepip', '--default-pip'], check=True)

    def Setup(self):
        ExternalLibraries = ['clipboard', 'cv2' 'geocoder', 'geopandas', 'getgfs', 'keyboard', 'matplotlib', 'numpy', 'pandas', 
                             'pygame', 'pyproj', 'requests', 'scipy', 'serial', 'shapely', 'simplekml', 'tzlocal', 'yt_dlp']
        MissingLibraries = []

        for library in ExternalLibraries:
            try:  __import__(library)
            except ImportError: MissingLibraries.append(library)

        self.Check(MissingLibraries)
        self.Upgrade(ExternalLibraries)

    def Check(self, MissingLibraries):
        if not MissingLibraries: return
        for Library in MissingLibraries: self.Install(Library)

    def Install(self, LibraryName):
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', LibraryName], check=True)
        except Exception:
            pass

    def Upgrade(self, ExternalLibraries):
        for Library in ExternalLibraries:
            try: subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', Library], check=True)
            except Exception: pass

python_libraries = libraries()

try:
    # Standard Libraries
    import base64
    import csv
    import datetime
    import json
    import locale
    import math
    import os
    import random
    import re
    import smtplib
    import socket
    import threading
    import time
    import tkinter as tk
    from tkinter import filedialog
    import webbrowser
    import xml.etree.ElementTree as ET

    # Third-Party Libraries
    import clipboard
    import cv2
    import geocoder
    import geopandas as gpd
    from getgfs import Forecast, url, Coordinate, Variable
    import keyboard
    import matplotlib.pyplot as plt
    import matplotlib.ticker as plticker
    import numpy as np
    import pandas as pd
    import pygame
    from pygame.locals import QUIT
    from pyproj import Transformer
    import requests
    from scipy.interpolate import interp1d
    import serial.tools.list_ports
    from shapely.geometry import shape, LineString, Polygon
    import simplekml
    from tzlocal import get_localzone
    import yt_dlp

except Exception:
    python_libraries.Setup()

class ClassSystem:
    def __init__(self):
        self.InitializePygame()
        self.InitializeSettings()

        self.InitializeColors()
        self.InitializeFonts()
        self.InitializeResources()

        self.LoadImages()
        self.LoadSounds()

        self.SetPreferences()

    def InitializePygame(self):
        pygame.font.init()
        pygame.mixer.init()
        pygame.joystick.init()
        pygame.init()

        self.W = pygame.display.Info().current_w
        self.H = self.W * (9 / 16)
        self.SF = min(self.W / 1920, self.H / 1080)
        self.Window = pygame.display.set_mode((self.W, self.H))

    def InitializeSettings(self):
        self.Running = True
        self.DarkMode = True
        self.MetricUnits = False
        self.Fullscreen = False
        self.Startup_Screen = True
        self.Date = datetime.datetime.now().strftime("%Y%m%d")
        self.Clock = pygame.time.Clock()
        self.Lock = threading.Lock()
        self.Manual = False
        self.AutoCOM = True
        self.ScreenSetting = 'Thumb'
        self.VideoURL = self.Cap = self.Frame = None
        self.LastFrameTime = 0
        self.VideoStartTime = 0

    def InitializeColors(self):
        self.ColorBlack = (15, 15, 15, 0.8) if self.DarkMode else (240, 240, 240, 0.8)
        self.ColorWhite = (255, 255, 255) if self.DarkMode else (0, 0, 0, 1)
        self.ColorDarkGray = (30, 30, 30, 0.6) if self.DarkMode else (225, 225, 225, 0.6)
        self.ColorLightGrey = (150, 150, 150, 0.2)
        self.ColorDarkBlue = (0, 44, 90)
        self.ColorLightBlue = (115, 198, 229)
        self.ColorDarkRed = (80, 0, 0)
        self.ColorLightRed = (120, 0, 0, 0.2)
        self.ColorGreen = (0, 200, 0)
        self.ColorYellow = (254, 227, 16)

    def InitializeFonts(self):
        self.FontBahnschrift40 = pygame.font.SysFont("Bahnschrift", int(40 * self.SF))
        self.FontBahnschrift35 = pygame.font.SysFont("Bahnschrift", int(35 * self.SF))
        self.FontBahnschrift30 = pygame.font.SysFont("Bahnschrift", int(30 * self.SF))
        self.FontBahnschrift25 = pygame.font.SysFont("Bahnschrift", int(25 * self.SF))
        self.FontBahnschrift20 = pygame.font.SysFont("Bahnschrift", int(20 * self.SF))
        self.FontBahnschrift15 = pygame.font.SysFont("Bahnschrift", int(15 * self.SF))
        self.FontBahnschrift13 = pygame.font.SysFont("Bahnschrift", int(13 * self.SF))
        self.FontBahnschrift10 = pygame.font.SysFont("Bahnschrift", int(10 * self.SF))
        self.FontCalibri50 = pygame.font.SysFont("Calibri", int(50 * self.SF))
        self.FontCalibri30 = pygame.font.SysFont("Calibri", int(30 * self.SF))
        self.FontCalibri20 = pygame.font.SysFont("Calibri", int(20 * self.SF))
        self.FontImpact120 = pygame.font.SysFont("Impact", int(120 * self.SF))
        self.FontImpact80 = pygame.font.SysFont("Impact", int(80 * self.SF))
        self.FontImpact30 = pygame.font.SysFont("Impact", int(30 * self.SF))
        self.FontImpact20 = pygame.font.SysFont("Impact", int(20 * self.SF))

    def InitializeResources(self):
        self.Directory = os.path.dirname(os.path.abspath(__file__))
        self.Resources = os.path.join(self.Directory, "Resources")

    def LoadImages(self):
        try:
            for file in os.listdir(self.Resources):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    setattr(self, file.split('.')[0], pygame.image.load(os.path.join(self.Resources, file)))
        except Exception:
            pass

    def LoadSounds(self):
        try:
            for file in os.listdir(self.Resources):
                if file.lower().endswith(('.mp3', '.wav', '.ogg')):
                    setattr(self, file.split('.')[0], os.path.join(self.Resources, file))
        except Exception:
            pass

    def SetPreferences(self):
        FilePath = os.path.join(self.Directory, "Preferences.json")
        PreferencesKeys = ["Window Width", "Window Height", "Metric Units", "Dark Mode", "Startup Screen"]

        def DefaultPreferences():
            Preferences = {
                "Window Width": self.W,
                "Window Height": self.H,
                "Metric Units": self.MetricUnits,
                "Dark Mode": self.DarkMode,
                "Startup Screen": self.Startup_Screen
            }

            with open(FilePath, 'w') as file: json.dump(Preferences, file, indent=4)

        if os.path.exists(FilePath):
            try:
                with open(FilePath, 'r') as file: Data = json.load(file)

                if all(key in Data for key in PreferencesKeys):
                    self.W = Data.get("Window Width", self.W)
                    self.H = Data.get("Window Height", self.H)
                    self.MetricUnits = Data.get("Metric Units", self.MetricUnits)
                    self.DarkMode = Data.get("Dark Mode", self.DarkMode)
                    self.Startup_Screen = Data.get("Startup Screen", self.Startup_Screen)
                else: DefaultPreferences()
            except Exception:
                DefaultPreferences()
        else: DefaultPreferences()

        self.SF = min(self.W / 1920, self.H / 1080)
        self.Window = pygame.display.set_mode((self.W, self.H))

    def UpdatePreferences(self):
        Preferences = {
            "Window Width": self.W,
            "Window Height": self.H,
            "Metric Units": self.MetricUnits,
            "Dark Mode": self.DarkMode,
            "Startup Screen": self.Startup_Screen
        }

        FilePath = os.path.join(self.Directory, "Preferences.json")

        if os.path.exists(FilePath):
            with open(FilePath, 'r+') as file:
                Data = json.load(file)
                Data.update(Preferences)
                file.seek(0)
                json.dump(Data, file, indent=4)
                file.truncate()
        else:
            with open(FilePath, 'w') as file: json.dump(Preferences, file, indent=4)

    def Refresh(self):
        try:
            self.InitializeColors()
            self.InitializeFonts()
            self.InitializeResources()

            self.LoadImages()
            self.LoadSounds()

            for _, _, condition, _, _, _, _, _ in InstanceInput.TextFields: globals()[condition] = False
        except Exception:
            pass

        try:
            InstanceTitle.__init__()
            InstanceMaps.__init__()
            InstanceScreen.__init__()
            InstanceAltimeter.__init__()
            InstanceNavigator.__init__()
            InstanceCompass.__init__()
            InstanceTimer.__init__()
            InstanceLaunch.__init__()
            InstanceRadios.__init__()
            InstanceOutput.__init__()
            InstanceControls.__init__()
            InstanceVent.__init__()
            InstanceIndicators.__init__()
            InstanceButtons.__init__()
            InstancePopups.__init__()
            InstanceDemo.__init__()
            InstanceSettings.__init__()
            InstanceInput.__init__() 
        except Exception:
            pass

    def Startup(self):
        if self.Startup_Screen == True:
            pygame.display.set_caption("HERMES")
            pygame.mouse.set_pos((self.W, self.H))
            pygame.display.set_icon(pygame.image.load(os.path.join(self.Resources, "LogoMNSGC.png")))
            locale.setlocale(locale.LC_ALL, '')

            LogoSurface = pygame.Surface((self.W, self.H))
            LogoSurface.fill((self.ColorBlack if self.DarkMode else self.ColorWhite))

            LogoRect = self.LogoMNSGC.get_rect(center=(self.W / 2, self.H / 2))
            LogoArea = LogoRect.inflate(10, 10)

            Stars = []
            while len(Stars) < 100:
                x = random.randint(0, int(self.W) - 1)
                y = random.randint(0, int(self.H) - 1)
                if not LogoArea.collidepoint(x, y):
                    Stars.append((x, y))

            for x, y in Stars: pygame.draw.circle(LogoSurface, (255, 255, 255), (x, y), 1)

            for alpha in range(0, 255, 1):
                pygame.transform.smoothscale(self.LogoMNSGC, (800 * self.SF, 800 * self.SF))

                LogoSurface.set_alpha(alpha)
                self.Window.blit(LogoSurface, (0, 0))
                self.LogoMNSGC.set_alpha(alpha)
                self.Window.blit(self.LogoMNSGC, ((self.W - self.LogoMNSGC.get_width()) / 2, (self.H - self.LogoMNSGC.get_height()) / 2))

                pygame.display.flip()
                pygame.time.delay(10)
        else:
            pass

    def Shutdown(self):
        InstanceRFD.Close()
        InstanceIridium.Close()
        InstanceAPRS.Close()
        InstanceUbiquiti.Close()
        InstanceArduino.Close()

        time.sleep(0.1)

        pygame.quit()
        sys.exit()

InstanceSystem = ClassSystem()

# Messaging and Input
InputText = ''
InputWindowW = InputWindowH = InputTrackerLat = InputTrackerLon = InputTrackerAlt = InputPayloadLat = InputPayloadLon = InputPayloadAlt = InputTargetLat = InputTargetLon = InputAltOpen = InputAltClose = InputVelClose = InputIMEI = InputURL = InputRFD = InputIridium = InputAPRS = InputUbiquiti = InputArduino = InputCOMRFD = InputCOMArduino = InputPredictionLat = InputPredictionLon = InputPredictionAlt = InputPredictionAscent = InputPredictionDescent = InputPredictionFinalAlt = InputPredictionDate = InputPredictionTime = InputPredictionFloatAlt = InputPredictionFloatTime = False

class ClassTracker:
    def __init__(self):
        self.Lat = self.Lon = self.Alt = self.Pan = self.Tilt = self.Distance2D = self.Distance3D = 0

InstanceTracker = ClassTracker()

class ClassPayload:
    def __init__(self):
        self.Lat = self.Lon = self.Alt = self.Pan = self.Tilt = self.Distance2D = self.Distance3D = 0

InstancePayload = ClassPayload()

class ClassTarget:
    def __init__(self):
        self.Lat = self.Lon = self.Alt = self.Pan = self.Tilt = self.Distance2D = self.Distance3D = 0

InstanceTarget = ClassTarget()

class ClassRFD:
    def __init__(self):
        self.Conditional = self.Active = False
        self.CurrentTime = time.time()
        self.PrevTime = time.time()
        self.UpdatePeriod = 1
        self.SerialPort = self.COMPort = None
        self.FileWrite = True
        self.Timestamp = None
        self.Lat = self.Lon = self.Alt = 0
        self.DataList = ''

    def Setup(self):
        self.Conditional = True

        try:
            RFDPorts = []
            Ports = serial.tools.list_ports.comports()

            for port in Ports:
                if 'RFD' in port.description: RFDPorts.append(port.device)

            if RFDPorts:
                try:
                    self.SerialPort = serial.Serial(
                        port=RFDPorts[0],
                        baudrate=57600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=None
                    )
                except Exception as e:
                    InstanceErrors.Message = e

                pygame.mixer.music.load(InstanceSystem.Blop)
                pygame.mixer.music.play()

                InstanceOutput.Message = 'RFD Connected'
                self.Conditional = False
                self.Active = True

                InstanceRadios.Display()

            else:
                ValidPorts = []

                for port in Ports:
                    if 'Arduino' not in port.description: ValidPorts.append(port.device)

                if ValidPorts:
                    try:
                        self.SerialPort = serial.Serial(
                            port=ValidPorts[0],
                            baudrate=57600,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            timeout=None
                        )
                    except Exception as e:
                        InstanceErrors.Message = e

                    pygame.mixer.music.load(InstanceSystem.Blop)
                    pygame.mixer.music.play()

                    self.Conditional = False
                    self.Active = True

                    InstanceRadios.Display()
                else: self.Close()

        except Exception as e:
            InstanceErrors.Message = e
            self.Close()

    def Update(self):
        if self.SerialPort:
            try:
                self.CurrentTime = time.time()
                if self.CurrentTime - self.PrevTime >= self.UpdatePeriod:
                    self.SerialPort.timeout = 0.1
                    RawData = self.SerialPort.readline()

                    if RawData:
                        DecodedData = RawData.decode("utf-8")
                        self.DataList = DecodedData.split(",")

                        if len(self.DataList) >= 30:
                            packet, siv, fix, lat, lon, alt, year, month, day, hour, minute, sec, nedN, nedE, nedD, \
                            bat, bat33, bat51, bat52, aint, aext, ptemp, dint, dent, pres, ax, ay, az, pitch, roll, \
                            yaw = self.DataList[:31]

                            if lat != 0: self.Lat = round(float(lat) * .0000001, 6)
                            if lon != 0: self.Lon = round(float(lon) * .0000001, 6)
                            if alt != 0: self.Alt = float(alt) / 1000 * 3.28084

                            self.Timestamp = ''.join([year, month, day, hour, minute, sec])

                            DataRow = [packet, siv, fix, lat, lon, alt, year, month, day, hour, minute, sec, nedN, nedE, nedD, bat, bat33, bat51, bat52, 
                                       aint, aext, ptemp, dint, dent, pres, ax, ay, az, pitch, roll, yaw]

                            if self.FileWrite:
                                try:
                                    RFDDirectory = os.path.join(InstanceSystem.Directory, "Data", "LogRFD")
                                    os.makedirs(RFDDirectory, exist_ok=True)

                                    FileName = f"RFD_{InstanceSystem.Date}.csv"
                                    FilePath = os.path.join(RFDDirectory, FileName)

                                    with open(FilePath, "a", newline='\n') as f:
                                        writer = csv.writer(f, delimiter=',')
                                        writer.writerow(DataRow)
                                except Exception as e:
                                    InstanceErrors.Message = e

                        self.PrevTime = self.CurrentTime

            except Exception as e:
                InstanceErrors.Message = e
                self.Close()

        else:
            self.DataList = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'END\r\n']

    def Close(self):
        self.Conditional = False
        self.Active = False

        if self.SerialPort and self.SerialPort.isOpen(): self.SerialPort.close()

        self.SerialPort = None

InstanceRFD = ClassRFD()

class ClassIridium:
    def __init__(self):
        self.Conditional = self.Active = False
        self.CurrentTime = time.time()
        self.PrevTime = time.time()
        self.UpdatePeriod = 2
        self.FileWrite = True
        self.Timestamp = self.Modem = self.IMEI = None
        self.Lat = self.Lon = self.Alt = self.AscentRate = 0
        self.BaseURL = "https://borealis.rci.montana.edu"
        self.Session = requests.Session()

    def Setup(self):
        self.Conditional = True

        try:
            req = requests.get("{}/api/meta/flights?modem_name={}".format(self.BaseURL, self.Modem))
            req.raise_for_status()

            pygame.mixer.music.load(InstanceSystem.Blop)
            pygame.mixer.music.play()

            InstanceOutput.Message = 'Iridium Connected'
            self.Conditional = False
            self.Active = True

            InstanceRadios.Display()

        except Exception as e:
            InstanceErrors.Message = e
            self.Close()

    def Update(self):
        if self.Active:
            try:
                self.CurrentTime = time.time()
                if self.CurrentTime - self.PrevTime >= self.UpdatePeriod:
                    try:
                        URL = "{}/api/meta/flights?modem_name={}".format(self.BaseURL, self.Modem)
                        Req = self.Session.get(URL)
                        Req.raise_for_status()
                    except Exception as e:
                        InstanceErrors.Message = e

                    ResponseJSON = Req.json()
                    LatestEntry = ResponseJSON[-1]

                    UID = LatestEntry["uid"]
                    URL = "{}/api/flight?uid={}".format(self.BaseURL, UID)

                    try:
                        Req = self.Session.get(URL)
                        Req.raise_for_status()
                        Data = Req.json()
                    except Exception as e:
                        InstanceErrors.Message = e

                    SortedData = sorted(Data["data"], key=lambda x: x[Data["fields"].index("datetime")], reverse=True)
                    Entry = SortedData[0]

                    self.Timestamp = datetime.datetime.fromtimestamp(Entry[Data["fields"].index("datetime")]).strftime("%Y%m%d%H%M%S")

                    try:
                        self.Lat = Entry[Data["fields"].index("latitude")]
                        self.Lon = Entry[Data["fields"].index("longitude")]
                        self.Alt = Entry[Data["fields"].index("altitude")] * 3.28084
                    except Exception as e:
                        InstanceErrors.Message = e

                    if self.FileWrite:
                        try:
                            IridiumDirectory = os.path.join(InstanceSystem.Directory, "Data", "LogIridium")
                            os.makedirs(IridiumDirectory, exist_ok=True)

                            FileName = f"Iridium_{InstanceSystem.Date}.csv"
                            FilePath = os.path.join(IridiumDirectory, FileName)

                            with open(FilePath, "a", newline='\n') as f:
                                Writer = csv.writer(f, delimiter=',')
                                Writer.writerow([self.Timestamp, self.Lat, self.Lon, self.Alt])
                        except Exception as e:
                            InstanceErrors.Message = e

                    self.PrevTime = self.CurrentTime

            except Exception as e:
                InstanceErrors.Message = e
                self.Close()

    def Close(self):
        self.Conditional = False
        self.Active = False

InstanceIridium = ClassIridium()

class ClassAPRS:
    def __init__(self):
        self.Conditional = self.Active = False
        self.CurrentTime = time.time()
        self.PrevTime = time.time()
        self.UpdatePeriod = 1
        self.Callsign = None
        self.FileWrite = True
        self.Timestamp = None
        self.Lat = self.Lon = self.Alt = 0
        self.Session = requests.Session()
        self.Session.headers.update({'Connection': 'keep-alive'})

    def Setup(self):
        self.Conditional = True

        try:
            URL = "https://api.aprs.fi/api/get"

            Parameters = {
                'name': self.Callsign,
                'what': 'loc',
                'apikey': '186239.PvPtIQBgYaOM92d',
                'format': 'xml'
            }

            Response = self.Session.get(URL, params=Parameters, timeout=None)
            Response.raise_for_status()

            if Response.status_code == 200:
                try:
                    root = ET.fromstring(Response.text)

                    entry = root.find('entries/entry')
                    name = entry.find('name').text
                    lat = entry.find('lat').text
                    lng = entry.find('lng').text
                    alt = entry.find('altitude').text
                    symbol = entry.find('symbol').text
                    comment = entry.find('comment').text

                    pygame.mixer.music.load(InstanceSystem.Blop)
                    pygame.mixer.music.play()

                    InstanceOutput.Message = 'APRS Connected'
                    self.Conditional = False
                    self.Active = True

                    InstanceRadios.Display()
                except Exception as e:
                    InstanceErrors.Message = e

        except Exception as e:
            InstanceErrors.Message = e
            self.Close()

    def Update(self):
        if self.Active:
            try:
                self.CurrentTime = time.time()
                if self.CurrentTime - self.PrevTime >= self.UpdatePeriod:
                    URL = "https://api.aprs.fi/api/get"

                    Parameters = {
                        'name': self.Callsign,
                        'what': 'loc',
                        'apikey': '186239.PvPtIQBgYaOM92d',
                        'format': 'xml'
                    }

                    Response = self.Session.get(URL, params=Parameters, timeout=None)
                    Response.raise_for_status()

                    if Response.status_code == 200:
                        root = ET.fromstring(Response.text)
                        entry = root.find('entries/entry')
                        name = entry.find('name').text
                        lat = entry.find('lat').text
                        lon = entry.find('lng').text
                        alt = entry.find('altitude').text
                        symbol = entry.find('symbol').text
                        comment = entry.find('comment').text

                        if lat != 0: self.Lat = round(float(lat), 6)
                        if lon != 0: self.Lon = round(float(lon), 6)
                        if alt != 0: self.Alt = round(float(alt) * 3.28084, 6)

                        self.Timestamp = datetime.datetime.fromtimestamp(int(entry.find('time').text)).strftime("%Y%m%d%H%M%S")

                        DataRow = [name, lat, lon, alt, symbol, comment]

                        if self.FileWrite:
                            try:
                                APRSDirectory = os.path.join(InstanceSystem.Directory, "Data", "LogAPRS")
                                os.makedirs(APRSDirectory, exist_ok=True)

                                FileName = f"APRS_{InstanceSystem.Date}.csv"
                                FilePath = os.path.join(APRSDirectory, FileName)

                                with open(FilePath, "a", newline='\n') as f:
                                    Writer = csv.writer(f, delimiter=',')
                                    Writer.writerow(DataRow)
                            except Exception as e:
                                InstanceErrors.Message = e

                    self.PrevTime = self.CurrentTime
                else:
                    raise requests.exceptions.RequestException

            except Exception as e:
                InstanceErrors.Message = e
                self.Close()

    def Close(self):
        self.Conditional = False
        self.Active = False

InstanceAPRS = ClassAPRS()

class ClassUbiquiti:
    def __init__(self):
        self.Conditional = self.Active = False
        self.IP = self.Port = self.RTSP = self.FPS = 0
        self.Cap = self.PreviousFrameSize = self.PreviousFrameTime = None

    def Setup(self):
        self.Conditional = True

        self.Port = 8554
        self.FPS = 30

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((self.IP, self.Port))
            s.shutdown(socket.SHUT_RDWR)
            s.close()

        except Exception as e:
            InstanceErrors.Message = e
            self.Close()

            return

        self.RTSP = "rtsp://{}:{}/payload".format(self.IP, self.Port)

        try:
            self.Cap = cv2.VideoCapture(self.RTSP)
            if not self.Cap.isOpened():
                self.Close()
            else:
                InstanceOutput.Message = 'Ubiquiti Connected'
                self.Conditional = False
                self.Active = True

                InstanceSystem.ScreenSetting = 'Stream'

        except Exception as e:
            InstanceErrors.Message = e
            self.Close()

    def Update(self):
        if self.Active:
            try:
                CurrentTime = pygame.time.get_ticks()
                if self.PreviousFrameTime is not None and CurrentTime - self.PreviousFrameTime < 1000 // self.FPS:
                    return

                self.PreviousFrameTime = CurrentTime

                Ret, Frame = self.Cap.read()

                if not Ret:
                    self.Cap.release()
                    self.Close()
                    return

                Frame = cv2.resize(Frame, (InstanceScreen.W, InstanceScreen.H))
                Frame = np.rot90(Frame, k=3)

                if PrevFrameSize != (InstanceScreen.W, InstanceScreen.H):
                    Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
                    PrevFrameSize = (InstanceScreen.W, InstanceScreen.H)

                InstanceScreen.Frame = pygame.surfarray.make_surface(Frame)
            except Exception as e:
                InstanceErrors.Message = e
                self.Close()
        else:
            pass

    def Close(self):
        self.Conditional = False
        self.Active = False

        InstanceScreen.Setting = 'Thumb'

InstanceUbiquiti = ClassUbiquiti()

class ClassArduino:
    def __init__(self):
        self.Conditional = self.Active = self.Tracking = False
        self.SerialPort = self.COMPort = None
        self.Time1 = self.Time2 = datetime.datetime.now()

    def Setup(self):
        self.Conditional = True

        try:
            time.sleep(2)

            if InstanceSystem.AutoCOM:
                ArduinoPorts = []
                Ports = serial.tools.list_ports.comports()

                for port in Ports:
                    if ('Arduino' in port.description or
                        (port.vid in {0x2341, 0x2A03} and port.pid in {0x0043, 0x0001})):
                        ArduinoPorts.append(port.device)

                if ArduinoPorts:
                    try:
                        self.SerialPort = serial.Serial(port=ArduinoPorts[0], baudrate=9600, timeout=0.1)

                        pygame.mixer.music.load(InstanceSystem.Blop)
                        pygame.mixer.music.play()

                        InstanceOutput.Message = 'Arduino Connected'
                        self.Conditional = False
                        self.Active = True

                        InstanceRadios.Display()
                    except:
                        pass
                else:
                    self.Close()
            else:
                self.SerialPort = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1) 

                pygame.mixer.music.load(InstanceSystem.Blop)
                pygame.mixer.music.play()

                self.Conditional = False
                self.Active = True

                InstanceRadios.Display()

        except Exception as e:
            InstanceErrors.Message = e
            self.Close()

    def Update(self):
        if self.Active:
            try:
                if self.Tracking:
                    Command = '{:.2f}'.format(InstancePayload.Pan + InstanceCalculations.TweakPan) + "," + '{:.2f}'.format(InstancePayload.Tilt + InstanceCalculations.TweakTilt)
                else:
                    Command = '{:.2f}'.format(InstanceCalculations.TweakPan) + "," + '{:.2f}'.format(InstanceCalculations.TweakTilt)

                self.Time2 = datetime.datetime.now()
                if (self.Time2 - self.Time1) > datetime.timedelta(seconds=1):
                    self.SerialPort.write(Command.encode())
                    self.Time1 = self.Time2

            except Exception as e:
                InstanceErrors.Message = e
                self.Close()

    def Close(self):
        self.Conditional = False
        self.Active = False

        if self.SerialPort and self.SerialPort.isOpen():
            self.SerialPort.close()

        self.SerialPort = None

InstanceArduino = ClassArduino()

class ClassCalculations:
    def __init__(self):
        self.TweakPan = self.TweakTilt = 0
        self.FileWrite = True
        self.AutoTrackerLocation = self.AutoPayloadLocation = False

    def Calculate(self):
        try:
            if not InstanceSystem.Manual:
                WeightedRFD = 0.5
                WeightedAPRS = 0.5

                if InstanceIridium.Active and InstanceIridium.Lat != 0 and InstanceIridium.Lon != 0 and InstanceIridium.Alt != 0:
                    InstancePayload.Lat = InstanceIridium.Lat
                    InstancePayload.Lon = InstanceIridium.Lon
                    InstancePayload.Alt = InstanceIridium.Alt

                    if InstanceRFD.Active and InstanceAPRS.Active:
                        if abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1 and abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1:
                            CorrectedLatRFD = InstanceRFD.Lat - InstanceIridium.Lat
                            CorrectedLonRFD = InstanceRFD.Lon - InstanceIridium.Lon
                            CorrectedRFDAlt = InstanceRFD.Alt - InstanceIridium.Alt

                            CorrectedAPRSLat = InstanceAPRS.Lat - InstanceIridium.Lat
                            CorrectedAPRSLon = InstanceAPRS.Lon - InstanceIridium.Lon
                            CorrectedAPRSAlt = InstanceAPRS.Alt - InstanceIridium.Alt

                            if InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0 and InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0:
                                InstancePayload.Lat = (WeightedRFD * CorrectedLatRFD + WeightedAPRS * CorrectedAPRSLat) / (WeightedRFD + WeightedAPRS)
                                InstancePayload.Lon = (WeightedRFD * CorrectedLonRFD + WeightedAPRS * CorrectedAPRSLon) / (WeightedRFD + WeightedAPRS)
                                InstancePayload.Alt = (WeightedRFD * CorrectedRFDAlt + WeightedAPRS * CorrectedAPRSAlt) / (WeightedRFD + WeightedAPRS)

                        elif abs(InstanceIridium.Lat - InstanceRFD.Lat) >= 0.1 and abs(InstanceIridium.Lat - InstanceAPRS.Lat) < 0.1:
                            InstancePayload.Lat = (InstanceAPRS.Lat + InstanceIridium.Lat) / 2
                            InstancePayload.Lon = (InstanceAPRS.Lon + InstanceIridium.Lon) / 2
                            InstancePayload.Alt = (InstanceAPRS.Alt + InstanceIridium.Alt) / 2
                        elif abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1 and abs(InstanceIridium.Lat - InstanceAPRS.Lat) >= 0.1:
                            InstancePayload.Lat = (InstanceRFD.Lat + InstanceIridium.Lat) / 2
                            InstancePayload.Lon = (InstanceRFD.Lon + InstanceIridium.Lon) / 2
                            InstancePayload.Alt = (InstanceRFD.Alt + InstanceIridium.Alt) / 2
                    elif InstanceRFD.Active and not InstanceAPRS.Active:
                        if InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0 and abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1:
                            InstancePayload.Lat = (InstanceRFD.Lat + InstanceIridium.Lat) / 2
                            InstancePayload.Lon = (InstanceRFD.Lon + InstanceIridium.Lon) / 2
                            InstancePayload.Alt = (InstanceRFD.Alt + InstanceIridium.Alt) / 2
                    elif not InstanceRFD.Active and InstanceAPRS.Active:
                        if InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0 and abs(InstanceIridium.Lat - InstanceAPRS.Lat) < 0.1:
                            InstancePayload.Lat = (InstanceAPRS.Lat + InstanceIridium.Lat) / 2
                            InstancePayload.Lon = (InstanceAPRS.Lon + InstanceIridium.Lon) / 2
                            InstancePayload.Alt = (InstanceAPRS.Alt + InstanceIridium.Alt) / 2

                if not InstanceIridium.Active:
                    if InstanceRFD.Active and not InstanceAPRS.Active and InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0:
                        InstancePayload.Lat = InstanceRFD.Lat
                        InstancePayload.Lon = InstanceRFD.Lon
                        InstancePayload.Alt = InstanceRFD.Alt
                    if not InstanceRFD.Active and InstanceAPRS.Active and InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0:
                        InstancePayload.Lat = InstanceAPRS.Lat
                        InstancePayload.Lon = InstanceAPRS.Lon
                        InstancePayload.Alt = InstanceAPRS.Alt
                    if InstanceRFD.Active and InstanceAPRS.Active and InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0:
                        if InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0:
                            InstancePayload.Lat = (InstanceRFD.Lat + InstanceAPRS.Lat) / 2
                            InstancePayload.Lon = (InstanceRFD.Lon + InstanceAPRS.Lon) / 2
                            InstancePayload.Alt = (InstanceRFD.Alt + InstanceAPRS.Alt) / 2
                        elif InstanceAPRS.Lat == 0 and InstanceAPRS.Lon == 0 and InstanceAPRS.Alt == 0:
                            InstancePayload.Lat = InstanceRFD.Lat
                            InstancePayload.Lon = InstanceRFD.Lon
                            InstancePayload.Alt = InstanceRFD.Alt
                        elif InstanceRFD.Lat == 0 and InstanceRFD.Lon == 0 and InstanceRFD.Alt == 0:
                            InstancePayload.Lat = InstanceAPRS.Lat
                            InstancePayload.Lon = InstanceAPRS.Lon
                            InstancePayload.Alt = InstanceAPRS.Alt

            if self.AutoTrackerLocation:
                try:
                    g = geocoder.ip('me')
                except Exception as e:
                    InstanceErrors.Message = e
                    self.AutoTrackerLocation = False
                if g.ok:
                    try:
                        InstanceTracker.Lat, InstanceTracker.Lon = g.latlng

                        URL = f'https://api.open-elevation.com/api/v1/lookup?locations={InstanceTracker.Lat},{InstanceTracker.Lon}'
                        response = requests.get(URL)
                        if response.status_code == 200:
                            data = response.json()
                            if 'results' in data and len(data['results']) > 0:
                                InstanceTracker.Alt = data['results'][0]['elevation'] if InstanceSystem.MetricUnits else data['results'][0]['elevation'] * 3.28084
                    except Exception as e:
                        InstanceErrors.Message = e
                        self.AutoTrackerLocation = False

                    self.AutoTrackerLocation = False

            if self.AutoPayloadLocation:
                try:
                    g = geocoder.ip('me')
                except Exception as e:
                    InstanceErrors.Message = e
                    self.AutoPayloadLocation = False
                if g.ok:
                    try:
                        InstancePayload.Lat, InstancePayload.Lon = g.latlng

                        URL = f'https://api.open-elevation.com/api/v1/lookup?locations={InstancePayload.Lat},{InstancePayload.Lon}'
                        response = requests.get(URL)
                        if response.status_code == 200:
                            data = response.json()
                            if 'results' in data and len(data['results']) > 0:
                                InstancePayload.Alt = data['results'][0]['elevation'] if InstanceSystem.MetricUnits else data['results'][0]['elevation'] * 3.28084
                    except Exception as e:
                        InstanceErrors.Message = e
                        self.AutoPayloadLocation = False

                    self.AutoPayloadLocation = False

            # Distance Calculation (Tracker to Payload)
            Pos1 = np.array([InstanceTracker.Lat, InstanceTracker.Lon, InstanceTracker.Alt * 0.3048])
            Pos2 = np.array([InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt * 0.3048])

            Lat1, Lon1, Lat2, Lon2 = np.radians([Pos1[0], Pos1[1], Pos2[0], Pos2[1]])
            Alt1, Alt2 = Pos1[2], Pos2[2]

            dLon = Lon2 - Lon1
            dLat = Lat2 - Lat1
            dAlt = Alt2 - Alt1

            R = 6371000.0
            a = np.sin(dLat/2)**2 + np.cos(Lat1) * np.cos(Lat2) * np.sin(dLon/2)**2
            c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
            d = R * c

            InstancePayload.Distance2D = 3958.8 * c
            InstancePayload.Distance3D = np.sqrt(InstancePayload.Distance2D**2 + dAlt**2)

            y = np.sin(dLon) * np.cos(Lat2)
            x = np.cos(Lat1) * np.sin(Lat2) - np.sin(Lat1) * np.cos(Lat2) * np.cos(dLon)

            Alpha = np.arctan2(y, x)
            Alpha = np.where(Alpha < 0, Alpha + 2 * np.pi, Alpha)

            Azimuth = (3 * np.pi / 2 - Alpha) % (2 * np.pi)
            Azimuth = np.where(Azimuth >= np.pi, Azimuth - 2 * np.pi, Azimuth)

            InstancePayload.Pan = (270) - np.degrees(Azimuth)
            InstancePayload.Pan = np.where(InstancePayload.Pan >= 360, InstancePayload.Pan - 360, InstancePayload.Pan)

            InstancePayload.Tilt = np.degrees(np.arctan2(dAlt, d))

            # Tweak Offset
            if self.TweakPan >= 360:
                self.TweakPan -= 360
            if self.TweakTilt >= 360:
                self.TweakTilt -= 360

            if self.TweakPan <= -360:
                self.TweakPan += 360
            if self.TweakTilt <= -360:
                self.TweakTilt += 360

        except Exception as e:
            InstanceErrors.Message = e

    def Log(self):
        HeaderRow = ["Tracker Lat (deg)", "Tracker Lon (deg)", "Tracker Alt (ft)", "Payload Lat (deg)", "Payload Lon (deg)", "Payload Alt (ft)", "2D Distance (mi)", "3D Distance (mi)", "Pan (deg)", "Tilt (deg)"]
        DataRow = [InstanceTracker.Lat, InstanceTracker.Lon, InstanceTracker.Alt, InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt, InstancePayload.Distance2D, InstancePayload.Distance3D, InstancePayload.Pan, InstancePayload.Tilt]

        # Aggregate Data Log
        if self.FileWrite:
            try:
                AggregateDirectory = os.path.join(InstanceSystem.Directory, "Data", "Aggregate")
                os.makedirs(AggregateDirectory, exist_ok=True)

                FileName = f"Aggregate_{InstanceSystem.Date}.csv"
                FilePath = os.path.join(AggregateDirectory, FileName)

                if DataRow[3] != 0 or DataRow[4] != 0 or DataRow[5] != 0:
                    if not os.path.isfile(FilePath):
                        with open(FilePath, "w", newline='') as f:
                            Writer = csv.writer(f, delimiter=',')
                            Writer.writerow(HeaderRow)
                            Writer.writerow(DataRow)
                    else:
                        with open(FilePath, "a", newline='') as f:
                            Writer = csv.writer(f, delimiter=',')
                            Writer.writerow(DataRow)
            except Exception as e:
                InstanceErrors.Message = e

    def Update(self):
        self.Calculate()
        self.Log()

InstanceCalculations = ClassCalculations()

class ClassDescent:
    def __init__(self):
        self.Automatic = False

InstanceDescent = ClassDescent()

class ClassTitle:
    def __init__(self):
        self.NASAX, self.NASAY, self.NASAW, self.NASAH = map(lambda x: (x * InstanceSystem.SF), [530, 60, 230, 200])
        self.NEBPX, self.NEBPY, self.NEBPW, self.NEBPH = map(lambda x: (x * InstanceSystem.SF), [1180, 60, 200, 200])

        self.TitleX, self.TitleY = map(lambda x: (x * InstanceSystem.SF), [960, 135])
        self.SubtitleX, self.SubtitleY = map(lambda x: (x * InstanceSystem.SF), [960, 220])

        self.Logos = [
            (pygame.transform.smoothscale(InstanceSystem.LogoNASA, (self.NASAW, self.NASAH)), (self.NASAX, self.NASAY)),
            (pygame.transform.smoothscale(InstanceSystem.LogoNEBP, (self.NEBPW, self.NEBPH)), (self.NEBPX, self.NEBPY))
        ]

        self.Texts = [
            (InstanceSystem.FontImpact120, "HERMES", InstanceSystem.ColorWhite, (self.TitleX, self.TitleY)),
            (InstanceSystem.FontBahnschrift40, "Video Telemetry GUI", InstanceSystem.ColorWhite, (self.SubtitleX, self.SubtitleY))
        ]

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active:
            for logo, pos in self.Logos:
                InstanceSystem.Window.blit(logo, pos)

            for font, text, color, pos in self.Texts:
                Text = font.render(text, True, color)
                TextRect = Text.get_rect(center=pos)
                InstanceSystem.Window.blit(Text, TextRect)

InstanceTitle = ClassTitle()

class ClassScreen:
    def __init__(self):
        self.X, self.Y, self.W, self.H = map(lambda x: (x * InstanceSystem.SF), [0, 0, 800, 600])
        self.URLX, self.URLY, self.URLW, self.URLH = map(lambda x: (x * InstanceSystem.SF), [600, 830, 500, 25])
        self.FullscreenX, self.FullscreenY, self.FullscreenW, self.FullscreenH, self.FullscreenR = map(lambda x: (x * InstanceSystem.SF), [1300, 330, 45, 45, 30])

        self.FullscreenHover = self.URLHover = False

        self.URL = 'https://www.youtube.com/watch?v=21X5lGlDOfg'
        self.URLUpdate = False

        self.ButtonFullscreen = pygame.transform.smoothscale(InstanceSystem.ButtonFullscreenA, (self.FullscreenW, self.FullscreenH))
        self.Thumb = pygame.transform.scale(pygame.image.load(os.path.join(InstanceSystem.Resources, "Thumb.png")), (self.W, self.H))

    def GetURL(self):
        ydl_opts = {'format': 'best', 'quiet': True}

        if InstanceSystem.ScreenSetting == 'Demo':
            try:
                return os.path.join(InstanceSystem.Resources, "Demo.mp4")
            except Exception as e:
                InstanceErrors.Message = e
                return None
        else:
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(self.URL, download=False)
                    if info['is_live']: InstanceSystem.ScreenSetting = 'Stream'
                    else: InstanceSystem.ScreenSetting = 'Video'
                    return info['url']
            except Exception as e:
                InstanceErrors.Message = e
                try:
                    return os.path.join(InstanceSystem.Resources, "RickAstley.mp4")
                except Exception as e:
                    InstanceErrors.Message = e
                    return None

    def StartStream(self):
        self.StopStream()
        InstanceSystem.VideoURL = self.GetURL()
        if InstanceSystem.VideoURL and (InstanceSystem.ScreenSetting != 'Thumb'):
            try:
                InstanceSystem.Cap = cv2.VideoCapture(InstanceSystem.VideoURL)
                InstanceSystem.VideoStartTime = time.time()
                if "RickAstley" in InstanceSystem.VideoURL:
                    pygame.mixer.music.load(InstanceSystem.RickAstley)
                    pygame.mixer.music.play()
            except Exception as e:
                InstanceErrors.Message = e

        self.URLUpdate = False

    def StopStream(self):
        if InstanceSystem.Cap is not None:
            pygame.mixer.music.stop()
            InstanceSystem.Cap.release()
            InstanceSystem.Cap = None

    def GetFrame(self):
        CurrentTime = time.time()
        if CurrentTime - InstanceSystem.LastFrameTime < 1/30: return

        InstanceSystem.LastFrameTime = CurrentTime
        if InstanceSystem.Cap is not None:
            if InstanceSystem.ScreenSetting == 'Video' or InstanceSystem.ScreenSetting == 'Demo':
                ExpectedPosition = (CurrentTime - InstanceSystem.VideoStartTime) * InstanceSystem.Cap.get(cv2.CAP_PROP_FPS)
                ActualPosition = InstanceSystem.Cap.get(cv2.CAP_PROP_POS_FRAMES)
                if ActualPosition < ExpectedPosition - 5: InstanceSystem.Cap.set(cv2.CAP_PROP_POS_FRAMES, ExpectedPosition)
            elif InstanceSystem.ScreenSetting == 'Stream':
                ExpectedPosition = (CurrentTime - InstanceSystem.VideoStartTime) * InstanceSystem.Cap.get(cv2.CAP_PROP_FPS)
                ActualPosition = InstanceSystem.Cap.get(cv2.CAP_PROP_POS_FRAMES)
                if ActualPosition < ExpectedPosition - 100: self.StartStream()

                Ret, InstanceSystem.Frame = InstanceSystem.Cap.read()
                if not Ret: self.StopStream()

            Ret, InstanceSystem.Frame = InstanceSystem.Cap.read()
            if not Ret: self.StopStream()

    def Display(self):
        if not InstanceSettings.Active:
            if self.URLUpdate:
                self.StopStream()
                if self.URL:
                    InstanceSystem.ScreenSetting = 'Video'
                    self.StartStream()
                else:
                    InstanceSystem.ScreenSetting = 'Thumb'
                self.URLUpdate = False

            if InstanceSystem.ScreenSetting == 'Video' or InstanceSystem.ScreenSetting == 'Demo':
                self.GetFrame()

            if InstanceSystem.ScreenSetting == 'Stream':
                self.GetFrame()

            if InstanceSystem.Fullscreen:
                self.W, self.H = InstanceSystem.W, InstanceSystem.H
                self.X, self.Y = 0, 0
            else:
                self.W, self.H = 800 * InstanceSystem.SF, 600 * InstanceSystem.SF
                self.X, self.Y = InstanceSystem.W / 2 - 400 * InstanceSystem.SF, InstanceSystem.H / 2 - 250 * InstanceSystem.SF

            ScreenOutlineWidth = 6
            ScreenDimensions = (self.X, self.Y, self.W, self.H)

            if InstanceSystem.ScreenSetting == 'Thumb':
                self.Thumb = pygame.transform.scale(pygame.image.load(os.path.join(InstanceSystem.Resources, "Thumb.png")), (self.W, self.H))
                InstanceSystem.Window.blit(self.Thumb, ScreenDimensions)
            elif (InstanceSystem.ScreenSetting != 'Thumb') and InstanceSystem.Frame is not None:
                ScaledFrame = cv2.resize(InstanceSystem.Frame, (int(self.W), int(self.H)))
                FrameRGB = cv2.cvtColor(ScaledFrame, cv2.COLOR_BGR2RGB)
                FrameSurface = pygame.image.frombuffer(FrameRGB.tobytes(), (int(self.W), int(self.H)), "RGB")
                InstanceSystem.Window.blit(FrameSurface, (self.X, self.Y))

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, ScreenDimensions, ScreenOutlineWidth, border_radius=ScreenOutlineWidth)

            if not InstanceSystem.Fullscreen and InstanceNavigator.Enabled:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkGray, (self.URLX, self.URLY, self.URLW, self.URLH))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.URLX, self.URLY, self.URLW, self.URLH), (3 if self.URLHover else 2))

                Text = InstanceSystem.FontBahnschrift15.render("YOUTUBE LIVESTREAM URL", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(midleft=(self.URLX + self.URLW / 10, self.URLY + self.URLH / 2))
                InstanceSystem.Window.blit(Text, TextRect)

            InstanceSystem.Window.blit(self.ButtonFullscreen, (self.FullscreenX - 20 * InstanceSystem.SF, self.FullscreenY - 20 * InstanceSystem.SF))

    def FullscreenClick(self):
        InstanceSystem.Fullscreen = not InstanceSystem.Fullscreen
        InstanceSystem.Refresh()

    def URLClick(self):
        global InputURL
        InputURL = True

InstanceScreen = ClassScreen()

class ClassAltimeter:
    def __init__(self):
        self.Enabled = True

        self.X, self.Y = map(lambda x: (x * InstanceSystem.SF), [1420, 300])

        self.BaseY = self.Y + (600 * InstanceSystem.SF)
        self.x1Long, self.x2Long = self.X + (22 * InstanceSystem.SF), self.X + (37 * InstanceSystem.SF)
        self.x1Short, self.x2Short = self.X + (25 * InstanceSystem.SF), self.X + (35 * InstanceSystem.SF)

        self.LineWidth = 1

        self.LightOn = pygame.transform.smoothscale(InstanceSystem.CircleGreen, (15 * InstanceSystem.SF, 15 * InstanceSystem.SF))
        self.LightOff = pygame.transform.smoothscale(InstanceSystem.CircleRed, (15 * InstanceSystem.SF, 15 * InstanceSystem.SF))

        self.TriangleSize = (10 * InstanceSystem.SF)
        self.TriangleX, self.TriangleY = self.X - self.TriangleSize + (65 * InstanceSystem.SF), [
            self.Y + ((597.5 if InstanceSystem.MetricUnits else 597.5) * InstanceSystem.SF),
            self.Y + ((510.0 if InstanceSystem.MetricUnits else 520.0) * InstanceSystem.SF),
            self.Y + ((338.0 if InstanceSystem.MetricUnits else 345.0) * InstanceSystem.SF),
            self.Y + ((167.0 if InstanceSystem.MetricUnits else 195.0) * InstanceSystem.SF),
            self.Y + ((81.0 if InstanceSystem.MetricUnits else 45.0) * InstanceSystem.SF)
        ]

        self.MilestoneValues = [
            (InstanceSystem.FontBahnschrift20, ("0 m" if InstanceSystem.MetricUnits else "0 ft"), (self.X + (65 * InstanceSystem.SF)), (self.Y + ((604 if InstanceSystem.MetricUnits else 604) * InstanceSystem.SF))),
            (InstanceSystem.FontBahnschrift20, ("5,000 m" if InstanceSystem.MetricUnits else "15,000 ft"), (self.X + (65 * InstanceSystem.SF)), (self.Y + ((517 if InstanceSystem.MetricUnits else 527) * InstanceSystem.SF))),
            (InstanceSystem.FontBahnschrift20, ("15,000 m" if InstanceSystem.MetricUnits else "50,000 ft"), (self.X + (65 * InstanceSystem.SF)), (self.Y + ((345 if InstanceSystem.MetricUnits else 352) * InstanceSystem.SF))),
            (InstanceSystem.FontBahnschrift20, ("25,000 m" if InstanceSystem.MetricUnits else "80,000 ft"), (self.X + (65 * InstanceSystem.SF)), (self.Y + ((174 if InstanceSystem.MetricUnits else 202) * InstanceSystem.SF))),
            (InstanceSystem.FontBahnschrift20, ("30,000 m" if InstanceSystem.MetricUnits else "110,000 ft"), (self.X + (65 * InstanceSystem.SF)), (self.Y + ((88 if InstanceSystem.MetricUnits else 52) * InstanceSystem.SF))),
        ]

        self.MilestoneDescriptors = [
            (InstanceSystem.FontImpact20, "SEA LEVEL", (self.X + (200 * InstanceSystem.SF)), (self.Y + ((601.5 if InstanceSystem.MetricUnits else 601.5) * InstanceSystem.SF))),
            (InstanceSystem.FontImpact20, "HIGH CLOUDS", (self.X + (200 * InstanceSystem.SF)), (self.Y + ((514.5 if InstanceSystem.MetricUnits else 524.5) * InstanceSystem.SF))),
            (InstanceSystem.FontImpact20, "STRATOSPHERE", (self.X + (200 * InstanceSystem.SF)), (self.Y + ((342.5 if InstanceSystem.MetricUnits else 349.5) * InstanceSystem.SF))),
            (InstanceSystem.FontImpact20, "FLOAT ALTITUDE", (self.X + (200 * InstanceSystem.SF)), (self.Y + ((171.5 if InstanceSystem.MetricUnits else 199.5) * InstanceSystem.SF))),
            (InstanceSystem.FontImpact20, "BURST ALTITUDE", (self.X + (200 * InstanceSystem.SF)), (self.Y + ((85.5 if InstanceSystem.MetricUnits else 49.5) * InstanceSystem.SF))),
        ]

        self.CalloutLabels = [
            (InstanceSystem.FontBahnschrift25, "ALTITUDE", (1380 * InstanceSystem.SF), (975 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift25, "DISTANCE", (1600 * InstanceSystem.SF), (975 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "ASCENT RATE", (1380 * InstanceSystem.SF), (1015 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "DOWNRANGE", (1600 * InstanceSystem.SF), (1015 * InstanceSystem.SF))
        ]

        self.CalloutValues = [
            (InstanceSystem.FontBahnschrift20, '', (1505 * InstanceSystem.SF), (977.5 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift20, '', (1725 * InstanceSystem.SF), (977.5 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, '', (1505 * InstanceSystem.SF), (1012.5 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, '', (1725 * InstanceSystem.SF), (1012.5 * InstanceSystem.SF))
        ]

        self.Ticks = []
        if InstanceSystem.MetricUnits:
            self.Ticks = []
            for i in range(0, 35001, 500):
                y = self.BaseY - (i * (600 / 35000) * InstanceSystem.SF)
                if i % 5000 == 0: self.Ticks.append((self.x1Long, self.x2Long, y))
                else: self.Ticks.append((self.x1Short, self.x2Short, y))
        else:
            self.Ticks = []
            for i in range(0, 120001, 1000):
                y = self.BaseY - (i * 0.005 * InstanceSystem.SF)
                if i % 5000 == 0: self.Ticks.append((self.x1Long, self.x2Long, y))
                else: self.Ticks.append((self.x1Short, self.x2Short, y))

        self.Lines = [
            ((self.X + (180 * InstanceSystem.SF), self.Y - (20 * InstanceSystem.SF)), (self.X + (180 * InstanceSystem.SF), self.Y + (620 * InstanceSystem.SF)), 4),
            (((1380 * InstanceSystem.SF), (950 * InstanceSystem.SF)), ((1780 * InstanceSystem.SF), (950 * InstanceSystem.SF)), 1)
        ]

        self.Lights = [
            (self.LightOff, (self.MilestoneValues[1][2] + 85 * InstanceSystem.SF, self.MilestoneValues[1][3] - 7.5 * InstanceSystem.SF)),
            (self.LightOff, (self.MilestoneValues[2][2] + 85 * InstanceSystem.SF, self.MilestoneValues[2][3] - 7.5 * InstanceSystem.SF)),
            (self.LightOff, (self.MilestoneValues[3][2] + 85 * InstanceSystem.SF, self.MilestoneValues[3][3] - 7.5 * InstanceSystem.SF)),
            (self.LightOff, (self.MilestoneValues[4][2] + 85 * InstanceSystem.SF, self.MilestoneValues[4][3] - 7.5 * InstanceSystem.SF))
        ]

        self.Alt1 = 0
        self.Alt2 = 0

        self.Thresholds = [
            (10000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C10000),
            (20000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C20000),
            (30000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C30000),
            (40000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C40000),
            (50000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C50000),
            (60000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C60000),
            (70000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C70000),
            (80000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C80000),
            (90000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C90000),
            (100000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C100000),
            (110000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C110000),
            (120000 * (0.3048 if InstanceSystem.MetricUnits else 1), InstanceSystem.C120000)
        ]

        for _, sound in self.Thresholds: pygame.mixer.music.load(sound)

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active and self.Enabled:
            # Altitude Ticks
            for x1, x2, y in self.Ticks:
                pygame.draw.line(
                    InstanceSystem.Window,
                    InstanceSystem.ColorWhite,
                    (x1, y),
                    (x2, y),
                    self.LineWidth
                )

            # Altitude Indicator
            Indicator = (self.Y + (600 * InstanceSystem.SF) - (0.005 * ((InstancePayload.Alt if not InstanceDemo.Enabled else InstanceDemo.CurrentAltitude) * 1.045 if InstanceSystem.MetricUnits else (InstancePayload.Alt if not InstanceDemo.Enabled else InstanceDemo.CurrentAltitude)) * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, Indicator), (self.X + (60 * InstanceSystem.SF), Indicator), 4)

            # Text Markings
            for font, text, x, y in self.MilestoneValues:
                TextSurface = font.render(text, True, InstanceSystem.ColorWhite)
                TextRect = TextSurface.get_rect(left=x, centery=y)
                InstanceSystem.Window.blit(TextSurface, TextRect)

            for font, text, x, y in self.MilestoneDescriptors:
                TextSurface = font.render(text, True, InstanceSystem.ColorWhite)
                TextRect = TextSurface.get_rect(left=x, centery=y)
                InstanceSystem.Window.blit(TextSurface, TextRect)

            # Triangle Markers
            for coordinate in self.TriangleY:
                pygame.draw.polygon(
                    InstanceSystem.Window, 
                    InstanceSystem.ColorWhite, 
                    [
                        (self.TriangleX, coordinate),
                        (self.TriangleX - self.TriangleSize, coordinate + self.TriangleSize / 2),
                        (self.TriangleX, coordinate + self.TriangleSize)
                    ],
                    0
                )

            # Altimeter Information
            for font, text, x, y in self.CalloutLabels:
                Text = font.render(text, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=x, centery=y)
                InstanceSystem.Window.blit(Text, TextRect)

            AltUnit = "m" if InstanceSystem.MetricUnits else "ft"
            DistUnit = "km" if InstanceSystem.MetricUnits else "mi"
            SpeedUnit = "m/s" if InstanceSystem.MetricUnits else "ft/s"
            AltFactor = 0.3048 if InstanceSystem.MetricUnits else 1
            DistFactor = 1.60934 if InstanceSystem.MetricUnits else 1

            self.CalloutValues[0] = (self.CalloutValues[0][0], "{:.0f} {}".format((InstancePayload.Alt if not InstanceDemo.Enabled else InstanceDemo.CurrentAltitude) * AltFactor, AltUnit), self.CalloutValues[0][2], self.CalloutValues[0][3])
            self.CalloutValues[1] = (self.CalloutValues[1][0], "{:.1f} {}".format(InstancePayload.Distance3D * DistFactor, DistUnit), self.CalloutValues[1][2], self.CalloutValues[1][3])
            self.CalloutValues[2] = (self.CalloutValues[2][0], "{:.1f} {}".format(InstanceIridium.AscentRate * AltFactor, SpeedUnit) if not InstanceSystem.Manual else "0 {}".format(SpeedUnit), self.CalloutValues[2][2], self.CalloutValues[2][3])
            self.CalloutValues[3] = (self.CalloutValues[3][0], "{:.1f} {}".format(InstancePayload.Distance2D * DistFactor, DistUnit), self.CalloutValues[3][2], self.CalloutValues[3][3])

            for font, text, x, y in self.CalloutValues:
                Text = font.render(text, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=x, centery=y)
                InstanceSystem.Window.blit(Text, TextRect)

            for start, end, weight in self.Lines: pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, start, end, weight)

            self.Lights[0] = (self.LightOn if (InstancePayload.Alt if not InstanceDemo.Enabled else InstanceDemo.CurrentAltitude) >= (5000 * 3.28084 if InstanceSystem.MetricUnits else 15000) else self.LightOff, self.Lights[0][1])
            self.Lights[1] = (self.LightOn if (InstancePayload.Alt if not InstanceDemo.Enabled else InstanceDemo.CurrentAltitude) >= (15000 * 3.28084 if InstanceSystem.MetricUnits else 50000) else self.LightOff, self.Lights[1][1])
            self.Lights[2] = (self.LightOn if (InstancePayload.Alt if not InstanceDemo.Enabled else InstanceDemo.CurrentAltitude) >= (25000 * 3.28084 if InstanceSystem.MetricUnits else 80000) else self.LightOff, self.Lights[2][1])
            self.Lights[3] = (self.LightOn if (InstancePayload.Alt if not InstanceDemo.Enabled else InstanceDemo.CurrentAltitude) >= (30000 * 3.28084 if InstanceSystem.MetricUnits else 110000) else self.LightOff, self.Lights[3][1])

            for image, pos in self.Lights: InstanceSystem.Window.blit(image, pos)

        self.Alt1 = self.Alt2
        self.Alt2 = InstancePayload.Alt

        for threshold, sound in self.Thresholds:
            if self.Alt1 < threshold <= self.Alt2 or self.Alt1 >= threshold > self.Alt2:
                pygame.mixer.music.load(sound)
                pygame.mixer.music.play()
                break

InstanceAltimeter = ClassAltimeter()

class ClassNavigator:
    def __init__(self):
        self.Enabled = True

        self.X = self.Y = map(lambda x: (x * InstanceSystem.SF), [0, 0])

        self.PreviousLat = self.PreviousLon = self.PreviousAlt = 0
        self.Mun = self.Cou = self.Sub = ''
        self.Position = "0.00°N, 0.00°E | 0 m" if InstanceSystem.MetricUnits else "0.00°N, 0.00°E | 0 ft"
        self.Location = "Location Not Set"

        self.OSM = True

        self.Rects = [
            ((600 * InstanceSystem.SF), (860 * InstanceSystem.SF), (780 * InstanceSystem.SF), (60 * InstanceSystem.SF), InstanceSystem.ColorDarkGray, 0),
            ((600 * InstanceSystem.SF), (860 * InstanceSystem.SF), (780 * InstanceSystem.SF), (60 * InstanceSystem.SF), InstanceSystem.ColorWhite, 1),
            ((1146 * InstanceSystem.SF), (820 * InstanceSystem.SF), (234 * InstanceSystem.SF), (40 * InstanceSystem.SF), InstanceSystem.ColorDarkGray, 0),
            ((1146 * InstanceSystem.SF), (820 * InstanceSystem.SF), (234 * InstanceSystem.SF), (40 * InstanceSystem.SF), InstanceSystem.ColorWhite, 1),
            ((1147 * InstanceSystem.SF), (840 * InstanceSystem.SF), (234 * InstanceSystem.SF), (50 * InstanceSystem.SF), InstanceSystem.ColorDarkGray, 0)
        ]

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active and self.Enabled:
            if (
                self.PreviousLat is None
                or self.PreviousLon is None
                or self.PreviousAlt is None
                or abs(InstancePayload.Lat - self.PreviousLat) >= 0.1
                or abs(InstancePayload.Lon - self.PreviousLon) >= 0.1
                or abs(InstancePayload.Alt - self.PreviousAlt) >= 100
            ):
                OSMData = None
                if self.OSM:
                    try:
                        Headers = {'User-Agent': 'jrcook394'}

                        Response = requests.get("https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}".format(InstancePayload.Lat, InstancePayload.Lon), headers=Headers)
                        Response.raise_for_status()
                        OSMData = Response.json()

                        if OSMData is not None:
                            Address = OSMData.get("address", {})
                            self.Mun = Address.get("town") or Address.get("city") or Address.get("nearest_town") or Address.get("nearest_city") or "Unknown"
                            self.Cou = Address.get("county")
                            self.Sub = Address.get("ISO3166-2-lvl4", "").split("-")[-1].strip()

                    except Exception as e:
                        InstanceErrors.Message = e
                        self.Location = "Location Unavailable"
                        self.OSM = False

                LatDirection = "N" if InstancePayload.Lat >= 0 else "S"
                LonDirection = "E" if InstancePayload.Lon >= 0 else "W"
                Altitude = InstancePayload.Alt * 0.3048 if InstanceSystem.MetricUnits else InstancePayload.Alt

                self.Position = "{:.2f}°{}, {:.2f}°{} | {:.0f} {}".format(abs(InstancePayload.Lat), LatDirection, abs(InstancePayload.Lon), LonDirection, Altitude, "m" if InstanceSystem.MetricUnits else "ft")

                if OSMData is not None:
                    if self.Mun != "Unknown":
                        if self.Sub: self.Location = "{}, {}".format(self.Mun, self.Sub)
                        else: self.Location = self.Mun
                    else:
                        if self.Sub: self.Location = "{}, {}".format(self.Cou if self.Cou else "Rural", self.Sub)
                        else: self.Location = "Location Not Set"
                else:
                    if InstancePayload.Lat != 0 and InstancePayload.Lon != 0 and InstancePayload.Lon != 0: self.Location = "Location Unavailable"
                    else: self.Location = "Location Not Set"

                if len(self.Location) > 20: self.Location = self.Location[:20] + "..."

                self.PreviousLat, self.PreviousLon, self.PreviousAlt = InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt

            if InstancePayload.Lat == 0 and InstancePayload.Lon == 0 and InstancePayload.Alt == 0: self.Position = "0.00°N, 0.00°E | 0 {}".format("m" if InstanceSystem.MetricUnits else "ft")

            # Coordinate and Altitude Display
            Text = InstanceSystem.FontBahnschrift25.render(self.Position, True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(midright=(1372.5 * InstanceSystem.SF, 845 * InstanceSystem.SF))

            self.Rects[2] = ((1360 * InstanceSystem.SF - Text.get_width()), self.Rects[2][1], (20 * InstanceSystem.SF + Text.get_width()), self.Rects[2][3], self.Rects[2][4], self.Rects[2][5])
            self.Rects[3] = ((1360 * InstanceSystem.SF - Text.get_width()), self.Rects[3][1], (20 * InstanceSystem.SF + Text.get_width()), self.Rects[3][3], self.Rects[3][4], self.Rects[3][5])
            self.Rects[4] = ((1361 * InstanceSystem.SF - Text.get_width()), self.Rects[4][1], (18 * InstanceSystem.SF + Text.get_width()), self.Rects[4][3], self.Rects[4][4], self.Rects[4][5])

            for x, y, w, h, color, weight in self.Rects: pygame.draw.rect(InstanceSystem.Window, color, (x, y, w, h), weight)

            InstanceSystem.Window.blit(Text, TextRect)

            # Geographic Location Display
            Text = InstanceSystem.FontBahnschrift40.render(self.Location if self.Location else "Location Unavailable", True, InstanceSystem.ColorWhite) if self.Location else InstanceSystem.FontBahnschrift30.render(self.Location if self.Location else "Location Unavailable", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(midright=(1372.5 * InstanceSystem.SF, 892.5 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

InstanceNavigator = ClassNavigator()

class ClassCompass:
    def __init__(self):
        self.Enabled = True

        self.X, self.Y, self.R = map(lambda x: (x * InstanceSystem.SF), [560, 890, 65])

        self.CompassHover = False

        if InstanceSystem.DarkMode:
            self.Shape1 = InstanceSystem.CircleWhite
            self.Shape2 = InstanceSystem.CircleBlack
        else:
            self.Shape1 = InstanceSystem.CircleBlack
            self.Shape2 = InstanceSystem.CircleWhite

        self.Shape1 = pygame.transform.smoothscale(self.Shape1, ((160 * InstanceSystem.SF), (160 * InstanceSystem.SF)))
        self.Shape2 = pygame.transform.smoothscale(self.Shape2, ((155 * InstanceSystem.SF), (155 * InstanceSystem.SF)))

        self.LargeTicks = 24
        self.SmallTicks = 3

        self.LargeAngle = 2 * math.pi / self.LargeTicks
        self.SmallAngle = self.LargeAngle / self.SmallTicks

        self.Directions = [
            ("N", (self.X, self.Y - (40 * InstanceSystem.SF))),
            ("E", (self.X + (40 * InstanceSystem.SF), self.Y)),
            ("S", (self.X, self.Y + (40 * InstanceSystem.SF))),
            ("W", (self.X - (40 * InstanceSystem.SF), self.Y)),
        ]

        self.Texts = {}
        for dir, pos in self.Directions:
            Text = InstanceSystem.FontBahnschrift20.render(dir, True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=pos)
            self.Texts[dir] = (Text, TextRect)

        (self.Shape1, self.Shape2) = (InstanceSystem.CircleWhite, InstanceSystem.CircleBlack) if InstanceSystem.DarkMode else (InstanceSystem.CircleBlack, InstanceSystem.CircleWhite)

        self.Shape1 = pygame.transform.smoothscale(self.Shape1, ((160 * InstanceSystem.SF), (160 * InstanceSystem.SF)))
        self.Shape2 = pygame.transform.smoothscale(self.Shape2, ((155 * InstanceSystem.SF), (155 * InstanceSystem.SF)))

        self.PrevTrackerLat = self.PrevTrackerLon = self.PrevTrackerAlt = 0
        self.PrevPayloadLat = self.PrevPayloadLon = self.PrevPayloadAlt = 0

        self.CompassNeedleX = self.CompassNeedleY = self.CompassBaseX = self.CompassBaseY = 0
        self.NeedleLength = 60 * InstanceSystem.SF
        self.Setting = 1

        self.CompassNeedleX, self.CompassNeedleY, self.CompassBaseX, self.CompassBaseY = self.PointNeedle(0, self.NeedleLength, self.X, self.Y)

    def PointNeedle(self, Pan, NeedleLength, x, y):
        Angle = math.radians(Pan) - math.pi / 2
        NeedleX = x + math.cos(Angle) * NeedleLength
        NeedleY = y + math.sin(Angle) * NeedleLength
        BaseX = x - math.cos(Angle) * 10 * InstanceSystem.SF
        BaseY = y - math.sin(Angle) * 10 * InstanceSystem.SF
        return NeedleX, NeedleY, BaseX, BaseY

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active and self.Enabled:
            # Compass Outline
            InstanceSystem.Window.blit(self.Shape1, ((self.X - 80 * InstanceSystem.SF), (self.X + 250 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(self.Shape2, ((self.X - 77.5 * InstanceSystem.SF), (self.X + 252.5 * InstanceSystem.SF)))

            # Large Circumferential Ticks
            for i in range(self.LargeTicks):
                pygame.draw.aaline(
                    InstanceSystem.Window,
                    InstanceSystem.ColorWhite,
                    ((self.X + math.cos(self.LargeAngle * i) * (60 * InstanceSystem.SF)), (self.Y + math.sin(self.LargeAngle * i) * (60 * InstanceSystem.SF))),
                    ((self.X + math.cos(self.LargeAngle * i) * (70 * InstanceSystem.SF)), (self.Y + math.sin(self.LargeAngle * i) * (70 * InstanceSystem.SF)))
                )

            # Small Circumferential Ticks
            for i in range(self.LargeTicks * self.SmallTicks):
                pygame.draw.aaline(
                    InstanceSystem.Window,
                    InstanceSystem.ColorWhite,
                    ((self.X + math.cos(self.SmallAngle * i) * (70 * InstanceSystem.SF)), (self.Y + math.sin(self.SmallAngle * i) * (70 * InstanceSystem.SF))),
                    ((self.X + math.cos(self.SmallAngle * i) * (72 * InstanceSystem.SF)), (self.Y + math.sin(self.SmallAngle * i) * (72 * InstanceSystem.SF)))
                )

            # Cardinal Directions
            for dir, (text, rect) in self.Texts.items(): InstanceSystem.Window.blit(text, rect)

            # Compass Needle
            Text = InstanceSystem.FontBahnschrift25.render("Tracker > Payload", True, InstanceSystem.ColorWhite)
            Pan = InstancePayload.Pan

            if self.Setting == 2:
                Text = InstanceSystem.FontBahnschrift25.render("Payload > Target", True, InstanceSystem.ColorWhite)
                Pan = InstanceTarget.Pan

            if self.PrevPayloadLat != InstancePayload.Lat or self.PrevTrackerLat != InstanceTracker.Lat:
                self.CompassNeedleX, self.CompassNeedleY, self.CompassBaseX, self.CompassBaseY = self.PointNeedle(Pan, self.NeedleLength, self.X, self.Y)
                self.PrevTrackerLat, self.PrevTrackerLon, self.PrevTrackerAlt = InstanceTracker.Lat, InstanceTracker.Lon, InstanceTracker.Alt
                self.PrevPayloadLat, self.PrevPayloadLon, self.PrevPayloadAlt = InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt

            if InstanceNavigator.Enabled:
                TextRect = Text.get_rect(left=(650 * InstanceSystem.SF), centery=(880 * InstanceSystem.SF))
                InstanceSystem.Window.blit(Text, TextRect)

                Text = InstanceSystem.FontBahnschrift15.render("Click Compass to Change", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=(650 * InstanceSystem.SF), centery=(905 * InstanceSystem.SF))
                InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.aaline(InstanceSystem.Window, (255, 0, 0), (self.CompassBaseX, self.CompassBaseY), (self.CompassNeedleX, self.CompassNeedleY))

            # Compass Center
            CompassCenter = pygame.transform.smoothscale(InstanceSystem.CircleWhite, ((20 * InstanceSystem.SF), (20 * InstanceSystem.SF))) if InstanceSystem.DarkMode else pygame.transform.smoothscale(InstanceSystem.CircleBlack, ((20 * InstanceSystem.SF), (20 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(CompassCenter, ((self.X - 9 * InstanceSystem.SF), (self.X + 320 * InstanceSystem.SF)))

    def CompassClick(self):
        self.Setting += 1 if self.Setting < 2 else 1

InstanceCompass = ClassCompass()

class ClassTimer:
    def __init__(self):
            self.Enabled = True

            self.X, self.Y, self.W, self.H = map(lambda x: (x * InstanceSystem.SF), [810, 270, 300, 95])

            self.Previous = self.Current = None
            self.LT = self.UTC = self.MET = None
            self.LocalTime = False
            self.TimerHover = False

    def Display(self):
        try:
            # Launch Timer Start
            if InstanceLaunch.Launched and InstanceLaunch.LaunchTime is None:
                InstanceLaunch.LaunchTime = datetime.datetime.now().strftime("%H:%M:%S")
                InstanceLaunch.StartTime = datetime.datetime.now()

                CountdownMapping = {
                    InstanceLaunch.Countdown1: (InstanceSystem.Launch10, "T  - 00:00:10"),
                    InstanceLaunch.Countdown2: (InstanceSystem.Launch30, "T  - 00:00:30"),
                    InstanceLaunch.Countdown3: (InstanceSystem.Launch60, "T  - 00:01:00"),
                }

                for setting, (music, countdown) in CountdownMapping.items():
                    if setting:
                        pygame.mixer.music.load(music)
                        pygame.mixer.music.play()
                        self.MET = countdown
                        break
                else:
                    pygame.mixer.music.load(InstanceSystem.Launch00)
                    pygame.mixer.music.play()
                    self.MET = "T  - 00:00:00"

                InstanceOutput.Message = "Launch Timer Commenced"

            # Launch Timer Halt
            if not InstanceLaunch.Launched:
                InstanceLaunch.LaunchTime = None
                InstanceLaunch.StartTime = None

                self.MET = "T  - 00:00:00"

            # Update MET and UTC
            LocalTime = datetime.datetime.now()
            CurrentUTC = LocalTime.astimezone(datetime.timezone.utc)

            Time = LocalTime if self.LocalTime else CurrentUTC

            if self.Previous is None or Time.second != self.Previous:
                self.Previous = Time.second

                if InstanceLaunch.Launched:
                    Elapsed = datetime.datetime.now() - InstanceLaunch.StartTime
                    S = Elapsed.total_seconds()

                    CountdownTime = 10 if InstanceLaunch.Countdown1 else 30 if InstanceLaunch.Countdown2 else 60 if InstanceLaunch.Countdown3 else 0

                    if S < CountdownTime:
                        S = CountdownTime - S
                        sign = " -"
                    else:
                        S = S - CountdownTime + 1
                        sign = "+"

                    H = int(S / 3600)
                    M = int((S % 3600) / 60)
                    S = int(S % 60)

                    self.MET = "T {} {:02d}:{:02d}:{:02d}".format(sign, H, M, S)

            self.LT = LocalTime.strftime("%H:%M:%S")
            self.UTC = CurrentUTC.strftime("%H:%M:%S")

            if not InstanceSystem.Fullscreen and not InstanceSettings.Active and self.Enabled:
                # Text Background
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkGray, (self.X, self.Y, self.W, self.H))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y, self.W, self.H), (3 if self.TimerHover else 2))

                # Text Boxes
                CountdownTimes = {0: "00:00:00", 1: "00:00:10", 2: "00:00:30", 3: "00:01:00"}
                CountdownIndex = InstanceLaunch.Countdown1 + InstanceLaunch.Countdown2 * 2 + InstanceLaunch.Countdown3 * 3
                CountdownValue = CountdownTimes.get(CountdownIndex, "00:00:00")

                Text = InstanceSystem.FontCalibri50.render("T  - " + CountdownValue, True, InstanceSystem.ColorWhite) if not InstanceLaunch.Launched else InstanceSystem.FontCalibri50.render(self.MET, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(center=((self.X + self.W / 2), (self.Y + self.H / 2.75)))
                InstanceSystem.Window.blit(Text, TextRect)

                Text = InstanceSystem.FontCalibri30.render((datetime.datetime.now().astimezone(get_localzone()).tzname() + " " + self.LT if self.LocalTime else "UTC " + self.UTC), True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(center=((self.X + self.W / 2), (self.Y + self.H / 1.25)))
                InstanceSystem.Window.blit(Text, TextRect)

        except Exception as e:
            InstanceErrors.Message = e
            InstanceOutput.Message = 'Launch Timer Error'

    def TimerClick(self):
        self.LocalTime = not self.LocalTime

InstanceTimer = ClassTimer()

class ClassRadios:
    def __init__(self):
        self.X, self.Y, self.W, self.H, self.S = map(lambda x: (x * InstanceSystem.SF), [200, 350, 60, 30, 70])

        self.RFDX, self.IridiumX, self.APRSX, self.UbiquitiX, self.ArduinoX = map(lambda x: (x * InstanceSystem.SF), [135, 205, 275, 345, 415])
        self.RFDY, self.IridiumY, self.APRSY, self.UbiquitiY, self.ArduinoY = map(lambda x: (x * InstanceSystem.SF), [350, 350, 350, 350, 350])
        self.RFDW, self.IridiumW, self.APRSW, self.UbiquitiW, self.ArduinoW = map(lambda x: (x * InstanceSystem.SF), [60, 60, 60, 60, 60])
        self.RFDH, self.IridiumH, self.APRSH, self.UbiquitiH, self.ArduinoH = map(lambda x: (x * InstanceSystem.SF), [30, 30, 30, 30, 30])

        self.RFDHover = self.IridiumHover = self.APRSHover = self.UbiquitiHover = self.ArduinoHover = False

        self.Buttons = [
            (self.RFDX, self.RFDY, self.RFDW, self.RFDH),
            (self.IridiumX, self.IridiumY, self.IridiumW, self.IridiumH),
            (self.APRSX, self.APRSY, self.APRSW, self.APRSH),
            (self.UbiquitiX, self.UbiquitiY, self.UbiquitiW, self.UbiquitiH),
            (self.ArduinoX, self.ArduinoY, self.ArduinoW, self.ArduinoH)
        ]

        self.Rectangles = [
            (self.RFDX, self.RFDY + 1.5 * self.RFDH, self.RFDW, self.RFDH / 1.5),
            (self.IridiumX, self.IridiumY + 1.5 * self.IridiumH, self.IridiumW, self.IridiumH / 1.5),
            (self.APRSX, self.APRSY + 1.5 * self.APRSH, self.APRSW, self.APRSH / 1.5),
            (self.UbiquitiX, self.UbiquitiY + 1.5 * self.UbiquitiH, self.UbiquitiW, self.UbiquitiH / 1.5),
            (self.ArduinoX, self.ArduinoY + 1.5 * self.ArduinoH, self.ArduinoW, self.ArduinoH / 1.5)
        ]

        self.Names = ["RFD", "Iridium", "APRS", "Ubiquiti", "Arduino"]
        self.Hovers = [self.RFDHover, self.IridiumHover, self.APRSHover, self.UbiquitiHover, self.ArduinoHover]
        self.Colors = [InstanceSystem.ColorGreen, InstanceSystem.ColorLightRed]
        self.Messages = [f'{name} Connected' if instance.Active else '' for name, instance in zip(self.Names, [InstanceRFD, InstanceIridium, InstanceAPRS, InstanceUbiquiti, InstanceArduino])]

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active:
            Text = InstanceSystem.FontBahnschrift25.render("RADIO/SERIAL CONNECTIVITY", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X + 105 * InstanceSystem.SF, 320 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

            Connections = [InstanceRFD.Active, InstanceIridium.Active, InstanceAPRS.Active, InstanceUbiquiti.Active, InstanceArduino.Active]
            Hovers = [self.RFDHover, self.IridiumHover, self.APRSHover, self.UbiquitiHover, self.ArduinoHover]

            for i in range(len(self.Buttons)):
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if Connections[i] else InstanceSystem.ColorLightRed), self.Buttons[i])
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorWhite if Hovers[i] else InstanceSystem.ColorDarkGray), self.Buttons[i], 3)
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkGray, self.Rectangles[i])

            def FormatTimestamp(Radio):
                if Radio.Active and Radio.Timestamp is not None: return f"Last Ping: {Radio.Timestamp[:4]}-{Radio.Timestamp[4:6]}-{Radio.Timestamp[6:8]} ({Radio.Timestamp[8:10]}:{Radio.Timestamp[10:12]}:{Radio.Timestamp[12:14]})"
                else: return ''

            self.Messages = [
                FormatTimestamp(InstanceRFD),
                FormatTimestamp(InstanceIridium),
                FormatTimestamp(InstanceAPRS),
                'Ubiquiti Connected' if InstanceUbiquiti.Active else '',
                'Arduino Connected' if InstanceArduino.Active else ''
            ]

            Message = next((self.Messages[i] for i in range(len(self.Buttons)) if self.Hovers[i]), None)
            if Message: InstanceOutput.Message = Message

            for i in range(len(self.Buttons)):
                Text = InstanceSystem.FontBahnschrift15.render(self.Names[i], True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(center=(self.Buttons[i][0] + self.W / 2, self.Y + 1.8 * self.H))
                InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - (65 * InstanceSystem.SF), self.Y - (12.5 * InstanceSystem.SF)), (self.X + (275 * InstanceSystem.SF), self.Y - (12.5 * InstanceSystem.SF)), 3)
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - (65 * InstanceSystem.SF), self.Y + (80 * InstanceSystem.SF)), (self.X + (275 * InstanceSystem.SF), self.Y + (80 * InstanceSystem.SF)), 3)

    def RFDClick(self):
        if InstanceRFD.Active:
            InstanceRFD.Close()
        else:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkRed, self.Buttons[0])
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, self.Buttons[0], 3)
            InstanceRFD.Setup()

    def IridiumClick(self):
        if InstanceIridium.Active:
            InstanceIridium.Close()
        else:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkRed, self.Buttons[1])
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, self.Buttons[1], 3)
            InstanceIridium.Setup()

    def APRSClick(self):
        if InstanceAPRS.Active:
            InstanceAPRS.Close()
        else:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkRed, self.Buttons[2])
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, self.Buttons[2], 3)
            InstanceAPRS.Setup()

    def UbiquitiClick(self):
        if InstanceUbiquiti.Active:
            InstanceUbiquiti.Close()
        else:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkRed, self.Buttons[3])
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, self.Buttons[3], 3)
            InstanceUbiquiti.Setup()

    def ArduinoClick(self):
        if InstanceArduino.Active:
            InstanceArduino.Close()
        else:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkRed, self.Buttons[4])
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, self.Buttons[4], 3)
            InstanceArduino.Setup()

InstanceRadios = ClassRadios()

class ClassOutput:
    def __init__(self):
        self.X, self.Y, self.W, self.H = map(lambda x: (x * InstanceSystem.SF), [135, 450, 340, 30])
        self.Message = ''
        self.RefreshTime = time.time()

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkGray, (self.X, self.Y, self.W, self.H))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y, self.W, self.H), 1)

            Text = InstanceSystem.FontBahnschrift20.render(self.Message, True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X + self.W / 2, self.Y + self.H / 2))
            InstanceSystem.Window.blit(Text, TextRect)

            if time.time() - self.RefreshTime > 10:
                self.Message = ''
                self.RefreshTime = time.time()

InstanceOutput = ClassOutput()

class ClassControls:
    def __init__(self):
        self.X, self.Y, self.R = map(lambda x: (x * InstanceSystem.SF), [300, 600, 50])

        self.TriangleHeight = math.sqrt(3) * self.R / 2

        self.ControlCenterX, self.ControlCenterY, self.ControlCenterR = self.X, self.Y, self.R
        self.ControlUpX, self.ControlUpY, self.ControlUpW, self.ControlUpH = (self.X - 0.75 * self.R), (self.Y - 2 * self.TriangleHeight), (1.5 * self.R), (1.5 * self.TriangleHeight)
        self.ControlLeftX, self.ControlLeftY, self.ControlLeftW, self.ControlLeftH = (self.X - 2 * self.TriangleHeight), (self.Y - 0.75 * self.R), (1.5 * self.TriangleHeight), (1.5 * self.R)
        self.ControlDownX, self.ControlDownY, self.ControlDownW, self.ControlDownH = (self.X - 0.75 * self.R), (self.Y + self.TriangleHeight), (1.5 * self.R), (1.5 * self.TriangleHeight)
        self.ControlRightX, self.ControlRightY, self.ControlRightW, self.ControlRightH = (self.X + self.TriangleHeight), (self.Y - 0.75 * self.R), (1.5 * self.TriangleHeight), (1.5 * self.R)

        self.ClearAnglesX, self.ClearAnglesY, self.ClearAnglesW, self.ClearAnglesH = map(lambda x: (x * InstanceSystem.SF), [150, 1030, 100, 30])
        self.ClearTweaksX, self.ClearTweaksY, self.ClearTweaksW, self.ClearTweaksH = map(lambda x: (x * InstanceSystem.SF), [255, 1030, 100, 30])

        self.ControlCenterHover = self.ControlUpHover = self.ControlLeftHover = self.ControlDownHover = self.ControlRightHover = False
        self.ClearAnglesHover = self.ClearTweaksHover = False

        self.Lines = [
            ((self.X - 20 * InstanceSystem.SF, self.Y - 20 * InstanceSystem.SF), (self.X - 70 * InstanceSystem.SF, self.Y - 70 * InstanceSystem.SF)),
            ((self.X - 160 * InstanceSystem.SF, self.Y - 70 * InstanceSystem.SF), (self.X - 60 * InstanceSystem.SF, self.Y - 70 * InstanceSystem.SF)),
            ((self.X - 77 * InstanceSystem.SF, self.Y + 7 * InstanceSystem.SF), (self.X - 120 * InstanceSystem.SF, self.Y + 50 * InstanceSystem.SF)),
            ((self.X - 260 * InstanceSystem.SF, self.Y + 50 * InstanceSystem.SF), (self.X - 110 * InstanceSystem.SF, self.Y + 50 * InstanceSystem.SF)),
            ((self.X - 150 * InstanceSystem.SF, self.Y + 140 * InstanceSystem.SF), (self.X - 150 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF)),
            ((self.X + 150 * InstanceSystem.SF, self.Y + 140 * InstanceSystem.SF), (self.X + 150 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF)),
            ((self.X - 155 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF), (self.X - 150 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF)),
            ((self.X + 150 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF), (self.X + 155 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF)),
            ((self.X - 150 * InstanceSystem.SF, self.Y + 200 * InstanceSystem.SF), (self.X + 150 * InstanceSystem.SF, self.Y + 200 * InstanceSystem.SF)),
            ((self.X, self.Y + 200 * InstanceSystem.SF), (self.X, self.Y + 210 * InstanceSystem.SF))
        ]

        self.Labels = [
            ("Pan: ", (self.X - 120 * InstanceSystem.SF, self.Y + 150 * InstanceSystem.SF)),
            ("Tilt: ", (self.X + 45 * InstanceSystem.SF, self.Y + 150 * InstanceSystem.SF))
        ]

        self.Shapes = [
            (InstanceSystem.ColorDarkGray, (self.ClearAnglesX, self.ClearAnglesY, self.ClearAnglesW, self.ClearAnglesH), 0),
            (InstanceSystem.ColorDarkGray, (self.ClearTweaksX, self.ClearTweaksY, self.ClearTweaksW, self.ClearTweaksH), 0),
            (InstanceSystem.ColorWhite, (self.ClearAnglesX, self.ClearAnglesY, self.ClearAnglesW, self.ClearAnglesH), 1),
            (InstanceSystem.ColorWhite, (self.ClearTweaksX, self.ClearTweaksY, self.ClearTweaksW, self.ClearTweaksH), 1)
        ]

        self.Texts = [
            ("TRACKING", InstanceSystem.FontBahnschrift20, InstanceSystem.ColorWhite, (self.X - 160 * InstanceSystem.SF, self.Y - (80 * InstanceSystem.SF)), 'midleft'),
            ("TWEAK OFFSET", InstanceSystem.FontBahnschrift20, InstanceSystem.ColorWhite, (self.X - 260 * InstanceSystem.SF, self.Y + 40 * InstanceSystem.SF), 'midleft'),
            ("POINTING ANGLES", InstanceSystem.FontBahnschrift20, InstanceSystem.ColorWhite, (self.X, self.Y + 230 * InstanceSystem.SF), 'center'),
            ("CLEAR ANGLES", InstanceSystem.FontBahnschrift13, InstanceSystem.ColorWhite, (self.ClearAnglesX + self.ClearAnglesW / 2, self.ClearAnglesY + self.ClearAnglesH / 2), 'center'),
            ("CLEAR TWEAKS", InstanceSystem.FontBahnschrift13, InstanceSystem.ColorWhite, (self.ClearTweaksX + self.ClearTweaksW / 2, self.ClearTweaksY + self.ClearTweaksH / 2), 'center')
        ]

        self.Images = [
            (pygame.transform.smoothscale(InstanceSystem.DPad, (170 * InstanceSystem.SF, 170 * InstanceSystem.SF)), ((self.X - 85 * InstanceSystem.SF), (self.Y - 85 * InstanceSystem.SF)), True),
            (pygame.transform.smoothscale(InstanceSystem.DPadUp, (170 * InstanceSystem.SF, 170 * InstanceSystem.SF)), ((self.X - 85 * InstanceSystem.SF), (self.Y - 85 * InstanceSystem.SF)), False),
            (pygame.transform.smoothscale(InstanceSystem.DPadLeft, (170 * InstanceSystem.SF, 170 * InstanceSystem.SF)), ((self.X - 85 * InstanceSystem.SF), (self.Y - 85 * InstanceSystem.SF)), False),
            (pygame.transform.smoothscale(InstanceSystem.DPadDown, (170 * InstanceSystem.SF, 170 * InstanceSystem.SF)), ((self.X - 85 * InstanceSystem.SF), (self.Y - 85 * InstanceSystem.SF)), False),
            (pygame.transform.smoothscale(InstanceSystem.DPadRight, (170 * InstanceSystem.SF, 170 * InstanceSystem.SF)), ((self.X - 85 * InstanceSystem.SF), (self.Y - 85 * InstanceSystem.SF)), False),
            (pygame.transform.smoothscale(InstanceSystem.DPadCenter, (100 * InstanceSystem.SF, 100 * InstanceSystem.SF)), ((self.ControlCenterX - self.ControlCenterR), (self.ControlCenterY - self.ControlCenterR)), False)
        ]

        self.Angles = [
            ("", (self.X - 60 * InstanceSystem.SF, self.Y + 145 * InstanceSystem.SF)),
            ("", (self.X + 95 * InstanceSystem.SF, self.Y + 145 * InstanceSystem.SF))
        ]

        self.Tweaks = [
            ("", (self.X - 120 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF)),
            ("", (self.X + 45 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF))
        ]

        self.Totals = [
            ("", InstanceSystem.FontBahnschrift25, InstanceSystem.ColorWhite, (self.X - 165 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF), 'midright'),
            ("", InstanceSystem.FontBahnschrift25, InstanceSystem.ColorWhite, (self.X + 165 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF), 'midleft')
        ]

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active:
            self.Images[1] = (self.Images[1][0], self.Images[1][1], self.ControlUpHover)
            self.Images[2] = (self.Images[2][0], self.Images[2][1], self.ControlLeftHover)
            self.Images[3] = (self.Images[3][0], self.Images[3][1], self.ControlDownHover)
            self.Images[4] = (self.Images[4][0], self.Images[4][1], self.ControlRightHover)
            self.Images[5] = (self.Images[5][0], self.Images[5][1], self.ControlCenterHover)

            # D-Pad Display
            for image, pos, condition in self.Images:
                if condition: InstanceSystem.Window.blit(image, pos)

            # Angle Labels
            for label, pos in self.Labels:
                Text = InstanceSystem.FontBahnschrift30.render(label, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(midleft=(pos[0], pos[1]))
                InstanceSystem.Window.blit(Text, TextRect)

            # Pointing Angles
            self.Angles[0] = (f"{int(np.round(InstancePayload.Pan))}°", self.Angles[0][1])
            self.Angles[1] = (f"{int(np.round(InstancePayload.Tilt))}°", self.Angles[1][1])

            for angle, pos in self.Angles:
                Text = InstanceSystem.FontImpact30.render(angle, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(midleft=(pos[0], pos[1]))
                InstanceSystem.Window.blit(Text, TextRect)

            # Tweak Angles
            self.Tweaks[0] = (f"Tweak: {int(np.round(InstanceCalculations.TweakPan))}°", self.Tweaks[0][1])
            self.Tweaks[1] = (f"Tweak: {int(np.round(InstanceCalculations.TweakTilt))}°", self.Tweaks[1][1])

            for tweak, pos in self.Tweaks:
                Text = InstanceSystem.FontCalibri20.render(tweak, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(midleft=(pos[0], pos[1]))
                InstanceSystem.Window.blit(Text, TextRect)

            # Total Angles
            TotalPan = f"{int(np.round(InstancePayload.Pan) + np.round(InstanceCalculations.TweakPan))}°"
            TotalTilt = f"{int(np.round(InstancePayload.Tilt) + np.round(InstanceCalculations.TweakTilt))}°"

            self.Totals[0] = (TotalPan, self.Totals[0][1], self.Totals[0][2], self.Totals[0][3], self.Totals[0][4])
            self.Totals[1] = (TotalTilt, self.Totals[1][1], self.Totals[1][2], self.Totals[1][3], self.Totals[1][4])

            for text, font, color, position, align in self.Totals:
                Text = font.render(text, True, color)
                TextRect = Text.get_rect()
                if align == 'midright': TextRect.midright = position
                elif align == 'midleft': TextRect.midleft = position
                InstanceSystem.Window.blit(Text, TextRect)

            # Lines
            for start, end in self.Lines: pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, start, end)

            # Shapes
            self.Shapes[2] = (self.Shapes[2][0], self.Shapes[2][1], (2 if self.ClearAnglesHover else 1))
            self.Shapes[3] = (self.Shapes[3][0], self.Shapes[3][1], (2 if self.ClearTweaksHover else 1))

            for color, pos, weight in self.Shapes: pygame.draw.rect(InstanceSystem.Window, color, pos, weight)

            # Text
            for text, font, color, pos, alignment in self.Texts:
                Text = font.render(text, True, color)
                TextRect = Text.get_rect()
                setattr(TextRect, alignment, (pos))
                InstanceSystem.Window.blit(Text, TextRect)

    def ControlCenterClick(self):
        if not InstanceArduino.Tracking and InstanceArduino.Active:
            InstanceOutput.Message = 'Tracking Commencing'
            InstanceArduino.Tracking = True
        elif InstanceArduino.Tracking and InstanceArduino.Active:
            InstanceOutput.Message = 'Tracking Terminating'
            InstanceArduino.Tracking = False

    def ControlUpClick(self):
        InstanceCalculations.TweakTilt += 1

    def ControlLeftClick(self):
        InstanceCalculations.TweakPan -= 1

    def ControlDownClick(self):
        InstanceCalculations.TweakTilt -= 1

    def ControlRightClick(self):
        InstanceCalculations.TweakPan += 1

    def ClearAnglesClick(self):
        for instance in [InstanceRFD, InstanceIridium, InstanceAPRS, InstanceTracker, InstancePayload, InstanceTarget]:
            instance.Lat = instance.Lon = instance.Alt = 0

        InstanceNavigator.Position = f"0.00°N, 0.00°E | {0 if InstanceSystem.MetricUnits else 0} {'m' if InstanceSystem.MetricUnits else 'ft'}"
        InstanceNavigator.Location = "Location Not Set"

    def ClearTweaksClick(self):
        InstanceCalculations.TweakPan = 0
        InstanceCalculations.TweakTilt = 0

InstanceControls = ClassControls()

class ClassLaunch:
    def __init__(self):
        self.X, self.Y, self.W, self.H, self.S = map(lambda x: (x * InstanceSystem.SF), [960, 1020, 30, 30, 40])

        self.Launch1X, self.Launch1Y, self.Launch1W, self.Launch1H = map(lambda x: (x * InstanceSystem.SF), [905, 1005, 30, 30])
        self.Launch2X, self.Launch2Y, self.Launch2W, self.Launch2H = map(lambda x: (x * InstanceSystem.SF), [985, 1005, 30, 30])

        self.Reset1X, self.Reset1Y, self.Reset1W, self.Reset1H = map(lambda x: (x * InstanceSystem.SF), [1100, 965, 20, 20])
        self.Reset2X, self.Reset2Y, self.Reset2W, self.Reset2H = map(lambda x: (x * InstanceSystem.SF), [1100, 995, 20, 20])
        self.Reset3X, self.Reset3Y, self.Reset3W, self.Reset3H = map(lambda x: (x * InstanceSystem.SF), [1100, 1025, 20, 20])
        self.Reset4X, self.Reset4Y, self.Reset4W, self.Reset4H = map(lambda x: (x * InstanceSystem.SF), [1100, 1055, 20, 20])

        self.Countdown1X, self.Countdown1Y, self.Countdown1W, self.Countdown1H = map(lambda x: (x * InstanceSystem.SF), [710, 1005, 50, 30])
        self.Countdown2X, self.Countdown2Y, self.Countdown2W, self.Countdown2H = map(lambda x: (x * InstanceSystem.SF), [765, 1005, 50, 30])
        self.Countdown3X, self.Countdown3Y, self.Countdown3W, self.Countdown3H = map(lambda x: (x * InstanceSystem.SF), [820, 1005, 50, 30])

        self.LaunchX = [self.Launch1X, self.Launch2X]
        self.LaunchY = [self.Launch1Y, self.Launch2Y]
        self.LaunchW = [self.Launch1W, self.Launch2W]
        self.LaunchH = [self.Launch1H, self.Launch2H]

        self.ResetX = [self.Reset1X, self.Reset2X, self.Reset3X, self.Reset4X]
        self.ResetY = [self.Reset1Y, self.Reset2Y, self.Reset3Y, self.Reset4Y]
        self.ResetW = [self.Reset1W, self.Reset2W, self.Reset3W, self.Reset4W]
        self.ResetH = [self.Reset1H, self.Reset2H, self.Reset3H, self.Reset4H]

        self.CountdownX = [self.Countdown1X, self.Countdown2X, self.Countdown3X]
        self.CountdownY = [self.Countdown1Y, self.Countdown2Y, self.Countdown3Y]
        self.CountdownW = [self.Countdown1W, self.Countdown2W, self.Countdown3W]
        self.CountdownH = [self.Countdown1H, self.Countdown2H, self.Countdown3H]

        self.Launch1Hover = self.Launch2Hover = False
        self.Reset1Hover = self.Reset2Hover = self.Reset3Hover = self.Reset4Hover = False
        self.Countdown1Hover = self.Countdown2Hover = self.Countdown3Hover = False

        self.Launched = self.Reset = self.Launch1 = self.Launch2 = self.Reset1 = self.Reset2 = self.Reset3 = self.Reset4 = self.Countdown1 = self.Countdown2 = self.Countdown3 = False
        self.LaunchTime = self.StartTime = None

        self.Lines = [
            ((self.X - 60 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.X - 60 * InstanceSystem.SF, 1080 * InstanceSystem.SF)),
            ((self.X + 60 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.X + 60 * InstanceSystem.SF, 1080 * InstanceSystem.SF)),
            ((self.X + 65 * InstanceSystem.SF, self.Y), 
            (self.X + 130 * InstanceSystem.SF, self.Y)),
            ((self.X + 135 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.X + 135 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)),
            ((self.X + 165 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.X + 165 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)),
            ((self.X - 85 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.X - 85 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)),
            ((self.X - 255 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.X - 255 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF))
        ]

        self.Shapes = [
            ((self.X - self.S - self.W / 2, self.Y - 60 * InstanceSystem.SF), 
            (self.W + 80 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF)),
            ((self.X - 55 * InstanceSystem.SF, self.Y + 20 * InstanceSystem.SF), 
            (self.W + 80 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF)),
            ((self.X + 170 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.W + 130 * InstanceSystem.SF, self.H + 90 * InstanceSystem.SF)),
            ((self.X - 250 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), 
            (self.W + 130 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF)),
            ((self.X - 250 * InstanceSystem.SF, self.Y + 20 * InstanceSystem.SF), 
            (self.W + 130 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF))
        ]

        self.Texts = [
            {"text": "LAUNCH", "font": InstanceSystem.FontBahnschrift25, "color": InstanceSystem.ColorWhite, "pos": (self.X, self.Y - (37.5 * InstanceSystem.SF))},
            {"text": "TIMER RESET", "font": InstanceSystem.FontBahnschrift25, "color": InstanceSystem.ColorWhite, "pos": (self.X + (250 * InstanceSystem.SF), self.Y - (37.5 * InstanceSystem.SF))},
            {"text": "SET CLOCK", "font": InstanceSystem.FontBahnschrift25, "color": InstanceSystem.ColorWhite, "pos": (self.X - (170 * InstanceSystem.SF), self.Y - (37.5 * InstanceSystem.SF))},
            {"text": "L1", "font": InstanceSystem.FontBahnschrift15, "color": InstanceSystem.ColorWhite, "pos": (self.X - self.S, self.Y + (40 * InstanceSystem.SF))},
            {"text": "L2", "font": InstanceSystem.FontBahnschrift15, "color": InstanceSystem.ColorWhite, "pos": (self.X + self.S, self.Y + (40 * InstanceSystem.SF))},
            {"text": "PRESS ALL FOUR", "font": InstanceSystem.FontBahnschrift15, "color": InstanceSystem.ColorWhite, "pos": (self.X + (250 * InstanceSystem.SF), self.Y + (10 * InstanceSystem.SF))},
            {"text": "TO HALT THE CLOCK", "font": InstanceSystem.FontBahnschrift15, "color": InstanceSystem.ColorWhite, "pos": (self.X + (250 * InstanceSystem.SF), self.Y + (30 * InstanceSystem.SF))},
            {"text": "T-10", "font": InstanceSystem.FontBahnschrift15, "color": (InstanceSystem.ColorWhite if InstanceSystem.DarkMode else InstanceSystem.ColorBlack), "pos": ((735 * InstanceSystem.SF), (1020 * InstanceSystem.SF))},
            {"text": "T-30", "font": InstanceSystem.FontBahnschrift15, "color": (InstanceSystem.ColorWhite if InstanceSystem.DarkMode else InstanceSystem.ColorBlack), "pos": ((790 * InstanceSystem.SF), (1020 * InstanceSystem.SF))},
            {"text": "T-60", "font": InstanceSystem.FontBahnschrift15, "color": (InstanceSystem.ColorWhite if InstanceSystem.DarkMode else InstanceSystem.ColorBlack), "pos": ((845 * InstanceSystem.SF), (1020 * InstanceSystem.SF))}
        ]

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active:
            # Launch Buttons
            for i in range(len(self.LaunchX)):
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if [self.Launch1, self.Launch2][i] else InstanceSystem.ColorLightRed), (self.LaunchX[i], self.LaunchY[i], self.LaunchW[i], self.LaunchH[i]))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.LaunchX[i], self.LaunchY[i], self.LaunchW[i], self.LaunchH[i]), (2 if [self.Launch1Hover, self.Launch2Hover][i] else 1))

            # Reset Buttons
            for i in range(len(self.ResetX)):
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if [self.Reset1, self.Reset2, self.Reset3, self.Reset4][i] else InstanceSystem.ColorLightRed), (self.ResetX[i], self.ResetY[i], self.ResetW[i], self.ResetH[i]))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.ResetX[i], self.ResetY[i], self.ResetW[i], self.ResetH[i]), (2 if [self.Reset1Hover, self.Reset2Hover, self.Reset3Hover, self.Reset4Hover][i] else 1))

            # Countdown Buttons
            for i in range(len(self.CountdownX)):
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if [self.Countdown1, self.Countdown2, self.Countdown3][i] else InstanceSystem.ColorLightRed), (self.CountdownX[i], self.CountdownY[i], self.CountdownW[i], self.CountdownH[i]))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.CountdownX[i], self.CountdownY[i], self.CountdownW[i], self.CountdownH[i]), (2 if [self.Countdown1Hover, self.Countdown2Hover, self.Countdown3Hover][i] else 1))

            # Lines
            for line in self.Lines:
                pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, line[0], line[1])

            # Shapes
            for shape in self.Shapes:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkGray, shape)
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, shape, 1)

            # Text
            for text in self.Texts:
                Text = text["font"].render(text["text"], True, text["color"])
                TextRect = Text.get_rect(center=text["pos"])
                InstanceSystem.Window.blit(Text, TextRect)

            if self.Reset1 and self.Reset2 and self.Reset3 and self.Reset4:
                time.sleep(0.5)

                pygame.mixer.music.load(InstanceSystem.Beep)
                pygame.mixer.music.play()

                InstanceOutput.Message = "Launch Timer Halted"

                self.Launched = self.Reset = False
                self.Launch1 = self.Launch2 = False
                self.Reset1 = self.Reset2 = self.Reset3 = self.Reset4 = False
                self.Countdown1 = self.Countdown2 = self.Countdown3 = False

    def Launch1Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Launch1 = True
        self.Launched = self.Launch1 and self.Launch2

    def Launch2Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Launch2 = True
        self.Launched = self.Launch1 and self.Launch2

    def Reset1Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Reset1 = True
        self.Reset = self.Reset1 and self.Reset2 and self.Reset3 and self.Reset4

    def Reset2Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Reset2 = True
        self.Reset = self.Reset1 and self.Reset2 and self.Reset3 and self.Reset4

    def Reset3Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Reset3 = True
        self.Reset = self.Reset1 and self.Reset2 and self.Reset3 and self.Reset4

    def Reset4Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Reset4 = True
        self.Reset = self.Reset1 and self.Reset2 and self.Reset3 and self.Reset4

    def Countdown1Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Countdown2 = self.Countdown3 = False
        self.Countdown1 = True

    def Countdown2Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Countdown1 = self.Countdown3 = False
        self.Countdown2 = True

    def Countdown3Click(self):
        pygame.mixer.music.load(InstanceSystem.Switch)
        pygame.mixer.music.play()
        self.Countdown1 = self.Countdown2 = False
        self.Countdown3 = True

InstanceLaunch = ClassLaunch()

class ClassVent:
    def __init__(self):
        self.VentX, self.VentY, self.VentW, self.VentH = map(lambda x: (x * InstanceSystem.SF), [150, 940, 100, 30])
        self.CutX, self.CutY, self.CutW, self.CutH = map(lambda x: (x * InstanceSystem.SF), [255, 940, 100, 30])

        self.GuardClosedX, self.GuardClosedY, self.GuardClosedW, self.GuardClosedH = self.VentX, self.VentY - (5 * InstanceSystem.SF), (205 * InstanceSystem.SF), self.VentH + (10 * InstanceSystem.SF)
        self.GuardOpenX, self.GuardOpenY, self.GuardOpenW, self.GuardOpenH = self.VentX, self.VentY + (40 * InstanceSystem.SF), self.GuardClosedW, self.GuardClosedH

        self.IMEIX, self.IMEIY, self.IMEIW, self.IMEIH = self.GuardOpenX, self.GuardOpenY, self.GuardOpenW, self.GuardOpenH

        self.IMEIHover = self.GuardClosedHover = self.GuardOpenHover = self.VentHover = self.CutHover = False

        self.CurrentTime = time.time()
        self.PrevTime = time.time()

        self.Guard, self.Manual, self.Vented, self.Cut = True, True, False, False

        self.AltOpen = self.AltClose = self.VelClose = None

        self.EmailSender = base64.b64decode("bmVicGlyaWRpdW1jb21tYW5kQGdtYWlsLmNvbQ==").decode('utf-8')
        self.EmailReceiver = "data@sbd.iridium.com"
        self.EmailSubject = self.EmailBody = self.EmailAttachment = self.Command = ""

        self.FileWrite = True

        self.Rects = [
            (InstanceSystem.ColorDarkGray, (self.GuardClosedX, self.GuardClosedY, self.GuardClosedW, self.GuardClosedH), 0, True),
            (InstanceSystem.ColorWhite, (self.GuardClosedX, self.GuardClosedY, self.GuardClosedW, self.GuardClosedH), 1, True),
            (InstanceSystem.ColorDarkGray, (self.IMEIX, self.IMEIY, self.IMEIW, self.IMEIH), 0, True),
            (InstanceSystem.ColorWhite, (self.IMEIX, self.IMEIY, self.IMEIW, self.IMEIH), 1, True),
            (InstanceSystem.ColorDarkGray, (self.GuardOpenX, self.GuardOpenY, self.GuardOpenW, self.GuardOpenH), 0, False),
            (InstanceSystem.ColorWhite, (self.GuardOpenX, self.GuardOpenY, self.GuardOpenW, self.GuardOpenH), 1, False),
            (InstanceSystem.ColorLightRed, (self.VentX, self.VentY, self.VentW, self.VentH), 0, False),
            (InstanceSystem.ColorWhite, (self.VentX, self.VentY, self.VentW, self.VentH), 1, False),
            (InstanceSystem.ColorLightRed, (self.CutX, self.CutY, self.CutW, self.CutH), 0, False),
            (InstanceSystem.ColorWhite, (self.CutX, self.CutY, self.CutW, self.CutH), 1, False)
        ]

        self.Texts = [
            (InstanceSystem.FontBahnschrift20, "REMOVE GUARD", InstanceSystem.ColorWhite, (self.GuardClosedX + self.GuardClosedW / 2, self.GuardClosedY + self.GuardClosedH / 2), True),
            (InstanceSystem.FontBahnschrift20, "IRIDIUM IMEI", InstanceSystem.ColorWhite, (self.IMEIX + self.IMEIW / 2, self.IMEIY + self.IMEIH / 2), True),
            (InstanceSystem.FontBahnschrift20, "REPLACE GUARD", InstanceSystem.ColorWhite, (self.GuardOpenX + self.GuardOpenW / 2, self.GuardOpenY + self.GuardOpenH / 2), False),
            (InstanceSystem.FontBahnschrift20, "VENT", InstanceSystem.ColorWhite, (self.VentX + self.VentW / 2, self.VentY + self.VentH / 2), False),
            (InstanceSystem.FontBahnschrift20, "CUT", InstanceSystem.ColorWhite, (self.CutX + self.CutW / 2, self.CutY + self.CutH / 2), False)
        ]

    def Display(self):
        if not InstanceSystem.Fullscreen and not InstanceSettings.Active:
            Text = InstanceSystem.FontBahnschrift25.render("VENT COMMANDS", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=(155 * InstanceSystem.SF), centery=(905.5 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (150 * InstanceSystem.SF, 920 * InstanceSystem.SF), (355 * InstanceSystem.SF, 920 * InstanceSystem.SF), 3)

            self.Rects[3] = (self.Rects[3][0], self.Rects[3][1], (2 if self.IMEIHover and self.Guard else 1), self.Rects[3][3])
            self.Rects[6] = ((InstanceSystem.ColorGreen if self.Vented else InstanceSystem.ColorLightRed), self.Rects[6][1], self.Rects[6][2], self.Rects[6][3])
            self.Rects[8] = ((InstanceSystem.ColorGreen if self.Cut else InstanceSystem.ColorLightRed), self.Rects[8][1], self.Rects[8][2], self.Rects[8][3])

            if self.Guard:
                for color, pos, weight, condition in self.Rects:
                    if condition: pygame.draw.rect(InstanceSystem.Window, color, pos, weight)

                for font, text, color, pos, condition in self.Texts:
                    if condition:
                        Text = font.render(text, True, color)
                        TextRect = Text.get_rect(center=pos)
                        InstanceSystem.Window.blit(Text, TextRect)

            if not self.Guard:
                for color, pos, weight, condition in self.Rects:
                    if not condition:
                        pygame.draw.rect(InstanceSystem.Window, color, pos, weight)

                for font, text, color, pos, condition in self.Texts:
                    if not condition:
                        Text = font.render(text, True, color)
                        TextRect = Text.get_rect(center=pos)
                        InstanceSystem.Window.blit(Text, TextRect)

        if self.Vented:
            self.CurrentTime = time.time()
            if self.CurrentTime - self.PrevTime >= 1:
                if InstanceOutput.Message == "-- VENTING --":
                    InstanceOutput.Message = ""
                else:
                    InstanceOutput.Message = "-- VENTING --"
                    pygame.mixer.music.load(InstanceSystem.Buzz)
                    pygame.mixer.music.play()
                self.PrevTime = self.CurrentTime
    
    def SendEmail(self):
        with open(self.EmailAttachment, "rb") as attachment:
            AttachmentData = base64.b64encode(attachment.read()).decode()

        Message = f"""\
From: {self.EmailSender}
To: {self.EmailReceiver}
Subject: {self.EmailSubject}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="boundary"

--boundary
Content-Type: text/plain
Content-Disposition: inline

{self.EmailBody}

--boundary
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="{self.Command}.sbd"
Content-Transfer-Encoding: base64

{AttachmentData}
--boundary--
"""

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(self.EmailSender, base64.b64decode("bGZzY2JwZHF0d2NlcGZmbQ==").decode('utf-8'))
            server.sendmail(self.EmailSender, self.EmailReceiver, Message)

    # Vent Opening
    def Open(self):
        if InstanceIridium.IMEI != 0:
            try:
                # Open Command
                self.Command = "011"
                FilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Resources/Commands/{self.Command}.sbd")

                self.EmailSubject = InstanceIridium.IMEI
                self.EmailAttachment = FilePath

                self.SendEmail()

                self.Vented = True

                self.Log("Vent Opened")
                InstanceOutput.Message = "Vent Opened"

            except Exception as e:
                self.Log("Attempted Vent Open - Failed to Send Command")
                InstanceOutput.Message = "Failed to Send Command"
                InstanceErrors.Message = e

    # Vent Closing
    def Close(self):
        if InstanceIridium.IMEI != 0:
            try:
                # Close Command
                self.Command = "100"
                FilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Resources/Commands/{self.Command}.sbd")

                self.EmailSubject = InstanceIridium.IMEI
                self.EmailAttachment = FilePath

                self.SendEmail()

                # Idle Command
                self.Command = "000"
                FilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Resources/Commands/{self.Command}.sbd")

                self.EmailSubject = InstanceIridium.IMEI
                self.EmailAttachment = FilePath

                self.SendEmail()

                self.Vented = False

                self.Log("Vent Closed")
                InstanceOutput.Message = "Vent Closed"

            except Exception as e:
                self.Log("Attempted Vent Close - Failed to Send Command")
                InstanceOutput.Message = "Failed to Send Command"
                InstanceErrors.Message = e

    # Vent Cutdown
    def Cutdown(self):
        if InstanceIridium.IMEI != 0:
            try:
                # Cut Command
                self.Command = "001"
                FilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Resources/Commands/{self.Command}.sbd")

                self.EmailSubject = InstanceIridium.IMEI
                self.EmailAttachment = FilePath

                self.SendEmail()

                # Idle Command
                self.Command = "000"
                FilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Resources/Commands/{self.Command}.sbd")

                self.EmailSubject = InstanceIridium.IMEI
                self.EmailAttachment = FilePath

                self.SendEmail()

                self.Cut = True

                self.Log("Cutdown Initiated")
                InstanceOutput.Message = "Cutdown Initiated"

            except Exception as e:
                self.Log("Attempted Cutdown - Failed to Send Command")
                InstanceOutput.Message = "Failed to Send Command"
                InstanceErrors.Message = e

    # Automatic Vent Control
    def Automatic(self):
        if InstanceIridium.Active and not InstanceDemo.Enabled and not self.Manual:
            if not self.Vented and self.AltOpen is not None and InstancePayload.Alt >= self.AltOpen - 100:
                self.Open()
            if (self.Vented and self.AltClose is not None and InstancePayload.Alt >= self.AltClose - 100) or (self.Vented and self.VelClose is not None and InstanceIridium.AscentRate <= self.VelClose + 0.5):
                self.Close()

    # Vent Data Log
    def Log(self, Action):
        if self.FileWrite:
            try:
                VentDirectory = os.path.join(InstanceSystem.Directory, "Data", "Vent")
                os.makedirs(VentDirectory, exist_ok=True)

                FileName = f"Vent_{InstanceSystem.Date}.txt"
                FilePath = os.path.join(VentDirectory, FileName)

                with open(FilePath, "a") as f: f.write("{} (MET: {}) | {}\n".format(InstanceTimer.UTC, InstanceTimer.MET, Action))
            except Exception as e:
                InstanceErrors.Message = e

    def IMEIClick(self):
        global InputIMEI
        if not self.Guard:
            InputIMEI = True

    def GuardClosedClick(self):
        global InputIMEI
        if self.Guard:
            pygame.mixer.music.load(InstanceSystem.Switch)
            pygame.mixer.music.play()

            self.Guard = False
            InputIMEI = False

    def GuardOpenClick(self):
        global InputIMEI
        if not self.Guard:
            pygame.mixer.music.load(InstanceSystem.Switch)
            pygame.mixer.music.play()

            self.Guard = True
            InputIMEI = False

    def VentClick(self):
        if not self.Guard and InstanceIridium.IMEI is not None:
            pygame.mixer.music.load(InstanceSystem.Switch)
            pygame.mixer.music.play()

            if self.Vented: self.Close()
            else: self.Open()

        elif self.Guard and InstanceIridium.IMEI is None:
            InstanceErrors.Message = "Iridium IMEI has no value"

    def CutClick(self):
        if not self.Guard and InstanceIridium.IMEI is not None:
            pygame.mixer.music.load(InstanceSystem.Switch)
            pygame.mixer.music.play()

            self.Cutdown()

InstanceVent = ClassVent()

class ClassMaps:
    def __init__(self):
        self.MapX, self.MapY, self.MapW, self.MapH, self.MapR = map(lambda x: (x * InstanceSystem.SF), [1220, 330, 45, 45, 30])

        self.MapHover = False

        self.PrevLat = self.PrevLon = self.PrevAlt = None

        self.MapDirectory = os.path.join(InstanceSystem.Directory, "Data", "Maps")
        os.makedirs(self.MapDirectory, exist_ok=True)

        self.BaseFileName = f"Map_{InstanceSystem.Date}"
        self.FilePath = self.GetFilePath()

        self.Colors = {'default': 'g', 'A': 'g', 'B': 'y', 'C': 'r'}

        self.RFDData = []
        self.IridiumData = []
        self.APRSData = []

    def Display(self):
        InstanceSystem.Window.blit(pygame.transform.smoothscale(InstanceSystem.ButtonMap, (self.MapW, self.MapH)), (self.MapX - (20 * InstanceSystem.SF), self.MapY - (20 * InstanceSystem.SF)))

    def PlotRivers(self, ax, dim, MinX, MaxX, MinY, MaxY):
        FlightBoundary = Polygon([(MinX, MinY), (MaxX, MinY), (MaxX, MaxY), (MinX, MaxY)])

        try:
            with open(os.path.join(InstanceSystem.Resources, "USRivers.json"), 'r') as file:
                GeoJSON = json.load(file)

            for feature in GeoJSON['features']:
                Geometry = shape(feature['geometry'])
                if Geometry.geom_type == 'LineString':
                    if Geometry.within(FlightBoundary) or Geometry.intersects(FlightBoundary):
                        Coordinates = Geometry.coords.xy
                        if dim == '2D':
                            Coordinates = [(x, y) for x, y in zip(Coordinates[0], Coordinates[1])]
                            if Coordinates: ax.plot(*zip(*Coordinates), color='b', alpha=0.1)
                        if dim == '3D':
                            Coordinates = [(x, y, 0) for x, y in zip(Coordinates[0], Coordinates[1])]
                            if Coordinates: ax.plot(*zip(*Coordinates), color='b', zdir='z', alpha=0.1)

        except Exception:
            pass

    def PlotRoads(self, ax, dim, MinX, MaxX, MinY, MaxY):
        CenterX = (MinX + MaxX) / 2
        CenterY = (MinY + MaxY) / 2

        Width = MaxX - MinX
        Height = MaxY - MinY

        MinX = CenterX - (1 * Width)
        MaxX = CenterX + (1 * Width)
        MinY = CenterY - (1 * Height)
        MaxY = CenterY + (1 * Height)

        FlightBoundary = Polygon([(MinX, MinY), (MaxX, MinY), (MaxX, MaxY), (MinX, MaxY)])

        try:
            with open(os.path.join(InstanceSystem.Resources, "USRoads.json"), 'r') as file: GeoJSON = json.load(file)

            for feature in GeoJSON['features']:
                if feature['geometry']['type'] == 'MultiLineString':
                    Lines = []
                    for coords in feature['geometry']['coordinates']: Lines.append([(coord[0], coord[1]) for coord in coords])

                    Coordinates = Lines

                    for coords in Coordinates:
                        Road = LineString(coords)
                        if Road.within(FlightBoundary) or Road.intersects(FlightBoundary):
                            x, y = Road.xy
                            if dim == '2D':
                                ax.plot(x, y, color='#9C9C9C', alpha=1, linewidth=1.5)
                            elif dim == '3D':
                                z = [0] * len(x)
                                ax.plot(x, y, z, color='#9C9C9C', zdir='z', alpha=1, linewidth=1.5)

        except Exception:
            pass

    def PlotCounties(self, ax, dim, MinX, MaxX, MinY, MaxY):
        FlightBoundary = Polygon([(MinX, MinY), (MaxX, MinY), (MaxX, MaxY), (MinX, MaxY)])

        try:
            with open(os.path.join(InstanceSystem.Resources, "USCounties.json"), 'r') as file: GeoJSON = json.load(file)

            for feature in GeoJSON['features']:
                Geometry = shape(feature['geometry'])
                if Geometry.geom_type == 'Polygon':
                    if Polygon(Geometry.exterior.coords).within(FlightBoundary) or Polygon(Geometry.exterior.coords).intersects(FlightBoundary):
                        if dim == '2D':
                            Coordinates = Geometry.exterior.coords.xy
                            Coordinates = [(x, y) for x, y in zip(Coordinates[0], Coordinates[1])]
                            if Coordinates: ax.plot(*zip(*Coordinates), color='k', alpha=0.1)
                        if dim == '3D':
                            Coordinates = Geometry.exterior.coords.xy
                            Coordinates = [(x, y, 0) for x, y in zip(Coordinates[0], Coordinates[1])]
                            if Coordinates: ax.plot(*zip(*Coordinates), color='k', zdir='z', alpha=0.1)

        except Exception:
            pass

    def PlotCities(self, ax, dim, MinX, MaxX, MinY, MaxY):
        try:
            with open(os.path.join(InstanceSystem.Resources, "USCities.json"), 'r') as file: GeoJSON = json.load(file)

            for feature in GeoJSON['features']:
                CityName = feature['properties']['name']
                Lat, Lon = feature['geometry']['coordinates']
                Population = feature['properties']['population']
                Size = (16 if Population >= 100000 else 12 if Population >= 40000 else 8)
                Weight = ('bold' if Population >= 40000 else 'normal')

                if MinX - 0.01 <= Lon <= MaxX + 0.01 and MinY - 0.01 <= Lat <= MaxY + 0.01:
                    if dim == '2D': ax.text(Lon, Lat, CityName, color='k', fontsize=Size, fontweight=Weight, ha='right')
                    if dim == '3D': ax.text(Lon, Lat, 0, CityName, color='k', fontsize=Size, fontweight=Weight, zdir='x', ha='right')

        except Exception:
            pass

    def MapClick(self):
        try:
            Root = tk.Tk()
            Root.withdraw()
            FilePath = filedialog.askopenfilename(
                initialdir=self.MapDirectory,
                title="Select JSON File",
                filetypes=[("GeoJSON files", "*.geojson")]
            )
            Root.destroy()

            gdf = gpd.read_file(FilePath, driver='GeoJSON', lazy_load=True)

            fig = plt.figure()
            figManager = plt.get_current_fig_manager()
            figManager.full_screen_toggle()

            ax = fig.add_subplot(111, projection='3d')
            ax.grid(False)

            UniquePoints = set()
            InterpolatedPoints = []

            for index, feature in gdf.iterrows():
                if feature.geometry.geom_type == 'Point':
                    x, y, z = feature.geometry.x, feature.geometry.y, feature.geometry.z
                    Point = (x, y, z)
                    if Point not in UniquePoints:
                        UniquePoints.add(Point)
                        InterpolatedPoints.append((x, y, z))
                        Category = 'default'
                        if 'category' in feature: Category = feature['category']

            ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)
            ax.zaxis.set_visible(False)

            ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
            ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
            ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

            ax.xaxis.pane.set_edgecolor('w')
            ax.yaxis.pane.set_edgecolor('w')
            ax.zaxis.pane.set_edgecolor('w')

            ax.xaxis.pane.fill = False
            ax.yaxis.pane.fill = False
            ax.zaxis.pane.fill = False

            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_zticks([])

            ax.axis('equal')

            MinX, MaxX = min(point[0] for point in UniquePoints), max(point[0] for point in UniquePoints)
            MinY, MaxY = min(point[1] for point in UniquePoints), max(point[1] for point in UniquePoints)

            RangeX = MaxX - MinX
            RangeY = MaxY - MinY

            if RangeX > RangeY:
                Adjustment = (RangeX - RangeY) / 2
                MinY -= Adjustment
                MaxY += Adjustment
            else:
                Adjustment = (RangeY - RangeX) / 2
                MinX -= Adjustment
                MaxX += Adjustment

            MinZ, MaxZ = min(point[2] for point in UniquePoints), max(point[2] for point in UniquePoints)

            ax.set_xlim(MinX, MaxX)
            ax.set_ylim(MinY, MaxY)
            ax.set_zlim(MinZ, MaxZ)

            self.PlotRivers(ax, '3D', MinX, MaxX, MinY, MaxY)
            self.PlotRoads(ax, '3D', MinX, MaxX, MinY, MaxY)
            self.PlotCounties(ax, '3D', MinX, MaxX, MinY, MaxY)
            self.PlotCities(ax, '3D', MinX, MaxX, MinY, MaxY)

            if len(InterpolatedPoints) > 1:
                xPoints, yPoints, zPoints = zip(*InterpolatedPoints)

                InterpFunctionX = interp1d(range(len(xPoints)), xPoints, kind='linear')
                InterpFunctionY = interp1d(range(len(yPoints)), yPoints, kind='linear')
                InterpFunctionZ = interp1d(range(len(zPoints)), zPoints, kind='linear')

                NumInterpolatedPoints = 100
                InterpolatedIndices = np.linspace(0, len(xPoints) - 1, num=NumInterpolatedPoints)

                InterpolatedX = InterpFunctionX(InterpolatedIndices)
                InterpolatedY = InterpFunctionY(InterpolatedIndices)
                InterpolatedZ = InterpFunctionZ(InterpolatedIndices)

                ax.plot(InterpolatedX, InterpolatedY, InterpolatedZ, color=self.Colors[Category])
                ax.plot(InterpolatedX, InterpolatedY, 0, color='k', alpha=0.3)

                for i in range(len(InterpolatedX)): ax.plot([InterpolatedX[i], InterpolatedX[i]], [InterpolatedY[i], InterpolatedY[i]], [InterpolatedZ[i], 0], color=self.Colors[Category])

            FileName = os.path.basename(FilePath)
            Pattern = r"(\d{4})(\d{2})(\d{2})"
            Match = re.search(Pattern, FileName)

            if Match:
                Year, Month, Day = Match.groups()
                Date = f"{int(Month):02d}/{int(Day):02d}/{Year}"

            ax.set_title('Flight History', fontsize=30, fontweight='bold')

            if Date: ax.set_title(f'Flight History - {Date}', fontsize=20, fontweight='bold')

            plt.show()
        except Exception:
            FilePath = None

    def ParserPlot(self, Data):

        print("Test 3")
        try:
            Longitudes = [point['Longitude'] for point in Data]
            Latitudes = [point['Latitude'] for point in Data]
            Altitudes = [point['Altitude'] for point in Data]
            time_since_midnight = [point['Time'] for point in Data]
            Times = np.array(time_since_midnight) - min(np.array(time_since_midnight))
            Dates = np.array([point['Date'] for point in Data])
            DateStr = Dates[0]

            fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
            fig1.suptitle(f'Lat, Long, and Altitude Data {DateStr}')
            MinX, MaxX = min(Longitudes), max(Longitudes)
            MinY, MaxY = min(Latitudes), max(Latitudes)

            ax1.set_xlim(MinX - (MaxX - MinX) / 10, MaxX + (MaxX - MinX) / 10)
            ax1.set_ylim(MinY - (MaxY - MinY) / 10, MaxY + (MaxY - MinY) / 10)

            self.PlotRivers(ax1, '2D', MinX, MaxX, MinY, MaxY)
            self.PlotRoads(ax1, '2D', MinX, MaxX, MinY, MaxY)
            self.PlotCounties(ax1, '2D', MinX, MaxX, MinY, MaxY)
            self.PlotCities(ax1, '2D', MinX, MaxX, MinY, MaxY)

        except Exception as e:
            InstanceErrors.Message = e

        try: 
            Pressure = [point['Pressure'] for point in Data]
            Temperature = [point['Temperature'] for point in Data]
            fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(14, 6))
            fig2.suptitle(f'Pressure and Temperatue Data {DateStr}')

        except Exception as e:
            InstanceErrors.Message = e
            print(InstanceErrors.Message)
            print("Pressure or temperature not defined")
        print("Test 4")



        ax1.plot(Longitudes, Latitudes, '.')
        ax1.set_title('Latitude and Longitude', fontweight='bold')
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax1.axis('equal')

        ax2.plot(Times, Altitudes, '.')
        ax2.set_title('Altitude vs. Time', fontweight='bold')
        ax2.xaxis.set_major_locator(plticker.MaxNLocator(20))
        ax2.yaxis.set_major_locator(plticker.MaxNLocator(15))
        ax2.set_xlabel("Time (Mins)")
        ax2.set_ylabel("Altitude (m)")
        ax2.grid(True)

        try:
            ax3.plot(Times, Pressure, '.')
            ax3.set_title('Pressure vs. Time', fontweight='bold')
            ax3.xaxis.set_major_locator(plticker.MaxNLocator(20))
            ax3.yaxis.set_major_locator(plticker.MaxNLocator(15))
            ax3.set_xlabel("Time (Mins)")
            ax3.set_ylabel("Pressure (Pa)")
            ax3.grid(True)

            ax4.plot(Times, Temperature, '.')
            ax4.set_title('Temperature vs. Time', fontweight='bold')
            ax4.xaxis.set_major_locator(plticker.MaxNLocator(20))
            ax4.yaxis.set_major_locator(plticker.MaxNLocator(15))
            ax4.set_xlabel("Time (Mins)")
            ax4.set_ylabel("Temperature (C)")
            ax4.grid(True)

        except Exception:   
            pass

        plt.figure(fig1.number)
        plt.tight_layout()

        plt.figure(fig2.number)
        plt.tight_layout()

        plt.show()

        self.RFDData = self.IridiumData = self.APRSData = []

    def GetFilePath(self):
        Count = 1
        while True:
            FileName = f"{self.BaseFileName}_{Count}.geojson"
            FilePath = os.path.join(self.MapDirectory, FileName)
            if not os.path.exists(FilePath): return FilePath
            Count += 1

    def CreateFile(self):
        with open(self.FilePath, "w") as file:
            Template = {"type": "FeatureCollection", "features": []}
            json.dump(Template, file, indent=2)

    def InsertFeature(self, feature):
        with open(self.FilePath, "r+") as file:
            data = json.load(file)
            data["features"].append(feature)
            file.seek(0)
            json.dump(data, file, indent=2)

    def Update(self):
        if (InstancePayload.Lat != self.PrevLat or InstancePayload.Lon != self.PrevLon or InstancePayload.Alt != self.PrevAlt) and (InstancePayload.Lat != 0 or InstancePayload.Lon != 0 or InstancePayload.Alt != 0) and not InstanceDemo.Enabled:
            if not os.path.exists(self.FilePath):
                self.CreateFile()

            if not InstanceVent.Vented and not InstanceVent.Cut: Property = "A"
            elif InstanceVent.Vented and not InstanceVent.Cut: Property = "B"
            elif InstanceVent.Cut: Property = "C"

            Feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [InstancePayload.Lon, InstancePayload.Lat, InstancePayload.Alt]
                },
                "properties": {
                    "category": Property
                }
            }

            self.InsertFeature(Feature)

            self.PrevLat = InstancePayload.Lat
            self.PrevLon = InstancePayload.Lon
            self.PrevAlt = InstancePayload.Alt

InstanceMaps = ClassMaps()

class ClassDemo:
    def __init__(self):
        self.Enabled = False

        self.CorrectionFactor = 80

        self.AscentDuration = (2*60*60) + (15*60) + 50
        self.DescentDuration = (23*60) + 23

        self.MinAltitude = 1000
        self.MaxAltitude = 113000

        self.AscentStep = (self.MaxAltitude - self.MinAltitude) / (self.AscentDuration * 1000 * self.CorrectionFactor)
        self.DescentStep = (self.MaxAltitude - self.MinAltitude) / (self.DescentDuration * 1000 * self.CorrectionFactor)

        self.CurrentAltitude = self.MinAltitude

        self.Time1 = time.time()
        self.Time2 = self.Time1

        self.State = "Ascent"

    def Update(self):
        if self.Enabled:
            self.Time2 = time.time()
            ElapsedTime = self.Time2 - self.Time1

            if self.State == "Ascent":
                self.CurrentAltitude += self.AscentStep * ElapsedTime

                if self.CurrentAltitude >= self.MaxAltitude:
                    self.CurrentAltitude = self.MaxAltitude
                    self.State = "Descent"
                    self.Time1 = self.Time2

            elif self.State == "Descent":
                self.CurrentAltitude -= self.DescentStep * ElapsedTime

                if self.CurrentAltitude <= self.MinAltitude:
                    self.CurrentAltitude = self.MinAltitude
                    self.State = "Ascent"
                    self.Time1 = self.Time2

InstanceDemo = ClassDemo()

class ClassPredictions:
    def __init__(self):
        self.Lat = 44.268237
        self.Lon = -92.992233
        self.Alt = 353
        self.Ascent = 5
        self.Descent = 7
        self.Date = "08/20"
        self.Time = "12:00"
        self.FinalAlt = 25000
        self.FloatAlt = 24000
        self.FloatTime = 0

        self.PredictionDirectory = os.path.join(InstanceSystem.Directory, 'Predictions')
        if not os.path.exists(self.PredictionDirectory): os.makedirs(self.PredictionDirectory)

    class ExtendedForecast(Forecast):
        def __init__(self, resolution, timestep):
            super().__init__(resolution, timestep)
            self.Queries = 999
            self.Indices = [999, 999]
            self.Middle = [999, 999]
            self.DataSave = []

        def Get(self, variables, DateTime, Lat, Lon):
            ForecastDate, ForecastTime, QueryTime = self.datetime_to_forecast(DateTime)

            lat1 = self.value_input_to_index("lat", Lat)
            start = int(lat1[1:-1]) - 7
            end = int(lat1[1:-1]) + 7
            Lat = "[" + str(start) + ":" + str(end) + "]"

            lon1 = self.value_input_to_index("lon", Lon)
            start = int(lon1[1:-1]) - 7
            end = int(lon1[1:-1]) + 7
            Lon = "[" + str(start) + ":" + str(end) + "]"

            self.Indices = [int(lat1[1:-1]), int(lon1[1:-1])]
            lev = "[0:%s]" % int(
                (self.coords["lev"]["minimum"] - self.coords["lev"]["maximum"])
                / self.coords["lev"]["resolution"]
            )

            Query = ""
            for variable in variables:
                if variable not in self.variables.keys():
                    raise ValueError(
                        "The variable {name} is not a valid choice for this weather model".format(
                            name=variable
                        )
                    )
                if self.variables[variable]["level_dependent"] == True and lev == []:
                    raise ValueError(
                        "The variable {name} requires the altitude/level to be defined".format(
                            name=variable
                        )
                    )
                elif self.variables[variable]["level_dependent"] == True:
                    Query += "," + variable + QueryTime + lev + Lat + Lon
                else:
                    Query += "," + variable + QueryTime + Lat + Lon

            if QueryTime != self.Queries:
                self.Middle = [int(lat1[1:-1]), int(lon1[1:-1])]
                Query = Query[1:]
                r = requests.get(
                    url.format(
                        res=self.resolution,
                        step=self.timestep,
                        date=ForecastDate,
                        hour=int(ForecastTime),
                        info="ascii?{query}".format(query=Query),
                    )
                )
                if r.status_code != 200:
                    raise Exception("The forecast information could not be downloaded")
                elif r.text[:6] == "<html>":
                    raise Exception("The forecast information could not be downloaded")
                else:
                    self.Queries = QueryTime
                    return ClassPredictions.File(r.text)
            self.Queries = QueryTime
            return 1

        def WindProfile(self, DateTime, Lat, Lon):
            info = self.Get(["ugrdprs", "vgrdprs", "ugrd10m", "vgrd10m", "hgtsfc", "hgtprs"], DateTime, Lat, Lon,)
            if info != 1:
                uWind = list(info.variables["ugrdprs"].data.flatten()) + list(info.variables["ugrd10m"].data.flatten())
                vWind = list(info.variables["vgrdprs"].data.flatten()) + list(info.variables["vgrd10m"].data.flatten())
                Alts = list(info.variables["hgtprs"].data.flatten()) + list(info.variables["hgtsfc"].data.flatten() + 10)
                Grid = int(math.sqrt(len(Alts) / 42))
                self.DataSave = [np.array(Alts).reshape(42, Grid, Grid), np.array(uWind).reshape(42, Grid, Grid), np.array(vWind).reshape(42, Grid, Grid)]

            Alts = []
            uWind = []
            vWind = []

            for layers in self.DataSave[0]: Alts.append(layers[self.Indices[0] - self.Middle[0] + 7][self.Indices[1] - self.Middle[1] + 7])
            for layers in self.DataSave[1]: uWind.append(layers[self.Indices[0] - self.Middle[0] + 7][self.Indices[1] - self.Middle[1] + 7])
            for layers in self.DataSave[2]: vWind.append(layers[self.Indices[0] - self.Middle[0] + 7][self.Indices[1] - self.Middle[1] + 7])

            return interp1d(Alts, uWind, fill_value=(uWind[-1], uWind[-2]), bounds_error=False), interp1d(Alts, vWind, fill_value=(vWind[-1], vWind[-2]), bounds_error=False)

    class File:
        def __init__(self, Text):
            Text = Text.splitlines()
            IndHead = 0
            variables = []
            while IndHead < len(Text):
                try:
                    variable_name = re.findall("(.*?), ", Text[IndHead])[0]
                except IndexError:
                    raise ValueError("Incorrect File Format")
                dims = re.findall(r"\[(.*?)\]", Text[IndHead]) # Syntax Change
                dims.reverse()
                LinesData = 0
                for dim in dims[1:]: LinesData = int(dim) * (LinesData + 1)
                dims.reverse()

                LinesMeta = len(dims) * 2
                NameLine = True
                coords = []
                for line in Text[IndHead + 2 + LinesData: IndHead + 3 + LinesData + LinesMeta]:
                    if NameLine:
                        name = re.findall("(.*?), ", line)[0]
                        NameLine = False
                    else:
                        coords.append(Coordinate(name, [float(v[:-1]) for v in line.split()]))
                        NameLine = True

                data = np.zeros(tuple([int(d) for d in dims]))
                data[:] = np.nan
                for line in Text[IndHead + 1: IndHead + 1 + LinesData - 1]:
                    if len(line) > 0 and line[0] == "[":
                        position = [int(v) for v in re.findall(r"\[(.*?)\]", line)] # Syntax Change
                        values = line.split()[1:]
                        if len(values) > 1:
                            for ind, value in enumerate(values):
                                if value[-1] == ",": value = value[:-1]
                                data = ClassPredictions.ReplaceValue(data, float(value), position + [ind])
                        else:
                            data = ClassPredictions.ReplaceValue(data, float(values[0]), position)

                coords = {c.name: c for c in coords}
                variables.append(Variable(variable_name, coords, data))

                IndHead += LinesData + LinesMeta + 2

            self.variables = {v.name: v for v in variables}

        def __str__(self):
            return "File Containing %s" % self.variables.keys()

    @staticmethod
    def ReplaceValue(arr, val, position):
        if not isinstance(position, list): raise TypeError("Invalid Replacement Position")
        if len(position) == 1: arr[position[0]] = val
        elif len(position) == 2: arr[position[0]][position[1]] = val
        elif len(position) == 3: arr[position[0]][position[1]][position[2]] = val
        elif len(position) == 4: arr[position[0]][position[1]][position[2]][position[3]] = val
        else: raise ValueError("Invalid Dimensions")

        return arr

    def CreateCSV(self, DateTime, Lat, Lon, Alt):
        FileName = os.path.join(self.PredictionDirectory, 'PredictionData.csv')
        with open(FileName, 'w', newline='') as f:
            Header = ['DateTime', 'Latitude', 'Longitude', 'Altitude']
            Data = [DateTime, Lat, Lon, Alt]
            Writer = csv.writer(f)

            self.FullData.append(Data)
            Writer.writerow(Header)
            Writer.writerows(self.FullData)

    @staticmethod
    def ConstantFloatCondition(DurationVal, AltitudeVal):
        return DurationVal, AltitudeVal

    @staticmethod
    def RealTimeCondition(RealTime):
        return RealTime

    @staticmethod
    def ConvertCoordinates(StartSystem, EndSystem, xPosition, yPosition):
        NewCoordinates = (Transformer.from_crs(StartSystem, EndSystem)).transform(xPosition, yPosition)
        return NewCoordinates[0], NewCoordinates[1]

    def CalculateDescentRate(self, Alt):
        Temp, Pressure = 0, 0

        if Alt > 25000:
            Temp = -131.21 + (0.00299 * Alt)
            Pressure = 2.488 * pow((Temp + 273.1) / 216.6, -11.388)
        if Alt <= 25000 and Alt > 11000:
            Temp = -56.46
            Pressure = 22.65 * math.exp(1.73 - (0.000157 * Alt))
        if Alt <= 11000:
            Temp = 15.04 - (0.00649 * Alt)
            Pressure = 101.29 * pow((Temp + 273.1) / 288.08, 5.256)

        Density = Pressure / (0.2869 * (Temp + 273.1))
        return (self.Descent * 60 * 1.1045) / (math.sqrt(Density))

    def CreateKML(self, List, FileName):
        PredictionMap = simplekml.Kml()
        Map = PredictionMap.newlinestring(name='Path', description="Path", coords=List)

        Map.style.linestyle.color = simplekml.Color.hotpink
        Map.style.linestyle.width = 5

        PredictionMap.save(os.path.join(self.PredictionDirectory, FileName))

    def PlotPredictionPath(self):
        FileName = os.path.join(self.PredictionDirectory, 'PredictionData.csv')
        Data = pd.read_csv(FileName)

        Latitudes = Data['Latitude'].tolist()
        Longitudes = Data['Longitude'].tolist()
        Altitudes = Data['Altitude'].tolist()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        ax.zaxis.set_visible(False)

        ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

        ax.xaxis.pane.set_edgecolor('w')
        ax.yaxis.pane.set_edgecolor('w')
        ax.zaxis.pane.set_edgecolor('w')

        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        try:
            MinX, MaxX = min(Longitudes), max(Longitudes)
            MinY, MaxY = min(Latitudes), max(Latitudes)

            ax.set_xlim(MinX, MaxX)
            ax.set_ylim(MinY, MaxY)

            ax.set_aspect('equal')

            InstanceMaps.PlotRivers(ax, '3D', MinX, MaxX, MinY, MaxY)
            InstanceMaps.PlotRoads(ax, '3D', MinX, MaxX, MinY, MaxY)
            InstanceMaps.PlotCounties(ax, '3D', MinX, MaxX, MinY, MaxY)
            InstanceMaps.PlotCities(ax, '3D', MinX, MaxX, MinY, MaxY)

        except Exception as e:
            InstanceErrors.Message = e

        PreviousAltitude = Altitudes[0]
        Color = 'green'
        SegmentStart = 0

        for i in range(1, len(Altitudes)):
            if PreviousAltitude < self.FloatAlt <= Altitudes[i]:
                ax.plot(Longitudes[SegmentStart:i+1], Latitudes[SegmentStart:i+1], Altitudes[SegmentStart:i+1], color=Color)
                SegmentStart = i
                Color = 'yellow'
            elif PreviousAltitude < self.FinalAlt <= Altitudes[i]:
                ax.plot(Longitudes[SegmentStart:i+1], Latitudes[SegmentStart:i+1], Altitudes[SegmentStart:i+1], color=Color)
                SegmentStart = i
                Color = 'red'

            PreviousAltitude = Altitudes[i]

        ax.plot(Longitudes[SegmentStart:], Latitudes[SegmentStart:], Altitudes[SegmentStart:], color=Color)
        ax.grid(False)

        plt.tight_layout()
        plt.show()

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

        PreviousAltitude = Altitudes[0]
        Color = 'green'
        SegmentStart = 0

        InstanceMaps.PlotRivers(ax1, '2D', MinX, MaxX, MinY, MaxY)
        InstanceMaps.PlotRoads(ax1, '2D', MinX, MaxX, MinY, MaxY)
        InstanceMaps.PlotCounties(ax1, '2D', MinX, MaxX, MinY, MaxY)
        InstanceMaps.PlotCities(ax1, '2D', MinX, MaxX, MinY, MaxY)

        for i in range(1, len(Altitudes)):
            if PreviousAltitude < self.FloatAlt <= Altitudes[i]:
                ax1.plot(Longitudes[SegmentStart:i+1], Latitudes[SegmentStart:i+1], color=Color)
                SegmentStart = i
                Color = 'yellow'
            elif PreviousAltitude < self.FinalAlt <= Altitudes[i]:
                ax1.plot(Longitudes[SegmentStart:i+1], Latitudes[SegmentStart:i+1], color=Color)
                SegmentStart = i
                Color = 'red'

            PreviousAltitude = Altitudes[i]

        ax1.plot(Longitudes[SegmentStart:], Latitudes[SegmentStart:], color=Color)
        ax1.set_xlabel('Longitude')
        ax1.set_ylabel('Latitude')
        ax1.set_title('Predicted Flight Path')

        ax1.set_aspect('equal')
        ax1.set_xlim(MinX - 0.05, MaxX + 0.05)
        ax1.set_ylim(MinY - 0.05, MaxY + 0.05)

        PreviousAltitude = Altitudes[0]
        Color = 'green'
        SegmentStart = 0

        for i in range(1, len(Altitudes)):
            if PreviousAltitude < self.FloatAlt <= Altitudes[i]:
                ax2.plot(range(SegmentStart, i+1), Altitudes[SegmentStart:i+1], color=Color)
                SegmentStart = i
                Color = 'yellow'
            elif PreviousAltitude < self.FinalAlt <= Altitudes[i]:
                ax2.plot(range(SegmentStart, i+1), Altitudes[SegmentStart:i+1], color=Color)
                SegmentStart = i
                Color = 'red'

            PreviousAltitude = Altitudes[i]

        ax2.plot(range(SegmentStart, len(Altitudes)), Altitudes[SegmentStart:], color=Color)
        ax2.set_xlabel('Time Step')
        ax2.set_ylabel('Altitude (m)')
        ax2.set_title('Predicted Altitude Profile')

        plt.tight_layout()
        plt.show()

    def RunPrediction(self):
        try:
            Year = datetime.datetime.now().year
            Month = self.Date[0:2]
            Day = self.Date[3:5]
            Hour = int(self.Time[:2])
            Minutes = int(self.Time[3:5])

            self.FullData = []
            self.GeoData = []
            self.StateStartLat, self.StateStartLon = self.ConvertCoordinates(4326, 26993, self.Lat, self.Lon)
            self.WindForecast = self.ExtendedForecast(resolution='0p25', timestep='1hr')
            self.FloatDuration, self.FloatAltitude = self.ConstantFloatCondition(self.FloatTime, self.FloatAlt)
            self.RealTimeVal = self.RealTimeCondition(False)
            self.RealTime = True
            self.StartCondition = False
            self.EndCondition = False

            while self.Alt >= 0:
                if Minutes < 10:
                    DateTime = f"{Year}{Month}{Day} {Hour}:0{Minutes}"
                    TimeString = f"{Hour}:0{Minutes}"
                else:
                    DateTime = f"{Year}{Month}{Day} {Hour}:{Minutes}"
                    TimeString = f"{Hour}:{Minutes}"

                self.CreateCSV(DateTime, self.Lat, self.Lon, self.Alt)

                self.GeoData.append((self.Lon, self.Lat))
                uComponent, vComponent = self.WindForecast.WindProfile(DateTime, self.Lat, self.Lon)
                self.StateStartLat += (uComponent(self.Alt) * 60)
                self.StateStartLon += (vComponent(self.Alt) * 60)
                self.Lat, self.Lon = self.ConvertCoordinates(26993, 4326, self.StateStartLat, self.StateStartLon)

                if self.RealTime and TimeString == self.RealTimeVal:
                    self.RealTime = False

                if self.Alt < self.FloatAltitude and self.RealTime:
                    self.Alt += (self.Ascent * 60)
                    if self.Alt > self.FloatAltitude:
                        self.Alt = self.FloatAltitude
                elif self.FloatDuration >= 0 and not self.EndCondition and self.RealTime:
                    self.StartCondition = True
                else:
                    self.FloatAltitude = -1
                    self.Alt -= self.CalculateDescentRate(self.Alt)

                if self.StartCondition and self.RealTime:
                    self.FloatDuration -= 1
                    self.Alt = self.Alt

                if self.FloatDuration <= 0 or not self.RealTime:
                    self.StartCondition = False
                    self.EndCondition = True
                    self.FloatAltitude = self.FinalAlt
                    self.FloatDuration = 1

                Minutes += 1
                if Minutes == 60:
                    Minutes = 0
                    Hour += 1
                    if Hour == 24:
                        Hour = 0
                        Day += 1

            Latitudes = [coord[1] for coord in self.GeoData]
            Longitudes = [coord[0] for coord in self.GeoData]
            MinLat, MaxLat = min(Latitudes) - 0.01, max(Latitudes) + 0.01
            MinLon, MaxLon = min(Longitudes) - 0.01, max(Longitudes) + 0.01

            self.CreateKML(self.GeoData, 'PredictionMap.kml')

            for (Lon, Lat) in self.GeoData:
                if MinLat <= Lat <= MaxLat and MinLon <= Lon <= MaxLon: break

            self.PlotPredictionPath()

        except Exception as e:
            InstanceErrors.Message = e

InstancePredictions = ClassPredictions()

class ClassAttitude:
    def __init__(self):
        self.Heading = 0

InstanceAttitude = ClassAttitude()

class ClassIndicators:
    def __init__(self):
        self.WifiX, self.WifiY, self.WifiW, self.WifiH = map(lambda x: (x * InstanceSystem.SF), [30, 30, 60, 60])
        self.TrackingX, self.TrackingY, self.TrackingW, self.TrackingH = map(lambda x: (x * InstanceSystem.SF), [120, 30, 60, 60])
        self.CaptureX, self.CaptureY, self.CaptureW, self.CaptureH = map(lambda x: (x * InstanceSystem.SF), [210, 30, 60, 60])

        self.WifiOn = pygame.transform.smoothscale(InstanceSystem.WifiOn, (self.WifiW, self.WifiH))
        self.WifiOff = pygame.transform.smoothscale(InstanceSystem.WifiOff, (self.WifiW, self.WifiH))

        self.TrackingOn = pygame.transform.smoothscale(InstanceSystem.TrackingOn, (self.TrackingW, self.TrackingH))
        self.TrackingOff = pygame.transform.smoothscale(InstanceSystem.TrackingOff, (self.TrackingW, self.TrackingH))

        self.CaptureOn = pygame.transform.smoothscale(InstanceSystem.CaptureOn, (self.CaptureW, self.CaptureH))
        self.CaptureOff = pygame.transform.smoothscale(InstanceSystem.CaptureOff, (self.CaptureW, self.CaptureH))

    def Display(self):
        if not InstanceSystem.Fullscreen:
            pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorBlack if InstanceSystem.DarkMode else InstanceSystem.ColorWhite), (0, 0, 300 * InstanceSystem.SF, 120 * InstanceSystem.SF))

        try:
            socket.create_connection(("www.google.com", 80))
            InstanceSystem.Window.blit(self.WifiOn, (self.WifiX, self.WifiY))
        except Exception:
            InstanceSystem.Window.blit(self.WifiOff, (self.WifiX, self.WifiY))

        if InstanceArduino.Tracking: InstanceSystem.Window.blit(self.TrackingOn, (self.TrackingX, self.TrackingY))
        else: InstanceSystem.Window.blit(self.TrackingOff, (self.TrackingX, self.TrackingY))

        if InstanceLaunch.Launched: InstanceSystem.Window.blit(self.CaptureOn, (self.CaptureX, self.CaptureY))
        else: InstanceSystem.Window.blit(self.CaptureOff, (self.CaptureX, self.CaptureY))

InstanceIndicators = ClassIndicators()

class ClassButtons:
    def __init__(self):
        self.PowerX, self.PowerY, self.PowerW, self.PowerH, self.PowerR = map(lambda x: (x * InstanceSystem.SF), [1860, 60, 45, 45, 25])
        self.HelpX, self.HelpY, self.HelpW, self.HelpH, self.HelpR = map(lambda x: (x * InstanceSystem.SF), [1740, 60, 45, 45, 25])
        self.SettingsX, self.SettingsY, self.SettingsW, self.SettingsH, self.SettingsR = map(lambda x: (x * InstanceSystem.SF), [1800, 60, 45, 45, 25])

        self.PowerHover = self.HelpHover = self.SettingsHover = False

        self.ButtonPower = pygame.transform.smoothscale(InstanceSystem.ButtonPower, (self.PowerW, self.PowerH))
        self.ButtonHelp = pygame.transform.smoothscale(InstanceSystem.ButtonHelp, (self.HelpW, self.HelpH))
        self.ButtonSettings = pygame.transform.smoothscale(InstanceSystem.ButtonSettings, (self.SettingsW, self.SettingsH))

        if InstanceSystem.Fullscreen:
            InstanceScreen.FullscreenX, InstanceScreen.FullscreenY = map(lambda x: (x * InstanceSystem.SF), [1840, 130])
            InstanceMaps.MapX, InstanceMaps.MapY = map(lambda x: (x * InstanceSystem.SF), [1760, 130])
            self.ButtonFullscreen = pygame.transform.smoothscale(InstanceSystem.ButtonFullscreenB, (InstanceScreen.FullscreenW, InstanceScreen.FullscreenH))
        else:
            InstanceScreen.FullscreenX, InstanceScreen.FullscreenY = map(lambda x: (x * InstanceSystem.SF), [1300, 330])
            InstanceMaps.MapX, InstanceMaps.MapY = map(lambda x: (x * InstanceSystem.SF), [1220, 330])
            self.ButtonFullscreen = pygame.transform.smoothscale(InstanceSystem.ButtonFullscreenA, (InstanceScreen.FullscreenW, InstanceScreen.FullscreenH))

    def Display(self):
        Buttons = [
            (self.PowerX, self.PowerY, self.PowerW, self.PowerH, self.PowerHover, self.ButtonPower),
            (self.HelpX, self.HelpY, self.HelpW, self.HelpH, self.HelpHover, self.ButtonHelp),
            (self.SettingsX, self.SettingsY, self.SettingsW, self.SettingsH, self.SettingsHover, self.ButtonSettings)
        ]

        for x, y, w, h, hover, button in Buttons:
            if hover:
                w, h = (w/1.1), (h/1.1)
                button = pygame.transform.smoothscale(button, (w, h))

            InstanceSystem.Window.blit(button, (x - w/2, y - h/2))

    def PowerClick(self):
        InstanceSystem.Shutdown()

    def HelpClick(self):
        try:
            webbrowser.open('https://docs.google.com/document/d/1o5DzYlDGw8EA5sNgJ2KQhO6NBD3abbEZ3APZ8Fw8ue4/edit?usp=sharing')
        except Exception as e:
            InstanceErrors.Message = e

    def SettingsClick(self):
        InstanceSettings.Active = not InstanceSettings.Active
        for _, _, condition, _, _, _, _, _ in InstanceInput.TextFields: globals()[condition] = False

InstanceButtons = ClassButtons()

class ClassPopups:
    def __init__(self):
        self.PopupTrackerX, self.PopupTrackerY, self.PopupTrackerR = map(lambda x: (x * InstanceSystem.SF), [380, 500, 40])
        self.PopupVentingX, self.PopupVentingY, self.PopupVentingR = map(lambda x: (x * InstanceSystem.SF), [380, 875, 40])
        self.PopupConnectionsX, self.PopupConnectionsY, self.PopupConnectionsR = map(lambda x: (x * InstanceSystem.SF), [1312.5, 252.5, 40])
        self.PopupParsersX, self.PopupParsersY, self.PopupParsersR = map(lambda x: (x * InstanceSystem.SF), [1312.5, 432.5, 40])
        self.PopupPredictionsX, self.PopupPredictionsY, self.PopupPredictionsR = map(lambda x: (x * InstanceSystem.SF), [1312.5, 522.5, 40])

        self.HintTrackerX, self.HintTrackerY, self.HintTrackerW, self.HintTrackerH = map(lambda x: (x * InstanceSystem.SF), [440, 500, 300, 290])
        self.HintVentingX, self.HintVentingY, self.HintVentingW, self.HintVentingH = map(lambda x: (x * InstanceSystem.SF), [440, 875, 300, 200])
        self.HintConnectionsX, self.HintConnectionsY, self.HintConnectionsW, self.HintConnectionsH = map(lambda x: (x * InstanceSystem.SF), [1000, 252.5, 300, 270])
        self.HintParsersX, self.HintParsersY, self.HintParsersW, self.HintParsersH = map(lambda x: (x * InstanceSystem.SF), [1000, 432.5, 300, 210])
        self.HintPredictionsX, self.HintPredictionsY, self.HintPredictionsW, self.HintPredictionsH = map(lambda x: (x * InstanceSystem.SF), [1000, 522.5, 300, 320])

        self.PopupTrackerHover = self.PopupVentingHover = self.PopupConnectionsHover = self.PopupParsersHover = self.PopupPredictionsHover = False
        self.PopupTrackerLinger = self.PopupVentingLinger = self.PopupConnectionsLinger = self.PopupParsersLinger = self.PopupPredictionsLinger = False

        self.IconOn = pygame.transform.smoothscale(InstanceSystem.HintOn, (50 * InstanceSystem.SF, 60 * InstanceSystem.SF))
        self.IconOff = pygame.transform.smoothscale(InstanceSystem.HintOff, (50 * InstanceSystem.SF, 60 * InstanceSystem.SF))

        self.HintTracker = [
            ("Tracking with HERMES", (0, 0)),
            ("Orient the ground station dish north", (465, 560)),
            ("and level with the ground", (465, 580)),
            ("This can be done manually or with", (465, 620)),
            ("tweak controls", (465, 640)),
            ("Ensure the ground station is plugged", (465, 680)),
            ("into the computer and Arduino is ON", (465, 700)),
            ("Click the center of the D-Pad to begin", (465, 740)),
            ("automatic tracking", (465, 760))
        ]

        self.HintVenting = [
            ("Venting and Floating", (0, 0)),
            ("HERMES can send open, close, and cut", (465, 935)),
            ("commands directly to the Iridium unit", (465, 955)),
            ("Be sure to monitor the ascent rate", (465, 995)),
            ("while the vent is open", (465, 1015)),
            ("See SETTINGS for automatic controls", (465, 1055))
        ]

        self.HintConnections = [
            ("Accessing Radios", (0, 0)),
            ("Iridium and APRS are used for tracking", (1025, 312.5)),
            ("The former expects a modem name;", (1025, 352.5)),
            ("the latter expects a callsign", (1025, 372.5)),
            ("RFD is likewise used for tracking, but", (1025, 412.5)),
            ("it connects via serial", (1025, 432.5)),
            ("Ubiquiti is the video streaming radio - ", (1025, 472.5)),
            ("connect by entering the IP address", (1025, 492.5))
        ]

        self.HintParsers = [
            ("Data Parsers", (0, 0)),
            ("Each radio saves its own data file", (1025, 492.5)),
            ("This tool converts the geospatial data", (1025, 532.5)),
            ("to a common format and plots it", (1025, 552.5)),
            ("Select a generated data file to analyze", (1025, 592.5)),
            ("and create lat/lon and altitude graphs", (1025, 612.5))
        ]

        self.HintPredictions = [
            ("Running Predictions", (0, 0)),
            ("This interface allows users to generate", (1025, 582.5)),
            ("flight path predictions for a balloon", (1025, 602.5)),
            ("using meteorological data", (1025, 622.5)),
            ("Enter the launch parameters including", (1025, 662.5)),
            ("coordinates, altitude, date, and time", (1025, 682.5)),
            ("The final altitude should be the apex", (1025, 722.5)),
            ("If the balloon is ascending to burst,", (1025, 762.5)),
            ("Enter 0 for the float altitude and time", (1025, 782.5)),
            ("Click 'RUN FLIGHT PREDICTIONS'", (1025, 822.5))
        ]

    def Display(self):
        if not InstanceSystem.Fullscreen:
            if not InstanceSettings.Active:
                InstanceSystem.Window.blit(self.IconOn if (self.PopupTrackerHover or self.PopupTrackerLinger) else self.IconOff, (self.PopupTrackerX, self.PopupTrackerY))
                InstanceSystem.Window.blit(self.IconOn if (self.PopupVentingHover or self.PopupVentingLinger) else self.IconOff, (self.PopupVentingX, self.PopupVentingY))
            else:
                InstanceSystem.Window.blit(self.IconOn if (self.PopupConnectionsHover or self.PopupConnectionsLinger) else self.IconOff, (self.PopupConnectionsX, self.PopupConnectionsY))
                InstanceSystem.Window.blit(self.IconOn if (self.PopupParsersHover or self.PopupParsersLinger) else self.IconOff, (self.PopupParsersX, self.PopupParsersY))
                InstanceSystem.Window.blit(self.IconOn if (self.PopupPredictionsHover or self.PopupPredictionsLinger) else self.IconOff, (self.PopupPredictionsX, self.PopupPredictionsY))

            def DrawPopup(condition, settings, x, y, w, h, hints):
                if condition and settings == InstanceSettings.Active:
                    pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorDarkGray, (x, y, w, h))
                    pygame.draw.rect(InstanceSystem.Window, (255, 255, 255, 1), (x, y, w, h), 1)

                    for idx, (text, pos) in enumerate(hints):
                        Text = (InstanceSystem.FontBahnschrift25 if idx == 0 else InstanceSystem.FontBahnschrift15).render(text, True, InstanceSystem.ColorWhite)
                        TextRect = Text.get_rect(center=(x + w / 2, y + 25 * InstanceSystem.SF)) if idx == 0 else Text.get_rect(left=pos[0] * InstanceSystem.SF, top=pos[1] * InstanceSystem.SF)
                        InstanceSystem.Window.blit(Text, TextRect)

            DrawPopup(self.PopupTrackerHover or self.PopupTrackerLinger, False, self.HintTrackerX, self.HintTrackerY, self.HintTrackerW, self.HintTrackerH, self.HintTracker)
            DrawPopup(self.PopupVentingHover or self.PopupVentingLinger, False, self.HintVentingX, self.HintVentingY, self.HintVentingW, self.HintVentingH, self.HintVenting)
            DrawPopup(self.PopupConnectionsHover or self.PopupConnectionsLinger, True, self.HintConnectionsX, self.HintConnectionsY, self.HintConnectionsW, self.HintConnectionsH, self.HintConnections)
            DrawPopup(self.PopupParsersHover or self.PopupParsersLinger, True, self.HintParsersX, self.HintParsersY, self.HintParsersW, self.HintParsersH, self.HintParsers)
            DrawPopup(self.PopupPredictionsHover or self.PopupPredictionsLinger, True, self.HintPredictionsX, self.HintPredictionsY, self.HintPredictionsW, self.HintPredictionsH, self.HintPredictions)

    def PopupTrackerClick(self):
        self.PopupTrackerLinger = not self.PopupTrackerLinger

    def PopupVentingClick(self):
        self.PopupVentingLinger = not self.PopupVentingLinger

    def PopupConnectionsClick(self):
        self.PopupConnectionsLinger = not self.PopupConnectionsLinger

    def PopupParsersClick(self):
        self.PopupParsersLinger = not self.PopupParsersLinger

    def PopupPredictionsClick(self):
        self.PopupPredictionsLinger = not self.PopupPredictionsLinger

InstancePopups = ClassPopups()

class ClassSettings:
    def __init__(self):
        self.Active = False

        self.MenuX, self.MenuY, self.MenuW, self.MenuH = map(lambda x: (x * InstanceSystem.SF), [320, 180, 1280, 720])

        self.HeaderW, self.HeaderH = self.MenuX, self.MenuY / 2
        self.HeaderX, self.HeaderY = self.MenuX + (self.MenuW - self.HeaderW) / 2, 3 * self.HeaderH / 2

        self.WidthX, self.WidthY, self.WidthW, self.WidthH = map(lambda x: (x * InstanceSystem.SF), [360, 300, 120, 30])
        self.HeightX, self.HeightY, self.HeightW, self.HeightH = map(lambda x: (x * InstanceSystem.SF), [490, 300, 120, 30])

        self.FlagUSX, self.FlagUSY, self.FlagUSW, self.FlagUSH = 70 * InstanceSystem.SF, 180 * InstanceSystem.SF, InstanceSystem.FlagUS.get_width(), InstanceSystem.FlagUS.get_height()
        self.FlagMNX, self.FlagMNY, self.FlagMNW, self.FlagMNH = 1650 * InstanceSystem.SF, 180 * InstanceSystem.SF, InstanceSystem.FlagMN.get_width(), InstanceSystem.FlagMN.get_height()

        self.AltimeterX, self.AltimeterY, self.AltimeterW, self.AltimeterH = map(lambda x: (x * InstanceSystem.SF), [360, 420, 20, 20])
        self.NavigatorX, self.NavigatorY, self.NavigatorW, self.NavigatorH = map(lambda x: (x * InstanceSystem.SF), [360, 460, 20, 20])
        self.CompassX, self.CompassY, self.CompassW, self.CompassH = map(lambda x: (x * InstanceSystem.SF), [360, 500, 20, 20])
        self.TimerX, self.TimerY, self.TimerW, self.TimerH = map(lambda x: (x * InstanceSystem.SF), [360, 540, 20, 20])

        self.TrackerLatX, self.TrackerLatY, self.TrackerLatW, self.TrackerLatH = map(lambda x: (x * InstanceSystem.SF), [360, 770, 120, 30])
        self.TrackerLonX, self.TrackerLonY, self.TrackerLonW, self.TrackerLonH = map(lambda x: (x * InstanceSystem.SF), [490, 770, 120, 30])
        self.TrackerAltX, self.TrackerAltY, self.TrackerAltW, self.TrackerAltH = map(lambda x: (x * InstanceSystem.SF), [620, 770, 120, 30])

        self.PayloadLatX, self.PayloadLatY, self.PayloadLatW, self.PayloadLatH = map(lambda x: (x * InstanceSystem.SF), [360, 715, 120, 30])
        self.PayloadLonX, self.PayloadLonY, self.PayloadLonW, self.PayloadLonH = map(lambda x: (x * InstanceSystem.SF), [490, 715, 120, 30])
        self.PayloadAltX, self.PayloadAltY, self.PayloadAltW, self.PayloadAltH = map(lambda x: (x * InstanceSystem.SF), [620, 715, 120, 30])

        self.AutoTrackerX, self.AutoTrackerY, self.AutoTrackerW, self.AutoTrackerH = map(lambda x: (x * InstanceSystem.SF), [750, 770, 30, 30])
        self.AutoPayloadX, self.AutoPayloadY, self.AutoPayloadW, self.AutoPayloadH = map(lambda x: (x * InstanceSystem.SF), [750, 715, 30, 30])

        self.TargetLatX, self.TargetLatY, self.TargetLatW, self.TargetLatH = map(lambda x: (x * InstanceSystem.SF), [845, 300, 115, 30])
        self.TargetLonX, self.TargetLonY, self.TargetLonW, self.TargetLonH = map(lambda x: (x * InstanceSystem.SF), [970, 300, 115, 30])

        self.COMRFDX, self.COMRFDY, self.COMRFDW, self.COMRFDH = map(lambda x: (x * InstanceSystem.SF), [845, 415, 115, 30])
        self.COMArduinoX, self.COMArduinoY, self.COMArduinoW, self.COMArduinoH = map(lambda x: (x * InstanceSystem.SF), [970, 415, 115, 30])

        self.IridiumX, self.IridiumY, self.IridiumW, self.IridiumH = map(lambda x: (x * InstanceSystem.SF), [1365, 300, 200, 30])
        self.APRSX, self.APRSY, self.APRSW, self.APRSH = map(lambda x: (x * InstanceSystem.SF), [1365, 345, 200, 30])
        self.UbiquitiX, self.UbiquitiY, self.UbiquitiW, self.UbiquitiH = map(lambda x: (x * InstanceSystem.SF), [1365, 390, 200, 30])

        self.VentAltOpenX, self.VentAltOpenY, self.VentAltOpenW, self.VentAltOpenH = map(lambda x: (x * InstanceSystem.SF), [1030, 710, 240, 30])
        self.VentAltCloseX, self.VentAltCloseY, self.VentAltCloseW, self.VentAltCloseH = map(lambda x: (x * InstanceSystem.SF), [1030, 770, 240, 30])
        self.VentVelCloseX, self.VentVelCloseY, self.VentVelCloseW, self.VentVelCloseH = map(lambda x: (x * InstanceSystem.SF), [940, 770, 40, 30])

        self.AutoCOMX, self.AutoCOMY, self.AutoCOMW, self.AutoCOMH = map(lambda x: (x * InstanceSystem.SF), [845, 455, 15, 15])
        self.AutoDescentX, self.AutoDescentY, self.AutoDescentW, self.AutoDescentH = map(lambda x: (x * InstanceSystem.SF), [845, 340, 15, 15])

        self.ManualCoordsX, self.ManualCoordsY, self.ManualCoordsR = map(lambda x: (x * InstanceSystem.SF), [375, 675, 15])
        self.DarkModeX, self.DarkModeY, self.DarkModeR = map(lambda x: (x * InstanceSystem.SF), [860, 525, 15])
        self.MetricUnitsX, self.MetricUnitsY, self.MetricUnitsR = map(lambda x: (x * InstanceSystem.SF), [860, 575, 15])
        self.AutoVentX, self.AutoVentY, self.AutoVentR = map(lambda x: (x * InstanceSystem.SF), [860, 675, 15])

        self.Parser1X, self.Parser1Y, self.Parser1W, self.Parser1H = map(lambda x: (x * InstanceSystem.SF), [1365, 480, 60, 30])
        self.Parser2X, self.Parser2Y, self.Parser2W, self.Parser2H = map(lambda x: (x * InstanceSystem.SF), [1435, 480, 60, 30])
        self.Parser3X, self.Parser3Y, self.Parser3W, self.Parser3H = map(lambda x: (x * InstanceSystem.SF), [1505, 480, 60, 30])

        self.PredictionLatX, self.PredictionLatY, self.PredictionLatW, self.PredictionLatH = map(lambda x: (x * InstanceSystem.SF), [1365, 570, 60, 30])
        self.PredictionLonX, self.PredictionLonY, self.PredictionLonW, self.PredictionLonH = map(lambda x: (x * InstanceSystem.SF), [1435, 570, 60, 30])
        self.PredictionAltX, self.PredictionAltY, self.PredictionAltW, self.PredictionAltH = map(lambda x: (x * InstanceSystem.SF), [1505, 570, 60, 30])
        self.PredictionAscentX, self.PredictionAscentY, self.PredictionAscentW, self.PredictionAscentH = map(lambda x: (x * InstanceSystem.SF), [1365, 610, 95, 30])
        self.PredictionDescentX, self.PredictionDescentY, self.PredictionDescentW, self.PredictionDescentH = map(lambda x: (x * InstanceSystem.SF), [1470, 610, 95, 30])
        self.PredictionFinalAltX, self.PredictionFinalAltY, self.PredictionFinalAltW, self.PredictionFinalAltH = map(lambda x: (x * InstanceSystem.SF), [1365, 650, 200, 30])
        self.PredictionDateX, self.PredictionDateY, self.PredictionDateW, self.PredictionDateH = map(lambda x: (x * InstanceSystem.SF), [1365, 690, 95, 30])
        self.PredictionTimeX, self.PredictionTimeY, self.PredictionTimeW, self.PredictionTimeH = map(lambda x: (x * InstanceSystem.SF), [1470, 690, 95, 30])
        self.PredictionFloatAltX, self.PredictionFloatAltY, self.PredictionFloatAltW, self.PredictionFloatAltH = map(lambda x: (x * InstanceSystem.SF), [1365, 730, 95, 30])
        self.PredictionFloatTimeX, self.PredictionFloatTimeY, self.PredictionFloatTimeW, self.PredictionFloatTimeH = map(lambda x: (x * InstanceSystem.SF), [1470, 730, 95, 30])
        self.RunPredictionsX, self.RunPredictionsY, self.RunPredictionsW, self.RunPredictionsH = map(lambda x: (x * InstanceSystem.SF), [1365, 770, 200, 30])

        self.DemoModeX, self.DemoModeY, self.DemoModeR = map(lambda x: (x * InstanceSystem.SF), [860, 925, 15])

        self.WidthHover = self.HeightHover = False
        self.AltimeterHover = self.NavigatorHover = self.CompassHover = self.TimerHover = False
        self.TrackerLatHover = self.TrackerLonHover = self.TrackerAltHover = False
        self.PayloadLatHover = self.PayloadLonHover = self.PayloadAltHover = False
        self.ManualCoordsHover = self.AutoDescentHover = self.AutoCOMHover =  self.AutoVentHover = False
        self.DarkModeHover = self.MetricUnitsHover = False
        self.AutoTrackerHover = self.AutoPayloadHover = False
        self.TargetLatHover = self.TargetLonHover = False
        self.COMRFDHover = self.COMArduinoHover = False
        self.AltOpenHover = self.AltCloseHover = self.VelCloseHover = False
        self.IridiumHover = self.APRSHover = self.UbiquitiHover = False
        self.Parser1Hover = self.Parser2Hover = self.Parser3Hover = False
        self.PredictionLatHover = self.PredictionLonHover = self.PredictionAltHover = False
        self.PredictionAscentHover = self.PredictionDescentHover = self.PredictionFinalAltHover = False
        self.PredictionDateHover = self.PredictionTimeHover = False
        self.PredictionFloatAltHover = self.PredictionFloatTimeHover = False
        self.RunPredictionsHover = False
        self.DemoModeHover = False

        self.ButtonOn = pygame.transform.smoothscale(InstanceSystem.CircleGreen, (30 * InstanceSystem.SF, 30 * InstanceSystem.SF))
        self.ButtonOff = pygame.transform.smoothscale(InstanceSystem.CircleRed, (30 * InstanceSystem.SF, 30 * InstanceSystem.SF))

        self.Rects = [
            (InstanceSystem.ColorBlack, (self.MenuX, self.MenuY, self.MenuW, self.MenuH), 0),
            (InstanceSystem.ColorWhite, (self.MenuX, self.MenuY, self.MenuW, self.MenuH), 2),
            (InstanceSystem.ColorBlack, (self.HeaderX, self.HeaderY, self.HeaderW, self.HeaderH), 0),
            (InstanceSystem.ColorWhite, (self.HeaderX, self.HeaderY, self.HeaderW, self.HeaderH), 2),
            (InstanceSystem.ColorWhite, (self.WidthX, self.WidthY, self.WidthW, self.WidthH), 1),
            (InstanceSystem.ColorWhite, (self.HeightX, self.HeightY, self.HeightW, self.HeightH), 1),
            (InstanceSystem.ColorGreen, (self.AltimeterX, self.AltimeterY, self.AltimeterW, self.AltimeterH), 0),
            (InstanceSystem.ColorWhite, (self.AltimeterX, self.AltimeterY, self.AltimeterW, self.AltimeterH), 1),
            (InstanceSystem.ColorGreen, (self.NavigatorX, self.NavigatorY, self.NavigatorW, self.NavigatorH), 0),
            (InstanceSystem.ColorWhite, (self.NavigatorX, self.NavigatorY, self.NavigatorW, self.NavigatorH), 1),
            (InstanceSystem.ColorGreen, (self.CompassX, self.CompassY, self.CompassW, self.CompassH), 0),
            (InstanceSystem.ColorWhite, (self.CompassX, self.CompassY, self.CompassW, self.CompassH), 1),
            (InstanceSystem.ColorGreen, (self.TimerX, self.TimerY, self.TimerW, self.TimerH), 0),
            (InstanceSystem.ColorWhite, (self.TimerX, self.TimerY, self.TimerW, self.TimerH), 1),
            (InstanceSystem.ColorLightGrey, (self.PayloadLatX, self.PayloadLatY, self.PayloadLatW, self.PayloadLatH), 1),
            (InstanceSystem.ColorLightGrey, (self.PayloadLonX, self.PayloadLonY, self.PayloadLonW, self.PayloadLonH), 1),
            (InstanceSystem.ColorLightGrey, (self.PayloadAltX, self.PayloadAltY, self.PayloadAltW, self.PayloadAltH), 1),
            (InstanceSystem.ColorWhite, (self.TrackerLatX, self.TrackerLatY, self.TrackerLatW, self.TrackerLatH), 1),
            (InstanceSystem.ColorWhite, (self.TrackerLonX, self.TrackerLonY, self.TrackerLonW, self.TrackerLonH), 1),
            (InstanceSystem.ColorWhite, (self.TrackerAltX, self.TrackerAltY, self.TrackerAltW, self.TrackerAltH), 1),
            (InstanceSystem.ColorWhite, (self.AutoTrackerX, self.AutoTrackerY, self.AutoTrackerW, self.AutoTrackerH), 1),
            (InstanceSystem.ColorWhite, (self.AutoPayloadX, self.AutoPayloadY, self.AutoPayloadW, self.AutoPayloadH), 1),
            (InstanceSystem.ColorWhite, (self.TargetLatX, self.TargetLatY, self.TargetLatW, self.TargetLatH), 1),
            (InstanceSystem.ColorWhite, (self.TargetLonX, self.TargetLonY, self.TargetLonW, self.TargetLonH), 1),
            (InstanceSystem.ColorLightRed, (self.AutoDescentX, self.AutoDescentY, self.AutoDescentW, self.AutoDescentH), 0),
            (InstanceSystem.ColorWhite, (self.AutoDescentX, self.AutoDescentY, self.AutoDescentW, self.AutoDescentH), 1),
            (InstanceSystem.ColorLightGrey, (self.COMRFDX, self.COMRFDY, self.COMRFDW, self.COMRFDH), 1),
            (InstanceSystem.ColorLightGrey, (self.COMArduinoX, self.COMArduinoY, self.COMArduinoW, self.COMArduinoH), 1),
            (InstanceSystem.ColorGreen, (self.AutoCOMX, self.AutoCOMY, self.AutoCOMW, self.AutoCOMH), 0),
            (InstanceSystem.ColorWhite, (self.AutoCOMX, self.AutoCOMY, self.AutoCOMW, self.AutoCOMH), 1),
            (InstanceSystem.ColorLightGrey, (self.VentAltOpenX, self.VentAltOpenY, self.VentAltOpenW, self.VentAltOpenH), 1),
            (InstanceSystem.ColorLightGrey, (self.VentVelCloseX, self.VentVelCloseY, self.VentVelCloseW, self.VentVelCloseH), 1),
            (InstanceSystem.ColorLightGrey, (self.VentAltCloseX, self.VentAltCloseY, self.VentAltCloseW, self.VentAltCloseH), 1),
            (InstanceSystem.ColorWhite, (self.IridiumX, self.IridiumY, self.IridiumW, self.IridiumH), 1),
            (InstanceSystem.ColorWhite, (self.APRSX, self.APRSY, self.APRSW, self.APRSH), 1),
            (InstanceSystem.ColorWhite, (self.UbiquitiX, self.UbiquitiY, self.UbiquitiW, self.UbiquitiH), 1),
            (InstanceSystem.ColorWhite, (self.Parser1X, self.Parser1Y, self.Parser1W, self.Parser1H), 1),
            (InstanceSystem.ColorWhite, (self.Parser2X, self.Parser2Y, self.Parser2W, self.Parser2H), 1),
            (InstanceSystem.ColorWhite, (self.Parser3X, self.Parser3Y, self.Parser3W, self.Parser3H), 1),
            (InstanceSystem.ColorWhite, (self.PredictionLatX, self.PredictionLatY, self.PredictionLatW, self.PredictionLatH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionLonX, self.PredictionLonY, self.PredictionLonW, self.PredictionLonH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionAltX, self.PredictionAltY, self.PredictionAltW, self.PredictionAltH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionAscentX, self.PredictionAscentY, self.PredictionAscentW, self.PredictionAscentH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionDescentX, self.PredictionDescentY, self.PredictionDescentW, self.PredictionDescentH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionFinalAltX, self.PredictionFinalAltY, self.PredictionFinalAltW, self.PredictionFinalAltH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionDateX, self.PredictionDateY, self.PredictionDateW, self.PredictionDateH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionTimeX, self.PredictionTimeY, self.PredictionTimeW, self.PredictionTimeH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionFloatAltX, self.PredictionFloatAltY, self.PredictionFloatAltW, self.PredictionFloatAltH), 1),
            (InstanceSystem.ColorWhite, (self.PredictionFloatTimeX, self.PredictionFloatTimeY, self.PredictionFloatTimeW, self.PredictionFloatTimeH), 1),
            (InstanceSystem.ColorWhite, (self.RunPredictionsX, self.RunPredictionsY, self.RunPredictionsW, self.RunPredictionsH), 1)
        ]

        self.Lines = [
            (InstanceSystem.ColorWhite, ((360 * InstanceSystem.SF, 755 * InstanceSystem.SF), (740 * InstanceSystem.SF, 755 * InstanceSystem.SF)), 4),
            (InstanceSystem.ColorWhite, ((840 * InstanceSystem.SF, 755 * InstanceSystem.SF), (1275 * InstanceSystem.SF, 755 * InstanceSystem.SF)), 4)
        ]

        self.Texts = [
            (InstanceSystem.FontImpact80, "SETTINGS", InstanceSystem.ColorWhite, 'Center', (self.MenuX + self.MenuW / 2, self.MenuY)),
            (InstanceSystem.FontBahnschrift30, "UI SCALE", InstanceSystem.ColorWhite, 'Left', (360 * InstanceSystem.SF, 280 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "UI WIDTH", InstanceSystem.ColorWhite, 'Center', (self.WidthX + self.WidthW / 2, self.WidthY + self.WidthH / 2)),
            (InstanceSystem.FontBahnschrift15, "UI WIDTH", InstanceSystem.ColorWhite, 'Center', (self.HeightX + self.HeightW / 2, self.HeightY + self.HeightH / 2)),
            (InstanceSystem.FontBahnschrift30, "PERIPHERALS", InstanceSystem.ColorWhite, 'Left', (360 * InstanceSystem.SF, 395 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift25, "Altimeter", InstanceSystem.ColorWhite, 'Left', (self.AltimeterX + 1.5 * self.AltimeterW, self.AltimeterY + self.AltimeterH / 2)),
            (InstanceSystem.FontBahnschrift25, "Navigator", InstanceSystem.ColorWhite, 'Left', (self.NavigatorX + 1.5 * self.NavigatorW, self.NavigatorY + self.NavigatorH / 2)),
            (InstanceSystem.FontBahnschrift25, "Compass", InstanceSystem.ColorWhite, 'Left', (self.CompassX + 1.5 * self.CompassW, self.CompassY + self.CompassH / 2)),
            (InstanceSystem.FontBahnschrift25, "Timer", InstanceSystem.ColorWhite, 'Left', (self.TimerX + 1.5 * self.TimerW, self.TimerY + self.TimerH / 2)),
            (InstanceSystem.FontBahnschrift30, "Automatic Radio Tracking", InstanceSystem.ColorWhite, 'Left', (360 * InstanceSystem.SF, 630 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift25, "Disable for Manual Entry", InstanceSystem.ColorWhite, 'Left', (self.ManualCoordsX + 2 * self.ManualCoordsR, self.ManualCoordsY)),
            (InstanceSystem.FontBahnschrift15, "PAYLOAD LAT", InstanceSystem.ColorLightGrey, 'Center', (self.PayloadLatX + self.PayloadLatW / 2, self.PayloadLatY + self.PayloadLatH / 2)),
            (InstanceSystem.FontBahnschrift15, "PAYLOAD LON", InstanceSystem.ColorLightGrey, 'Center', (self.PayloadLonX + self.PayloadLonW / 2, self.PayloadLonY + self.PayloadLonH / 2)),
            (InstanceSystem.FontBahnschrift15, "PAYLOAD ALT", InstanceSystem.ColorLightGrey, 'Center', (self.PayloadAltX + self.PayloadAltW / 2, self.PayloadAltY + self.PayloadAltH / 2)),
            (InstanceSystem.FontBahnschrift15, "TRACKER LAT", InstanceSystem.ColorWhite, 'Center', (self.TrackerLatX + self.TrackerLatW / 2, self.TrackerLatY + self.TrackerLatH / 2)),
            (InstanceSystem.FontBahnschrift15, "TRACKER LON", InstanceSystem.ColorWhite, 'Center', (self.TrackerLonX + self.TrackerLonW / 2, self.TrackerLonY + self.TrackerLonH / 2)),
            (InstanceSystem.FontBahnschrift15, "TRACKER ALT", InstanceSystem.ColorWhite, 'Center', (self.TrackerAltX + self.TrackerAltW / 2, self.TrackerAltY + self.TrackerAltH / 2)),
            (InstanceSystem.FontBahnschrift15, "", InstanceSystem.ColorWhite, 'Center', (550 * InstanceSystem.SF, 820 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "", InstanceSystem.ColorWhite, 'Center', (550 * InstanceSystem.SF, 840 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift30, "GUIDED DESCENT", InstanceSystem.ColorWhite, 'Left', (845 * InstanceSystem.SF, 280 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "TARGET LAT", InstanceSystem.ColorWhite, 'Center', (self.TargetLatX + self.TargetLatW / 2, self.TargetLatY + self.TargetLatH / 2)),
            (InstanceSystem.FontBahnschrift15, "TARGET LON", InstanceSystem.ColorWhite, 'Center', (self.TargetLonX + self.TargetLonW / 2, self.TargetLonY + self.TargetLonH / 2)),
            (InstanceSystem.FontBahnschrift15, "SAME AS TRACKER", InstanceSystem.ColorWhite, 'Left', (self.AutoDescentX + 1.5 * self.AutoDescentW, self.AutoDescentY + self.AutoDescentH / 2)),
            (InstanceSystem.FontBahnschrift30, "SERIAL COMMUNICATION", InstanceSystem.ColorWhite, 'Left', (845 * InstanceSystem.SF, 395 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "RFD COM", InstanceSystem.ColorLightGrey, 'Center', (self.COMRFDX + self.COMRFDW / 2, self.COMRFDY + self.COMRFDH / 2)),
            (InstanceSystem.FontBahnschrift15, "ARDUINO COM", InstanceSystem.ColorLightGrey, 'Center', (self.COMArduinoX + self.COMArduinoW / 2, self.COMArduinoY + self.COMArduinoH / 2)),
            (InstanceSystem.FontBahnschrift15, "AUTO COM PORT DETECTION", InstanceSystem.ColorWhite, 'Left', (self.AutoCOMX + 1.5 * self.AutoCOMW, self.AutoCOMY + self.AutoCOMH / 2)),
            (InstanceSystem.FontBahnschrift25, "Dark Mode", InstanceSystem.ColorWhite, 'Left', (self.DarkModeX + 2 * self.DarkModeR, self.DarkModeY)),
            (InstanceSystem.FontBahnschrift25, "Metric Units", InstanceSystem.ColorWhite, 'Left', (self.MetricUnitsX + 2 * self.MetricUnitsR, self.MetricUnitsY)),
            (InstanceSystem.FontBahnschrift30, "Automatic Vent Commanding", InstanceSystem.ColorWhite, 'Left', (845 * InstanceSystem.SF, 630 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift25, "Enable for Automatic Float", InstanceSystem.ColorWhite, 'Left', (self.AutoVentX + 2 * self.AutoVentR, self.AutoVentY)),
            (InstanceSystem.FontBahnschrift20, "BEGIN VENTING AT", InstanceSystem.ColorWhite, 'Center', (930 * InstanceSystem.SF, 730 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "ALTITUDE (ft)", InstanceSystem.ColorLightGrey, 'Center', (self.VentAltOpenX + self.VentAltOpenW / 4, self.VentAltOpenY + self.VentAltOpenH / 2)),
            (InstanceSystem.FontBahnschrift20, "CLOSE AT            OR", InstanceSystem.ColorWhite, 'Left', (845 * InstanceSystem.SF, 785 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "ft/s", InstanceSystem.ColorLightGrey, 'Center', (self.VentVelCloseX + self.VentVelCloseW / 2, self.VentVelCloseY + self.VentVelCloseH / 2)),
            (InstanceSystem.FontBahnschrift15, "ALTITUDE (ft)", InstanceSystem.ColorLightGrey, 'Center', (self.VentAltCloseX + self.VentAltCloseW / 4, self.VentAltCloseY + self.VentAltCloseH / 2)),
            (InstanceSystem.FontBahnschrift15, "", InstanceSystem.ColorLightGrey, 'Center', (1060 * InstanceSystem.SF, 820 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift30, "CONNECTIONS", InstanceSystem.ColorWhite, 'Left', (1365 * InstanceSystem.SF, 280 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "IRIDIUM MODEM", InstanceSystem.ColorWhite, 'Center', (self.IridiumX + self.IridiumW / 2, self.IridiumY + self.IridiumH / 2)),
            (InstanceSystem.FontBahnschrift15, "APRS CALLSIGN", InstanceSystem.ColorWhite, 'Center', (self.APRSX + self.APRSW / 2, self.APRSY + self.APRSH / 2)),
            (InstanceSystem.FontBahnschrift15, "STREAM IP", InstanceSystem.ColorWhite, 'Center', (self.UbiquitiX + self.UbiquitiW / 2, self.UbiquitiY + self.UbiquitiH / 2)),
            (InstanceSystem.FontBahnschrift30, "DATA PARSERS", InstanceSystem.ColorWhite, 'Left', (1365 * InstanceSystem.SF, 460 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "RFD", InstanceSystem.ColorWhite, 'Center', (self.Parser1X + self.Parser1W / 2, self.Parser1Y + self.Parser1H / 2)),
            (InstanceSystem.FontBahnschrift15, "IRIDIUM", InstanceSystem.ColorWhite, 'Center', (self.Parser2X + self.Parser2W / 2, self.Parser2Y + self.Parser2H / 2)),
            (InstanceSystem.FontBahnschrift15, "APRS", InstanceSystem.ColorWhite, 'Center', (self.Parser3X + self.Parser3W / 2, self.Parser3Y + self.Parser3H / 2)),
            (InstanceSystem.FontBahnschrift30, "PREDICTIONS", InstanceSystem.ColorWhite, 'Left', (1365 * InstanceSystem.SF, 550 * InstanceSystem.SF)),
            (InstanceSystem.FontBahnschrift15, "LAT", InstanceSystem.ColorWhite, 'Center', (self.PredictionLatX + self.PredictionLatW / 2, self.PredictionLatY + self.PredictionLatH / 2)),
            (InstanceSystem.FontBahnschrift15, "LON", InstanceSystem.ColorWhite, 'Center', (self.PredictionLonX + self.PredictionLonW / 2, self.PredictionLonY + self.PredictionLonH / 2)),
            (InstanceSystem.FontBahnschrift15, "ALT", InstanceSystem.ColorWhite, 'Center', (self.PredictionAltX + self.PredictionAltW / 2, self.PredictionAltY + self.PredictionAltH / 2)),
            (InstanceSystem.FontBahnschrift15, "ASCENT", InstanceSystem.ColorWhite, 'Center', (self.PredictionAscentX + self.PredictionAscentW / 2, self.PredictionAscentY + self.PredictionAscentH / 2)),
            (InstanceSystem.FontBahnschrift15, "DESCENT", InstanceSystem.ColorWhite, 'Center', (self.PredictionDescentX + self.PredictionDescentW / 2, self.PredictionDescentY + self.PredictionDescentH / 2)),
            (InstanceSystem.FontBahnschrift15, "FINAL ALTITUDE", InstanceSystem.ColorWhite, 'Center', (self.PredictionFinalAltX + self.PredictionFinalAltW / 2, self.PredictionFinalAltY + self.PredictionFinalAltH / 2)),
            (InstanceSystem.FontBahnschrift15, "DATE", InstanceSystem.ColorWhite, 'Center', (self.PredictionDateX + self.PredictionDateW / 2, self.PredictionDateY + self.PredictionDateH / 2)),
            (InstanceSystem.FontBahnschrift15, "TIME", InstanceSystem.ColorWhite, 'Center', (self.PredictionTimeX + self.PredictionTimeW / 2, self.PredictionTimeY + self.PredictionTimeH / 2)),
            (InstanceSystem.FontBahnschrift15, "FLOAT ALT", InstanceSystem.ColorWhite, 'Center', (self.PredictionFloatAltX + self.PredictionFloatAltW / 2, self.PredictionFloatAltY + self.PredictionFloatAltH / 2)),
            (InstanceSystem.FontBahnschrift15, "FLOAT TIME", InstanceSystem.ColorWhite, 'Center', (self.PredictionFloatTimeX + self.PredictionFloatTimeW / 2, self.PredictionFloatTimeY + self.PredictionFloatTimeH / 2)),
            (InstanceSystem.FontBahnschrift15, "RUN FLIGHT PREDICTIONS", InstanceSystem.ColorWhite, 'Center', (self.RunPredictionsX + self.RunPredictionsW / 2, self.RunPredictionsY + self.RunPredictionsH / 2)),
            (InstanceSystem.FontBahnschrift15, "HERMES RELEASE VERSION 1.16 | PRODUCED AND TESTED BY NASA'S MINNESOTA SPACE GRANT CONSORTIUM (MnSGC) AT THE UNIVERSITY OF MINNESOTA TWIN CITIES", InstanceSystem.ColorWhite, 'Center', (self.MenuX + self.MenuW / 2, self.MenuY + self.MenuH - self.MenuH / 32))
        ]

        self.Images = [
            (pygame.transform.smoothscale(InstanceSystem.FlagUS, (200 * InstanceSystem.SF, 720 * InstanceSystem.SF)), (self.FlagUSX, self.FlagUSY)),
            (pygame.transform.smoothscale(InstanceSystem.FlagMN, (200 * InstanceSystem.SF, 720 * InstanceSystem.SF)), (self.FlagMNX, self.FlagMNY)),
            (self.ButtonOff, (self.DarkModeX - self.DarkModeR, self.DarkModeY - self.DarkModeR)),
            (self.ButtonOff, (self.MetricUnitsX - self.MetricUnitsR, self.MetricUnitsY - self.MetricUnitsR)),
            (self.ButtonOff, (self.ManualCoordsX - self.ManualCoordsR, self.ManualCoordsY - self.ManualCoordsR)),
            (self.ButtonOff, (self.AutoVentX - self.AutoVentR, self.AutoVentY - self.AutoVentR))
            # (self.ButtonOff, (self.DemoModeX - self.DemoModeR, self.DemoModeY - self.DemoModeR))
        ]

    def Display(self):
        if self.Active:
            self.Rects[4] = (self.Rects[4][0], self.Rects[4][1], (2 if self.WidthHover else 1))
            self.Rects[5] = (self.Rects[5][0], self.Rects[5][1], (2 if self.HeightHover else 1))
            self.Rects[6] = ((InstanceSystem.ColorGreen if InstanceAltimeter.Enabled else InstanceSystem.ColorLightRed), self.Rects[6][1], self.Rects[6][2])
            self.Rects[7] = (self.Rects[7][0], self.Rects[7][1], (2 if self.AltimeterHover else 1))
            self.Rects[8] = ((InstanceSystem.ColorGreen if InstanceCompass.Enabled else InstanceSystem.ColorLightRed), self.Rects[8][1], self.Rects[8][2])
            self.Rects[9] = (self.Rects[9][0], self.Rects[9][1], (2 if self.NavigatorHover else 1))
            self.Rects[10] = ((InstanceSystem.ColorGreen if InstanceNavigator.Enabled else InstanceSystem.ColorLightRed), self.Rects[10][1], self.Rects[10][2])
            self.Rects[11] = (self.Rects[11][0], self.Rects[11][1], (2 if self.CompassHover else 1))
            self.Rects[12] = ((InstanceSystem.ColorGreen if InstanceTimer.Enabled else InstanceSystem.ColorLightRed), self.Rects[12][1], self.Rects[12][2])
            self.Rects[13] = (self.Rects[13][0], self.Rects[13][1], (2 if self.TimerHover else 1))
            self.Rects[14] = ((InstanceSystem.ColorWhite if InstanceSystem.Manual else InstanceSystem.ColorLightGrey), self.Rects[14][1], (2 if self.PayloadLatHover and InstanceSystem.Manual else 1))
            self.Rects[15] = ((InstanceSystem.ColorWhite if InstanceSystem.Manual else InstanceSystem.ColorLightGrey), self.Rects[15][1], (2 if self.PayloadLonHover and InstanceSystem.Manual else 1))
            self.Rects[16] = ((InstanceSystem.ColorWhite if InstanceSystem.Manual else InstanceSystem.ColorLightGrey), self.Rects[16][1], (2 if self.PayloadAltHover and InstanceSystem.Manual else 1))
            self.Rects[17] = (self.Rects[17][0], self.Rects[17][1], (2 if self.TrackerLatHover else 1))
            self.Rects[18] = (self.Rects[18][0], self.Rects[18][1], (2 if self.TrackerLonHover else 1))
            self.Rects[19] = (self.Rects[19][0], self.Rects[19][1], (2 if self.TrackerAltHover else 1))
            self.Rects[20] = (self.Rects[20][0], self.Rects[20][1], (3 if self.AutoTrackerHover else 1))
            self.Rects[21] = (self.Rects[21][0], self.Rects[21][1], (3 if self.AutoPayloadHover else 1))
            self.Rects[22] = ((InstanceSystem.ColorLightGrey if InstanceDescent.Automatic else InstanceSystem.ColorWhite), self.Rects[22][1], (2 if self.TargetLatHover and not InstanceDescent.Automatic else 1))
            self.Rects[23] = ((InstanceSystem.ColorLightGrey if InstanceDescent.Automatic else InstanceSystem.ColorWhite), self.Rects[23][1], (2 if self.TargetLonHover and not InstanceDescent.Automatic else 1))
            self.Rects[24] = ((InstanceSystem.ColorGreen if InstanceDescent.Automatic else InstanceSystem.ColorLightRed), self.Rects[24][1], self.Rects[24][2])
            self.Rects[25] = (self.Rects[25][0], self.Rects[25][1], (2 if self.AutoDescentHover else 1))
            self.Rects[26] = ((InstanceSystem.ColorLightGrey if InstanceSystem.AutoCOM else InstanceSystem.ColorWhite), self.Rects[26][1], (2 if self.COMRFDHover and not InstanceSystem.AutoCOM else 1))
            self.Rects[27] = ((InstanceSystem.ColorLightGrey if InstanceSystem.AutoCOM else InstanceSystem.ColorWhite), self.Rects[27][1], (2 if self.COMArduinoHover and not InstanceSystem.AutoCOM else 1))
            self.Rects[28] = ((InstanceSystem.ColorGreen if InstanceSystem.AutoCOM else InstanceSystem.ColorLightRed), self.Rects[28][1], self.Rects[28][2])
            self.Rects[29] = (self.Rects[29][0], self.Rects[29][1], (2 if self.AutoCOMHover else 1))
            self.Rects[30] = ((InstanceSystem.ColorLightGrey if InstanceVent.Manual else InstanceSystem.ColorWhite), self.Rects[30][1], (2 if self.AltOpenHover and not InstanceVent.Manual else 1))
            self.Rects[31] = ((InstanceSystem.ColorLightGrey if InstanceVent.Manual else InstanceSystem.ColorWhite), self.Rects[31][1], (2 if self.VelCloseHover and not InstanceVent.Manual else 1))
            self.Rects[32] = ((InstanceSystem.ColorLightGrey if InstanceVent.Manual else InstanceSystem.ColorWhite), self.Rects[32][1], (2 if self.AltCloseHover and not InstanceVent.Manual else 1))
            self.Rects[33] = (self.Rects[33][0], self.Rects[33][1], (2 if self.IridiumHover else 1))
            self.Rects[34] = (self.Rects[34][0], self.Rects[34][1], (2 if self.APRSHover else 1))
            self.Rects[35] = (self.Rects[35][0], self.Rects[35][1], (2 if self.UbiquitiHover else 1))
            self.Rects[36] = (self.Rects[36][0], self.Rects[36][1], (2 if self.Parser1Hover else 1))
            self.Rects[37] = (self.Rects[37][0], self.Rects[37][1], (2 if self.Parser2Hover else 1))
            self.Rects[38] = (self.Rects[38][0], self.Rects[38][1], (2 if self.Parser3Hover else 1))
            self.Rects[39] = (self.Rects[39][0], self.Rects[39][1], (2 if self.PredictionLatHover else 1))
            self.Rects[40] = (self.Rects[40][0], self.Rects[40][1], (2 if self.PredictionLonHover else 1))
            self.Rects[41] = (self.Rects[41][0], self.Rects[41][1], (2 if self.PredictionAltHover else 1))
            self.Rects[42] = (self.Rects[42][0], self.Rects[42][1], (2 if self.PredictionAscentHover else 1))
            self.Rects[43] = (self.Rects[43][0], self.Rects[43][1], (2 if self.PredictionDescentHover else 1))
            self.Rects[44] = (self.Rects[44][0], self.Rects[44][1], (2 if self.PredictionFinalAltHover else 1))
            self.Rects[45] = (self.Rects[45][0], self.Rects[45][1], (2 if self.PredictionDateHover else 1))
            self.Rects[46] = (self.Rects[46][0], self.Rects[46][1], (2 if self.PredictionTimeHover else 1))
            self.Rects[47] = (self.Rects[47][0], self.Rects[47][1], (2 if self.PredictionFloatAltHover else 1))
            self.Rects[48] = (self.Rects[48][0], self.Rects[48][1], (2 if self.PredictionFloatTimeHover else 1))
            self.Rects[49] = (self.Rects[49][0], self.Rects[49][1], (2 if self.RunPredictionsHover else 1))

            self.Texts[10] = (self.Texts[10][0], ("Enable for Automatic Entry" if InstanceSystem.Manual else "Disable for Manual Entry"), self.Texts[10][2], self.Texts[10][3], self.Texts[10][4])
            self.Texts[11] = (self.Texts[11][0], self.Texts[11][1], (InstanceSystem.ColorWhite if InstanceSystem.Manual else InstanceSystem.ColorLightGrey), self.Texts[11][3], self.Texts[11][4])
            self.Texts[12] = (self.Texts[12][0], self.Texts[12][1], (InstanceSystem.ColorWhite if InstanceSystem.Manual else InstanceSystem.ColorLightGrey), self.Texts[12][3], self.Texts[12][4])
            self.Texts[13] = (self.Texts[13][0], self.Texts[13][1], (InstanceSystem.ColorWhite if InstanceSystem.Manual else InstanceSystem.ColorLightGrey), self.Texts[13][3], self.Texts[13][4])
            self.Texts[17] = (self.Texts[17][0], ("Tracker: ({:.2f}°, {:.2f}°) {:.0f} {}".format(InstanceTracker.Lat, InstanceTracker.Lon, (InstanceTracker.Alt * 0.3048 if InstanceSystem.MetricUnits else InstanceTracker.Alt), ("m" if InstanceSystem.MetricUnits else "ft"))), self.Texts[17][2], self.Texts[17][3], self.Texts[17][4])
            self.Texts[18] = (self.Texts[18][0], ("Payload: ({:.2f}°, {:.2f}°) {:.0f} {}".format(InstancePayload.Lat, InstancePayload.Lon, (InstancePayload.Alt * 0.3048 if InstanceSystem.MetricUnits else InstancePayload.Alt), ("m" if InstanceSystem.MetricUnits else "ft"))), self.Texts[18][2], self.Texts[18][3], self.Texts[18][4])
            self.Texts[20] = (self.Texts[20][0], self.Texts[20][1], (InstanceSystem.ColorLightGrey if InstanceDescent.Automatic else InstanceSystem.ColorWhite), self.Texts[20][3], self.Texts[20][4])
            self.Texts[21] = (self.Texts[21][0], self.Texts[21][1], (InstanceSystem.ColorLightGrey if InstanceDescent.Automatic else InstanceSystem.ColorWhite), self.Texts[21][3], self.Texts[21][4])
            self.Texts[24] = (self.Texts[24][0], self.Texts[24][1], (InstanceSystem.ColorLightGrey if InstanceSystem.AutoCOM else InstanceSystem.ColorWhite), self.Texts[24][3], self.Texts[24][4])
            self.Texts[25] = (self.Texts[25][0], self.Texts[25][1], (InstanceSystem.ColorLightGrey if InstanceSystem.AutoCOM else InstanceSystem.ColorWhite), self.Texts[25][3], self.Texts[25][4])
            self.Texts[30] = (self.Texts[30][0], ("Enable for Automatic Float" if InstanceVent.Manual else "Disable for Manual Float"), self.Texts[30][2], self.Texts[30][3], self.Texts[30][4])
            self.Texts[32] = (self.Texts[32][0], ("ALTITUDE (m)" if InstanceSystem.MetricUnits else "ALTITUDE (ft)"), (InstanceSystem.ColorLightGrey if InstanceVent.Manual else InstanceSystem.ColorWhite), self.Texts[32][3], self.Texts[32][4])
            self.Texts[34] = (self.Texts[34][0], ("m/s" if InstanceSystem.MetricUnits else "ft/s"), (InstanceSystem.ColorLightGrey if InstanceVent.Manual else InstanceSystem.ColorWhite), self.Texts[34][3], self.Texts[34][4])
            self.Texts[35] = (self.Texts[35][0], ("ALTITUDE (m)" if InstanceSystem.MetricUnits else "ALTITUDE (ft)"), (InstanceSystem.ColorLightGrey if InstanceVent.Manual else InstanceSystem.ColorWhite), self.Texts[35][3], self.Texts[35][4])
            self.Texts[36] = (self.Texts[35][0], ("Vent Alt: {}  |  Float Alt: {}  |  Float Vel: {}".format(("None" if InstanceVent.AltOpen is None else "{:.0f} {}".format(InstanceVent.AltOpen * 0.3048 if InstanceSystem.MetricUnits else InstanceVent.AltOpen, "m" if InstanceSystem.MetricUnits else "ft")), ("None" if InstanceVent.AltClose is None else  "{:.0f} {}".format(InstanceVent.AltClose * 0.3048 if InstanceSystem.MetricUnits else InstanceVent.AltClose, "m" if InstanceSystem.MetricUnits else "ft")), ("None" if InstanceVent.VelClose is None else "{:.1f} {}".format(InstanceVent.VelClose * 0.3048 if InstanceSystem.MetricUnits else InstanceVent.VelClose, "m/s" if InstanceSystem.MetricUnits else "ft/s")))), (InstanceSystem.ColorLightGrey if InstanceVent.Manual else InstanceSystem.ColorWhite), self.Texts[36][3], self.Texts[36][4])

            self.Images[2] = [(self.ButtonOn if InstanceSystem.DarkMode else self.ButtonOff), self.Images[2][1]]
            self.Images[3] = [(self.ButtonOn if InstanceSystem.MetricUnits else self.ButtonOff), self.Images[3][1]]
            self.Images[4] = [(self.ButtonOn if not InstanceSystem.Manual else self.ButtonOff), self.Images[4][1]]
            self.Images[5] = [(self.ButtonOn if not InstanceVent.Manual else self.ButtonOff), self.Images[5][1]]
            # self.Images[6] = [(self.ButtonOn if InstanceDemo.Enabled else self.ButtonOff), self.Images[6][1]]

            for color, rect, weight in self.Rects: pygame.draw.rect(InstanceSystem.Window, color, rect, weight)
            for color, pos, weight in self.Lines: pygame.draw.line(InstanceSystem.Window, color, pos[0], pos[1], weight)
            for font, text, color, justify, pos in (self.Texts):
                Text = font.render(text, True, color)
                if justify == 'Left': TextRect = Text.get_rect(left=pos[0], centery=pos[1])
                if justify == 'Right': TextRect = Text.get_rect(right=pos[0], centery=pos[1])
                if justify == 'Center': TextRect = Text.get_rect(center=(pos[0], pos[1]))
                InstanceSystem.Window.blit(Text, TextRect)
            for image, pos in self.Images: InstanceSystem.Window.blit(image, pos)

    def AltimeterClick(self):
        if self.Active: InstanceAltimeter.Enabled = not InstanceAltimeter.Enabled

    def NavigatorClick(self):
        if self.Active: InstanceNavigator.Enabled = not InstanceNavigator.Enabled

    def CompassClick(self):
        if self.Active: InstanceCompass.Enabled = not InstanceCompass.Enabled

    def TimerClick(self):
        if self.Active: InstanceTimer.Enabled = not InstanceTimer.Enabled

    def AutoTrackerClick(self):
        if self.Active:
            pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen), (self.AutoTrackerX, self.AutoTrackerY, self.AutoTrackerW, self.AutoTrackerH))
            pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorWhite), (self.AutoTrackerX, self.AutoTrackerY, self.AutoTrackerW, self.AutoTrackerH), 3)

            InstanceCalculations.AutoTrackerLocation = not InstanceCalculations.AutoTrackerLocation

    def AutoPayloadClick(self):
        if self.Active:
            pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen), (self.AutoPayloadX, self.AutoPayloadY, self.AutoPayloadW, self.AutoPayloadH))
            pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorWhite), (self.AutoPayloadX, self.AutoPayloadY, self.AutoPayloadW, self.AutoPayloadH), 3)

        InstanceCalculations.AutoPayloadLocation = not InstanceCalculations.AutoPayloadLocation

    def TargetLatClick(self):
        global InputTargetLat
        if self.Active:
            InputTargetLat = True

    def TargetLonClick(self):
        global InputTargetLon
        if self.Active:
            InputTargetLon = True

    def ManualCoordsClick(self):
        if self.Active:
            InstanceSystem.Manual = not InstanceSystem.Manual

    def AutoVentClick(self):
        if self.Active:
            InstanceVent.Manual = not InstanceVent.Manual

    def AutoCOMClick(self):
        if self.Active:
            InstanceSystem.AutoCOM = not InstanceSystem.AutoCOM

    def AutoDescentClick(self):
        if self.Active:
            InstanceDescent.Automatic = not InstanceDescent.Automatic

    def DarkModeClick(self):
        if self.Active:
            InstanceSystem.DarkMode = not InstanceSystem.DarkMode
            InstanceSystem.Refresh()
            InstanceSystem.UpdatePreferences()

    def MetricUnitsClick(self):
        if self.Active:
            InstanceSystem.MetricUnits = not InstanceSystem.MetricUnits
            InstanceSystem.Refresh()
            InstanceSystem.UpdatePreferences()

    def Parser1Click(self):
        try:
            Root = tk.Tk()
            Root.withdraw()
            FilePath = filedialog.askopenfilename(title="Select RFD Log", filetypes=[("CSV Files", "*.csv")])
            Root.destroy()

            InstanceMaps.RFDData = []

            if FilePath:
                with open(FilePath, 'r') as file:
                    next(file)
                    for line in file:
                        Parts = line.strip().split(',')
                        if len(Parts) >= 29 and Parts[0].isdigit():
                            Record = {
                                'Time': datetime(int(Parts[6]), int(Parts[7]), int(Parts[8]), int(Parts[9]), int(Parts[10]), int(Parts[11])).strftime('%Y-%m-%d %H:%M:%S'),
                                'Latitude': float(Parts[3]) / 1000000,
                                'Longitude': float(Parts[4]) / 1000000,
                                'Altitude': float(Parts[5])
                            }
                            InstanceMaps.RFDData.append(Record)

                Directory = os.path.join(InstanceSystem.Directory, 'Parsers')
                FileName = os.path.join(Directory, 'ParsedRFD.csv')

                if not os.path.exists(Directory): os.makedirs(Directory)

                with open(FileName, 'w', newline='') as csvfile:
                    Headers = ['Time', 'Latitude', 'Longitude', 'Altitude']
                    Writer = csv.DictWriter(csvfile, fieldnames=Headers)

                    Writer.writeheader()
                    for data in InstanceMaps.RFDData: Writer.writerow(data)

                InstanceMaps.ParserPlot(InstanceMaps.RFDData)
        except Exception as e:
            InstanceErrors.Message = e

    def Parser2Click(self):
        try:
            Root = tk.Tk()
            Root.withdraw()
            FilePath = filedialog.askopenfilename(initialdir=InstanceSystem.Directory, title="Select Iridium Log", filetypes=[("CSV Files", "*.csv")])
            Root.destroy()

            InstanceMaps.IridiumData = []

            if FilePath:
                with open(FilePath, 'r') as file:
                    next(file)
                    for line in file:
                        Parts = line.strip().split(',')
                        if len(Parts) == 10:
                            Record = {
                                'Time': (datetime.datetime.strptime(Parts[1].strip().strip('"'), '%Y-%m-%dT%H:%M:%SZ')).strftime('%Y-%m-%d %H:%M:%S'),
                                'Latitude': float(Parts[2]),
                                'Longitude': float(Parts[3]),
                                'Altitude': float(Parts[4]) * 3.28084
                            }
                            InstanceMaps.IridiumData.append(Record)

                Directory = os.path.join(InstanceSystem.Directory, 'Parsers')
                FileName = os.path.join(Directory, 'ParsedIridium.csv')

                if not os.path.exists(Directory): os.makedirs(Directory)

                with open(FileName, 'w', newline='') as csvfile:
                    Headers = ['Time', 'Latitude', 'Longitude', 'Altitude']
                    Writer = csv.DictWriter(csvfile, fieldnames=Headers)

                    Writer.writeheader()
                    for data in InstanceMaps.IridiumData: Writer.writerow(data)

                InstanceMaps.ParserPlot(InstanceMaps.IridiumData)
        except Exception as e:
            InstanceErrors.Message = e

    # APRS Parser

    def Parser3Click(self):

        def time_string_to_seconds(time_str):
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s
        
        try:
            Root = tk.Tk()
            Root.withdraw()
            FilePath = filedialog.askopenfilename(initialdir=InstanceSystem.Directory, title="Select APRS Log", filetypes=[("Text Files", "*.txt")])
            Root.destroy()

            InstanceMaps.APRSData = []
            if FilePath:
                with open(FilePath, 'r') as file:
                    next(file)
                    for line in file:
                        TimeMatch = re.search(r'\d{2}:\d{2}:\d{2}', line)
                        DateMatch = re.search(r'\d{4}-\d{2}-\d{2}', line)
                        LatLonMatch = re.search(r'!(\d{4}\.\d{2})([NS])/(\d{5}\.\d{2})([EW])', line)
                        AltMatch = re.search(r'/A=(\d+)', line)
                        PressureMatch = re.search(r'\d{4,}Pa', line)
                        TemperatureMatch = re.search(r',\d{1,3}C|-\d{1,3}C', line)

                        if TimeMatch:
                            Time = TimeMatch.group(0)
                            Time = int((time_string_to_seconds(Time))/60)

                        if DateMatch:
                            Date = DateMatch.group(0)                            

                        if LatLonMatch:
                            Lat = float(LatLonMatch.group(1)) / 100 if LatLonMatch.group(2) == 'N' else -(float(LatLonMatch.group(1)) / 100)
                            Lon = float(LatLonMatch.group(3)) / 100 if LatLonMatch.group(4) == 'E' else -(float(LatLonMatch.group(3)) / 100)

                        if AltMatch:
                            Alt = float(AltMatch.group(1))

                        if PressureMatch:
                            Pressure = float(PressureMatch.group(0).replace("Pa", ""))

                        if TemperatureMatch:
                            Temp = int(TemperatureMatch.group(0).replace(",", "").replace("C", ""))


                        Record = {
                            'Time': Time,
                            'Latitude': Lat,
                            'Longitude': Lon,
                            'Altitude': Alt,
                            'Pressure': Pressure,
                            'Temperature': Temp,
                            'Date' : Date
                        }
                        InstanceMaps.APRSData.append(Record)

                Directory = os.path.join(InstanceSystem.Directory, 'Parsers')
                FileName = os.path.join(Directory, 'ParsedAPRS.csv')

                if not os.path.exists(Directory): os.makedirs(Directory)

                with open(FileName, 'w', newline='') as csvfile:
                    Headers = ['Date','Time', 'Latitude', 'Longitude', 'Altitude', 'Pressure', 'Temperature']
                    Writer = csv.DictWriter(csvfile, fieldnames=Headers)

                    Writer.writeheader()
                    for data in InstanceMaps.APRSData: Writer.writerow(data)

                InstanceMaps.ParserPlot(InstanceMaps.APRSData)
        except Exception as e:
            InstanceErrors.Message = e
            print("There is an error!")
            print(InstanceErrors.Message)

    def RunPredictionsClick(self):
        InstancePredictions.RunPrediction()

    def DemoModeClick(self):
        if InstanceDemo.Enabled:
            self.Active = False
            InstanceDemo.Enabled = False
            InstanceLaunch.Launched = False
            InstanceSystem.ScreenSetting = 'Thumb'
        else:
            InstanceDemo.Enabled = True
            self.Active = False
            InstanceLaunch.Launched = True
            InstanceSystem.ScreenSetting = 'Demo'
            InstanceScreen.StartStream()

InstanceSettings = ClassSettings()

class ClassInput:
    def __init__(self):
        self.CircleButtons = [
            (InstanceCompass, 'CompassHover', 'CompassClick', 'X', 'Y', 'R'),
            (InstanceButtons, 'PowerHover', 'PowerClick', 'PowerX', 'PowerY', 'PowerR'),
            (InstanceButtons, 'HelpHover', 'HelpClick', 'HelpX', 'HelpY', 'HelpR'),
            (InstanceButtons, 'SettingsHover', 'SettingsClick', 'SettingsX', 'SettingsY', 'SettingsR'),
            (InstanceScreen, 'FullscreenHover', 'FullscreenClick', 'FullscreenX', 'FullscreenY', 'FullscreenR'),
            (InstanceControls, 'ControlCenterHover', 'ControlCenterClick', 'ControlCenterX', 'ControlCenterY', 'ControlCenterR'),
            (InstanceMaps, 'MapHover', 'MapClick', 'MapX', 'MapY', 'MapR'),
            (InstancePopups, 'PopupTrackerHover', 'PopupTrackerClick', 'PopupTrackerX', 'PopupTrackerY', 'PopupTrackerR'),
            (InstancePopups, 'PopupVentingHover', 'PopupVentingClick', 'PopupVentingX', 'PopupVentingY', 'PopupVentingR'),
            (InstancePopups, 'PopupConnectionsHover', 'PopupConnectionsClick', 'PopupConnectionsX', 'PopupConnectionsY', 'PopupConnectionsR'),
            (InstancePopups, 'PopupParsersHover', 'PopupParsersClick', 'PopupParsersX', 'PopupParsersY', 'PopupParsersR'),
            (InstancePopups, 'PopupPredictionsHover', 'PopupPredictionsClick', 'PopupPredictionsX', 'PopupPredictionsY', 'PopupPredictionsR'),
            (InstanceSettings, 'ManualCoordsHover', 'ManualCoordsClick', 'ManualCoordsX', 'ManualCoordsY', 'ManualCoordsR'),
            (InstanceSettings, 'AutoVentHover', 'AutoVentClick', 'AutoVentX', 'AutoVentY', 'AutoVentR'),
            (InstanceSettings, 'DarkModeHover', 'DarkModeClick', 'DarkModeX', 'DarkModeY', 'DarkModeR'),
            (InstanceSettings, 'MetricUnitsHover', 'MetricUnitsClick', 'MetricUnitsX', 'MetricUnitsY', 'MetricUnitsR'),
            (InstanceSettings, 'DemoModeHover', 'DemoModeClick', 'DemoModeX', 'DemoModeY', 'DemoModeR')
        ]

        self.SquareButtons = [
            (InstanceScreen, 'URLHover', 'URLClick', 'URLX', 'URLY', 'URLW', 'URLH'),
            (InstanceTimer, 'TimerHover', 'TimerClick', 'X', 'Y', 'W', 'H'),
            (InstanceLaunch, 'Launch1Hover', 'Launch1Click', 'Launch1X', 'Launch1Y', 'Launch1W', 'Launch1H'),
            (InstanceLaunch, 'Launch2Hover', 'Launch2Click', 'Launch2X', 'Launch2Y', 'Launch2W', 'Launch2H'),
            (InstanceLaunch, 'Reset1Hover', 'Reset1Click', 'Reset1X', 'Reset1Y', 'Reset1W', 'Reset1H'),
            (InstanceLaunch, 'Reset2Hover', 'Reset2Click', 'Reset2X', 'Reset2Y', 'Reset2W', 'Reset2H'),
            (InstanceLaunch, 'Reset3Hover', 'Reset3Click', 'Reset3X', 'Reset3Y', 'Reset3W', 'Reset3H'),
            (InstanceLaunch, 'Reset4Hover', 'Reset4Click', 'Reset4X', 'Reset4Y', 'Reset4W', 'Reset4H'),
            (InstanceLaunch, 'Countdown1Hover', 'Countdown1Click', 'Countdown1X', 'Countdown1Y', 'Countdown1W', 'Countdown1H'),
            (InstanceLaunch, 'Countdown2Hover', 'Countdown2Click', 'Countdown2X', 'Countdown2Y', 'Countdown2W', 'Countdown2H'),
            (InstanceLaunch, 'Countdown3Hover', 'Countdown3Click', 'Countdown3X', 'Countdown3Y', 'Countdown3W', 'Countdown3H'),
            (InstanceRadios, 'RFDHover', 'RFDClick', 'RFDX', 'RFDY', 'RFDW', 'RFDH'),
            (InstanceRadios, 'IridiumHover', 'IridiumClick', 'IridiumX', 'IridiumY', 'IridiumW', 'IridiumH'),
            (InstanceRadios, 'APRSHover', 'APRSClick', 'APRSX', 'APRSY', 'APRSW', 'APRSH'),
            (InstanceRadios, 'UbiquitiHover', 'UbiquitiClick', 'UbiquitiX', 'UbiquitiY', 'UbiquitiW', 'UbiquitiH'),
            (InstanceRadios, 'ArduinoHover', 'ArduinoClick', 'ArduinoX', 'ArduinoY', 'ArduinoW', 'ArduinoH'),
            (InstanceControls, 'ControlUpHover', 'ControlUpClick', 'ControlUpX', 'ControlUpY', 'ControlUpW', 'ControlUpH'),
            (InstanceControls, 'ControlLeftHover', 'ControlLeftClick', 'ControlLeftX', 'ControlLeftY', 'ControlLeftW', 'ControlLeftH'),
            (InstanceControls, 'ControlDownHover', 'ControlDownClick', 'ControlDownX', 'ControlDownY', 'ControlDownW', 'ControlDownH'),
            (InstanceControls, 'ControlRightHover', 'ControlRightClick', 'ControlRightX', 'ControlRightY', 'ControlRightW', 'ControlRightH'),
            (InstanceControls, 'ClearAnglesHover', 'ClearAnglesClick', 'ClearAnglesX', 'ClearAnglesY', 'ClearAnglesW', 'ClearAnglesH'),
            (InstanceControls, 'ClearTweaksHover', 'ClearTweaksClick', 'ClearTweaksX', 'ClearTweaksY', 'ClearTweaksW', 'ClearTweaksH'),
            (InstanceVent, 'IMEIHover', 'IMEIClick', 'IMEIX', 'IMEIY', 'IMEIW', 'IMEIH'),
            (InstanceVent, 'GuardClosedHover', 'GuardClosedClick', 'GuardClosedX', 'GuardClosedY', 'GuardClosedW', 'GuardClosedH'),
            (InstanceVent, 'GuardOpenHover', 'GuardOpenClick', 'GuardOpenX', 'GuardOpenY', 'GuardOpenW', 'GuardOpenH'),
            (InstanceVent, 'VentHover', 'VentClick', 'VentX', 'VentY', 'VentW', 'VentH'),
            (InstanceVent, 'CutHover', 'CutClick', 'CutX', 'CutY', 'CutW', 'CutH'),
            (InstanceSettings, 'AltimeterHover', 'AltimeterClick', 'AltimeterX', 'AltimeterY', 'AltimeterW', 'AltimeterH'),
            (InstanceSettings, 'NavigatorHover', 'NavigatorClick', 'NavigatorX', 'NavigatorY', 'NavigatorW', 'NavigatorH'),
            (InstanceSettings, 'CompassHover', 'CompassClick', 'CompassX', 'CompassY', 'CompassW', 'CompassH'),
            (InstanceSettings, 'TimerHover', 'TimerClick', 'TimerX', 'TimerY', 'TimerW', 'TimerH'),
            (InstanceSettings, 'AutoTrackerHover', 'AutoTrackerClick', 'AutoTrackerX', 'AutoTrackerY', 'AutoTrackerW', 'AutoTrackerH'),
            (InstanceSettings, 'AutoPayloadHover', 'AutoPayloadClick', 'AutoPayloadX', 'AutoPayloadY', 'AutoPayloadW', 'AutoPayloadH'),
            (InstanceSettings, 'TargetLatHover', 'TargetLatClick', 'TargetLatX', 'TargetLatY', 'TargetLatW', 'TargetLatH'),
            (InstanceSettings, 'TargetLonHover', 'TargetLonClick', 'TargetLonX', 'TargetLonY', 'TargetLonW', 'TargetLonH'),
            (InstanceSettings, 'AutoCOMHover', 'AutoCOMClick', 'AutoCOMX', 'AutoCOMY', 'AutoCOMW', 'AutoCOMH'),
            (InstanceSettings, 'AutoDescentHover', 'AutoDescentClick', 'AutoDescentX', 'AutoDescentY', 'AutoDescentW', 'AutoDescentH'),
            (InstanceSettings, 'Parser1Hover', 'Parser1Click', 'Parser1X', 'Parser1Y', 'Parser1W', 'Parser1H'),
            (InstanceSettings, 'Parser2Hover', 'Parser2Click', 'Parser2X', 'Parser2Y', 'Parser2W', 'Parser2H'),
            (InstanceSettings, 'Parser3Hover', 'Parser3Click', 'Parser3X', 'Parser3Y', 'Parser3W', 'Parser3H'),
            (InstanceSettings, 'RunPredictionsHover', 'RunPredictionsClick', 'RunPredictionsX', 'RunPredictionsY', 'RunPredictionsW', 'RunPredictionsH')
        ]

        self.TextFields = [
            (InstanceVent, 'IMEIHover', 'InputIMEI', 'ex: 123456789012345', (InstanceVent.IMEIX, InstanceVent.IMEIY, InstanceVent.IMEIW, InstanceVent.IMEIH), (0, 0), 14, 'center'),
            (InstanceScreen, 'URLHover', 'InputURL', 'ex: https://www.youtube.com/', (InstanceScreen.URLX, InstanceScreen.URLY, InstanceScreen.URLW, InstanceScreen.URLH), (-200, 0), 55, 'left'),
            (InstanceSettings, 'WidthHover', 'InputWindowW', 'ex: 1920', (InstanceSettings.WidthX, InstanceSettings.WidthY, InstanceSettings.WidthW, InstanceSettings.WidthH), (0, 0), 4, 'center'),
            (InstanceSettings, 'HeightHover', 'InputWindowH', 'ex: 1080', (InstanceSettings.HeightX, InstanceSettings.HeightY, InstanceSettings.HeightW, InstanceSettings.HeightH), (0, 0), 4, 'center'),
            (InstanceSettings, 'TrackerLatHover', 'InputTrackerLat', 'ex: 44.9333293', (InstanceSettings.TrackerLatX, InstanceSettings.TrackerLatY, InstanceSettings.TrackerLatW, InstanceSettings.TrackerLatH), (0, 0), 8, 'center'),
            (InstanceSettings, 'TrackerLonHover', 'InputTrackerLon', 'ex: -93.1323551', (InstanceSettings.TrackerLonX, InstanceSettings.TrackerLonY, InstanceSettings.TrackerLonW, InstanceSettings.TrackerLonH), (0, 0), 8, 'center'),
            (InstanceSettings, 'TrackerAltHover', 'InputTrackerAlt', ('ex: 260' if InstanceSystem.MetricUnits else 'ex: 853'), (InstanceSettings.TrackerAltX, InstanceSettings.TrackerAltY, InstanceSettings.TrackerAltW, InstanceSettings.TrackerAltH), (0, 0), 8, 'center'),
            (InstanceSettings, 'PayloadLatHover', 'InputPayloadLat', 'ex: 44.9333293', (InstanceSettings.PayloadLatX, InstanceSettings.PayloadLatY, InstanceSettings.PayloadLatW, InstanceSettings.PayloadLatH), (0, 0), 8, 'center'),
            (InstanceSettings, 'PayloadLonHover', 'InputPayloadLon', 'ex: -93.1323551', (InstanceSettings.PayloadLonX, InstanceSettings.PayloadLonY, InstanceSettings.PayloadLonW, InstanceSettings.PayloadLonH), (0, 0), 8, 'center'),
            (InstanceSettings, 'PayloadAltHover', 'InputPayloadAlt', ('ex: 260' if InstanceSystem.MetricUnits else 'ex: 853'), (InstanceSettings.PayloadAltX, InstanceSettings.PayloadAltY, InstanceSettings.PayloadAltW, InstanceSettings.PayloadAltH), (0, 0), 8, 'center'),
            (InstanceSettings, 'COMRFDHover', 'InputCOMRFD', 'ex: COM4', (InstanceSettings.COMRFDX, InstanceSettings.COMRFDY, InstanceSettings.COMRFDW, InstanceSettings.COMRFDH), (0, 0), 5, 'center'),
            (InstanceSettings, 'COMArduinoHover', 'InputCOMArduino', 'ex: COM6', (InstanceSettings.COMArduinoX, InstanceSettings.COMArduinoY, InstanceSettings.COMArduinoW, InstanceSettings.COMArduinoH), (0, 0), 5, 'center'),
            (InstanceSettings, 'IridiumHover', 'InputIridium', 'ex: UOM002', (InstanceSettings.IridiumX, InstanceSettings.IridiumY, InstanceSettings.IridiumW, InstanceSettings.IridiumH), (0, 0), 16, 'center'),
            (InstanceSettings, 'APRSHover', 'InputAPRS', 'ex: KD0AWK-7', (InstanceSettings.APRSX, InstanceSettings.APRSY, InstanceSettings.APRSW, InstanceSettings.APRSH), (0, 0), 16, 'center'),
            (InstanceSettings, 'UbiquitiHover', 'InputUbiquiti', 'ex: 192.168.2.101', (InstanceSettings.UbiquitiX, InstanceSettings.UbiquitiY, InstanceSettings.UbiquitiW, InstanceSettings.UbiquitiH), (0, 0), 16, 'center'),
            (InstanceSettings, 'AltOpenHover', 'InputAltOpen', 'ex: 20000' if InstanceSystem.MetricUnits else 'ex: 70000', (InstanceSettings.VentAltOpenX, InstanceSettings.VentAltOpenY, InstanceSettings.VentAltOpenW, InstanceSettings.VentAltOpenH), (-70, 0), 20, 'center'),
            (InstanceSettings, 'AltCloseHover', 'InputAltClose', 'ex: 25000' if InstanceSystem.MetricUnits else 'ex: 80000', (InstanceSettings.VentAltCloseX, InstanceSettings.VentAltCloseY, InstanceSettings.VentAltCloseW, InstanceSettings.VentAltCloseH), (-70, 0), 20, 'center'),
            (InstanceSettings, 'VelCloseHover', 'InputVelClose', '0.2' if InstanceSystem.MetricUnits else '0.3', (InstanceSettings.VentVelCloseX, InstanceSettings.VentVelCloseY, InstanceSettings.VentVelCloseW, InstanceSettings.VentVelCloseH), (0, 0), 3, 'center'),
            (InstanceSettings, 'PredictionLatHover', 'InputPredictionLat', '44.93', (InstanceSettings.PredictionLatX, InstanceSettings.PredictionLatY, InstanceSettings.PredictionLatW, InstanceSettings.PredictionLatH), (0, 0), 4, 'center'),
            (InstanceSettings, 'PredictionLonHover', 'InputPredictionLon', '-93.1', (InstanceSettings.PredictionLonX, InstanceSettings.PredictionLonY, InstanceSettings.PredictionLonW, InstanceSettings.PredictionLonH), (0, 0), 4, 'center'),
            (InstanceSettings, 'PredictionAltHover', 'InputPredictionAlt', ('m' if InstanceSystem.MetricUnits else 'ft'), (InstanceSettings.PredictionAltX, InstanceSettings.PredictionAltY, InstanceSettings.PredictionAltW, InstanceSettings.PredictionAltH), (0, 0), 4, 'center'),
            (InstanceSettings, 'PredictionAscentHover', 'InputPredictionAscent', ('m/s' if InstanceSystem.MetricUnits else 'ft/s'), (InstanceSettings.PredictionAscentX, InstanceSettings.PredictionAscentY, InstanceSettings.PredictionAscentW, InstanceSettings.PredictionAscentH), (0, 0), 7, 'center'),
            (InstanceSettings, 'PredictionDescentHover', 'InputPredictionDescent', ('m/s' if InstanceSystem.MetricUnits else 'ft/s'), (InstanceSettings.PredictionDescentX, InstanceSettings.PredictionDescentY, InstanceSettings.PredictionDescentW, InstanceSettings.PredictionDescentH), (0, 0), 7, 'center'),
            (InstanceSettings, 'PredictionFinalAltHover', 'InputPredictionFinalAlt', ('Termination Altitude (m)' if InstanceSystem.MetricUnits else 'Termination Altitude (ft)'), (InstanceSettings.PredictionFinalAltX, InstanceSettings.PredictionFinalAltY, InstanceSettings.PredictionFinalAltW, InstanceSettings.PredictionFinalAltH), (0, 0), 16, 'center'),
            (InstanceSettings, 'PredictionDateHover', 'InputPredictionDate', 'MM/DD', (InstanceSettings.PredictionDateX, InstanceSettings.PredictionDateY, InstanceSettings.PredictionDateW, InstanceSettings.PredictionDateH), (0, 0), 7, 'center'),
            (InstanceSettings, 'PredictionTimeHover', 'InputPredictionTime', 'HH:MM', (InstanceSettings.PredictionTimeX, InstanceSettings.PredictionTimeY, InstanceSettings.PredictionTimeW, InstanceSettings.PredictionTimeH), (0, 0), 7, 'center'),
            (InstanceSettings, 'PredictionFloatAltHover', 'InputPredictionFloatAlt', ('m' if InstanceSystem.MetricUnits else 'ft'), (InstanceSettings.PredictionFloatAltX, InstanceSettings.PredictionFloatAltY, InstanceSettings.PredictionFloatAltW, InstanceSettings.PredictionFloatAltH), (0, 0), 7, 'center'),
            (InstanceSettings, 'PredictionFloatTimeHover', 'InputPredictionFloatTime', 'min', (InstanceSettings.PredictionFloatTimeX, InstanceSettings.PredictionFloatTimeY, InstanceSettings.PredictionFloatTimeW, InstanceSettings.PredictionFloatTimeH), (0, 0), 7, 'center')
        ]

    def Update(self):
        global InputRFD, InputIridium, InputAPRS, InputUbiquiti, InputArduino, InputCOMRFD, InputCOMArduino, InputText, InputTrackerLat, InputTrackerLon, InputTrackerAlt, InputPayloadLat, InputPayloadLon, InputPayloadAlt, InputTargetLat, InputTargetLon, InputAltOpen, InputAltClose, InputVelClose, InputIMEI, InputURL, InputWindowW, InputWindowH, InputPredictionLat, InputPredictionLon, InputPredictionAlt, InputPredictionAscent, InputPredictionDescent, InputPredictionFinalAlt, InputPredictionDate, InputPredictionTime, InputPredictionFloatAlt, InputPredictionFloatTime
        
        for instance, hover, condition, prompt, rect, offset, limit, justify in self.TextFields:
            if globals()[condition]:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorBlack, rect)
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if condition else InstanceSystem.ColorLightRed), rect, 2)

                if len(InputText) > int(limit) and (condition): 
                    DisplayText = InputText[len(InputText) - int(limit) - 1:len(InputText) - 1]
                else: DisplayText = InputText

                if InputURL:
                    InstanceNavigator.Display()
                    InstanceCompass.Display()

                if InputText == '':
                    Font = InstanceSystem.FontBahnschrift15
                    Text = prompt
                    Color = (100, 100, 100, 0.8)
                    Position = (rect[0] + rect[2] / 2 + offset[0] * InstanceSystem.SF, rect[1] + rect[3] / 2 + offset[1] * InstanceSystem.SF)
                else:
                    Font = InstanceSystem.FontBahnschrift15 if InputURL else InstanceSystem.FontBahnschrift20
                    Text = DisplayText
                    Color = InstanceSystem.ColorWhite
                    Position = (rect[0] + rect[2] / 2 + offset[0] * InstanceSystem.SF, rect[1] + rect[3] / 2 + offset[1] * InstanceSystem.SF)

                Text = Font.render(Text, True, Color)

                if justify == 'center': TextRect = Text.get_rect(center=Position)
                elif justify == 'left': TextRect = Text.get_rect(midleft=Position)
                elif justify == 'right': TextRect = Text.get_rect(midright=Position)

                InstanceSystem.Window.blit(Text, TextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                InstanceSystem.Shutdown()
            
            MouseX, MouseY = pygame.mouse.get_pos()
            MousePos = pygame.mouse.get_pos()

            #### Hover ####

            for instance, hover, click, x, y, r in self.CircleButtons:
                if (MouseX - getattr(instance, x)) ** 2 + (MouseY - getattr(instance, y)) ** 2 <= getattr(instance, r) ** 2: setattr(instance, hover, True)
                else: setattr(instance, hover, False)
            
            for instance, hover, click, x, y, w, h in self.SquareButtons:
                if pygame.Rect(getattr(instance, x), getattr(instance, y), getattr(instance, w), getattr(instance, h)).collidepoint(MousePos): setattr(instance, hover, True)
                else: setattr(instance, hover, False)

            for instance, hover, condition, prompt, rect, offset, limit, justify in self.TextFields:
                if pygame.Rect(rect).collidepoint(MousePos): setattr(instance, hover, True)
                else: setattr(instance, hover, False)

            #### Left Click ####

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for instance, hover, click, x, y, r in self.CircleButtons:
                    if (MouseX - getattr(instance, x)) ** 2 + (MouseY - getattr(instance, y)) ** 2 <= getattr(instance, r) ** 2:
                        ClickMethod = getattr(instance, click)
                        ClickMethod()

                for instance, hover, click, x, y, w, h in self.SquareButtons:
                    if pygame.Rect(getattr(instance, x), getattr(instance, y), getattr(instance, w), getattr(instance, h)).collidepoint(MousePos):
                        ClickMethod = getattr(instance, click)
                        ClickMethod()

                for instance, hover, condition, prompt, rect, offset, limit, justify in self.TextFields:
                    if pygame.Rect(rect).collidepoint(MousePos):
                        if not ((condition == 'InputPayloadLat' or condition == 'InputPayloadLon' or condition == 'InputPayloadAlt') and not InstanceSystem.Manual):
                            if not ((condition == 'InputAltOpen' or condition == 'InputAltClose' or condition == 'InputVelClose') and InstanceVent.Manual):
                                if not ((condition == 'InputCOMRFD' or condition == 'InputCOMArduino') and InstanceSystem.AutoCOM):
                                    globals()[condition] = True
                                    for _, _, other, _, _, _, _, _ in self.TextFields:
                                        if other != condition: globals()[other] = False

            #### Keyboard ####

            if event.type == pygame.KEYDOWN:
                if keyboard.is_pressed('w') and InstanceArduino.Active: InstanceCalculations.TweakTilt += 1
                if keyboard.is_pressed('a') and InstanceArduino.Active: InstanceCalculations.TweakPan -= 1
                if keyboard.is_pressed('s') and InstanceArduino.Active: InstanceCalculations.TweakTilt -= 1
                if keyboard.is_pressed('d') and InstanceArduino.Active: InstanceCalculations.TweakPan += 1

                if any(condition for _, _, condition, _, _, _, _, _ in self.TextFields):
                    if event.key == pygame.K_ESCAPE:
                        for _, _, condition, _, _, _, _, _ in self.TextFields: globals()[condition] = False
                        InputText = ''
                    elif event.key == pygame.K_RETURN:
                        try:
                            if InputIMEI:
                                InstanceIridium.IMEI = str(InputText)
                                InputIMEI = False

                            if InputURL:
                                InstanceScreen.URL = str(InputText)
                                InstanceScreen.URLUpdate = True
                                InputURL = False

                            if InputWindowW:
                                if 512 <= float(InputText) <= 3840:
                                    InstanceSystem.W = float(InputText)
                                    InstanceSystem.H = InstanceSystem.W * (9/16)
                                    InstanceSystem.SF = min(InstanceSystem.W / 1920, InstanceSystem.H / 1080)
                                    self.Window = pygame.display.set_mode((InstanceSystem.W, InstanceSystem.H))

                                    InstanceSystem.Refresh()
                                    InstanceSystem.UpdatePreferences()

                                    InputWindowW = False
                                else:
                                    InstanceErrors.Message = "Width must be within [512, 3840] pixels"

                            if InputWindowH:
                                if 288 <= float(InputText) <= 2160:
                                    InstanceSystem.H = float(InputText)
                                    InstanceSystem.W = InstanceSystem.H * (16/9)
                                    InstanceSystem.SF = min(InstanceSystem.W / 1920, InstanceSystem.H / 1080)
                                    self.Window = pygame.display.set_mode((InstanceSystem.W, InstanceSystem.H))

                                    InstanceSystem.Refresh()
                                    InstanceSystem.UpdatePreferences()

                                    InputWindowH = False
                                else:
                                    InstanceErrors.Message = "Height must be within [288, 2160] pixels"

                            if InputTrackerLat or InputTrackerLon or InputTrackerAlt:
                                InstanceCalculations.AutoPayloadLocation = False
                                if InputTrackerLat: InstanceTracker.Lat = float(InputText)
                                if InputTrackerLon: InstanceTracker.Lon = float(InputText)
                                if InputTrackerAlt: InstanceTracker.Alt = float(InputText) * 3.28084 if InstanceSystem.MetricUnits else float(InputText)

                            if InputPayloadLat or InputPayloadLon or InputPayloadAlt:
                                InstanceCalculations.AutoPayloadLocation = False
                                if InputPayloadLat: InstancePayload.Lat = float(InputText)
                                if InputPayloadLon: InstancePayload.Lon = float(InputText)
                                if InputPayloadAlt: InstancePayload.Alt = float(InputText) * 3.28084 if InstanceSystem.MetricUnits else float(InputText)

                            if InputCOMRFD:
                                InstanceRFD.COMPort = str(InputText)

                            if InputCOMArduino:
                                InstanceArduino.COMPort = str(InputText)

                            if InputAltOpen:
                                InstanceVent.AltOpen = float(InputText) * 3.28084 if InstanceSystem.MetricUnits else float(InputText)

                            if InputAltClose:
                                InstanceVent.VelClose = None
                                InstanceVent.AltClose = float(InputText) * 3.28084 if InstanceSystem.MetricUnits else float(InputText)

                            if InputVelClose:
                                InstanceVent.AltClose = None
                                InstanceVent.VelClose = float(InputText) * 3.28084 if InstanceSystem.MetricUnits else float(InputText)

                            if InputIridium:
                                InstanceIridium.Modem = str(InputText)

                            if InputAPRS:
                                InstanceAPRS.Callsign = str(InputText)

                            if InputUbiquiti:
                                InstanceUbiquiti.IP = str(InputText)

                            if InputPredictionLat:
                                InstancePredictions.Lat = float(InputText)

                            if InputPredictionLon:
                                InstancePredictions.Lon = float(InputText)

                            if InputPredictionAlt:
                                InstancePredictions.Alt = float(InputText) if InstanceSystem.MetricUnits else float(InputText) / 3.28084

                            if InputPredictionAscent:
                                InstancePredictions.Ascent = float(InputText) if InstanceSystem.MetricUnits else float(InputText) / 3.28084

                            if InputPredictionDescent:
                                InstancePredictions.Descent = float(InputText) if InstanceSystem.MetricUnits else float(InputText) / 3.28084

                            if InputPredictionFinalAlt:
                                InstancePredictions.FinalAlt = float(InputText) if InstanceSystem.MetricUnits else float(InputText) / 3.28084

                            if InputPredictionDate:
                                Match = re.match(r'(\d{1,2})/(\d{1,2})', InputText)
                                if Match:
                                    Month, Day = Match.groups()
                                    InstancePredictions.Date = f"{int(Month):02}/{int(Day):02}"
                                else:
                                    InstanceErrors.Message = "Date format must follow MM/DD; M/DD; MM/D; M/D"

                            if InputPredictionTime:
                                Match = re.match(r'(\d{1,2}):(\d{2})', InputText)
                                if Match:
                                    Hour, Minute = Match.groups()
                                    InstancePredictions.Time = f"{int(Hour):02}:{int(Minute):02}"
                                else:
                                    InstanceErrors.Message = "Time format must follow HH:MM; H:MM"

                            if InputPredictionFloatAlt:
                                InstancePredictions.FloatAlt = float(InputText) if InstanceSystem.MetricUnits else float(InputText) / 3.28084

                            if InputPredictionFloatTime:
                                InstancePredictions.FloatTime = float(InputText)

                            for _, _, condition, _, _, _, _, _ in self.TextFields: globals()[condition] = False
                            InputText = ''

                        except Exception as e:
                            InstanceErrors.Message = e
                    elif event.key == pygame.K_BACKSPACE:
                        InputText = InputText[:-1]
                    elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        Clipboard = clipboard.paste()
                        while '\0' in Clipboard:
                            Clipboard = Clipboard.replace('\0', '')
                        InputText += Clipboard
                    else:
                        InputText += event.unicode.replace('\0', '')

            try:
                # Joystick Handling
                if event.type == pygame.JOYDEVICEADDED:
                    try:
                        if pygame.joystick.get_count() > 0:
                            joystick = pygame.joystick.Joystick(0)
                            joystick.init()
                    except Exception as e:
                        InstanceOutput.Message = 'Controller Error'
                        InstanceErrors.Message = e

                JoystickX, JoystickY = 0, 1

                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == JoystickX:
                        if event.value < -0.5: InstanceCalculations.TweakPan -= 1
                        elif event.value > 0.5: InstanceCalculations.TweakPan += 1
                    elif event.axis == JoystickY:
                        if event.value < -0.5: InstanceCalculations.TweakTilt += 1
                        elif event.value > 0.5: InstanceCalculations.TweakTilt -= 1
            except KeyError as e:
                if str(e) != '5': raise

InstanceInput = ClassInput()

class ClassErrors:
    def __init__(self):
        self.ErrorDisp = False
        self.FileWrite = True
        self.Message = self.String = ''
        self.Time1 = self.Time2 = datetime.datetime.now()

    def Update(self):
        # Display Error
        if self.Message != '':
            self.String = str(self.Message)
            self.ErrorDisp = True

        if self.ErrorDisp:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorYellow, (0, 0, InstanceSystem.W, InstanceSystem.H / 20))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (0, 0, InstanceSystem.W, InstanceSystem.H / 20), 1)

            Text = InstanceSystem.FontCalibri30.render(self.String, True, InstanceSystem.ColorBlack)
            TextRect = Text.get_rect(center=((InstanceSystem.W / 2), (InstanceSystem.H / 40)))
            InstanceSystem.Window.blit(Text, TextRect)

        self.Time2 = datetime.datetime.now()
        if (self.Time2 - self.Time1) > datetime.timedelta(seconds=5):
            self.ErrorDisp = False
            self.Time1 = self.Time2

        # Generate Error Log
        try:
            HeaderRow = ["Timestamp (UTC)", "Error Message"]
            DataRow = [InstanceTimer.UTC, self.Message]
        except Exception:
            try: DataRow = ["Null Time", self.Message]
            except Exception: DataRow = ["Null Time", "Null Message"]

        if self.FileWrite and self.Message is not None and self.Message != '':
            try:
                if not os.path.exists("Errors"):
                    ErrorDirectory = os.path.join(os.getcwd(), "Errors")
                    os.makedirs(ErrorDirectory, exist_ok=True)

                FileName = f"Error_{InstanceSystem.Date}.csv"
                FilePath = os.path.join(ErrorDirectory, FileName)

                if not os.path.isfile(FilePath):
                    with open(FilePath, "w", newline='') as f:
                        Writer = csv.writer(f, delimiter=',')
                        Writer.writerow(HeaderRow)
                        Writer.writerow(DataRow)
                else:
                    with open(FilePath, "a", newline='') as f:
                        Writer = csv.writer(f, delimiter=',')
                        Writer.writerow(DataRow)
            except Exception:
                pass

            self.Message = ''

InstanceErrors = ClassErrors()

##############################

InstanceSystem.Startup()
InstanceSystem.Refresh()

while InstanceSystem.Running:
    # Handle Quit Events
    for event in pygame.event.get():
        if event.type == QUIT: InstanceSystem.Shutdown()

    # Clear Window
    InstanceSystem.Window.fill(InstanceSystem.ColorBlack)

    # Initialize Threads
    ThreadRFD = threading.Thread(target=InstanceRFD.Update)
    ThreadIridium = threading.Thread(target=InstanceIridium.Update)
    ThreadAPRS = threading.Thread(target=InstanceAPRS.Update)
    ThreadUbiquiti = threading.Thread(target=InstanceUbiquiti.Update)
    ThreadArduino = threading.Thread(target=InstanceArduino.Update)
    ThreadCalculations = threading.Thread(target=InstanceCalculations.Update)
    ThreadMaps = threading.Thread(target=InstanceMaps.Update)
    ThreadDemo = threading.Thread(target=InstanceDemo.Update)
    ThreadErrors = threading.Thread(target=InstanceErrors.Update)
    ThreadInput = threading.Thread(target=InstanceInput.Update)

    # Start Threads
    ThreadRFD.start()
    ThreadIridium.start()
    ThreadAPRS.start()
    ThreadUbiquiti.start()
    ThreadArduino.start()
    ThreadCalculations.start()
    ThreadMaps.start()
    ThreadDemo.start()
    ThreadInput.start()

    # Join Threads
    ThreadRFD.join()
    ThreadIridium.join()
    ThreadAPRS.join()
    ThreadUbiquiti.join()
    ThreadArduino.join()
    ThreadCalculations.join()
    ThreadMaps.join()
    ThreadDemo.join()
    ThreadInput.join()

    # Displays Everything

    InstanceTitle.Display()
    InstanceScreen.Display()

    InstanceAltimeter.Display()
    InstanceNavigator.Display()
    InstanceCompass.Display()
    InstanceTimer.Display()

    InstanceRadios.Display()
    InstanceOutput.Display()
    InstanceControls.Display()
    InstanceLaunch.Display()
    InstanceVent.Display()
    InstanceMaps.Display()
    InstanceDemo.Update()

    InstanceIndicators.Display()
    InstanceButtons.Display()
    InstanceSettings.Display()
    InstancePopups.Display()
    InstanceErrors.Update()
    InstanceInput.Update()

    # Window Frame
    pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (0, 0, InstanceSystem.W, InstanceSystem.H), 3)

    # Refresh Display
    pygame.display.update()

    # Loop Frequency
    InstanceSystem.Clock.tick(0)

# Close GUI
InstanceSystem.Shutdown()

#### CREDITS AND ACKNOWLEDGEMENTS #### (Jesse)

# https://eric.clst.org/tech/usgeojson/
# https://simplemaps.com/data/us-cities
# https://hub.arcgis.com/datasets/esri::usa-rivers-and-streams
# https://catalog.data.gov/dataset/gps-roads/resource/b6ec6509-f91f-4a67-b031-3719a8e95050
# https://www.openstreetmap.org/#map=5/38.007/-95.844

#### CREDITS AND ACKNOWLEDGEMENTS #### (Lani)
# https://www.youtube.com/watch?v=ix9cRaBkVe0&t=6031s