WHITE, BLACK = ' ', '#'



def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for _ in range(int(size/2)):
        pattern = WHITE + BLACK
        print(pattern * int(size/2))
        pattern = BLACK + WHITE
        print(pattern * int(size/2))