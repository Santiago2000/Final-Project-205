"""
Filename: finalProject.py
Author:   debajban, santiago
Date:     12/12/2016
Details:  This program does the Lab#16 exercise

"""

import java.awt.Font as Font

def drawScreen():
  pic = makeEmptyPicture(300,300,white)
  addLine(pic, 100,0,100,300,red)
  addLine(pic, 200,0,200,300,red)
  addLine(pic, 0,100,300,100,red)
  addLine(pic, 0,200,300,200,red)
  
  addText(pic, 50,90, "1")
  addText(pic, 50,190, "4")
  addText(pic, 50,290, "7")
  
  addText(pic, 150,90, "2")
  addText(pic, 150,190, "5")
  addText(pic, 150,290, "8")

  addText(pic, 250,90, "3")
  addText(pic, 250,190, "6")
  addText(pic, 250,290, "9")

  return pic

def paintPic(pic, pos, type):
  if type == "X":
    if pos == 1:
      addText(pic, 50,50, "X", red)
    if pos == 2:
      addText(pic, 150,50, "X", red)
    if pos == 3:
      addText(pic, 250,50, "X", red)
    if pos == 4:
      addText(pic, 50,150, "X", red)
    if pos == 5:
      addText(pic, 150,150, "X", red)
    if pos == 6:
      addText(pic, 250,150, "X", red)
    if pos == 7:
      addText(pic, 50,250, "X", red)
    if pos == 8:
      addText(pic, 150,250, "X", red)
    if pos == 9:
      addText(pic, 250,250, "X", red)
  if type == "O":
    if pos == 1:
      addText(pic, 50,50, "O", blue)
    if pos == 2:
      addText(pic, 150,50, "O", blue)
    if pos == 3:
      addText(pic, 250,50, "O", blue)
    if pos == 4:
      addText(pic, 50,150, "O", blue)
    if pos == 5:
      addText(pic, 150,150, "O", blue)
    if pos == 6:
      addText(pic, 250,150, "O", blue)
    if pos == 7:
      addText(pic, 50,250, "O", blue)
    if pos == 8:
      addText(pic, 150,250, "O", blue)
    if pos == 9:
      addText(pic, 250,250, "O", blue)

  return pic 
  
def checkWinner(positionDict, picture):
  if positionDict[1] == "X" and positionDict[2] == "X" and positionDict[3] == "X":
    addLine(picture, 50,50, 250,50,red)
    #repaint(picture)
    return "X"
  if positionDict[1] == "O" and positionDict[2] == "O" and positionDict[3] == "O":
    addLine(picture, 50,50, 250,50,blue)     
    #repaint(picture)
    return "O"
  if positionDict[4] == "X" and positionDict[5] == "X" and positionDict[6] == "X":
    addLine(picture, 50,150, 250,150,red)
    #repaint(picture)
    return "X"
  if positionDict[4] == "O" and positionDict[5] == "O" and positionDict[6] == "O":
    addLine(picture, 50,150, 250,150,blue)     
    #repaint(picture)
    return "O"
  if positionDict[7] == "X" and positionDict[8] == "X" and positionDict[9] == "X":
    addLine(picture, 50,250, 250,250,red)
    #repaint(picture)
    return "X"
  if positionDict[7] == "O" and positionDict[8] == "O" and positionDict[9] == "O":
    addLine(picture, 50,250, 250,250,blue)     
    #repaint(picture)
    return "O"    
  if positionDict[1] == "X" and positionDict[4] == "X" and positionDict[7] == "X":
    addLine(picture, 50,50, 50,250,red)
    #repaint(picture)
    return "X"
  if positionDict[1] == "O" and positionDict[4] == "O" and positionDict[7] == "O":
    addLine(picture, 50,50, 50,250,blue)     
    #repaint(picture)
    return "O"    
  if positionDict[2] == "X" and positionDict[5] == "X" and positionDict[8] == "X":
    addLine(picture, 150,50, 150,250,red)
    #repaint(picture)
    return "X"
  if positionDict[2] == "O" and positionDict[5] == "O" and positionDict[8] == "O":
    addLine(picture, 150,50, 150,250,blue)     
    #repaint(picture)
    return "O"   
  if positionDict[3] == "X" and positionDict[6] == "X" and positionDict[9] == "X":
    addLine(picture, 250,50, 250,250,red)
    #repaint(picture)
    return "X"
  if positionDict[3] == "O" and positionDict[6] == "O" and positionDict[9] == "O":
    addLine(picture, 250,50, 250,250,blue)     
    #repaint(picture)
    return "O"   
  if positionDict[1] == "X" and positionDict[5] == "X" and positionDict[9] == "X":
    addLine(picture, 50,50, 250,250,red)
    #repaint(picture)
    return "X"
  if positionDict[1] == "O" and positionDict[5] == "O" and positionDict[9] == "O":
    addLine(picture, 50,50, 250,250,blue)     
    #repaint(picture)
    return "O"  
  if positionDict[3] == "X" and positionDict[5] == "X" and positionDict[7] == "X":
    addLine(picture, 250,50, 50,250,red)
    #repaint(picture)
    return "X"
  if positionDict[3] == "O" and positionDict[5] == "O" and positionDict[7] == "O":
    addLine(picture, 250,50, 50,250,blue)     
    #repaint(picture)
    return "O"    
  return ""
def final():
  positionDict = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
  picture = drawScreen()
  repaint(picture)
  showInformation("Take turns to play - enter cell number in your input ")
  cnt = 1;
  while true:
    while true:
      x = requestString("Enter where you want X")
      try:
        x0 = int(x)
        if int(x) >0 and int(x) <10:
          positionDict[int(x)]="X"      
          picture = paintPic(picture, int(x), "X")
          break
        else:
          showInformation("Only numbers between 1 and 9 are allowed..retry")  
      except ValueError:
        showInformation("Only numbers between 1 and 9 are allowed..retry")
      
    repaint(picture)
    winner=checkWinner(positionDict, picture)
    if winner == "X":
      message = "  X IS THE WINNER !!!"
      myFont = makeStyle("Times New Roman", Font.ITALIC, 20)
      addTextWithStyle( picture, 20, 125, message,myFont, red)
      repaint(picture)
      break
      
    while true:
      o = requestString("Enter where you want O")
      try:
        y0 = int(o)
        if int(o) >0 and int(o) < 10:
          positionDict[int(o)]="O"
          picture = paintPic(picture, int(o), "O")
          break
        else:
          showInformation("Only numbers between 1 and 9 are allowed..retry")  
      except ValueError:
        showInformation("Only numbers between 1 and 9 are allowed..retry")           
        
    repaint(picture)
    winner=checkWinner(positionDict, picture)    
    if winner == "O":
      message = "  O IS THE WINNER !!!"
      myFont = makeStyle("Times New Roman", Font.ITALIC, 20)
      addTextWithStyle( picture, 20, 125, message,myFont, blue)
      repaint(picture)   
      break
    cnt = cnt + 1
    if cnt > 9:
      break;