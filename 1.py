class Door:
    def __init__(self):
        self.state = "закрыта"  
        self.broken = False     
    def toggle(self):
        if not self.broken:
            if self.state == "закрыта":
                self.state = "открыта"
            else:
                self.state = "закрыта"

    def break_in(self):
        if self.state == "закрыта" and not self.broken:
            self.broken = True
            self.state = "открыта"  
            print("Дверь взломана!")
        elif self.state == "открыта" and not self.broken:
            print("Нельзя взломать открытую дверь!")
        elif self.broken:
            print("Дверь уже взломана!")

    def print_state(self):
        status = "взломана" if self.broken else "не взломана"
        print(f"Дверь {self.state}, {status}")

door = Door()
door.print_state()  
