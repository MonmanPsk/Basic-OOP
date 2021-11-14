import random

sizeX = random.randint(1,6)
sizeY = random.randint(1,6)
posX = random.randint(-7,7)
posY = random.randint(-7,7)

class SquareGame:
    def __init__(self, sizeX, sizeY, posX, posY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.area = sizeX * sizeY

    def guess(self):
        print("Guess the position from -10 to 10 and area")
        self.player_x = int(input("Enter X = "))
        self.player_y = int(input("Enter Y = "))
        self.player_area = int(input("Enter Area = "))

    def checkPos(self):
        if self.posX + (self.sizeX/2) >= self.player_x and self.posX - (self.sizeX/2) <= self.player_x and self.posY + (self.sizeY/2) >= self.player_y and self.posY - (self.sizeY/2) <= self.player_y:
            return True
        else:
            return False

    def checkArea(self):
        if self.player_area == self.area:
            return True
        else:
            return False

    def showResult(self):
        if self.checkPos() == True:
            print("In the square, Win!")
        else:
            print("Not in the square, Lose!")
        if self.checkArea() == True:
            print("The area is", self.area, "Correct!")
        else:
            print("The area is", self.area, "Incorrect!")

square = SquareGame(sizeX, sizeY, posX, posY)
square.guess()
square.showResult()