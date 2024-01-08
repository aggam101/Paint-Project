                                             #Aggam Grewal
                                            #PaintProject.py
# This Paint Project is Avengers themed and it allows the user to play with different types of tools, stamps, and background. 
# It allows the user to make a picture on the canvas and save it to their device.
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog

root = Tk() 
root.withdraw()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (209, 209, 209)
YELLOW = (255,255,0)
RED = (255,0,0)

drawCol = (0,0,0) #makes starting colour black

screen = display.set_mode((800,600))#screen size

tools =[]
tool = "pencil" #makes the pencil tool to be the default tool

mainBack = image.load("backgroundFSE101.jpg")#background image

#---------------------------------loading images for the program------------------------------------
#loading tool images
pencil = image.load("pensilFSE.png")
eraser = image.load("eraserFSE3.jpg")
highlighter = image.load("highlighter.png")
spraypaint = image.load("spraypaint.png")
paintbrush = image.load("paintbrush.png")

#loading stamp images
stamp1 = image.load("stamp1.png")
stamp1Larger = image.load("stamp1Larger.png")
stamp2 = image.load("stamp2.png")
stamp2Larger = image.load("stamp2 copy.png")
stamp3 = image.load("stamp4.png")
stamp3Larger = image.load("stamp4 copy.png")
stamp4 = image.load("stamp5.png")
stamp4Larger = image.load("stamp5 copy.png")
stamp5 = image.load("stamp6.png")
stamp5Larger = image.load("stamp6 copy.png")
stamp6 = image.load("stamp6.tiff")
stamp6Larger = image.load("stamp6 copy.tiff")

#loading background imaged
background1 = image.load("backgroundFSE1.jpeg")
background1Larger = image.load("backgroundFSE1 copy.jpeg")
background2 = image.load("backgroundFSE2.jpg")
background2Larger = image.load("backgroundFSE2 copy.jpg")
background3 = image.load("backgroundFSE3.jpg")
background3Larger = image.load("backgroundFSE3 copy.jpg")


col = image.load("colpallet.png")#loading the colour pallet
loadbutton = image.load("load1.png")#loading the load button
savebutton = image.load("save1.png")#loading the save button
      
font.init()

imageX= 55
imageY = 100
size1 = 40

#------------------creating varibles for all the rect. so its easier to make the rect when i need to use them-------------------
pencilRect = Rect(imageX-2, imageY,55,55)
eraserRect = Rect(imageX-2, imageY+70, 55,56)
canvasRect = Rect(160,100,490,390)

lineRect = Rect(imageX+5,imageY+160,size1,size1)
filledSquareRect = Rect(imageX-20,imageY+220,size1,size1)
unfilledSquareRect = Rect(imageX+30, imageY+220, size1,size1)
filledCirclesRect = Rect(imageX-20,imageY+280,size1,size1)
unfilledCirclesRect = Rect(imageX+30, imageY+280, size1,size1)

highlighterRect = Rect(imageX+645,imageY,55,55)
spraypaintRect = Rect(imageX+645,imageY+80,55,55)
brushRect = Rect(imageX+645,imageY+160,55,55)

stamp1Rect = Rect(imageX+135, imageY+420, 55,55)
stamp2Rect = Rect(imageX+210, imageY+420, 55,55)
stamp3Rect = Rect(imageX+285, imageY+420, 56,55)
stamp4Rect = Rect(imageX+360, imageY+420, 55,55)
stamp5Rect = Rect(imageX+435, imageY+420, 55,55)
stamp6Rect = Rect(imageX+505, imageY+420, 55,55)

background1Rect = Rect(imageX+620, imageY+240, 45,45)
background2Rect = Rect(imageX+680, imageY+240, 47,47)
background3Rect = Rect(imageX+680, imageY+300, 48,48)
background4Rect = Rect(imageX+620, imageY+300, 45,45)

loadRect = Rect(658,imageY+417, 62,62)
saveRect = Rect(728, imageY+417, 62,62)


brush = Surface((20,20),SRCALPHA)#making the brush so it's a bit transparents
draw.circle(brush, drawCol+(15,), (10,10),10)


screen.blit(mainBack, (-30,0))#blitting the main background
draw.rect(screen, WHITE, canvasRect)#drawing the canvas

sx, sy = (0,0)#this is the startX and startY (used this in the shapeConditions, drawLine, and drawShape functions) 
back = screen.copy()#replaces screen with a copied version of the canvas

#-------------------------------------------------FUNCTIONS------------------------------------------------------
running =True
def shapeConditions(sx, sy, mx, my, mb): #conditions so the user can move the mouse in all directions and it works
    if mx<sx and my<sy and mb[0]==1:#when user goes to the top left
        rect=Rect(mx,my,sx-mx,sy-my)
    elif mx<sx and my>sy and mb[0]==1:#when user goes to the botton left
        rect=Rect(mx,sy,sx-mx,my-sy)
    elif mx>sx and my<sy and mb[0]==1:#when user goes to the top right
        rect=Rect(sx,my,mx-sx,sy-my)
    elif mx>sx and my>sy and mb[0]==1:#when user goes to the bottom right
        rect=Rect(sx,sy,mx-sx,my-sy)
    else:
        rect=Rect(mx,my,0,0)
    return rect

def hover(screen, BLACK,rect): #draws a black rect. around a button when called
    draw.rect(screen,BLACK,rect,1)

def drawLine(drawCol, screen, tool, canvasRect, sx, sy, back, mx, my, mb): #draws a straight line when tool == "line" -->starts drawing from the start position (sx,sy) to the mouse position(mx,my)
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == "line":
            screen.blit(back, (0,0))
            draw.line(screen, drawCol, (sx, sy), (mx,my))
        screen.set_clip(None)
        
def drawshapes(drawCol, screen, tool, canvasRect, drawShape, sx, sy, back, mx, my, mb):#draws all shapes (using shapeConditions) when user changes the tool to any shape ***not line***
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == "unfill oval":
            screen.blit(back, (0,0))
            rect = shapeConditions(sx, sy, mx, my, mb)
            draw.ellipse(screen,drawCol,rect,1)
        if tool == "fill oval":
            screen.blit(back, (0,0))
            rect = shapeConditions(sx, sy, mx, my, mb)
            draw.ellipse(screen,drawCol,rect,0)
        if tool == "unfill Rect":
            screen.blit(back, (0,0))
            rect = shapeConditions(sx, sy, mx, my, mb)
            draw.rect(screen,drawCol,rect,1)
        if tool == "fill Rect":
            screen.blit(back, (0,0))
            rect = shapeConditions(sx, sy, mx, my, mb)
            draw.rect(screen,drawCol,rect,0)   
        screen.set_clip(None)

def drawbackgrounds(canvasRect, background, text, pos, mb, mx, my):#function that blits the background onto the canvas
    global tool
    if mb[0] == 1:
        screen.set_clip(canvasRect)
        if tool == text:
          screen.blit(background, pos)
        screen.set_clip(None)
        
def background_clear(WHITE, screen, tool, canvasRect, mx, my, mb): #function that clears the canvas
    if mb[0] == 1:
        screen.set_clip(canvasRect)
        if tool == "clear":
          draw.rect(screen, WHITE, (0,0,1000,1000))
        screen.set_clip(None)

def drawstamps(canvasRect, stamp, text, pos, mb, mx,my):#allows the user to blit any stamp on the canvas
    global tool
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == text:
          screen.blit(back, (0,0))
          screen.blit(stamp, pos)
        screen.set_clip(None)
  
def selected(rect, text):#keeps the tool user selected highlighted (yellow box around it)
    global tool
    if tool == text:
        draw.rect(screen, YELLOW, rect,1)  

def pick(rect, text): #function thats called when user hovers over a button and/or click down on it --> changes the tool
    global tool
    if rect.collidepoint(mx,my):
        hover( screen,BLACK, rect)
        if mb[0] == 1:
            screen.blit(back, (0,0))
            draw.rect(screen,YELLOW,rect,1)
            tool = text

def stamps(screen, WHITE, rect, small, large ,text, xy, pos):#a final stamps function, that groups together all functions used so there's no copy/paste
    draw.rect(screen, WHITE, rect)
    screen.blit(small, xy)
    pick(rect, text)
    drawstamps(canvasRect, large, text, pos, mb, mx,my)
    selected(rect, text)

def background(screen, WHITE, rect, small, large ,text, xy, pos):#a final background function, that groups together all functions used so there's no copy/paste
    draw.rect(screen, WHITE, rect)
    screen.blit(small, xy)
    pick(rect, text)
    drawbackgrounds(canvasRect, large, text, pos, mb, mx,my)

def shapes(screen, WHITE, BLACK, rect, text, mb, mx,my): #a final shape function, that groups together all functions used so there's no copy/paste
    draw.rect(screen, WHITE, rect)
    #draws all the shapes/line on the button so user knows what the button does 
    if text == "line":
        draw.line(screen, BLACK, (imageX+10, imageY+165),(imageX+33,imageY+190))
    if text == "fill Rect":
        draw.rect(screen, BLACK, (imageX-8, imageY+230, 15, 20))
    if text == "unfill Rect":
        draw.rect(screen, BLACK, (imageX+42, imageY+230,15,20),1)
    if text == "fill oval":
        draw.ellipse(screen, BLACK, (imageX-10, imageY+286, 20,25))
    if text == "unfill oval":
        draw.ellipse(screen, BLACK, (imageX+40, imageY+286, 20,25),1)
    pick(rect, text)
    if text != "line":
        drawshapes(drawCol, screen, tool, canvasRect, shapeConditions, sx, sy, back, mx, my, mb) 
    if text == "line":
        drawLine(drawCol, screen, tool, canvasRect, sx, sy, back, mx, my, mb)
    selected(rect, text)

#---------------------------------------START OF LOOP-------------------------------------------------------     
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
           if e.button == 1:
               sx, sy = e.pos
               back = screen.copy()

    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    
    #bliting the title "Art with the         " and "Avengers" seperatly so the 'Avengers' can change to the colour the user selects
    fnt = font.SysFont("Times New Roman", 60)
    txt = fnt.render("Art with the              ", True, BLACK)
    wid = txt.get_width()
    hei = txt.get_height()
    screen.blit(txt, ((800-wid)//2, (100-hei)//2))
    txt = fnt.render("Avengers", True, drawCol)
    screen.blit(txt, (450, (100-hei)//2))
    
#---------------------------------------pensil & eraser tools--------------------------------------------------
    #drawing pencil icon
    draw.rect(screen, WHITE, pencilRect)
    screen.blit(pencil, (imageX+3,imageY+5))
    #using the pencil
    pick(pencilRect, "pencil")#calls the pick function so user can select/choose the pencil
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect) #set clip so nothing is drawn outside the canvas
        if tool == "pencil":
            draw.line(screen,drawCol,(omx,omy),(mx,my),2)
        screen.set_clip(None)
    selected(pencilRect, "pencil")#keeping the button highlighted
    
    #drawing eraser icon
    screen.blit(eraser, (imageX-2,imageY+70))
    #using the eraser
    pick(eraserRect, "eraser")#calls the pick function so user can select/choose the eraser
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == "eraser": 
            draw.circle(screen,(255,255,255),(mx,my),20) #dimensions for the eraser
        screen.set_clip(None)
    selected(eraserRect, "eraser")#keeping the button highlighted

#----------------------------------------drawing the shape tools--------------------------------------------------
                                        
    shapes(screen, WHITE, BLACK, lineRect, "line", mb, mx,my)#function to draw, use, pick, highlight(selected function) the line
    shapes(screen, WHITE, BLACK, filledSquareRect, "fill Rect", mb, mx,my)#function to draw, use, pick, highlight(selected function) the fill rect
    shapes(screen, WHITE, BLACK, unfilledSquareRect, "unfill Rect", mb, mx,my)#function to draw, use, pick, highlight(selected function) the unfill rect
    shapes(screen, WHITE, BLACK, filledCirclesRect, "fill oval", mb, mx,my)#function to draw, use, pick, highlight(selected function) the fill oval
    shapes(screen, WHITE, BLACK, unfilledCirclesRect, "unfill oval", mb, mx,my)#function to draw, use, pick, highlight(selected function) the unfill oval
    
#--------------------------------------drawing and using of the indiviual features---------------------------------------------------
    
    draw.rect(screen, WHITE, highlighterRect)#drawing the highlighter button
    screen.blit(highlighter, (imageX+655, imageY+5))
    if highlighterRect.collidepoint(mx,my): #does the same thing as the pick function but adds a text
        hover(screen, BLACK, highlighterRect)
        fnt = font.SysFont("Times New Roman", 7) 
        txt = fnt.render("YELLOW ONLY", True, RED)
        screen.blit(txt, (imageX+647, imageY+1))#shows "YELLOW ONLY" when user hovers over the rect.
        if mb[0] == 1: 
            screen.blit(back, (0,0))
            draw.rect(screen, YELLOW, highlighterRect, 1) 
            tool = "highlighter"
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == "highlighter":
            screen.blit(back, (0,0))
            draw.line(screen, YELLOW, (sx, sy), (mx,my),15) #dimensions of the highlighter
        screen.set_clip(None)
    selected(highlighterRect, "highlighter")#keeps the yellow box around the rect to show the user the tool their using

    draw.rect(screen, WHITE, spraypaintRect)#drawing the spray paint button
    screen.blit(spraypaint, (imageX+650, imageY+85))
    pick(spraypaintRect, "spray paint")#calls the pick function so user can select/choose the spray paint
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == "spray paint":
            sprayX = randint(mx-15,mx+15)#getting the randon x position 
            sprayY = randint(my-15,my+15)#getting the random y position
            if hypot(mx-sprayX,my-sprayY)<15:#without the hypot it would be a in a rectangle not a circle
                draw.circle(screen,drawCol,(sprayX,sprayY),1)#drawing the circles
        screen.set_clip(None)
    selected(spraypaintRect, "spray paint")#keeps the yellow box around the rect to show the user the tool their using

    draw.rect(screen, WHITE, brushRect)#draws the brush rect
    screen.blit(paintbrush, (imageX+652, imageY+170))
    pick(brushRect, "brush")#calls the pick function so user can select/choose the brush
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == "brush" and (mx != omx or my!= omy):
                dist=hypot(mx-omx,my-omy)#calculates the distance between mx and omx, my and omy 
                dist=int(dist)#doesn't work if it's a float so must be turned into a int
                for i in range(dist):
                    bx=i*(mx-omx)//dist#gets the bx (every pixel between omx and mx)
                    by=i*(my-omy)//dist#gets the by (every pixel between omy and my)
                    brushCol = tuple(drawCol[:3])+(15,)#gets a lighter/transparent version of drawCol 
                    draw.circle(brush,brushCol,(10,10),10)#draws the circle with radius 10
                    screen.blit(brush, (omx+bx-10,omy+by-10)) 
        screen.set_clip(None)
    selected(brushRect, "brush")#keeps the yellow box around the rect to show the user the tool their using
    
#--------------------------------------different backgrounds--------------------------------------------
            
    background(screen, WHITE, background1Rect, background1,background1Larger, "background1", (imageX+620,imageY+240), (-120,100))#function to draw, use, pick background1
    background(screen, WHITE, background2Rect, background2,background2Larger, "background2", (imageX+680,imageY+240), (55,100))#function to draw, use, pick background2
    background(screen, WHITE, background3Rect, background3,background3Larger, "background3", (imageX+680,imageY+300), (-45,80))#function to draw, use, pick background3

    draw.rect(screen, WHITE, (background4Rect))#drawing the clear button
    fnt = font.SysFont("Times New Roman", 13)
    txt = fnt.render("Clear", True, BLACK)
    screen.blit(txt, (imageX+627, imageY+315))#blits 'clear' on the rect so user knows what the button does
    pick(background4Rect, "clear")#calls the pick function so user can select/choose the clear button
    background_clear(WHITE, screen, tool, canvasRect, mx, my, mb)#calling the background_clear function to put a blank canvas

#--------------------------------------------Stamps--------------------------------------------------
                                        
    stamps(screen, WHITE, stamp1Rect, stamp1,stamp1Larger, "stamp 1", (imageX+135,imageY+430), (mx-100,my-50))#function to draw,use,highlight(selected function),pick stamp1
    stamps(screen, WHITE, stamp2Rect, stamp2,stamp2Larger, "stamp 2", (imageX+214,imageY+418), (mx-60,my-70))#function to draw,use,highlight(selected function),pick stamp2
    stamps(screen, WHITE, stamp3Rect, stamp3,stamp3Larger, "stamp 3", (imageX+284,imageY+425), (mx-60,my-40))#function to draw,use,highlight(selected function),pick stamp3
    stamps(screen, WHITE, stamp4Rect, stamp4,stamp4Larger, "stamp 4", (imageX+360,imageY+419), (mx-50,my-50))#function to draw,use,highlight(selected function),pick stamp4
    stamps(screen, WHITE, stamp5Rect, stamp5,stamp5Larger, "stamp 5", (imageX+443,imageY+422), (mx-50,my-50))#function to draw,use,highlight(selected function),pick stamp5
    stamps(screen, WHITE, stamp6Rect, stamp6,stamp6Larger, "stamp 6", (imageX+517,imageY+425), (mx-40,my-50))#function to draw,use,highlight(selected function),pick stamp6

#---------------------------------------colour pallet-------------------------------------------------------------   
    screen.blit(col, (2, 505))#blits the colour pallet
    if 2<mx<170 and 505<my<595 and mb[0] == 1:
        drawCol = screen.get_at((mx,my))#gets the colour where the mouseX and mouseY gets clicked
#----------------------------------------Load & Save--------------------------------------------------------
    #load BUTTON --> able to load a drawing user perivously drew
    draw.rect(screen, GREY, loadRect)
    screen.blit(loadbutton, (660,imageY+420))
    if loadRect.collidepoint(mx,my):
        hover(screen, BLACK, loadRect)
        fnt = font.SysFont("Times New Roman",13)
        txt = fnt.render("LOAD", True, RED)
        screen.blit(txt, (670, imageY+425))#blits the word 'LOAD' when user hovers over the rect
        if mb[0] == 1:
            draw.rect(screen, YELLOW, loadRect, 1)
            tool = "load"
    if mb[0] == 1:
        if tool == "load":
            result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])
            file = image.load(result)
            screen.blit(file, canvasRect)#puts the image user choose on the canvas
    
    #save BUTTON --> allows user to save what's drawn on the canvas 
    draw.rect(screen, GREY, saveRect)
    screen.blit(savebutton, (730, imageY+420))
    if saveRect.collidepoint(mx,my): 
        hover(screen, BLACK, saveRect)
        fnt = font.SysFont("Times New Roman",13)
        txt = fnt.render("SAVE", True, RED)
        screen.blit(txt, (740, imageY+425))#blits the word 'SAVE' when user hovers over the rect
        if mb[0] == 1:
            draw.rect(screen, YELLOW, saveRect, 1)
            tool = "save"
    if mb[0] == 1:
        if tool == "save":
            sav = screen.subsurface(canvasRect)
            display.set_caption("Your Art is Saved")
            result = filedialog.asksaveasfilename()
            image.save(sav, result+".jpg")
            print(result)
#-----------------------------------------END OF CODE---------------------------------------------------------
    omx, omy = mx,my
    print(mx,",",my, ", tool -->",tool)
    display.flip()
quit()