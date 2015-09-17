def Chess(configuration, player):
  for element in configuration:

    # Extracted elements of input.
    color = element[0]
    piece = element[1]
    letterPos = element[2]
    numPos = element[3]

    # Next position variables.
    newletterPos = letterPos
    newnumPos = numPos

    # Formatted strings for print statements.
    prevPos = " <" + letterPos + ":" + str(numPos) + ">"  
    stringsentence = piece + " at" + prevPos + " can move to"

    # Checks if a given position is empty or not. If occupied, returns the color of the piece that occupies the position.
    def emptyPosition(configuration, givenletPos, givennumPos):
      for element in configuration:
        currentcolorPos = element[0]
        currentletPos = element[2]
        currentnumPos = element[3]

        if(currentletPos == givenletPos) and (currentnumPos == givennumPos): 
          return currentcolorPos
          break

    # Checks if the given piece can move to the new position. If True, prints out possible move.
    def movePiece(piece, newletterPos, newnumPos):

      # Bounded by A - H, and 1 - 8 inclusive.
      if (65 <= ord(newletterPos) <= 72) and (1 <= newnumPos <= 8): 

        # Piece can be moved if the given coordinates are empty.
        if (emptyPosition(configuration, newletterPos , newnumPos) == None) :
          print(stringsentence + " <" + newletterPos + ":" + str(newnumPos) + ">")
          return True

        # Piece can be moved if the given coordinates are not empty BUT occupied by a different color piece. 
        if (emptyPosition(configuration, newletterPos , newnumPos) != None) and (emptyPosition(configuration, newletterPos, newnumPos) != color):
          print(stringsentence + " <" + newletterPos + ":" + str(newnumPos) + ">")
          return emptyPosition(configuration, newletterPos , newnumPos)


    if piece == "Pawn":
      # Pawn may move one position up.
      if movePiece(piece, letterPos, numPos + 1) == True:
        # Pawn may only move two positions up if it can move one position up.
        movePiece(piece, letterPos, numPos + 2)

      # Pawn may move diagonally iff the diagonal spot is occupied by an opponent's piece,
      if emptyPosition(configuration, chr(ord(letterPos) + 1), numPos + 1) != None:
        # Pawn may move right diagonally.
        movePiece(piece, chr(ord(letterPos) + 1), numPos + 1)

      if emptyPosition(configuration, chr(ord(letterPos) - 1), numPos + 1) != None:
        # Pawn may move left diagonally.
        movePiece(piece, chr(ord(letterPos) - 1), numPos + 1)


    elif piece == "Bishop":

      # Bishop can move right and up diagonally. 
      newletterPos = chr(ord(letterPos) + 1)
      newnumPos = numPos + 1
      while movePiece(piece, newletterPos, newnumPos) == True:
        newletterPos = chr(ord(newletterPos) + 1)
        newnumPos += 1

      # Bishop can move right and down diagonally.
      newletterPos = chr(ord(letterPos) + 1)
      newnumPos = numPos - 1
      while movePiece(piece, newletterPos, newnumPos) == True:
        newletterPos = chr(ord(newletterPos) + 1)
        newnumPos -= 1
  
      # Bishop can move left and up diagonally.
      newletterPos = chr(ord(letterPos) - 1)
      newnumPos = numPos + 1
      while movePiece(piece, newletterPos, newnumPos) == True:
        newletterPos = chr(ord(newletterPos) - 1)
        newnumPos += 1

      # Bishop can move left and down diagonally.
      newletterPos = chr(ord(letterPos) - 1)
      newnumPos = numPos - 1
      while movePiece(piece, newletterPos, newnumPos) == True:
        newletterPos = chr(ord(newletterPos) - 1)
        newnumPos -= 1


    elif piece == "Rook":
    
      # Rook may move up mutiple spaces.
      newletterPos = letterPos
      newnumPos = numPos + 1
      while movePiece(piece, newletterPos, newnumPos) == True:
        newnumPos += 1
      
      # Rook may move down multiple spaces.
      newletterPos = letterPos
      newnumPos = numPos - 1
      while movePiece(piece, newletterPos, newnumPos) == True:
        newnumPos -= 1

      # Rook may move right multiple spaces.
      newletterPos = chr(ord(letterPos) + 1)
      newnumPos = numPos
      while movePiece(piece, newletterPos , newnumPos) == True:
        newletterPos = chr(ord(newletterPos) + 1)
      
      # Rook may move left multiple spaces.
      newletterPos = chr(ord(letterPos) - 1)
      newnumPos = numPos
      while movePiece(piece, newletterPos , newnumPos) == True:
        newletterPos = chr(ord(newletterPos) - 1)

    # King may move one space in any direction.
    elif piece == "King":

      # Up.
      movePiece(piece, letterPos, numPos + 1)

      # Diagonally right and up.
      movePiece(piece, chr(ord(letterPos) + 1), numPos + 1)

      # Right.
      movePiece(piece, chr(ord(letterPos) + 1), numPos)

      # Diagonally right and down.
      movePiece(piece, chr(ord(letterPos) + 1), numPos - 1)

      # Down.
      movePiece(piece, letterPos, numPos - 1)

      # Diagonally left and down.
      movePiece(piece, chr(ord(letterPos) - 1), numPos - 1)

      # Left.
      movePiece(piece, chr(ord(letterPos) - 1), numPos)

      # Diagonally left and up.
      movePiece(piece, chr(ord(letterPos) - 1), numPos + 1)


def main():
  
  print("Pawn Test Cases:")
  Chess([["White","Pawn", "B", 3], ["Black", "Pawn", "E", 6]], "White") 
  Chess([["White","Pawn", "B", 3], ["White", "Pawn", "E", 6]], "White") 
  Chess([["White","Pawn", "B", 3], ["Black", "Pawn", "E", 7]], "White") 
  Chess([["White","Pawn", "D", 4], ["Black", "Pawn", "D", 5]], "White")
  Chess([["White","Pawn", "D", 4], ["Black", "Pawn", "D", 5]], "White")
  Chess([["White","Pawn", "D", 4], ["Black", "Knight", "C", 5]], "White")  
  print (" ")
  
  print("Bishop Test Cases:")
  Chess([["White","Bishop", "D", 2], ["Black", "Bishop", "G", 5]], "White")
  Chess([["White","Bishop", "D", 2], ["White", "Bishop", "G", 5]], "White")
  print(" ")

  print("Rook Test Cases:")
  Chess([["White","Rook", "F", 3], ["Black", "Pawn", "F", 6]], "White") 
  Chess([["White","Rook", "F", 3], ["White", "Bishop", "F", 6]], "White")
  Chess([["White","Rook", "G", 6], ["White", "Bishop", "F", 1]], "White")
  Chess([["White","Rook", "G", 6], ["White", "Bishop", "H", 6]], "White")
  Chess([["White","Rook", "G", 6], ["Black", "Bishop", "H", 6]], "White")
  Chess([["White","Rook", "G", 6], ["Black", "Pawn", "B", 6]], "White")
  print(" ")

  print("King Test Cases:")
  Chess([["White","King", "D", 2], ["Black", "Pawn", "G", 5]], "White")
  Chess([["White","King", "D", 2], ["White", "Pawn", "D", 3]], "White")
  Chess([["White","King", "D", 2], ["Black", "Pawn", "D", 3]], "White")
  print(" ")

main()





