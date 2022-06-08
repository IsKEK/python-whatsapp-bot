import codecs
from io import BytesIO
from pickle import GLOBAL
from numpy import outer
import pyautogui as pag
import win32clipboard
from PIL import Image

pag.FAILSAFE = True
pag.PAUSE = 1
messagesSent = 0
scrollPower = -86
textToSend = "Добрый день!\n\nДелимся с вами отличной новостью \U0001F90D\n\nСкидки -20% и -30% на всю весеннюю коллекцию \U0001F4AB\n\nЖдём вас на шопинг в Rinascimento \U0001F1EE\U0001F1F9\n\nг. Алматы:\n\U0001F4CDТРЦ Dostyk Plaza: +7 707 183 3518\n\U0001F4CDТРЦ Mega Alma-Ata: +7 707 210 5164\n\nг.Нур-Султан:\n\U0001F4CDТРЦ Mega Silk Way: +7 707 434 12 14\n\U0001F4CDТРЦ Хан Шатыр: +7 707 434 12 14\n\nМы в Instagram: https://instagram.com/rinascimentokz?utm_medium=copy_link\n\nСистема лояльности: UDS Game Rinascimento"
image = Image.open("./rina.jpg")
output = BytesIO()
image.convert('RGB').save(output, 'BMP')
imageToSend = output.getvalue()[14:]
output.close()

def sendMessage():
    global messagesSent
    global flag
    messagesSent += 1
    isConfirmed = pag.confirm("Do you want to send the message?")
    print(isConfirmed)
    if isConfirmed != "Cancel":
        pag.click()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, imageToSend)
        win32clipboard.CloseClipboard()
        pag.hotkey('ctrl', 'v')
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, textToSend)
        win32clipboard.CloseClipboard()
        pag.hotkey('ctrl', 'v')
        pag.press('enter')
        return True
    return False

while(True):
    sendMessage()
    pag.moveRel(0, 90, 0.1)
    if pag.position().y >= 900:
        sendMessage()
        break

pag.scroll(scrollPower)

while(True):
    flag = sendMessage()
    if flag:
        pag.scroll(scrollPower*messagesSent)
    else:
        pag.scroll(scrollPower)