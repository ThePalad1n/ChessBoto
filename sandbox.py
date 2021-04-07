import chess

board = chess.Board()

board.legal_moves 
chess.Move.from_uci("a8a1") in board.legal_moves
False

board.push_san("e4")

board.push_san("e5")


board.is_checkmate()
True
