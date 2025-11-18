import copy


class MagicSquare:
    def __init__(self):
        self._solutions = []

    def print_solutions(self, N):
        for solution in self._solutions:
            for i in range(N):
                for elem in solution[i*N:(i+1)*N]:
                    print(elem, end=' ')
                print()

            print('-'*2*N)

    def _is_valid_solution(self, solution, N):
        M = (N*(N*N+1))/2

        # verifica del vincolo sulle righe
        for row in range(N):
            sum = 0
            sub_list = solution[row*N:(row+1)*N]
            for num in sub_list:
                sum += num

            if sum != M:
                return False

        # verifica del vincolo sulle colonne
        for col in range(N):
            sum = 0
            sub_list = solution[col : (N-1)*N+col+1: N]
            for num in sub_list:
                sum += num

            if sum != M:
                return False

        # verifica del vincolo sulla prima diagonale
        sum = 0
        for row_col in range(N):
            sum += solution[row_col*N+row_col]

        if sum != M:
            return False

        # verifica del vincolo sulla seconda diagonale
        sum = 0
        for row_col in range(N):
            sum += solution[row_col*N+(N-1-row_col)]

        if sum != M:
            return False

        return True



    def solve_magic_square(self, N):

        self._recursion([], set(range(1, N*N+1)), N)

    def _recursion(self, partial, remaining, N):
        if len(partial) == N*N :
            if self._is_valid_solution(partial, N):
                self._solutions.append(copy.deepcopy(partial))
            return

        else :
            for num in remaining :
                partial.append(num)
                new_remaining = copy.deepcopy(remaining)
                new_remaining.remove(num)
                self._recursion(partial, new_remaining, N)
                partial.pop()

if __name__ == '__main__':
    N = 3
    ms = MagicSquare()

    ms.solve_magic_square(N)
    ms.print_solutions(N)