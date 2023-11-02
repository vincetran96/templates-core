from typing import List, Set


def print_moves(
    pieces: List[int],
    current_tower: str,
    destination_tower: str, 
    towers: Set[str]
):
    if len(pieces) == 1:
        print(
            f"Move {pieces[0]} from {current_tower} to {destination_tower}")
    else:
        print_moves(
            pieces[:-1],
            current_tower,
            (towers - {current_tower, destination_tower}).pop(),
            towers
        )
        print_moves(
            pieces[-1:],
            current_tower,
            destination_tower,
            towers
        )
        print_moves(
            pieces[:-1],
            (towers - {current_tower, destination_tower}).pop(),
            destination_tower,
            towers
        )


if __name__ == "__main__":
    print_moves([1, 2, 3], "A", "C", {"A", "B", "C"})
