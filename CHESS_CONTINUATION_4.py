#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

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


# In[7]:

TotalGames = []
TotalGameAnswers = []
k = 1
play = False
End = False
moves = -1
board2 = chess.Board()
for i in (range(3,len(a))):
    if play:
        moves -= 1
        try:
            board2.push_san(a[i])
        except:
            #meaningless instruction necessary for except block to work
            j = 'j'
            
    if "White" in a[i] or "Black" in a[i] or "Draw" in a[i]:
        b = a[i].split(",")
        play = True
        moves = boardmoves + (boardmoves // 2)
        
    if moves == 0:
        play = False
        
        if ((board2.board_fen() == boardtest) and "1." not in a[i+k]):
            TotalGames.append([b[0],b[1]])
            TotalGameAnswers.append([b[3],a[i + k]])
        moves = -1
        End = False
        board2 = chess.Board()
        

        
df = pd.DataFrame(np.array(TotalGames),
                   columns = ['WhiteELO', 'BlackELO'])
dfAnswers = pd.DataFrame(np.array(TotalGameAnswers),
                        columns = ['Winner', 'NextMove'])
print(df)
print(dfAnswers)

# In[ ]:





# In[2]:


import pandas as pd
import numpy as np


# In[ ]:





# In[3]:


print(df)


# In[4]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# In[ ]:





# In[5]:


X_train, X_test, y_train, y_test = train_test_split(df, dfAnswers, test_size=0.3, random_state=42)


# In[6]:


scaler.fit(X_train)
print(X_train.min())
print(X_train.max())
ScaledData=scaler.transform(X_train)


# In[8]:


print(ScaledData.min())
print(ScaledData.max())


# In[ ]:




