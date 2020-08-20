class Solution:
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        else:
            m_num = 0
            neibor = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                      (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            for k1, k2 in neibor:
                if 0 <= k1 < m and 0 <= k2 < n and board[k1][k2] == 'M':
                    m_num += 1

            if m_num == 0:
                board[i][j] = 'B'
                for k1, k2 in neibor:
                    if 0 <= k1 < m and 0 <= k2 < n and board[k1][k2] == 'E':
                        self.updateBoard(board, [k1, k2])
            else:
                board[i][j] = str(m_num)

        return board
