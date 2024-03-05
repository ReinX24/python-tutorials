from operator import le


def isValidChessBoard(board_dict):
    spaces = [
        "1a",
        "2a",
        "3a",
        "4a",
        "5a",
        "6a",
        "7a",
        "8a",
        "1b",
        "2b",
        "3b",
        "4b",
        "5b",
        "6b",
        "7b",
        "8b",
        "1c",
        "2c",
        "3c",
        "4c",
        "5c",
        "6c",
        "7c",
        "8c",
        "1d",
        "2d",
        "3d",
        "4d",
        "5d",
        "6d",
        "7d",
        "8d",
        "1e",
        "2e",
        "3e",
        "4e",
        "5e",
        "6e",
        "7e",
        "8e",
        "1f",
        "2f",
        "3f",
        "4f",
        "5f",
        "6f",
        "7f",
        "8f",
        "1g",
        "2g",
        "3g",
        "4g",
        "5g",
        "6g",
        "7g",
        "8g",
        "1h",
        "2h",
        "3h",
        "4h",
        "5h",
        "6h",
        "7h",
        "8h",
    ]

    colors = ["w", "b"]
    roles = ["pawn", "knight", "bishop", "rook", "queen", "king"]

    wking = 0
    bking = 0
    piece_count = 0
    wpawns = 0
    bpawns = 0

    for k, v in board_dict.items():
        if k not in spaces:
            print("Invalid Position Error")
            return False
        elif v[0] not in colors:
            print("Color Error")
            return False
        elif v[1:] not in roles:
            return False
        elif v == "wking":
            wking += 1
            if wking > 1:
                print("White King Error")
                return False
        elif v == "bking":
            bking += 1
            if bking > 1:
                print("Black King Error")
                return False
        elif piece_count > 16:
            print("Piece Count Error")
        elif v == "wpawn":
            wpawns += 1
            if wpawns > 8:
                print("White Pawn Error")
                return False
        elif v == "bpawn":
            bpawns += 1
            if bpawns > 8:
                print("Black Pawn Error")
                return False

        piece_count += 1

    return True


if __name__ == "__main__":
    exampleOne = {
        "1h": "bking",
        "6c": "wqueen",
        "2g": "bbishop",
        "5h": "bqueen",
        "3e": "wking",
    }
    print(isValidChessBoard(exampleOne))
