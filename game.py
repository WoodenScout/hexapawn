from piece import Color

class Game:
    def __init__(self, board):
        self.winner = None
        self.board = board

    
    def count_pieces(self) -> int:
        """ Returns the number of black and red pieces on the board """
        reds, blacks = 0, 0
        for i in range(self.board.num_tiles):
            for j in range(self.board.num_tiles):
                tile = self.board.get_tile_from_pos(i, j)

                if tile.piece is None:
                    continue
                if tile.piece.color == Color.RED:
                    reds += 1
                if tile.piece.color == Color.BLACK:
                    blacks += 1

        return reds, blacks
    

    def no_moves(self) -> Color|None:
        """ Returns the RED if BLACK has no legal moves or BLACK if RED has no legal moves, None otherwise """
        all_moves = []
        for i in range(self.board.num_tiles):
            for j in range(self.board.num_tiles):
                tile = self.board.get_tile_from_pos(i, j)

                if tile.piece is not None and tile.piece.color == self.board.turn:
                    for move in tile.piece.valid_moves():
                        all_moves.append(move)
                    for take in tile.piece.valid_takes():
                        all_moves.append(take)
        if len(all_moves) == 0:
            return Color.BLACK if self.board.turn == Color.RED else Color.RED
        else:
            return None
        
    

    def check_last_rank(self) -> Color|None:
        """ Returns BLACK if a BLACK piece has reached the last rank, returns RED if a RED piece has reached the last rank, returns None otherwise """
        for i in range(self.board.num_tiles):
            first_row_tile = self.board.get_tile_from_pos(i, 0)
            last_row_tile = self.board.get_tile_from_pos(i, self.board.num_tiles - 1)

            if first_row_tile.piece is not None and first_row_tile.piece.color == Color.RED:
                return Color.RED
            
            if last_row_tile.piece is not None and last_row_tile.piece.color == Color.BLACK:
                return Color.BLACK
        return None
            

    def check_winner(self) -> bool:
        """ Returns True if any player has won, returns False otherwise """
        reds, blacks = self.count_pieces()
        last_row_winner = self.check_last_rank()
        if reds == 0 or blacks == 0:
            self.winner = Color.RED if reds > blacks else Color.BLACK
            return True
        elif (last_row_winner := self.check_last_rank()) is not None:
            self.winner = last_row_winner
            return True
        elif (no_move_winner := self.no_moves()) is not None:
            self.winner = no_move_winner
            return True
        else:
            return False
        

    def message(self):
        """ Prints out the winner """
        winner = 'Black' if self.winner == Color.BLACK else 'Red'
        print(f'Winner: {winner}')

                
