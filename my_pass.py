#!/usr/bin/python3

class phone:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.color = color

        def Display_info(self):
        """Display the infomation about the phone."""
        info = f"phone: {self.color} {self.make} {self.model}
        print(info)

        def main():
        """main function."""
        my_phone = Phone("Iphone", "Iphone15promax", "Red")
        my_phone.display_info()

        if __name__ == "__main__":
        main()
