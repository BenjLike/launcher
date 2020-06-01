from os import path
import os, subprocess
from helper import getCachePath
from sys import platform
from shutil import which

def binaryFound(binary):
    return which(binary) is not None

def runGenericGame(game, data):
    gamePath = os.path.normpath(getCachePath(game))
    linuxNative = False
    runningLinux = platform in ["linux", "linux2"]
    gameData = data["windows"]
    if "linux" in data:
        if runningLinux and binaryFound(gameData["exe"]):
            gameData = data["linux"]
            linuxNative = True

    if "path" in gameData:
        gamePath = gamePath + '/' + gameData['path']

    call = [gameData["exe"]]
    if not linuxNative and runningLinux:
        call.insert(0, "wine")

    if "params" in gameData:
        for index, param in enumerate(gameData['params']):
            call.append(param)

    subprocess.call(call, cwd=gamePath)
