from tkinter import Grid, N, W, S, E
import math
from ui.launcherwindow import LauncherWindow
from config import Config

config = Config()
config.load("launcher.json")
launcherWindow = LauncherWindow()

cache = False;

try:
    cache = config.getValue(["launcher", "cache"])  == "True"
except:
    cache = False;

try:
    rowLength = config.getValue(["launcher", "rowLength"])
except:
    rowLength = 4

launcherWindow.createMenu(config.getValue(["launcher", "menu"]))
currentColumn = 1;
for index, content in enumerate(config.getValue(["games"])):
    gameButton = launcherWindow.getAppButton(content, config.getConfig(["games", content]))
    rawRow = (index+1) / rowLength
    currentRow = math.ceil(rawRow)
    launcherWindow.frame.rowconfigure(currentRow)
    Grid.rowconfigure(launcherWindow.frame, currentRow)
    gameButton.grid(row=int(currentRow), column=currentColumn, sticky=N+S+E+W)
    if currentColumn == rowLength:
        currentColumn = 0;
    currentColumn += 1;
launcherWindow.mainloop()
