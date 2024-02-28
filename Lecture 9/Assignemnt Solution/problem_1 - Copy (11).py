class TreeNode:
    def __init__(self, board_status, turn):
        self._board_status = board_status
        self._turn = turn
        self._score = None
        self._children = []

    def grow(self):
        # Implement you code here for part 1.A.
        if self._score is not None or self._evaluate(self._board_status) != None:
            self._score = self._evaluate(self._board_status)
            return

        for i in range(3):
            for j in range(3):
                if self._board_status[i][j] is None:
                    new_board_status = [row[:] for row in self._board_status]
                    new_board_status[i][j] = self._turn
                    new_turn = "O" if self._turn == "X" else "X"
                    child_node = TreeNode(new_board_status, new_turn)
                    self._children.append(child_node)
                    child_node.grow()

    def _evaluate(self, cur_board_status):
        # Implement you code here for part 1.A.

        # Check rows
        for i in range(3):
            if (cur_board_status[i][0] == cur_board_status[i][1] == cur_board_status[i][2]
                    and cur_board_status[i][0] is not None):
                return 1 if cur_board_status[i][0] == "X" else -1

        # Check columns
        for i in range(3):
            if (cur_board_status[0][i] == cur_board_status[1][i] == cur_board_status[2][i]
                    and cur_board_status[0][i] is not None):
                return 1 if cur_board_status[0][i] == "X" else -1

        # Check diagonals
        if (cur_board_status[0][0] == cur_board_status[1][1] == cur_board_status[2][2]
                and cur_board_status[0][0] is not None):
            return 1 if cur_board_status[0][0] == "X" else -1
        if (cur_board_status[0][2] == cur_board_status[1][1] == cur_board_status[2][0]
                and cur_board_status[0][2] is not None):
            return 1 if cur_board_status[0][2] == "X" else -1

        # It's a draw if the board is full
        if (cur_board_status[0][0] and cur_board_status[0][1] and cur_board_status[0][2] and
                cur_board_status[1][0] and cur_board_status[1][1] and cur_board_status[1][2] and
                cur_board_status[2][0] and cur_board_status[2][1] and cur_board_status[2][2]):
            return 0

        return None  # No winner yet

    def propagate_score(self):
        # Implement you code here for part 1.B.
        if self._score is not None:
            return self._score

        if not self._children:
            self._score = self._evaluate(self._board_status)
            return self._score

        if self._turn == "X":
            self._score = max(child.propagate_score() for child in self._children)
        else:
            self._score = min(child.propagate_score() for child in self._children)

        return self._score


def main():
    board = [
        ["O", "O", "X"],
        [None, None, "X"],
        ["O", "X", None]
    ]
    gameTreeRoot = TreeNode(board, "X")
    gameTreeRoot.grow()
    gameTreeRoot.propagate_score()
    print("Player X can win: ", gameTreeRoot._score == 1)  # should be true


if __name__ == '__main__':
    main()
