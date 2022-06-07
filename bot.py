import pyautogui as pag

pag.FAILSAFE = True

def sendMessage():
    isConfirmed = pag.confirm("Do you want to send the message?")
    if isConfirmed != "Cancel":
        pag.click()
        pag.hotkey('ctrl', 'v')
        pag.press('enter')

while(True):
    sendMessage()
    pag.moveRel(0, 107, 0.5)
    if pag.position().y >= 1300:
        sendMessage()
        break

while(True):
    pag.PAUSE = 0.5
    pag.scroll(-86)
        sendMessage()