import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(suppress=True)

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
P8 - PAWN8
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
  
TESTBOARD = np.array([ # USING IDEAL PIECE PLACEMENT
  [0, 0, 0, "P4", "P5", 0, 0, 0],
  [0, 0, "P3", 0, "K1", 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, "R1", 0, 0, 0, 0],
  ["KG", "B1", 0, 0, "Q", 0, "B2", "K2"],
  [0, 0, 0, 0, 0, "R2", 0, 0],
  ["P1", "P2", 0, 0, 0, "P6", "P7", "P8"],
  [0, 0, 0, 0, 0, 0, 0, 0]
  ])
  
NUMBER_MAPPING = { # USING IDEAL NUMBER MAPPING
  "P6":2,
  "P5":3,
  "P4":5, 
  "P7":7,
  "P8":11,
  "P3":13, 
  "P2":17,
  "P1":19,
  "K2":23,
  "KG":29,
  "K1":31,
  "B1":37,
  "B2":41,
  "Q":43, 
  "R1":47,
  "R2":53
}

# if using both sets of pieces (black and white), separate into distinct boards and invert the one with pieces at the top
def compute_moves(board): 
  move_set = {}
  for i,r in enumerate(board):
    for j,c in enumerate(r):
      if c != "0":
        
        move_set[c] = []
        #move_set[c].append((i,j))
        
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
  

def generate_random_board(board, move_set):
  from random import choice
  
  while True:
    piece = choice(list(move_set.keys()))
    
    if move_set[piece] != []:  
      move = choice(move_set[piece])
      break
    
  for i,r in enumerate(board):
    for j,c in enumerate(r):
      if c == piece:
        board[i][j] = "0"
        board[move[0]][move[1]] = piece
        print(f"Moved: {piece}; To: {move}")
        return board
  
  return board


def get_rgb_matrix(matrix):
    rgb_matrix = []
    for i,r in enumerate(matrix):
        row = []
        for j,c in enumerate(r):
            value = matrix[i][j]
            if value == 1:
                row.append((0,0,0))
            elif value > 1 and value <= 100:
                row.append((int(value)+100,0,0))
            elif value > 100 and value < 1000:
                row.append((0,int(value)%255,0))
            elif value >= 1000:
                row.append((0, 0, int(value)%255))
        rgb_matrix.append(row)
    return rgb_matrix

  
def random_pixelated_tests():
  arrays = []
  for x in range(0, 100):
    moves = compute_moves(DEFAULT_BOARD)
    generated_prod = generate_prod_board(moves)
    arrays.append(get_rgb_matrix(generated_prod))
    DEFAULT_BOARD = generate_random_board(DEFAULT_BOARD, moves)
  
  # saves board changes into gif 
  from celluloid import Camera
  
  fig = plt.figure()
  camera = Camera(fig)
  for a in arrays:
      plt.imshow(a, interpolation='nearest')
      camera.snap()
  anim = camera.animate()
  anim.save('im.gif')
  
# question: how can we find similar/equal boards with different piece placements/number mappings?

# 1. is there a number mapping that makes two product boards equal?
# 2. can that be done without using a different number of pieces?
# 3. same number mapping?
# 4. how can we know the max achievable value given some number mapping?


# 5. what is the board and mapping pair which yields the greatest values in the product matrix?
# can be broken down into two questions:
# a) given a set of pieces, what is the mapping to the set of positions that yields the greatest number of intersections between the posible moves set of each piece?
# b) what is the number mapping that produces the greatest products? (has to depend on the previous question...)
# regarding possible movements, we are checking for the greatest number of intersections between lines... (geometry?); we may also verify if an arrangement is possible
# any specific sequence for increasing (prime) ordered number mappings?

print(generate_prod_board(compute_moves(TESTBOARD)))
