import pyautogui
import time
import mouse
import keyboard
import os
from win32gui import GetWindowText, GetForegroundWindow


def click_submit():
    time.sleep(0.1)
    mouse.move("1180", "840")
    mouse.click()


def unmask_password():
    time.sleep(0.1)
    mouse.move("1480", "734")
    time.sleep(0.3)
    mouse.click()


def enter_password(password):
    time.sleep(0.1)
    mouse.move("1300", "740")
    mouse.click()
    time.sleep(0.1)
    keyboard.write(password)


def open_model():
    time.sleep(0.1)
    keyboard.press('r')
    time.sleep(1)
    keyboard.release('r')


def wiggle():
    keyboard.press('a')
    time.sleep(0.1)
    keyboard.release('a')

    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')


print('-----Starting Script------')
house_name = input("What's the name of the house? ")
print('Waiting 5 seconds after game is in focus!')

game_not_in_focus = False
pointer = 0
output_folder = house_name

while not game_not_in_focus:
    time.sleep(5)
    print('Checking game is in focus')
    game_not_in_focus = GetWindowText(GetForegroundWindow()) == 'Mortal Online 2  '

try:
    os.mkdir(f'output/{output_folder}', 0o666)
except FileExistsError:
    print('Folder already exists')

with open('files/word-list.txt') as f:
    word_list = f.read().splitlines()


try:
    with open(f'output/{output_folder}/pointer.txt', 'r+') as f:
        last_word = f.read()
except FileNotFoundError:
    last_word = ''

if last_word:
    pointer = word_list.index(last_word)

print(f'Starting at index: {pointer}')
time.sleep(2)
for i in range(pointer, len(word_list)):
    if not keyboard.is_pressed('F1'):

        if i % 100 == 0:
            wiggle()

        open_model()
        unmask_password()
        enter_password(word_list[i].lower())
        click_submit()

        with open(f'output/{output_folder}/pointer.txt', 'w') as f:
            f.write(word_list[i])

        myScreenshot = pyautogui.screenshot(f'output/{output_folder}/{word_list[i]}.png')
    else:
        print('F1 key has been pressed!')
        print('Stopping the script!')
        exit()
