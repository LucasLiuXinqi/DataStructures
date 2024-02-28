import copy
class TreeNode:
    def __init__(self, board_status, turn):
        self._board_status = board_status
        self._turn = turn
        self._score = None
        self._children = []

    def grow(self):
        if self._turn == 'X':
            next_turn = 'O'
        else:
            next_turn = 'X'

        if self._evaluate(self._board_status) != 0 or not self.not_full(self._board_status):
            return self

        else:
            for line in range(3):
                for column in range(3):
                    if self._board_status[line][column] == None:
                        board = TreeNode(copy.deepcopy(self._board_status), next_turn)

                        board._board_status[line][column] = self._turn
                        self._children.append(board.grow())

            return self




    def _evaluate(self, cur_board_status):
        # status = True
        #
        # if not (self.not_full(cur_board_status)) or self.X_win(cur_board_status) or self.O_win(cur_board_status):
        #     status = False
        #
        # return status


        if self.X_win(cur_board_status):
            self._score = +1

        elif self.O_win(cur_board_status):
            self._score = -1

        else:
            self._score = 0


        return self._score




    def X_win(self, cur_board_status):
        status = False

        horizontal_status = ['X', 'X', 'X'] in cur_board_status

        vertical_status = False
        for i in range(3):
            if cur_board_status[0][i] == cur_board_status[1][i] == cur_board_status[2][i] == 'X':
                vertical_status = True

        diagonal_status = ((cur_board_status[0][0] == cur_board_status[1][1] == cur_board_status[2][2] == 'X') or
                           (cur_board_status[0][2] == cur_board_status[1][1] == cur_board_status[2][0] == 'X'))

        if horizontal_status or vertical_status or diagonal_status:
            status = True

        return status

    def O_win(self, cur_board_status):
        status = False

        horizontal_status = ['O', 'O', 'O'] in cur_board_status

        vertical_status = False
        for i in range(3):
            if cur_board_status[0][i] == cur_board_status[1][i] == cur_board_status[2][i] == 'O':
                vertical_status = True

        diagonal_status = ((cur_board_status[0][0] == cur_board_status[1][1] == cur_board_status[2][2] == 'O') or
                           (cur_board_status[0][2] == cur_board_status[1][1] == cur_board_status[2][0] == 'O'))

        if horizontal_status or vertical_status or diagonal_status:
            status = True

        return status

    def not_full(self, cur_board_status):
        full_status = False
        for i in cur_board_status:
            if None in i:
                full_status = True

        return full_status


    # def X_propagate(self):
    #     if self._turn == 'X':
    #         last_turn = 'O'
    #     else:
    #         last_turn = 'X'
    #
    #     if not self._children:
    #         if self.X_win(self._board_status):
    #             self._score = +1
    #
    #         elif self.O_win(self._board_status):
    #             self._score = -1
    #
    #         elif not self.not_full(self._board_status):
    #             self._score = 0
    #
    #
    #     else:
    #         if last_turn == 'X':
    #             self._score = min(i.X_propagate() for i in self._children)
    #         else:
    #             self._score = max(i.X_propagate() for i in self._children)
    #
    #     return self._score
    #
    #
    # def O_propagate(self):
    #     if self._turn == 'X':
    #         last_turn = 'O'
    #     else:
    #         last_turn = 'X'
    #
    #     if not self._children:
    #         if self.X_win(self._board_status):
    #             self._score = -1
    #
    #         elif self.O_win(self._board_status):
    #             self._score = +1
    #
    #         elif not self.not_full(self._board_status):
    #             self._score = 0
    #
    #
    #     else:
    #         if last_turn == 'O':
    #             self._score = min(i.O_propagate() for i in self._children)
    #         else:
    #             self._score = max(i.O_propagate() for i in self._children)
    #
    #     return self._score

    def propagate_score(self):
        # Implement you code here for part 1.B.
        if self._turn == 'X':
            last_turn = 'O'
        else:
            last_turn = 'X'


        if not self._children:
            # if self.X_win(self._board_status):
            #     self._score = +1
            #
            # elif self.O_win(self._board_status):
            #     self._score = -1
            #
            # elif not self.not_full(self._board_status):
            #     self._score = 0
            return self._score

        else:
            if last_turn == 'X':
                self._score = min(i.propagate_score() for i in self._children)
            else:
                self._score = max(i.propagate_score() for i in self._children)

        return self._score

        # if self._turn == 'X':
        #     self._score = self.X_propagate()
        #
        # else:
        #     self._score = self.O_propagate()
        #
        # return self._score



    def print_tree(self, level=0):
        result = ""
        indent = " " * 6 * level  # Adjust the spacing as needed

        board = self._board_status
        board_str = "\n".join([f"{indent}{row}" for row in board])

        result += f"{board_str}\n"

        for child in self._children:
            result += child.print_tree(level + 1)

        return result

def main():
    # board = [
    #     ["O", "O", "X"],
    #     [None, None, "X"],
    #     ["O", "X", None]
    # ]
    # gameTreeRoot = TreeNode(board, "X")
    # gameTreeRoot.grow()
    # gameTreeRoot.propagate_score()
    # print(gameTreeRoot.print_tree())
    # print("Player X can win: ", gameTreeRoot._score == 1)  # should be true

    # board = [
    #     ["O", "X", "X"],
    #     ['X', 'O', None],
    #     ["O", "X", None]
    # ]

    board = [
        ["O", 'O', 'O'],
        ['O', 'O', 'O'],
        [None, None, None]
    ]
    # board = [
    #     [None, None, None],
    #     [None, None, None],
    #     [None, None, None]
    # ]
    gameTreeRoot = TreeNode(board, "X")
    #print(gameTreeRoot.X_evaluate(gameTreeRoot._board_status))
    gameTreeRoot.grow()
    gameTreeRoot.propagate_score()
    print(gameTreeRoot._evaluate(board))
    print("Player X can win: ", gameTreeRoot._score == 1, gameTreeRoot._score)


if __name__ == '__main__':
    main()
