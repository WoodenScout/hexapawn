from enum import Enum
from tile import Tile

DEBUG = 0

class Color(Enum):
    BLACK = -1
    RED = 1

class Piece:
    def __init__(self, pos: tuple[int, int], color: Color, board):
        self.pos = pos
        self.color = color
        self.board = board

    def move(self, tile: Tile) -> bool:
        """ Moves the pawn to the specified tile if applicable, returns True if move was applicable, returns False otherwise """
        valid_moves = self.valid_moves()
        valid_takes = self.valid_takes()
        move = (tile.y_index - self.pos[0], tile.x_index - self.pos[1]) # (row, col)
        if DEBUG == 5: print(f'pos: {self.pos[0], self.pos[1]}')
        if DEBUG == 5: print(f'move: {move[0], move[1]}')

        if DEBUG == 5: print(f'valid moves: {valid_moves}')
        if DEBUG == 5: print(f'valid takes: {valid_takes}')
        if move in self.valid_moves():
            prev = self.board.get_tile_from_pos(self.pos[1], self.pos[0])
            self.pos = (tile.y_index, tile.x_index)
            prev.piece = None
            tile.piece = self
            self.board.selected_piece = None
            return True

        if move in valid_takes:
            prev = self.board.get_tile_from_pos(self.pos[1], self.pos[0])
            self.pos = (tile.y_index, tile.x_index)
            prev.piece = None
            tile.piece = self
            self.board.selected_piece = None
            return True

        else:
            self.board.selected_piece = None
            return False