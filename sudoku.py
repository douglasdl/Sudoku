# import the necessary packages
import numpy as np

class Sudoku():
    def __init__(self):
        self.sudoku = []
        self.solutions = list()


    def createGame(self):
        self.sudoku = np.array([5, 3, 0, 0, 7, 0, 0, 0, 0,
                                6, 0, 0, 1, 9, 5, 0, 0, 0,
                                0, 9, 8, 0, 0, 0, 0, 6, 0,
                                8, 0, 0, 0, 6, 0, 0, 0, 3,
                                4, 0, 0, 8, 0, 3, 0, 0, 1,
                                7, 0, 0, 0, 2, 0, 0, 0, 6,
                                0, 6, 0, 0, 0, 0, 2, 8, 0,
                                0, 0, 0, 4, 1, 9, 0, 0, 5,
                                0, 0, 0, 0, 8, 0, 0, 7, 9]).reshape([9, 9])
        return self.sudoku


    def getLine(self, line):
        return self.sudoku[line, :]


    def getColumn(self, column, asLine = True):
        if asLine:
            return self.sudoku[:, column]
        else:
            return self.sudoku[:, column].reshape([9, 1])


    def getSquare(self, size = 3, x = 0, y = 4):
        x2 = x // size
        y2 = y // size
        return self.sudoku[x2 * size : (x2 + 1) * size, y2 * size : (y2 + 1) * size]


    def isValid(self, x, y, input):
        return input not in self.getLine(x) and input not in self.getColumn(y) and input not in self.getSquare(x=x, y=y)


    def getAllValids(self, x, y):
        validNumbers = list()
        for number in range(1, 10):  
            if self.isValid(x=x, y=y, input=number):
                validNumbers.append(number)
        return validNumbers        

    def solveGame(self):
        # ndenumerate function returns the index of an array element 
        for (x, y), number in np.ndenumerate(self.sudoku):
            # Get empty places
            if number == 0:
                # Solve empty places
                for answer in self.getAllValids(x, y):
                    self.sudoku[x, y] = answer
                    self.solveGame()
                    self.sudoku[x, y] = 0
                    return
                self.solutions.append(self.sudoku.copy())
        print(self.sudoku)            


    def printGrids(self, symbol = "-"):
        for line in range(0, 13):
            for column in range(0, 13):
                if line == 0 and column < 12:
                    print(symbol),
                elif line == 0 or column == 13:
                    print(symbol)
                elif line % 4 == 0 and column < 12:
                    print(symbol),    
                elif line == 13:
                    print(symbol),    
                else:
                    if column == 0:
                        print(symbol),
                    elif column == 12:
                        print(symbol)
                    elif column % 4 == 0:
                        print(symbol),    
                    else:
                        print(column),      
        

def main():
    print("SUDOKU")
    game = Sudoku()
    #game.printGrids()
    game.createGame()
    #l = game.getLine(3)
    #c = game.getColumn(0)
    #q = game.getSquare()
    #v = game.isValid(0, 0, 5)
    #vn = game.getAllValids(1, 1)
    game.solveGame()
    for solution in game.solutions:
        print(solution)
    

    #print(l)


if __name__ == '__main__':
    main()