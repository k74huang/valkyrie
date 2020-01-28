import time
import imageHandler
import threading
import wx
import wx.adv
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

locale = wx.Locale.GetSystemLanguage()
lastFile = ""

folderToMonitor = "../walls/"

class customFSHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Created file: " + event.src_path[len(folderToMonitor):] + "!")
        time.sleep(2)
        imageHandler.handle()

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item

def monitorDirectory():
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    path = folderToMonitor
    event_handler = customFSHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.set_icon("../icon.png")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Say Hello', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        iconBmp = wx.Bitmap(path, type=wx.BITMAP_TYPE_PNG)
        iconBmp.SetMask(wx.Mask(iconBmp, wx.WHITE)) #sets the transparency colour to white 
        icon = wx.Icon(iconBmp)
        self.SetIcon(icon, "Watching: " + folderToMonitor)

    def on_left_down(self, event):
        print('Tray icon was left-clicked.')

    def on_hello(self, event):
        print('Hello, world!')

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)

class mainProgram(wx.App):
    def OnPreInit(self):
        thread = threading.Thread(target=monitorDirectory, args=())
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    app = mainProgram(redirect=False)
    app.locale = wx.Locale(locale)
    TaskBarIcon()
    app.MainLoop()