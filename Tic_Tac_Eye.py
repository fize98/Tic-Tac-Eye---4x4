"""
Created on Tues 4 13:25:06 2020

@author: Fidan Zeynalova

1. Read the code THOROUGHLY (there's something new for everyone)
2. Run the code
3. Change where required FIRST then continue editing.

Here I designed a minimalistic, yet very dynamic 4x4 board for my Tic Tac Toe.
I added an animated gradient background for my screen.
Also, I drew a black board with white outlines and grids to add more legibility, 
minimalism, and separation. I set the gradiation of the background to change from
pink to blue to show a visually pleasing contrast in the animation.

In this script, I added 9 squares, made out of turtles, to position in the middle 
of each square drawn in the board script. I made these 9 turtles clickable buttons
in order to stamp two image icons for my players. Here, all the 9 turtles can be clicked
and alternate between two images each time any turtle gets clicked.

To Play the game you should:
    1. Wait for the Splash creen to load and a text pop up, saying "PRESS SPACE TO START"
    2. Press space key & watch the board and the players take their position.
    3. Start playing the game with just clicking the white squares on the screen
    
Closed eye is the "X" and Open eye is the "O" of the game :)

"""

import turtle, random, time
import checkWin
turtle.tracer(0)   
turtle.colormode(255) # ADD THIS TO YOUR CODE!

# =========CLASSES=========
        
class GameManagerParent(): # My parent ManagerClass
    def __init__(self):
        
        '''Sets up my panel size and adds a global set up for the splash creen'''

        # Global varialbles & set up for the other classes
        self.panel=turtle.Screen() 
        self.w=900
        self.h=900
        turtle.setup(self.w,self.h)

        # Code below is connected to the methods, clearScreen, drawSplash down below in the child class
        self.boardList = [] #scoreBoard for scorekeeping
        self.size = 3 # number of "tiles" on each side (3**2 = total number of tiles)
        for i in range(3**2):
            self.boardList.append([])        
                
class GameManager(GameManagerParent): # My Child GameManager class
    def __init__(self):
        super().__init__() 
        
        '''Sets up the image and text values in order to draw 
        a splash screen before the game.'''
        
        # Making my Splash screen with Dr. Z's example code
        self.splash_IMG = "splash.gif"
        self.splashTurt = turtle.Turtle()
        self.text = turtle.Turtle(visible=False)
        self.font = ('Helvetica', 20,'bold')
        
        self.drawSplash()
        self.panel.listen()
  
    def clearScreen(self):
        
        '''Clears the creen and calls my classes in specific order'''
        
        # for onkeypress callback function
        self.splashTurt.clear()
        self.text.clear()
        self.board = Board('white',5,10,'black')
        self.player = Player(self.panel)
        self.background = Background(self.panel)

        
    def drawSplash(self):
        
        '''Adds the image and stamps it on the center of my page. 
        Adds the text below the image as well'''
        
        # set turtle to be an image
        self.panel.addshape(self.splash_IMG)
        self.splashTurt.shape(self.splash_IMG)
  
        # draw image in center (home)
        self.splashTurt.stamp()
        
        # add text
        self.text.up()
        self.text.goto(0,-200)
        self.text.write("PRESS SPACE TO START!", align='Center',font=self.font)
        self.panel.onkeypress(self.clearScreen,"space")


            
class Player(): # My class that deals with Players
    
    def __init__(self,panel):
        
        '''Sets up the number, location, and image of my players'''
        
        # setting up my turtle for the player
        self.turtList = []
        self.numTurt = 16 # Since I added 4x4 tile I increased my turtle numbers
        self.steps = 0 
        
        # Global variables
        self.numside = 4 # number of spaces per side of the board
        self.empty = "" # I'll use an empty list to indicate an UNPLAYED position on the board
        
        self.panel = panel
        # Imports my images for the players
        self.image1 = "eye_open.gif"
        self.image2 = "eye_closed.gif"
        
        # My list to contain two of my images
        self.imageList = [self.image1,self.image2]
        
        # list of my coordinates for each of the 9 squares to go to
        self.squareLocations = [(-225,225),(-75,225),(75,225),(225,225),
                                (-225,75),(-75,75),(75,75),(225,75),
                                (-225,-75),(-75,-75),(75,-75),(225,-75),
                                (-225,-225),(-75,-225),(75,-225),(225,-225)]
    
        self.boardList = self.makeBoardList(empty=self.empty)
        print(self.boardList)
        # Setting up my turtles and connecting it to the turtList
        for i in range(self.numTurt):
            squares = turtle.Turtle(shape='square')
            squares.shapesize(5)
            squares.pensize(5)
            squares.pencolor('white')
            squares.color('white')
            squares.fillcolor('white')
            squares.onclick(self.nextStep) # Connecting each square to a click command
            squares.up()
            squares.goto(self.squareLocations[i])
            squares.down()
            self.turtList.append(squares) # append adds a turtle to the end of the list
            
    # A whole function to assign clickable locations for my turtles and changes the images alternating between two
    def nextStep(self,x,y): # function uses x and y coordinates to 
    
        '''Adds the positions and a change on click action with two images'''
        
        # I was advised to use modulo to alternate between the images on each clicke by my brother
        self.steps = self.steps+1 # starting from the first step of on click command
        rightImage = self.steps%2 # Lets my tutles use modulo operator to alternate between two images 
        turtleImage = self.imageList[rightImage] # Using rightImage to pick from the imageList to use for the shape of my turtle
        # attaches the image used for the players
        self.panel.addshape(turtleImage)
        
        
        # Row 1
        if (x >= -300 and x <= -150 and y >= 150 and y <= 300):
            self.turtList[0].shape(turtleImage)
            
            if rightImage:
                self.boardList[0][0] ='X'
            else:
                self.boardList[0][0] ='o'

                
        if (x >= -150 and x <= 0 and y >= 150 and y <= 300):
            self.turtList[1].shape(turtleImage)
            if rightImage:
                self.boardList[0][1] ='X'
            else:
                self.boardList[0][1] ='o'

            
        if (x >= 0 and x <= 150 and y >= 150 and y <= 300):
            self.turtList[2].shape(turtleImage)
            
            if rightImage:
                self.boardList[0][2] ='X'
            else:
                self.boardList[0][2] ='o'

        
        if (x >= 150 and x <= 300 and y >= 150 and y <= 300):
            self.turtList[3].shape(turtleImage)
            
            if rightImage:
                self.boardList[0][3] ='X'
            else:
                self.boardList[0][3] ='o'

      
            
        # Row 2        
        if (x >= -300 and x <= -150 and y >= 0 and y <= 150):
            self.turtList[4].shape(turtleImage)
            
            if rightImage:
                self.boardList[1][0] ='X'
            else:
                self.boardList[1][0] ='o'

        
        if (x >= -150 and x <= 0 and y >= 0 and y <= 150):
            self.turtList[5].shape(turtleImage)
            
            if rightImage:
                self.boardList[1][1] ='X'
            else:
                self.boardList[1][1] ='o'

            
        if (x >= 0 and x <= 150 and y >= 0 and y <= 150):
            self.turtList[6].shape(turtleImage)
            
            if rightImage:
                self.boardList[1][2] ='X'
            else:
                self.boardList[1][2] ='o'

            
        if (x >= 150 and x <= 300 and y >= 0 and y <= 150):
            self.turtList[7].shape(turtleImage) 
            
            if rightImage:
                self.boardList[1][3] ='X'
            else:
                self.boardList[1][3] ='o'

 
             
        # Row 3
        if (x >= -300 and x <= -150 and y >= -150 and y <= 0):
            self.turtList[8].shape(turtleImage)
            
            if rightImage:
                self.boardList[2][0] ='X'
            else:
                self.boardList[2][0] ='o'

        
        if (x >= -150 and x <= 0 and y >= -150 and y <= 0):
            self.turtList[9].shape(turtleImage)
            
            if rightImage:
                self.boardList[2][1] ='X'
            else:
                self.boardList[2][1] ='o'

            
        if (x >= 0 and x <= 150 and y >= -150 and y <= 0):
            self.turtList[10].shape(turtleImage)
            
            if rightImage:
                self.boardList[2][2] ='X'
            else:
                self.boardList[2][2] ='o'

            
        if (x >= 150 and x <= 300 and y >= -150 and y <= 0):
            self.turtList[11].shape(turtleImage)
            
            if rightImage:
                self.boardList[2][3] ='X'
            else:
                self.boardList[2][3] ='o'

            
            
        # Row 4    
        if (x >= -300 and x <= -150 and y >= -300 and y <= -150):
            self.turtList[12].shape(turtleImage)
            
            if rightImage:
                self.boardList[3][0] ='X'
            else:
                self.boardList[3][0] ='o'

        
        if (x >= -150 and x <= 0 and y >= -300 and y <= -150):
            self.turtList[13].shape(turtleImage)
            
            if rightImage:
                self.boardList[3][1] ='X'
            else:
                self.boardList[3][1] ='o'

            
        if (x >= 0 and x <= 150 and y >= -300 and y <= -150):
            self.turtList[14].shape(turtleImage)
            
            if rightImage:
                self.boardList[3][2] ='X'
            else:
                self.boardList[3][2] ='o'

            
        if (x >= 150 and x <= 300 and y >= -300 and y <= -150):
            self.turtList[15].shape(turtleImage) 
            
            if rightImage:
                self.boardList[3][3] ='X'
            else:
                self.boardList[3][3] ='o'

            
        self.checkGameOver()
            
    # Modified code from Dr. Z.
    def makeBoardList(self,numside=4,empty=[]):
        '''Makes an empty scoreboard for tictactoe, based on the number of sides.
        The default 3x3 looks like this:
            [ [ [],[],[] ],
              [ [],[],[] ],
              [ [],[],[] ] ]
        Parameters-
        numside - (int) number of squares per side of the tic tac toe board
        empty - the indicator to use for an empty board. Try 0 or a string value.'''
        boardList = [] # empty list
        for i in range(self.numside):
            #make rows
            boardRow=[]
            for k in range(self.numside):
                # make columns
                boardRow.append(empty)
            boardList.append(boardRow)
        return boardList
    
    def checkGameOver(self):
        
        print(self.boardList[0],'\n',
              self.boardList[1],'\n',
              self.boardList[2],'\n',
              self.boardList[3]) # show the boardlist, but so it looks like a board!
        
        # Now lets check to see if there's a winner
        WINNER = checkWin.checkWin(self.boardList)
        print(WINNER)
        #==============================================================
        #                        STOP! READ!
        # You want to check for a winner all the time, but a STALEMATE
        # only happens when teh board is FULL. So we'll check for winners
        # but if we get a stalemate, we'll also check to see that the board
        # is full!
        #==============================================================
        
        gameOver = False # some variable to tell if my game is over. 
        # USE THIS TO DRAW YOUR GAMEOVER SCREEN (if you're doing that)
        
        if type(WINNER) == str and WINNER != self.empty:
            print(WINNER + ' is the winner!')
            gameOver = True # we have a winner, so the game is done.
            
        else:
            for row in self.boardList:
                if self.empty in row:
                    # are there any values equal to our "empty space" value?? 
                    # if so, gameOver isn't happening!
                    gameOver = False
                else: 
                    gameOver = True
                    
                    print("It's a draw! No winner! \n",
                              '\n',
                              "Play again?")
        if gameOver:
            # From PC06
              gameOver = turtle.Turtle()
              gameOver.color('red')
              style = ('Helvetica', 80, 'bold')
              gameOver.up()
              gameOver.hideturtle()
              gameOver.goto(0,-50)
                    
              # gameover condition
              gameOver.write('GAMEOVER!', font=style, align='center')
              turtle.done()

# added a class to draw my board  
class Board():
    
    def __init__(self,color='white',width=5,speed=10,fillcolor='black'):
        
        '''Sets up my board turtle with its characteristics and locations/positions. 
        Adds list of inside margin lines that draw 3 lines horizontally and 3 lines vertically'''

        # list of my coordinates for the inside margins of the board
        self.insideBoard = [(-300,150),(-300,-150),(-300,0),(-150,-300),(150,-300), (0,-300)] 

        self.boardTurt = turtle.Turtle(shape='square') # created a new turtle to draw the board
        
        self.boardTurt.color(color) 
        self.boardTurt.width(width)
        self.boardTurt.speed(speed)
        self.boardTurt.fillcolor(fillcolor)
        
        # Starting postion of my turtle on the bottom left to start drawing the board
        self.boardTurt.up()
        self.boardTurt.goto(-300,-300)
        self.boardTurt.down()
        
        # For loop to draw my square for the board
        self.boardTurt.begin_fill()
        for i in range(4): 
        
            self.boardTurt.forward(600) 
            self.boardTurt.left(90) 
        self.boardTurt.end_fill() 
        
        # Code for inner grids of the board
        self.boardTurt.penup() 
        self.boardTurt.goto(self.insideBoard[0])
        self.boardTurt.pendown() 
        self.boardTurt.forward(600) 
          
        self.boardTurt.penup() 
        self.boardTurt.goto(self.insideBoard[1]) 
        self.boardTurt.pendown() 
        self.boardTurt.forward(600) 
        
        self.boardTurt.penup() 
        self.boardTurt.goto(self.insideBoard[2])
        self.boardTurt.pendown() 
        self.boardTurt.forward(600) 
        
        
        self.boardTurt.penup() 
        self.boardTurt.goto(self.insideBoard[3])
        self.boardTurt.pendown() 
        self.boardTurt.left(90)
        self.boardTurt.forward(600) 
          
        self.boardTurt.penup() 
        self.boardTurt.goto(self.insideBoard[4]) 
        self.boardTurt.pendown() 
        self.boardTurt.forward(600)
        
        self.boardTurt.penup() 
        self.boardTurt.goto(self.insideBoard[5]) 
        self.boardTurt.pendown() 
        self.boardTurt.forward(600)
        self.boardTurt.penup()
        self.boardTurt.hideturtle() # To hide my turtle at when finished with the board

# added a class for my background animation        
class Background():
    
    def __init__(self,panel):
        
        '''Creates the animated background with the gradience of colors'''
                    
        self.running = True # for controlling the while loop
        
        # Creates a colorful background and steps for my turtles to take
        self.red = 255
        self.green = 0
        self.blue = 255
        self.inc = 5
        
        # code will execute in order within the loop
        while self.running:
            
            # global panel
            
            # To animate the gradient background by changing the incrementing value
            if self.red >= 255:
                self.inc *= -1 # change it to negative so it goes back to 0
            elif self.red <= 0:
                self.inc *= -1
            
            # added a limit for my numbers not to exceed 255 or be lower than 0 when changing colors
            self.red += self.inc
            if (self.red < 0):
                self.red = 0
            elif (self.red > 255):
                self.red = 255
        
            time.sleep(0.1) # lets the color of the background change in a certain timeframe
            
            panel.update() # runs the while loop to execute the animation
                
            panel.bgcolor(self.red, self.green, self.blue) # used color values in the panel background
        
    
# Call back instances for my classes
game = GameManager()
   
# =========LISTENERS & CLEANUP =========
game.panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.



""" I played this game with my sister and the only feedback she provided was trashing my choice of background animation.
She repeatedly told me that the change of color was hurting her eyes, which I believe is very important for my future 
projects to be friendly towards people who might also take the color changes like the one in this game, creating an issue 
to focus on the actual game. """


