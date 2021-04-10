#!/usr/bin/env python
# coding: utf-8
#King = K, Queen = Q, Bishop = B, Knight = N, Rook = R, Pawn = no notation.
#Capturing an enemy piece sees an “x” placed between the piece moved and the square the captured piece was upon.
#When the opponent’s king is threatened by check, a “+” sign is added to the end of the notation.
#Checkmate is denoted with either “++” or “#”
#From left-to-right the squares are ordered alphabetically with letters from “a” through to “h”.
#Additionally, Each square also gets a unique number, from “1” to “8”. 
#Castling kingside (with the rook that begins on the “h” file), is written as “0-0”. 
#Castling queenside (with the rook that begins on the “a” file) is notated with “0-0-0”.
#If a pawn makes it all the way to the end of the board to promote to a new piece, add a “=” symbol

# In[1]:


import chess
import re
import csv


# In[2]:


board = chess.Board()
print("insert a legal move using chess notation: ")
while True:
    x=input("insert a legal move: ")
    try:
        board.push_san(x)
    except:
        print("That is not a legal move.")
    y=input("Continue? (Y/N): ")
    if y == "N":
        break
print(board.board_fen())


# In[3]:


#Base chess board
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
#Chess board after e4 Nf6 Nf3 Nxe4
#rnbqkb1r/pppppppp/8/8/4n3/5N2/PPPP1PPP/RNBQKB1R
#Chess board after e4 Nf6 Nf3 Ng4
#nbqkb1r/pppppppp/8/8/4P1n1/5N2/PPPP1PPP/RNBQKB1R
#Chess board after e4 e5 Nf3 Nc6
#r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R


# In[4]:


database = open("2016_CvH.csv",'r')


# In[5]:


boardmoves = board.ply()
boardtest = board.board_fen()
text = database.read()


# In[6]:


a = text.split()
print(len(a))
print(a[:200])


# In[7]:


totalwhitewins = 0
totalblackwins = 0
totaldraws = 0
play = False
moves = -1
board2 = chess.Board()
for i in range(len(a)):
    if a[i] == '[Result':
        whitewins=0
        blackwins=0
        draws=0
        if a[i+1] == '"1-0"]':
            whitewins+=1
        elif a[i+1] == '"0-1"]':
            blackwins+=1
        else:
            draws+=1
    if play:
        moves -= 1
        try:
            board2.push_san(a[i])
        except:
            #meaningless instruction necessary for except block to work
            j = 'j'
            
    if a[i] == '1.':
        play = True
        moves = boardmoves + (boardmoves // 2)
    if moves == 0 or ('{' in a[i]):
        play = False
        if (board2.board_fen() == boardtest):
            
            totalwhitewins += whitewins
            totalblackwins += blackwins
            totaldraws += draws
        whitewins=0
        blackwins=0
        draws=0 
        board2 = chess.Board()
        moves = -1

        
print("Total wins for white in inputted position:", totalwhitewins)
print("Total wins for black in inputted position:",totalblackwins)
print("Total draws in current position:", totaldraws)


# In[8]:


if ((totalwhitewins > totalblackwins) & (totalwhitewins > totaldraws)):
    print("White is winning in the inputted position")
elif ((totalblackwins > totalwhitewins) & (totalblackwins > totaldraws)):
    print("Black is winning in the inputted position")
elif ((totaldraws > totalblackwins) & (totaldraws > totalwhitewins)):
    print("The inputted position is drawish")
else:
    print("Inconclusive")


# In[ ]:




