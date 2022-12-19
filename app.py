import pyautogui
import sqlite3
import time
import random

# lyrics = open('drake_lyrics.txt', 'r')

time.sleep(5)
# for lyric in lyrics:
#     print(lyric)
#     pyautogui.write(f'{lyric}')
#     pyautogui.press('enter')
#     time.sleep(.1)

conn = sqlite3.connect('quotes.db')
c = conn.cursor()

c.execute("SELECT rowid, * FROM quotes")
quotes_data = c.fetchall()
for text in range(5):
    index = random.randint(0, (len(quotes_data)-1))

    print(f'{quotes_data[index][1]} - {quotes_data[index][2]}')
    pyautogui.write(f'{quotes_data[index][1]} - {quotes_data[index][2]}')
    pyautogui.press('enter')
    time.sleep(.1)
