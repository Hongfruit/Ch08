import tkinter as tk
from time import sleep
from threading import Thread
from pytz import all_timezones, timezone
from datetime import datetime

class Callbacks():
    def __init__(self,oop):
        self.oop = oop
    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        self.scr.insert(tk.INSERT, value + '\n')

    def defaultFileEntries(self):
        self.oop.fileEntry.delete(0,tk.END)
        self.oop.fileEntry.insert(0,'Z:\\')
        self.oop.fileEntry.config(state = "readonly")
        self.oop.newEntry.delete(0,tk.END)
        self.oop.newEntry.insert(0, 'Z:\\Backup')

    def _combo(self, val = 0):
        value = self.oop.combo.get()
        self.oop.scr.insert(tk.INSERT, value +'\n')

    def checkCallback(self, *ignoredArgs):
        # only enable one checkbutton
        if self.chVarUn.get():
            self.check3.configure(state='disabled')
        else:
            self.check3.configure(state='normal')
        if self.chVarEn.get():
            self.check2.configure(state='disabled')
        else:
            self.check2.configure(state='normal')

        # Radiobutton callback function

    def radCall(self):
        radSel = self.radVar.get()
        if radSel == 0:
            self.widgetFrame.configure(text=self.i18n.WIDGET_LABEL + self.i18n.colorsIn[0])
        elif radSel == 1:
            self.widgetFrame.configure(text=self.i18n.WIDGET_LABEL + self.i18n.colorsIn[1])
        elif radSel == 2:
            self.widgetFrame.configure(text=self.i18n.WIDGET_LABEL + self.i18n.colorsIn[2])

        # Exit GUI cleanly

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def methodInAThread(self, numOfLoops=10):
        for idx in range(numOfLoops):
            sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n')
        sleep(1)
        print('methodInAThread():', self.runT.isAlive())

    # Running methods in Threads
    def createThread(self, num):
        self.runT = Thread(target=self.methodInAThread, args=[num])
        self.runT.setDaemon(True)
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

        # textBoxes are the Consumers of Queue data
        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()

    # Create Queue instance
    def useQueues(self):
        # Now using a class member Queue
        while True:
            qItem = self.guiQueue.get()
            print(qItem)
            self.scr.insert(tk.INSERT, qItem + '\n')

            # Button callback

    def insertQuote(self):
        title = self.bookTitle.get()
        page = self.pageNumber.get()
        quote = self.quote.get(1.0, tk.END)
        print(title)
        print(quote)
        self.mySQL.insertBooks(title, page, quote)

        # Button callback

    def getQuote(self):
        allBooks = self.mySQL.showBooks()
        print(allBooks)
        self.quote.insert(tk.INSERT, allBooks)

    # Button callback
    def modifyQuote(self):
        raise NotImplementedError("This still needs to be implemented for the SQL command.")

    # TZ Button callback
    def allTimeZones(self):
        for tz in all_timezones:
            self.scr.insert(tk.INSERT, tz + '\n')

    # TZ Local Button callback
    def localZone(self):
        from tzlocal import get_localzone
        self.scr.insert(tk.INSERT, get_localzone())

    # Format local US time with TimeZone info
    def getDateTime(self):
        fmtStrZone = "%Y-%m-%d %H:%M:%S %Z%z"
        # Get Coordinated Universal Time
        utc = datetime.now(timezone('UTC'))
        print(utc.strftime(fmtStrZone))

        # # Convert UTC datetime object to Los Angeles TimeZone
        # la = utc.astimezone(timezone('America/Los_Angeles'))
        # print(la.strftime(fmtStrZone))

        # Convert UTC datetime object to SEOUL
        seoul = utc.astimezone(timezone('Asia/Seoul'))
        print(seoul.strftime(fmtStrZone))

        # update GUI label with local Time and Zone
        #         self.lbl2.set(la.strftime(fmtStrZone))

        # update GUI label with NY Time and Zone
        self.lbl2.set(seoul.strftime(fmtStrZone))



    #####################################################################################
