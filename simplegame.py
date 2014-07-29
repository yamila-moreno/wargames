BOARD = [
    ('o', 'x', ''),
    ('o', 'x', ''),
    ('', 'o', 'x'),
]

def there_is_a_winner(board):
    return False

def get_empty_squares(board):
    empty_squares = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if col == '':
                empty_squares.append((x,y))

    if empty_squares:
        return True, empty_squares

    return False, []

def play(board=BOARD):
    # make a move
    keep_playing, empty_squares = get_empty_squares(board)
    if keep_playing:
        print('Keep playing')
    else:
        if there_is_a_winner(board):
            print('there is a winner!')
        else:
            print('tie!')


if __name__ == "__main__":
    play(BOARD)
