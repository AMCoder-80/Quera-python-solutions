class Piece:
    def __init__(self, sort, color, position):
        self.sort = sort
        self.color = color
        self.position = position
    

class Board():
    def __init__(self):
        self.position = {
            (10, 10): Piece('K', 'black', (10, 10)),
            (-10, -10): Piece('K', 'white', (-10, -10)),
            }

    def add(self, piece):
        if piece.sort != 'K' and piece.position not in self.position.keys():
            self.position[piece.position] = piece
        else:
            print('invalid query')

    def remove(self, position):
        if position in self.position.keys() and self.position[position].sort != 'K':
            del self.position[position]
        else:
            print('invalid query')

    def move(self, piece, position2):
        if self.position[piece.position] == piece:
            if position2 not in self.position.keys() or \
                    (self.position[position2].sort == 'P' and self.position[position2].color != piece.color):
                del self.position[piece.position]
                self.position[position2] = piece
            else:
                print('invalid query')
        else:
            print('invalid query')

    def is_mate(self, color):
        king = self.position[list(filter(lambda x: 
            self.position[x].color == color and self.position[x].sort == 'K', self.position))[0]]
        
        for col in range(king.position[0]-8, king.position[0]+9):
            for row in range(king.position[1]-8, king.position[1]+9):
                if (col, row) in self.position.keys():
                    if self.position[(col, row)].sort == 'P' and \
                        self.position[(col, row)].color != king.color:
                            return True
        return False

