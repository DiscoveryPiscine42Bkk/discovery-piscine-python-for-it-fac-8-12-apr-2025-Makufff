from checkmate import checkmate
import sys

if __name__ == "__main__":

    files = [f for f in sys.argv[1:] if f.endswith(".chess")]
    
    if files:
        for file_name in files:
            with open(file_name, 'r') as f:
                board_str = f.read()
                checkmate(board_str)
