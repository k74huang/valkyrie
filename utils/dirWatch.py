import time
import imageHandler
import threading
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
import wx
import wx.adv
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

lastFile = ""
# w = Watcher()

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item

def monitorDirectory():
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    path = "../walls/"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# class Watcher:
#     DIRECTORY_TO_WATCH = "../walls/"

#     def __init__(self):
#         self.observer = Observer()

#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
#         self.observer.start()
#         try:
#             while True:
#                 time.sleep(5)
#         except:
#             self.observer.stop()
#             print("Error")

#         self.observer.join()


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
        self.SetIcon(icon, "Watching: ../walls/")

    def on_left_down(self, event):
        print('Tray icon was left-clicked.')

    def on_hello(self, event):
        print('Hello, world!')

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        # exit()

# class Handler(FileSystemEventHandler):

#     @staticmethod
#     def on_any_event(event):
#         if event.is_directory:
#             return None

#         elif event.event_type == 'created':
#             # Take any action here when a file is first created.
#             print("Received created event - %s." % event.src_path)

#         elif event.event_type == 'modified':
#             global lastFile
#             # Taken any action here when a file is modified.
#             if(event.src_path == lastFile):
#                 print("duplicate event, ignored")
#             else:
#                 print("Received modified event - %s." % event.src_path)
#                 lastFile = event.src_path
#                 time.sleep(5)
#                 imageHandler.handle()


if __name__ == '__main__':
    monitorDirectory()
    # w.run();
    # app = wx.App()
    # app.MainLoop()