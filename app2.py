import pyautogui

import time


lyrics = open('drake_lyrics.txt', 'r')

time.sleep(5)
for lyric in lyrics:
    print(lyric)
    pyautogui.write(f'{lyric}')
    pyautogui.press('enter')
    time.sleep(.1)