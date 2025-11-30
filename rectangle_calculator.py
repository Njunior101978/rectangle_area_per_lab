#Nikkshai Junior
#CIS261
#Lab: Course Project Phase 1
#Date: 11/30/2025

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def calculate_perimeter(self):
        return 2 * (self.height + self.width)
    
    def calculate_area(self):
        return self.height * self.width
    
    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or row == self.height - 1:
                    print("*", end=" ")
                elif col == 0 or col == self.width - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    print("Rectangle Calculator")
    print()
    
    while True:
        height = get_positive_integer("Height: ")
        width = get_positive_integer("Width: ")
        
        rectangle = Rectangle(height, width)
        
        perimeter = rectangle.calculate_perimeter()
        area = rectangle.calculate_area()
        
        print(f"Perimeter: {perimeter}")
        print(f"Area: {area}")
        
        rectangle.draw()
        
        print()
        continue_choice = input("Continue? (y/n): ").lower()
        
        if continue_choice != 'y':
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()

