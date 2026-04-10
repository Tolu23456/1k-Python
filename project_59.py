def calculate_area(length: int, width: int) -> int:
    area: int = length * width
    return area

calculated_area: int = calculate_area(5, 10)
print(f"The area is: {calculated_area}")