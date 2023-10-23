from piece import Piece, Color
from tile import Tile
from pawn import Pawn, DEBUG

class Board:
    def __init__(self, turn:Color = Color.RED, board_size:int = 600, num_tiles=3, board: Color|None = None):
        self.turn = turn
        self.board_size = board_size
        self.num_tiles = num_tiles
        self.tile_size = self.board_size // self.num_tiles
        self.selected_piece = None

        if board is None:
            self.board = [[Color.BLACK for _ in range(self.num_tiles)]]
            for _ in range(self.num_tiles - 2):
                self.board.append([0 for _ in range(self.num_tiles)])
            self.board.append([Color.RED for _ in range(self.num_tiles)])
        else:
            self.board = board

        self.tiles_list = self._generate_tiles()

    def _generate_tiles(self):
        """ Creates a list of tiles for the board with the piece on the tiles according to self.board initialization """
        tiles_list = []
        for i in range(self.num_tiles):
            for j in range(self.num_tiles):
                new_tile = Tile(i, j, self.tile_size)
                if self.board[i][j] == Color.BLACK:
                    new_tile.piece = Pawn((i, j), Color.BLACK, self, self.tile_size)
                elif self.board[i][j] == Color.RED:
                    new_tile.piece = Pawn((i, j), Color.RED, self, self.tile_size)
                tiles_list.append(new_tile)
        return tiles_list


    def draw(self, display):
        """ Draws the board with the tiles and the piece one the tiles """
        for tile in self.tiles_list:
            tile.draw(display)
        
        if DEBUG >= 1 and self.selected_piece is not None: print(f'position of selected piece: {self.selected_piece.pos}')


    def get_tile_from_pos(self, x:int, y:int):
        """ Expects parameters: x/col, y/row 
            Returns the tile at position (row, col)"""
        for tile in self.tiles_list:
            if (tile.x_index, tile.y_index) == (x, y):
                return tile

    
    def handle_click(self, x, y):
        """ Highlights clicked tile, selects the piece on clicked tile if applicable, moves piece if applicable """
        x = x // self.tile_size
        y = y // self.tile_size
        clicked_tile = self.get_tile_from_pos(x, y)
        if DEBUG >= 2: print(f'clicked tile pos: {clicked_tile}')

        if DEBUG >= 2: print(f'clicked tile: {clicked_tile}')
        if DEBUG >= 2: print(f'selected piece: {self.selected_piece}')
        if DEBUG >= 2: print(f'clicked tile piece: {clicked_tile.piece}')
        if DEBUG >= 2: print(f'clicked tile piece color: {clicked_tile.piece}')
        if DEBUG >= 2: print(f'turn: {self.turn}')

        if self.selected_piece is None and clicked_tile.piece is not None and clicked_tile.piece == self.turn:
            self.selected_piece = clicked_tile.piece

        elif self.selected_piece is not None and self.selected_piece.move(clicked_tile):
            self.turn = Color.BLACK if self.turn == Color.RED else Color.RED

        elif clicked_tile.piece is not None and clicked_tile.piece.color == self.turn:
            self.selected_piece = clicked_tile.piece

        for tile in self.tiles_list:
            tile.highlight = False
        clicked_tile.highlight = True
