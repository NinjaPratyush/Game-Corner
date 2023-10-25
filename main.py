import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from random import randint
from tkinter import messagebox
import random
def show_frame(frame):
    frame.tkraise()
window=Tk()
window.state("zoomed")
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.title("Game Corner")
frame1=tk.Frame(window)
frame2=tk.Frame(window)
frame3=tk.Frame(window)
frame4=tk.Frame(window)
frame5=tk.Frame(window)
frame6=tk.Frame(window)
frame7=tk.Frame(window)
frame8=tk.Frame(window)
for frame in(frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8):
    frame.grid(row=0,column=0,sticky='nsew')
#Frame 1 code (Main Screen)
frame1_title=tk.Label(frame1,text="Game Corner",bg='red',font=("Poppins",30))
frame1_title.pack(fill='x')
frame1.configure(bg="Purple")
frame1_btn=tk.Button(frame1,text="Tic Tac Toe",command=lambda:show_frame(frame2),bg="Orange",font=("Poppins",40))
frame1_btn2=tk.Button(frame1,text="Rock Paper and Scissors",command=lambda:show_frame(frame3),bg="Green",font=("Poppins",40))
frame1_btn3=tk.Button(frame1,text="Color Change",command=lambda:show_frame(frame4),bg="Yellow",font=("Poppins",40))
frame1_btn4=tk.Button(frame1,text="Quiz Game",command=lambda:show_frame(frame5),bg="Blue",fg="Yellow",font=("Poppins",40))
frame1_btn.pack(pady=20)
frame1_btn2.pack(pady=20)
frame1_btn3.pack(pady=20)
frame1_btn4.pack(pady=20)

#-----------------------------------------------Frame 2 code(Tic Tac Toe)-------------------------------------------------------

frame2_title=tk.Label(frame2,text="Tic Tac Toe",bg="yellow",font=("Arial",40))
frame2_title.pack()
frame2.configure(bg="#856ff8")
#Make a dictionary to store initial value of each button and to check win condition

board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" "}

turn="x"

def CheckForWin(player):   #Winning condition for player
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True
    

def RestartGame():
    for button in buttons:
        button["text"]=" "

    for i in board.keys():
        board[i]=" "
    winningLabel=Label(frame2,text="                                          ",font=("Arial",25),bg="#856ff8")
    winningLabel.place(x=900,y=300)

    

def play(event): #alternatively changes from x and o
    global turn
    button=event.widget
    buttonText=str(button)
    clicked=buttonText[-1]  #This will help to convert string into integer of each position
    print(clicked)
    if clicked =="n": #reason because integer value of first box is represented as 'n' and not '1'
        clicked=1
    else:
        clicked=int(clicked)

    if button["text"]==" ":
        if(turn=="x"):
            button["text"]="X"
            board[clicked]=turn
            if CheckForWin(turn):
                winningLabel=Label(frame2,text=f"{turn} wins the game!!",bg="#856ff8",font=("Arial",25))
                winningLabel.place(x=900,y=300)
            turn="o"

        else:
            button["text"]="O"
            board[clicked]=turn
            if CheckForWin(turn):
                winningLabel=Label(frame2,text=f"{turn} wins the game!!",bg="#856ff8",font=("Arial",25))
                winningLabel.place(x=900,y=300)
            turn="x"
    print(board)
#Tic Tac Toe Board
frame2_btn=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn.place(x=400,y=80)
frame2_btn.bind("<Button-1>",play)

frame2_btn2=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn2.place(x=525,y=80)
frame2_btn2.bind("<Button-1>",play)

frame2_btn3=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn3.place(x=650,y=80)
frame2_btn3.bind("<Button-1>",play)

frame2_btn4=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn4.place(x=400,y=230)
frame2_btn4.bind("<Button-1>",play)

frame2_btn5=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn5.place(x=525,y=230)
frame2_btn5.bind("<Button-1>",play)

frame2_btn6=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn6.place(x=650,y=230)
frame2_btn6.bind("<Button-1>",play)

frame2_btn7=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn7.place(x=400,y=380)
frame2_btn7.bind("<Button-1>",play)

frame2_btn8=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn8.place(x=525,y=380)
frame2_btn8.bind("<Button-1>",play)

frame2_btn9=Button(frame2,text=" ",width=4,height=2,font=("Arial",35),bg="orange",relief=RAISED)
frame2_btn9.place(x=650,y=380)
frame2_btn9.bind("<Button-1>",play)

frame2_btn10=Button(frame2,text="Back",command=lambda:show_frame(frame1),bg="Yellow",font=("Arial",20))
frame2_btn10.place(x=780,y=560)

restartbutton=Button(frame2,text="Restart",command=RestartGame,bg="Green",font=("Arial",20))
restartbutton.place(x=780,y=500)

#Restart Game
buttons=[frame2_btn,frame2_btn2,frame2_btn3,frame2_btn4,frame2_btn5,frame2_btn6,frame2_btn7,frame2_btn8,frame2_btn9]


#-----------------------------------------------Frame 3 Rock Paper and Scissors Game---------------------------------------------------------
frame3_title=Label(frame3,text="Rock Paper and Scissors",font=("Aerial",20),bg="Green")
frame3_title.pack()
frame3.configure(bg="white")

#picture
rock_img=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("scissors_image.jpg"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock_image.png"))

paper_img_comp=ImageTk.PhotoImage(Image.open("paper_image.jpg"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissors_image.png"))

#insert picture
user_label=Label(frame3,image=scissor_img,bg="white")
comp_label=Label(frame3,image=scissor_img_comp,bg="white")

comp_label.place(x=0,y=0)
user_label.place(x=840,y=0)
#scores

playerScore=Label(frame3,text=0,font=100,bg="white",fg="black")
computerScore=Label(frame3,text=0,font=100,bg="white",fg="black")
computerScore.place(x=500,y=200)
playerScore.place(x=750,y=200)

#indicators
user_indicator=Label(frame3,font=50,text="USER",bg="white")
comp_indicator=Label(frame3,font=50,text="COMPUTER",bg="white")
user_indicator.place(x=900,y=0)
comp_indicator.place(x=300,y=0)

#messages
msg=Label(frame3,font=50,bg="white")
msg.place(x=600,y=400)

#update messages
def updateMessage(x):
    msg['text']=x

#update user and computer score

def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)

def updateCompScore():
    score=int(computerScore["text"])
    score+=1
    computerScore["text"]=str(score)

#check winner

def RestartGame2():
    playerScore["text"]="0"
    computerScore["text"]="0"

def checkWin(player,computer):
    if(player==computer):
        updateMessage("Its a Tie")
    elif(player=="rock"):
        if(computer=="paper"):
            updateMessage("Computer Wins")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    elif player=="paper":
        if(computer=="scissor"):
            updateMessage("Computer Wins")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player=="scissor":
        if(computer=="rock"):
            updateMessage("Computer Wins")  
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass  
#update the choices

choices=["rock","paper",'scissor']


def updateChoice(x):

#for computer
    compChoice=choices[randint(0,2)]
    if(compChoice=="rock"):
        comp_label.configure(image=rock_img_comp)
    elif(compChoice=="paper"):
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#for user
    if(x=="rock"):
        user_label.configure(image=rock_img)
    elif(x=="paper"):
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)

#buttons
rock=Button(frame3,width=20,height=2,text="ROCK",bg="red",fg="white",command=lambda:updateChoice("rock"))
paper=Button(frame3,width=20,height=2,text="PAPER",bg="green",fg="white",command=lambda:updateChoice("paper"))
scissor=Button(frame3,width=20,height=2,text="SCISSOR",bg="orange",fg="white",command=lambda:updateChoice("scissor"))
rock.place(x=400,y=500)
paper.place(x=550,y=500)
scissor.place(x=700,y=500)

frame3_btn=Button(frame3,text="Back",command=lambda:show_frame(frame1),bg="#FFD700",font=("Poppins",20))
frame3_btn.place(x=800,y=570)

restartbutton2=Button(frame3,text="Restart",command=RestartGame2,bg="#D2691E",font=("Poppins",20))
restartbutton2.place(x=600,y=570)

#---------------------------------------Frame 4 Color Game--------------------------------------------------------
colors=["Red","Blue","Green","Pink","Black","Yellow","Orange","White","Purple","Brown"]

score=0
timeleft=30

def startGame(play):
    if timeleft==30:  #time reduce hoga aur color bhi change hoga
        countdown()

    nextcolor()
    

def countdown():
    global timeleft
    if timeleft ==0:
        messagebox.showinfo("Time Left","Time khatam ho gya!! Khatam tata bye bye Your score is:"+str(score))
    if timeleft > 0:
        timeleft-=1
        timeLabel.config(text="Time Left:"+str(timeleft))
        timeLabel.after(1000,countdown)
def nextcolor():
    global score
    global timeleft
    if timeleft >0:
        e.focus_set()  #e is for entry box
        if e.get().lower() == colors[1].lower(): #user capital,lowercase,kisi mein bhi enter kar sakta hai
            score+=1

        e.delete(0,tk.END) # entry box ki value ko bhi delete karte rahena hai
        random.shuffle(colors)

        label.config(fg=str(colors[1]),text=str(colors[0])) # text=red,color=black aaya
    scoreLabel.config(text="Score: "+str(score))
def RestartGame3():
    global timeleft
    global score
    score=0
    timeleft=30
    if timeleft ==0:
        messagebox.showinfo("Time Left","Time khatam ho gya!! Khatam tata bye bye Your score is:"+str(score))
    if timeleft > 0:
        timeleft-=1
        timeLabel.config(text="Time Left:"+str(timeleft))
        timeLabel.after(1000,countdown)
    scoreLabel.config(text="Score: "+str(score),bg="#800000",fg="yellow")

#window
frame4_title=Label(frame4,text="Color Game",font=("Aerial",20),bg="Green")
frame4_title.pack()
frame4.configure(bg="#32CD32")

instructions=Label(frame4,text="Type the color of the words,and not the word text!",font=("Aerial",20),bg="#191970",fg="yellow",borderwidth=1)
instructions.pack()

instructions2=Label(frame4,text="Hover from mouse from main to current window to change question",font=("Aerial"),bg="#191970",fg="yellow",borderwidth=1)
instructions2.pack()
scoreLabel=Label(frame4,text="Hover towards the window name to change question",font=("san-serif",12))
scoreLabel.pack()

timeLabel=Label(frame4,text="Time Left:"+str(timeleft),font=("san-serif",12),bg="#800000",fg="yellow")
timeLabel.pack()

label=Label(frame4,font=("Helvetica",60))
label.pack()

frame4_btn=Button(frame4,text="Back",command=lambda:show_frame(frame1),bg="#556B2F",fg="yellow",font=("Aerial",20))
frame4_btn.place(x=600,y=340)

restartbutton3=Button(frame4,text="Restart",command=RestartGame3,bg="#008080",fg="Yellow",font=("Aerial",20))
restartbutton3.place(x=600,y=280)


e=tk.Entry(frame4)
frame4.bind("<Enter>",startGame)
e.pack()
e.focus_set()


#---------------------------Frame 5 Quiz Game---------------------------------------------------

questions = ["Which animal does not appear in the Chinese zodiac?","How many elements are there on the periodic table(most recently)?","What is the deadliest snake?","What animal is associated with ancient Egypt?","What is the highest-grossing video game franchise to date?"]
options = [['Dragon','Rabbit','Dog','Hummingbird','Hummingbird'],['112','118','119','120','118'],
           ['Python','Anaconda','Black Mamba','Viper','Black Mamba'],['Lion','Cat','Rabbit','Tortoise','Cat'],['Mario','Pokemon','Street Fighter','Run Race','Pokemon']]


frame = tk.Frame(frame5, padx=10, pady=10,bg='#fff')
question_label = tk.Label(frame,height=5, width=28,bg='grey',fg="#fff", 
                          font=('Verdana', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'


    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'


frame5_btn=Button(frame5,text="Back",command=lambda:show_frame(frame1),bg="blue",fg="yellow",font=("Aerial",20))
frame5_btn.place(x=300,y=500)

displayNextQuestion()
show_frame(frame1)

window.mainloop()