import pyautogui as pag

pag.FAILSAFE = True
pag.PAUSE = 0.5

def sendMessage():
    isConfirmed = pag.confirm("Do you want to send the message?")
    print(isConfirmed)
    if isConfirmed != "Cancel":
        pag.click()
        pag.hotkey('ctrl', 'v')
        pag.press('enter')

while(True):
    sendMessage()
    pag.moveRel(0, 107, 0.1)
    if pag.position().y >= 1300:
        sendMessage()
        break

while(True):
    pag.scroll(-86)
    sendMessage()