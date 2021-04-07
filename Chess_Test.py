#!/usr/bin/env python
# coding: utf-8

# In[3]:


import chess


# In[10]:


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


# In[8]:


#Base chess board
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
#Chess board after e4 Nf6 Nf3 Nxe4
#rnbqkb1r/pppppppp/8/8/4n3/5N2/PPPP1PPP/RNBQKB1R
#Chess board after e4 Nf6 Nf3 Ng4
#nbqkb1r/pppppppp/8/8/4P1n1/5N2/PPPP1PPP/RNBQKB1R
#Chess board after e4 e5 Nf3 Nc6
#r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R


# In[ ]:




