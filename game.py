from tkinter import *
from PIL import Image, ImageTk
from random import randint



# main window
root=Tk()
root.title('Rock,Paper,Scissors')
root.configure(background='#9b59b6')

# picture
rock_image=ImageTk.PhotoImage(Image.open('rock.png'))
rock_image_comp=ImageTk.PhotoImage(Image.open('rock.png'))
paper_image=ImageTk.PhotoImage(Image.open('paper.png'))
paper_image_comp=ImageTk.PhotoImage(Image.open('paper.png'))
scissors_image=ImageTk.PhotoImage(Image.open('scissors.png'))
scissors_image_comp=ImageTk.PhotoImage(Image.open('scissors.comp.png'))

# insert picture
user_label= Label (root,image=scissors_image,background='#9b59b6')
comp_label=Label(root, image=scissors_image_comp,background='#9b59b6')
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=6)

# scores
PlayerScore= Label(root,text=0,font=100,background='#9b59b6', foreground='white')
computerScore= Label(root,text=0, font=100, background='#9b59b6', foreground='white')
computerScore.grid(row=1,column=1)
PlayerScore.grid(row=1,column=3)

# indicators
user_indicators=Label(root,text='USER', font=50, background='#9b59b6', foreground='white').grid(row=0,column=3)
comp_indicators=Label(root, text='COMPUTER', font=50, background='#9b59b6', foreground='white').grid(row=0,column=1)

# messages
msg=Label(root,font=80,background='#9b59b6', foreground='white')
msg.grid(row=3,column=2)

# updatemessage
def updatemessage(x):
    msg["text"]=x
# update user score
def updateUserScore():
    score=int(PlayerScore["text"])
    score+=1
    PlayerScore["text"]= str(score)

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner


def checkwinner(player,computer):
    if player == computer:
        updatemessage("Its is Tie !!!")
    elif player=='rock':
        if computer == 'paper':
            updatemessage("You Loose !!! ")
            updateCompScore()
        else:
            updatemessage("You Win !!!!")
            updateUserScore()
    elif player== 'paper':
        if computer == 'scissors':
            updatemessage("You Loose!!!")
            updateCompScore()
        else:
            updatemessage("You Win !!!")
            updateUserScore()
    elif player == 'scissors':
        if computer == 'rock':
            updatemessage("You Loose!!!")
            updateCompScore()
        else:
            updatemessage("You Win!!!")
            updateUserScore()
    else:
        pass
# update choices
choices=['rock','paper','scissors']


def updateChoice(x):
    # for computer
    CompChoice =choices[randint(0,2)]
    if CompChoice == 'rock':
        comp_label.configure(image=rock_image_comp)
    elif CompChoice == 'paper':
        comp_label.configure(image=paper_image_comp)
    else:
        comp_label.configure(image=scissors_image_comp)



    # for user
    if x=='rock':
        user_label.configure(image=rock_image)
    elif x=='paper':
        user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissors_image)
    checkwinner(x,CompChoice)


# button
rock= Button(root, width=20,height=2, text='Rock', background='#FF3E4D',foreground='white',borderwidth=10,command=lambda:updateChoice('rock'))
rock.grid(row=2,column=1)
paper=Button(root, width=20,height=2, text='Paper', background='#FF3E4D',foreground='white',borderwidth=10,command=lambda:updateChoice('paper'))
paper.grid(row=2,column=2)
scissor=Button(root, width=20,height=2, text='Scissors', background='#FF3E4D',foreground='white',borderwidth=10,command=lambda:updateChoice('scissors'))
scissor.grid(row=2,column=3)



root.mainloop()