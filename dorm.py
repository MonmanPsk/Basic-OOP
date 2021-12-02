class Guest:
    def __init__(self):
        self.name = input("Enter name : ")
        self.length = int(input("Enter "+self.name+" lived : "))

class Manager:
    def __init__(self) -> None:
        self.full_price = int(input("Enter amount : "))
        self.bill_period = input("Enter bill period : ")

    def cal_rent(self, guests_length):
        self.guest1_price = self.full_price * guests_length[0] / (guests_length[0] + guests_length[1])
        self.guest2_price = self.full_price * guests_length[1] / (guests_length[0] + guests_length[1])

    def show_bill(self, guests_name):
        print("Period :", self.bill_period)
        print(guests_name[0], "pays", self.guest1_price)
        print(guests_name[1], "pays", self.guest2_price)