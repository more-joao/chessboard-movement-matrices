import numpy as np

'''
K1 - KNIGHT1
K2 - KNIGHT2
R1 - ROOK1
R2 - ROOK2
B1 - BISHOP1
B2 - BISHOP2
Q - QUEEN
P1 - PAWN1
P2 - PAWN2
P3 - PAWN3
P4 - PAWN4
P5 - PAWN5
P6 - PAWN6
P7 - PAWN7
P8 - PAWN18
KG - KING
'''

DEFAULT_BOARD = np.array([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
  ["R1", "K1", "B1", "Q", "KG", "B2", "K2", "R2"]
  ])
  
TESTBOARD = np.array([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, "Q", 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, "KG", 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, "K1", 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, "R1", 0, 0, 0, 0, 0, 0]
  ])
  
NUMBER_MAPPING = {
  "K1":2,
  "K2":3,
  "R1":5, 
  "R2":7,
  "B1":11,
  "B2":13, 
  "Q":17,
  "P1":19,
  "P2":23,
  "P3":29,
  "P4":31,
  "P5":37,
  "P6":41,
  "P7":43, 
  "P8":47,
  "KG":53
}

# if using both sets of pieces (black and white), separate into distinct boards and invert the one with pieces at the top
def compute_moves(board): 
  move_set = {}
  for i,r in enumerate(board):
    for j,c in enumerate(r):
      if c != "0":
        
        move_set[c] = []
        
        # PAWN MOVEMENT CHECK
        if "P" in c:
          try:
            if board[i-1][j] == "0": # does not consider two-square movement for pawns
              move_set[c].append((i-1,j))
          except:
            pass
          
        # ROOK MOVEMENT CHECK
        elif "R" in c:
          try:
            for x in range(1,8):
              if board[i][j+x] == "0":
                move_set[c].append((i, j+x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i][j-x] == "0" and j>=x:
                move_set[c].append((i, j-x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i+x][j] == "0":
                move_set[c].append((i+x, j))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i-x][j] == "0" and i>=x:
                move_set[c].append((i-x, j))
              else:
                raise Exception()
          except:
            pass
          
        # BISHOP MOVEMENT CHECK
        elif "B" in c:
          try:
            for x in range(1,8):
              if board[i+x][j+x] == "0":
                move_set[c].append((i+x, j+x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i+x][j-x] == "0" and j>=x:
                move_set[c].append((i+x, j-x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i-x][j-x] == "0" and i>=x and j>=x:
                move_set[c].append((i-x, j-x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i-x][j+x] == "0" and i>=x:
                move_set[c].append((i-x, j+x))
              else:
                raise Exception()
          except:
            pass
        
        # KING MOVEMENT CHECK
        elif "KG" in c:
          try:
            if board[i][j+1] == "0":
              move_set[c].append((i, j+1))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i][j-1] == "0" and j>=1:
              move_set[c].append((i, j-1))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i+1][j] == "0":
              move_set[c].append((i+1, j))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i-1][j] == "0" and i>=1:
              move_set[c].append((i-1, j))
            else:
              raise Exception()
          except:
            pass
            
          
        # QUEEN MOVEMENT CHECK
        elif "Q" in c:
          try:
            for x in range(1,8):
              if board[i+x][j+x] == "0":
                move_set[c].append((i+x, j+x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i+x][j-x] == "0" and j>=x:
                move_set[c].append((i+x, j-x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i-x][j-x] == "0" and i>=x and j>=x:
                move_set[c].append((i-x, j-x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i-x][j+x] == "0" and i>=x:
                move_set[c].append((i-x, j+x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i][j+x] == "0":
                move_set[c].append((i, j+x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i][j-x] == "0" and j>=x:
                move_set[c].append((i, j-x))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i+x][j] == "0":
                move_set[c].append((i+x, j))
              else:
                raise Exception()
          except:
            pass
          
          try:
            for x in range(1,8):
              if board[i-x][j] == "0" and i>=x:
                move_set[c].append((i-x, j))
              else:
                raise Exception()
          except:
            pass
        
        # KNIGHT MOVEMENT CHECK
        else:
          try:
            if board[i-1][j-2] == "0" and i>=1 and j>=2:
              move_set[c].append((i-1, j-2))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i-2][j-1] == "0" and i>=2 and j>=1:
              move_set[c].append((i-2, j-1))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i-2][j+1] == "0" and i>=2:
              move_set[c].append((i-2, j+1))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i-1][j+2] == "0" and i>=1:
              move_set[c].append((i-1, j+2))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i+1][j+2] == "0":
              move_set[c].append((i+1, j+2))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i+2][j+1] == "0":
              move_set[c].append((i+2, j+1))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i+2][j-1] == "0" and j>=1:
              move_set[c].append((i+2, j-1))
            else:
              raise Exception()
          except:
            pass
          
          try:
            if board[i+1][j-2] == "0" and j>=2:
              move_set[c].append((i+1, j-2))
            else:
              raise Exception()
          except:
            pass
          
          
  return move_set


def generate_prod_board(move_set):
  # must adjust if not 8x8 board
  
  prod_board = np.ones((8, 8))
  
  for x in move_set:
    for pos in move_set[x]:
      prod_board[pos[0]][pos[1]] = prod_board[pos[0]][pos[1]]*NUMBER_MAPPING[x]
      
  return prod_board
  
print(generate_prod_board(compute_moves(TESTBOARD)))
  
# question: how can we find similar/equal boards with different piece placements/number mappings?

# 1. is there a number mapping that makes two product boards equal?
# 2. can that be done without using a different number of pieces?
# 3. same number mapping?

