def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def calculate_diagonal(length, width):
    return (length**2 + width**2)**0.5

def main():
    print("Rectangle Calculator")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    diagonal = calculate_diagonal(length, width)

    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")
    print(f"Diagonal length of the rectangle: {diagonal}")

if __name__ == "__main__":
    main()
