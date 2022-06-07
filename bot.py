import pyautogui as pag

pag.FAILSAFE = True
# startingPoint = pag.position()
# print(startingPoint)
lastPoint = NULL

while(True):
    isConfirmed = pag.confirm("Do you want to send the message?")
    if isConfirmed != "Cancel":
        pag.click()
        pag.hotkey('ctrl', 'v')
        pag.press('enter')
    pag.moveRel(0, 107, 0)
    if pag.position().y >= 1300:
        break

while(True):
    # pag.PAUSE = 1
    pag.scroll(-86)
    isConfirmed = pag.confirm("Do you want to send the message?")
    if isConfirmed != "Cancel":
        pag.click()
        pag.hotkey('ctrl', 'v')
        pag.press('enter')
# print(pag.position())
# print(pag.size())