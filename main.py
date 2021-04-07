#Chess move advisor for CMPSC 445
#Authors: Jason Ayling, Evan Green, Mis Champa, Nicholas Gahman
#Date: 04/07/2021


#Notation:
  #King = K, Queen = Q, Bishop = B, Knight = N, Rook = R, Pawn = no notation
  #Checkmate is denoted with either “++” or “#”
  #Castling kingside (with the rook that begins on the “h” file), is written as “0-0”. Castling queenside (with the rook that 
  #begins on the “a” file) is notated with “0-0-0”.
  #A 'check' is denoted with ++ or #
  #If a pawn makes it all the way to the end of the board to promote to a new piece, add a “=” symbol
  

#import chess
#import numpy as np
#import pandas as pd
# Keras is to create the Neural Network.
#from tensorflow import keras
#from tensorflow.keras import layers

#df = pd.read_fwf('chess_data.txt')
#data = df['moves'].tolist()[:500]
#split_data = []
#indice = 500
sandbox()