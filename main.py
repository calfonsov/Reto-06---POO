from .shapes import (
    Point, Line, Shape, Rectangle, Square,
    Triangle, Equilateral, Isosceles, Scalene
)

if __name__ == "__main__":
    print("----- SHAPE TESTING -----")

    try:
        # Rectangle
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(4, 3)
        p4 = Point(0, 3)
        rect = Rectangle([p1, p2, p3, p4])
        print("\n----- Rectangle -----")
        print("Perimeter:", rect.compute_perimeter())
        print("Area:", rect.compute_area())
        print("Inner angles:", rect.compute_inner_angles())
        print("Is regular?:", rect.is_regular)

    except (InvalidPointError, InvalidShapeError, MathComputationError, TypeError) as e:
        print(f"Error in Rectangle: {e}")


    try:
        # Square
        q1 = Point(0, 0)
        q2 = Point(3, 0)
        q3 = Point(3, 3)
        q4 = Point(0, 3)
        squ = Square([q1, q2, q3, q4])
        print("\n----- Square -----")
        print("Perimeter:", squ.compute_perimeter())
        print("Area:", squ.compute_area())
        print("Inner angles:", squ.compute_inner_angles())
        print("Is regular?:", squ.is_regular)

    except (InvalidPointError, InvalidShapeError, MathComputationError, TypeError) as e:
        print(f"Error in Square: {e}")


    try:
        # Equilateral triangle
        a = Point(0, 0)
        b = Point(3, 0)
        c = Point(1.5, 2.598)  # Height ≈ sqrt(3)/2 * 3
        equ = Equilateral([a, b, c])
        print("\n----- Equilateral Triangle -----")
        print("Perimeter:", equ.compute_perimeter())
        print("Area:", equ.compute_area())
        print("Inner angles:", equ.compute_inner_angles())
        print("Is regular?:", equ.is_regular)

    except (InvalidPointError, InvalidShapeError, MathComputationError, TypeError) as e:
        print(f"Error in Equilateral Triangle: {e}")


    try:
        # Isosceles triangle
        i1 = Point(0, 0)
        i2 = Point(4, 0)
        i3 = Point(2, 3)
        iso = Isosceles([i1, i2, i3])
        print("\n----- Isosceles Triangle -----")
        print("Perimeter:", iso.compute_perimeter())
        print("Area:", iso.compute_area())
        print("Inner angles:", iso.compute_inner_angles())
        print("Is regular?:", iso.is_regular)

    except (InvalidPointError, InvalidShapeError, MathComputationError, TypeError) as e:
        print(f"Error in Isosceles Triangle: {e}")


    try:
        # Scalene triangle
        s1 = Point(0, 0)
        s2 = Point(4, 0)
        s3 = Point(2, 1)
        esc = Scalene([s1, s2, s3])
        print("\n----- Scalene Triangle -----")
        print("Perimeter:", esc.compute_perimeter())
        print("Area:", esc.compute_area())
        print("Inner angles:", esc.compute_inner_angles())
        print("Is regular?:", esc.is_regular)

    except (InvalidPointError, InvalidShapeError, MathComputationError, TypeError) as e:
        print(f"Error in Scalene Triangle: {e}")


    # Example of forced exception
    try:
        print("\n----- Invalid Test (collinear points) -----")
        x1 = Point(0, 0)
        x2 = Point(1, 1)
        x3 = Point(2, 2)  # These three are collinear
        bad_triangle = Scalene([x1, x2, x3])
        print("Area:", bad_triangle.compute_area())

    except MathComputationError as e:
        print(f"Expected error detected: {e}")

