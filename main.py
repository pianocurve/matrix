# -*- coding: utf-8 -*-
import sys
import pygame as pg
from pygame.constants import CONTROLLER_BUTTON_RIGHTSHOULDER
from pygame.midi import *

TITLE='MATRIX'
FGCOLOR='#8BC34A'
BGCOLOR='#FFD740'
ALTCOLOR='#F9A825'
MINROW=2
MINCOL=4


row=MINROW
col=MINCOL

width=600
height=400

# ドラッグ開始から終了まで選択する＝色を変えてみる

def winini(win):
  rects=[]
  win.fill(pg.Color(BGCOLOR)) # 背景色の指定。
  for y in range( 0,row):
    for x in range( 0,col):
      celWidth=width/col
      celHeight=height/row
      rects.append(pg.draw.rect(win,(FGCOLOR),( x * celWidth + 1, y * celHeight + 1, celWidth -1 ,celHeight -1),0) )
 
  pg.display.update(rects) # 画面更新



def main():
 
  pg.init() # 初期化

  global width
  global height
  global col
  global row


  x_tmp=0
  y_tmp=0

  win = pg.display.set_mode((width, height), pg.RESIZABLE) # ウィンドウサイズの指定

  pg.display.set_caption(TITLE) #タイトル
  win.fill(pg.Color(BGCOLOR)) # 背景色の指定。

  myclock = pg.time.Clock()

  pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)


  winini(win)


  mainLoop = True
  while mainLoop:
    
    # フレームレートの設定　このタイミングで実行される
    myclock.tick_busy_loop(30)
    

    for event in pg.event.get(): # 終了および　ダンパーペダル、note off

      if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
          x_s, y_s = event.pos
          celWidth=width/col
          celHeight=height/row
          x_tmp = int(x_s/celWidth)
          y_tmp = int(y_s/celHeight)
          #print (xx,yy)
          rect= pg.draw.rect(win,(ALTCOLOR),( x_tmp * celWidth + 1, y_tmp * celHeight + 1, celWidth -1 ,celHeight -1),0)
          pg.display.update(rect)

        if event.button == 4: #上
          row=row*2
          col=col*2
          winini(win)
        if event.button == 5: #下
          if MINROW <=row and MINCOL <= col:
            row=int(row/2)
            col=int(col/2)
            winini(win)
      if event.type == pg.MOUSEMOTION:
        buttons= pg.mouse.get_pressed()
        if buttons[0]: 
          x_s, y_s= event.pos
          celWidth=width/col
          celHeight=height/row
          xx = int(x_s/celWidth)
          yy = int(y_s/celHeight)
          if x_tmp != xx or y_tmp != yy:
            x_tmp=xx
            y_tmp=yy
            rect= pg.draw.rect(win,(ALTCOLOR),( x_tmp * celWidth + 1, y_tmp * celHeight + 1, celWidth -1 ,celHeight -1),0)
            pg.display.update(rect)
   
        
      if event.type == pg.VIDEORESIZE:
        width, height = event.size
        winini(win)
        #print(width,height)  # test
      if event.type == pg.QUIT:
        mainLoop = False
        pg.display.update()
        pg.quit()
        sys.exit()

if __name__ == '__main__':
  main()