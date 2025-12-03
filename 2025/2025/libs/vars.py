

def dirs(right, up, left, down):
    return {right: (1, 0), left: (-1, 0), up: (0, -1), down: (0, 1)}


def letters():
    _ret = {}
    
    for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
        _ret[letter] = i
        _ret[i] = letter
    
    return _ret

