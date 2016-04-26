"""$Id: tetrismod.py, 8c507338968c  makhtar $
Module for a simple command-line Tetris game, with a nontrivial implementation"""
import sys
from random import choice, randint

__author__ = "Makhtar Diouf <makhtar.diouf@gmail.com>"
dbgon = False

class Piece:
    """Model blocks that fall through the board"""

    def __init__(self, _p):
        self.p = _p
        # Coordinates
        self.x = 1
        self.y = 1
        # Width & Height
        self.w = len(_p[0])
        self.h = len(_p)
        self.ymax = 20
        self.xmax = 20

    # **** Operations on a piece, triggered after safety checks done by Tetris()
    def move_left(self):
        if self.x > 1:
            self.x -= 1
            return True
        return False

    def move_right(self):
        if (self.x + self.w + 1) < self.xmax:
            self.x += 1
            return True
        return False

    def rotate_left(self):
        """Rotate 90 deg counter clockwise if ending within the grid,
            self.p[0][0] is the reference point for the rotation
            """
        _p = [list(reversed(r)) for r in self.p]
        _p = [list(r) for r in zip(*_p)]
        width = len(_p[0])

        if (self.x + width) < self.xmax:
            self.p = _p
            self.w = width
            self.h = len(_p)
            #self.y -= 1
            return True

        return False

    def rotate_right(self):
        """Rotate 90 deg clockwise if ending within the grid,
            self.p[0][0] is the reference point for the rotation
            """
        _p = [list(r) for r in zip(*self.p)]
        _p = [list(reversed(r)) for r in _p]
        width = len(_p[0])

        # if ((self.x - width) > 0) and (
        if (self.x + width) < self.xmax:
            self.p = _p
            self.w = width
            self.h = len(_p)
            return True

        return False


# ****** *******
class Tetris:
    """Model the board and its operations"""

    def __init__(self, rows=20, cols=20):
        self.msg = ""
        self.nRows = rows
        self.nCols = cols
        self.board = [["*"] * self.nRows for j in range(cols)]
        self.pieces_list = []
        self.kopts = {'a': "move left", 'd': "move right",
                      'w': "rotate left ->>", 's': "rotate right = clockwise <<-"}

        # Pieces shapes
        type1 = [[1, 1, 1, 1]]
        type2 = [[1, 0], [1, 0], [1, 1]]
        type3 = [[0, 1], [0, 1], [1, 1]]
        type4 = [[0, 1], [1, 1], [1, 0]]
        type5 = [[1, 1], [1, 1]]

        self.shapes = ([Piece(type1), Piece(type2), Piece(type3),
                        Piece(type4), Piece(type5)])

    def init_board(self):
        """Prepare the default board """
        for i in range(0, self.nRows):
            for j in range(0, self.nCols):
                if (j == 0) or (j == self.nCols - 1):
                    self.board[i][j] = "*"
                elif i != (self.nRows - 1):
                    self.board[i][j] = " "

    def draw_board(self):
        """ Redraw the board once filled """
        for i in range(0, self.nRows):
            sys.stdout.write("\t {0:3} ".format(i))
            for j in range(0, self.nCols):
                sys.stdout.write(self.board[i][j])
            sys.stdout.write("\n")

    def fill_board(self):
        """Fill parts of the board where pieces should be drawn"""
        print("Pieces: ", len(self.pieces_list))
        if dbgon:
            print("Current piece: ", self.pieces_list[-1].p, "\n")

        try:
            for piece in self.pieces_list:
                # Start from the location of each piece
                i = piece.y
                j = piece.x
                p = piece.p
                for k in range(len(p)):
                    for m in range(len(p[k])):
                        if p[k][m] == 1:
                            self.board[i][j] = "*"

                        # Don't clear an occupied cell
                        elif self.board[i][j] != "*":
                            self.board[i][j] = " "
                        j += 1

                    i += 1
                    # Backtrack to this piece's 1st column
                    if j - piece.w > 0:
                        j -= piece.w

        finally:
            self.draw_board()
            return self.board

    def add_piece(self):
        """Randomly add next piece to operate on"""
        piece = choice(self.shapes)
        # Pad
        piece.x = randint(1, self.nCols - piece.w - 2)
        piece.y = 0

        # Workaround pieces that get wrongfully rotated at the grid top
        detected = False
        for s in self.shapes:
            if piece.p != s.p:
                continue
            else:
                detected = True
                break

        tmp = [(1, 1, 0), (0, 1, 1)]
        if not detected or (piece.p == tmp):
            pass  # piece.rotate_right()

        self.pieces_list.append(piece)
        return piece

    def reset_piece(self, piece, restore=False):
        """Clear or restore the piece's current filling before showing it at its new position"""
        i = piece.y
        j = piece.x
        p = piece.p
        for k in range(len(p)):
            for m in range(len(p[k])):
                if dbgon:
                    print(locals())

                if j < (self.nCols - 1):
                    if restore and (p[k][m] == 1):
                        self.board[i][j] = "*"

                    # Avoid clearing an adjacent cell belonging to
                    # another piece
                    elif p[k][m] == 1:
                        self.board[i][j] = " "
                    j += 1

	    # Backtrack to 1st col
            if j - piece.w > 0:
                j -= piece.w
            if i < (self.nRows - 1):
                i += 1

        return self.board

    def can_move_down(self, piece):
        """ Check if the last row won't partly overlap with other pieces """
        try:
            for m in range(len(piece.p[-1])):
                if (piece.p[-1][m] == 1) and \
                        (self.board[piece.y + piece.h][piece.x + m] == "*"):
                    return False

        except IndexError:
            return False
        return True

    def can_move_left(self, piece):
        """Check if part of the 1st column won't bump on an occupied cell"""
        try:
            for k in range(len(piece.p)):
                if (piece.p[k][0] == 1) and (
                        self.board[piece.y + k][piece.x - 1] == "*"):
                    return False

        except IndexError:
            return False
        return True

    def can_move_right(self, piece):
        """Check if part of the last column won't bump on an occupied cell"""
        try:
            for k in range(len(piece.p)):
                if (piece.p[k][-1] == 1) and (self.board[piece.y + k]
                                              [piece.x + piece.w] == "*"):
                    return False

        except IndexError:
            return False
        return True

    def can_rotate_left(self, piece):
        """Check if not overlapping on target destination"""       
        return self.can_move_right(piece) and self.can_move_down(piece)

    def can_rotate_right(self, piece):
        """Check if clockwise rotation won't overlapping on target destination"""
        return self.can_move_left(piece) and self.can_move_down(piece)
