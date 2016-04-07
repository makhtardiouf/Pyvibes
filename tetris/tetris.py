#!/usr/bin/env python3
"""$Id: tetris.py, 8c507338968c  makhtar $
 Simple command-line Tetris game

 Usage: python3 tetris.py
 Quick autotest: python3 tetris.py < tetris-input.txt
"""
import os
from tetrismod import *
#from makhtar import utils

__author__ = "Makhtar Diouf <makhtar.diouf@gmail.com>"

#@utils.do_cprofile
def run_game_loop():
    """ Run the game """
    t = Tetris()
    t.init_board()

    # Current piece to operate on
    piece = t.add_piece()
    infomsg = "\n"

    while True:
        # Clear the screen and redraw
        os.system('cls' if os.name == 'nt' else 'clear')
        t.fill_board()

        print(infomsg)
        if dbgon:
            print(t.msg)

        # Commands
        for k in sorted(t.kopts):
            print(k, ":", t.kopts[k])

        key = input("q : quit or 'Enter': continue >  ")
        if key == 'q':
            print("Goodbye~")
            exit()

        # Operations
        pchanged = False
        t.board = t.reset_piece(piece)

        if key == 'a' and t.can_move_left(piece):
            pchanged = piece.move_left()

        elif key == 'd' and t.can_move_right(piece):
            pchanged = piece.move_right()

        elif key == 'w' and t.can_rotate_left(piece):
            pchanged = piece.rotate_left()

        elif key == 's' and t.can_rotate_right(piece):
            pchanged = piece.rotate_right()

        # Enter key just continues
        elif not key:
            pchanged = True

        if pchanged:
            infomsg = ""
        else:
            try:
                infomsg = "\n\tThis block cannot " + \
                    str(t.kopts[key]).upper() + " '" + key + "'\n"

            except KeyError:
                infomsg = str("\n\tInvalid option: '").upper() + key + "'\n"
            continue

        if t.can_move_down(piece):
            piece.y += 1

        # Piece blocked at the top
        elif piece.y == 0:
            print("\n\t*** Game over~")
            # Avoid abrupt closure on windows
            input("Press any key to exit\n")
            exit()

        else:
            t.reset_piece(piece, restore=True)
            piece = t.add_piece()


# main
try:
    run_game_loop()

except Exception:
    print("Unexpected error:")
    raise
