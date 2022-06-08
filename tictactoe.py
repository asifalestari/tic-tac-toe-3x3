import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_pemain_pertama(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_pemain_menang(self, player):
        win = None

        n = len(self.board)

        #pengecekan kondisi baris
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        #pengecekan kondisi kolom
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        #pengecekan kondisi diagonal
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n-1-i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_terisi(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_pemain_giliran(self, player):
        return 'X' if player == 'O' else 'O'

    def show_papan(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def mulai(self):
        self.create_board()

        player = 'X' if self.get_random_pemain_pertama() == 1 else 'O'
        while True:
            print(f"Bagian pemain {player}")

            self.show_papan()

            #mengambil input dari user
            row, col = list(
                map(int, input("Masukkan nomor baris dan kolom untuk memperbaiki : ").split())
            )
            print()

            #memperbaiki posisi
            self.fix_spot(row - 1, col - 1, player)

            #cek apakah pemain yang main menang atau tidak
            if self.is_pemain_menang(player):
                print(f"Pemain {player} memenangkan permainan")
                break

            #cek apakah pemain dalam keadaan draw atau tidak
            if self.is_board_terisi():
                print(f"Permainan Seri!!!")
                break

            #pergantian giliran
            player = self.swap_pemain_giliran(player)

        #menampilkan final hasil papan permainan
        print()
        self.show_papan()

#memulai permainan
tic_tac_toe = TicTacToe()
tic_tac_toe.mulai()