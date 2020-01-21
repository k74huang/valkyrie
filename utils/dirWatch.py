import time
import imageHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import wx
import wx.adv

lastFile = ""

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.set_icon("../favicon-96x96.png")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Say Hello', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon()
        self.SetIcon(icon, "abababababa")

    def on_left_down(self, event):
        print('Tray icon was left-clicked.')

    def on_hello(self, event):
        print('Hello, world!')

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        exit()

class Watcher:
    DIRECTORY_TO_WATCH = "../walls/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            global lastFile
            # Taken any action here when a file is modified.
            if(event.src_path == lastFile):
                print("duplicate event, ignored")
            else:
                print("Received modified event - %s." % event.src_path)
                lastFile = event.src_path
                time.sleep(5)
                imageHandler.handle()


if __name__ == '__main__':
    app = wx.App()
    TaskBarIcon()
    app.MainLoop()
    w = Watcher()
    w.run()