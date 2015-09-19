def Chess(configuration, player):
  for element in configuration:

    # Gives possible moves for the only the current player's pieces.
    color = element[0]
    if (color != player):
      
      # Extracted elements of input.
      piece = element[1]
      letterPos = element[2]
      numPos = element[3]

      # Next possible position.
      newletterPos = letterPos
      newnumPos = numPos

      # Formatted strings for print statements.
      prevPos = " <" + letterPos + ":" + str(numPos) + ">"  
      stringsentence = piece + " at" + prevPos + " can move to"

      # Checks if a given square is empty or not. If occupied, returns the color of the piece that occupies the square.
      def emptySquare(configuration, givenletPos, givennumPos):
        for element in configuration:
          currentcolorPos = element[0]
          currentletPos = element[2]
          currentnumPos = element[3]

          if(currentletPos == givenletPos) and (currentnumPos == givennumPos): 
            return currentcolorPos
            break

      # Checks if the given piece can move to the new square. If true, prints out the move.
      def movePiece(newletterPos, newnumPos):

        # Piece positions are bounded by A - H and 1 - 8, inclusive.
        if (65 <= ord(newletterPos) <= 72) and (1 <= newnumPos <= 8): 

          # Piece can be moved if the given coordinates are empty.
          if (emptySquare(configuration, newletterPos , newnumPos) == None) :
            print(stringsentence + " <" + newletterPos + ":" + str(newnumPos) + ">")
            return True

          # Piece can be moved if the given coordinates are not empty BUT occupied by a different color piece. 
          if (emptySquare(configuration, newletterPos , newnumPos) != None) and (emptySquare(configuration, newletterPos, newnumPos) != color):
            print(stringsentence + " <" + newletterPos + ":" + str(newnumPos) + ">")
            return emptySquare(configuration, newletterPos , newnumPos)

      # Will loop over movePiece to continue to check if a piece can move in a given direction.
      def loop(newletterPos, newnumPos, x, y): 

        # x affects letter direction, y moves affects the number direction.
        newletterPos = chr(ord(letterPos) + x)
        newnumPos = numPos + y

        while movePiece(newletterPos, newnumPos) == True:
          newletterPos = chr(ord(newletterPos) + x)
          newnumPos = newnumPos + y

      # Will call loop with all combinations of a given input array;
      def combinations(array):
        for x in array:
          for y in array:
            loop(newletterPos,newnumPos, x, y) 

      # Moves a piece in all four diagonal directions.
      def moveDiagonal():
        
        array = [ 1, -1]
        combinations(array)

      # Moves a piece in North, South, West, and East directions.
      def moveNSWE():
        
        loop(newletterPos, newnumPos, 0, 1)
        loop(newletterPos, newnumPos, 0, -1)
        loop(newletterPos, newnumPos, 1, 0)
        loop(newletterPos, newnumPos, -1, 0)
      

      if piece == "Pawn":
        
        # Pawn may move one square up.
        if movePiece(newletterPos, numPos + 1) == True:
          # Pawn may only move two squares up if it can move one square up.
          movePiece(newletterPos, numPos + 2)


        # Pawn may move diagonally iff the diagonal square is occupied by an opponent's piece,
        if emptySquare(configuration, chr(ord(letterPos) + 1), numPos + 1) != None:
          # Pawn may move right diagonally.
          movePiece(chr(ord(letterPos) + 1), numPos + 1)

        if emptySquare(configuration, chr(ord(letterPos) - 1), numPos + 1) != None:
          # Pawn may move left diagonally.
          movePiece(chr(ord(letterPos) - 1), numPos + 1)


      # Bishop may only move diagonally.
      elif piece == "Bishop":
        
        moveDiagonal()
      

      # Rook may only move North, South, East, West.
      elif piece == "Rook":

        moveNSWE()
      

      # Queen may move like a Bishop or Rook.
      elif piece == "Queen":

        moveNSWE()
        moveDiagonal()


      elif piece == "King":

        # King may move one square up.
        movePiece(letterPos, numPos + 1)

        # King may move one square down
        movePiece(letterPos, numPos - 1)

        # King may move one square left
        movePiece(chr(ord(letterPos) - 1), numPos)

        # King may move one square right.
        movePiece(chr(ord(letterPos) + 1), numPos)



        # King may move one square diagonally right and up.
        movePiece(chr(ord(letterPos) + 1), numPos + 1)

        # King may move one square right and down.
        movePiece(chr(ord(letterPos) + 1), numPos - 1)

        # King may move one square diagonally left and down.
        movePiece(chr(ord(letterPos) - 1), numPos - 1)

        # King may move one square diagonally left and up.
        movePiece(chr(ord(letterPos) - 1), numPos + 1)

      
      elif piece == "Knight":
        # 2 up, 1 right
        movePiece(chr(ord(letterPos) + 1), numPos + 2)

        # 2 up, 1 left
        movePiece(chr(ord(letterPos) - 1), numPos + 2)
        
        # 2 down, 1 right
        movePiece(chr(ord(letterPos) + 1), numPos - 2)
        
        # 2 down, 1 left
        movePiece(chr(ord(letterPos) - 1), numPos - 2)
        
        # 2 right, 1 up
        movePiece(chr(ord(letterPos) + 2), numPos + 1)
        
        # 2 right, 1 down 
        movePiece(chr(ord(letterPos) + 2), numPos - 1)
        
        # 2 left, 1 up
        movePiece(chr(ord(letterPos) - 2), numPos + 1)
        
        # 2 left, 1 down
        movePiece(chr(ord(letterPos) - 2), numPos - 1)


def main(): 
  
  print("Pawn Test Cases:")
  Chess([["White","Pawn", "B", 3], ["Black", "Pawn", "E", 6]], "Black") 
  Chess([["White","Pawn", "B", 3], ["White", "Pawn", "E", 6]], "Black") 
  Chess([["White","Pawn", "B", 3], ["Black", "Pawn", "E", 7]], "Black") 
  Chess([["White","Pawn", "D", 4], ["Black", "Pawn", "D", 5]], "Black")
  Chess([["White","Pawn", "D", 4], ["Black", "Pawn", "D", 5]], "Black")
  Chess([["White","Pawn", "D", 4], ["Black", "Knight", "C", 5]], "Black")  
  print (" ")

  print("Bishop Test Cases:")
  Chess([["White","Bishop", "D", 2], ["Black", "Bishop", "G", 5]], "Black")
  Chess([["White","Bishop", "D", 2], ["White", "Bishop", "G", 5]], "White")
  print(" ")

  print("Rook Test Cases:")
  Chess([["White","Rook", "F", 3], ["Black", "Pawn", "F", 6]], "Black") 
  Chess([["White","Rook", "F", 3], ["White", "Bishop", "F", 6]], "Black")
  Chess([["White","Rook", "G", 6], ["White", "Bishop", "F", 1]], "Black")
  Chess([["White","Rook", "G", 6], ["White", "Bishop", "H", 6]], "Black")
  Chess([["White","Rook", "G", 6], ["Black", "Bishop", "H", 6]], "Black")
  Chess([["White","Rook", "G", 6], ["Black", "Pawn", "B", 6]], "Black")
  print(" ")

  print("Queen Test Cases:")
  Chess([["White","Queen", "D", 2], ["Black", "Pawn", "G", 5]], "Black")
  Chess([["White","Queen", "D", 2], ["White", "Pawn", "G", 5]], "Black")
  print(" ")
  
  print("King Test Cases:")
  Chess([["White","King", "D", 2], ["Black", "Pawn", "G", 5]], "Black")
  Chess([["White","King", "D", 2], ["White", "Pawn", "D", 3]], "Black")
  
  Chess([["White","King", "D", 2], ["Black", "Pawn", "D", 3]], "Black")
  print(" ")

  print("Knight Test Cases:")
  Chess([["White","Knight", "D", 4], ["Black", "Pawn", "H", 1]], "White")
  Chess([["White","Knight", "D", 4], ["White", "Pawn", "E", 2]], "White")
  Chess([["White","Knight", "D", 4], ["Black", "Pawn", "E", 2]], "White")
  print(" ")
  
main()