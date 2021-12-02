from dorm import Guest, Manager

#instantiate object
manager = Manager()
guest1 = Guest()
guest2 = Guest()
manager.cal_rent([guest1.length, guest2.length])
manager.show_bill([guest1.name, guest2.name])