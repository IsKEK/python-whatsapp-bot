from asyncio.windows_events import NULL
import pyautogui as pag

pag.FAILSAFE = True
# startingPoint = pag.position()
# print(startingPoint)
lastPoint = NULL

while(True):
    pag.click()
    pag.moveRel(0, 107, 1)
    if pag.position().y >= 1300:
        break

while(True):
    pag.PAUSE = 1
    pag.scroll(-87)
    pag.click()
# print(pag.position())
# print(pag.size())