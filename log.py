import os
from datetime import datetime
from pathlib import Path
import sys

resources_path = Path("resources")
log_path = resources_path / "log.txt"
os.system("color")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def logSuccess(message:str) -> None:
    time = datetime.strftime(datetime.now(),"%H:%M:%S")
    date = datetime.today().strftime('%d-%m-%y')
    print(f"{bcolors.OKGREEN}[{date}] [{time}] [Success] {message}")
    with open(log_path,"a") as f:
        f.write(f"[{date}] [{time}] [Success] {message}\n")
    f.close()

def logWarning(message:str) -> None:
    time = datetime.strftime(datetime.now(),"%H:%M:%S")
    date = datetime.today().strftime('%d-%m-%y')
    print(f"{bcolors.WARNING}[{date}] [{time}] [Warning] {message}")
    with open(log_path,"a") as f:
        f.write(f"[{date}] [{time}] [Warning] {message}\n")
    f.close()

def logError(message:str) -> None:
    time = datetime.strftime(datetime.now(),"%H:%M:%S")
    date = datetime.today().strftime('%d-%m-%y')
    print(f"{bcolors.FAIL}[{date}] [{time}] [Error] {message}")
    with open(log_path,"a") as f:
        f.write(f"[{date}] [{time}] [Error] {message}\n")
    f.close()

def logInfo(message:str) -> None:
    time = datetime.strftime(datetime.now(),"%H:%M:%S")
    date = datetime.today().strftime('%d-%m-%y')
    print(f"{bcolors.OKCYAN}[{date}] [{time}] [Info] {message}")
    with open(log_path,"a") as f:
        f.write(f"[{date}] [{time}] [Info] {message}\n")
    f.close()

def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)