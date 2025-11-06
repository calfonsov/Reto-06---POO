import math

# Custom exception classes
class InvalidPointError(Exception):
    """Raised when a point has invalid (non-numeric) coordinates."""
    pass

class InvalidShapeError(Exception):
    """Raised when a shape does not have enough vertices to exist."""
    pass

class MathComputationError(Exception):
    """Raised when a math error occurs, such as a negative square root."""
    pass


class Point:
    def __init__(self, x: float, y: float):
        # Validate that coordinates are numeric
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise InvalidPointError("Point coordinates must be numeric values.")
        self.x = x
        self.y = y
    
    def compute_distance(self, point):
        # Validate that the argument is a Point object
        if not isinstance(point, Point):
            raise TypeError("The argument must be a Point object.")
        # Euclidean distance formula
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        # Validate that both arguments are Point objects
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("Both endpoints must be Point objects.")
        self.start_point = start_point
        self.end_point = end_point
        self.length = start_point.compute_distance(end_point)


class Shape:
    def __init__(self, vertices: list):
        # A shape must have at least 3 vertices
        if not isinstance(vertices, list) or len(vertices) < 3:
            raise InvalidShapeError("A shape must have at least three vertices.")
        self.vertices = vertices
        self.is_regular = False
        self.edges = self.make_edges()
        self.inner_angles = []

    def make_edges(self):
        edges = []
        for i in range(len(self.vertices)):
            start = self.vertices[i]
            end = self.vertices[(i + 1) % len(self.vertices)]  # Connects last vertex with first
            edges.append(Line(start, end))
        return edges

    def compute_area(self):
        raise NotImplementedError("This method must be defined in the subclass.")
    
    def compute_perimeter(self):
        perimeter = 0
        for edge in self.edges:
            perimeter += edge.length
        return perimeter
    
    def compute_inner_angles(self):
        raise NotImplementedError("This method must be defined in the subclass.")


class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_regular = True
        
    def compute_area(self):
        base = self.edges[0].length
        height = self.edges[1].length
        return base * height

    def compute_inner_angles(self):
        return [90.0, 90.0, 90.0, 90.0]


class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_regular = True


class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.inner_angles = self.compute_inner_angles()
    
    def compute_area(self):
        # Heron's formula for area of triangle
        a, b, c = [edge.length for edge in self.edges]
        s = (a + b + c) / 2
        try:
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        except ValueError:
            # Negative inside sqrt means collinear points
            raise MathComputationError("Cannot compute area: points may be collinear.")
    
    def compute_inner_angles(self):
        # Law of Cosines to compute angles
        a, b, c = [edge.length for edge in self.edges]
        try:
            A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
            B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
            C = 180 - (A + B)
            return [A, B, C]
        except ValueError:
            raise MathComputationError("Error computing angles: check vertex positions.")


class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_regular = all(abs(e1.length - e2.length) < 1e-6 for e1 in self.edges for e2 in self.edges)


class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        lengths = [round(edge.length, 3) for edge in self.edges]
        self.is_regular = len(set(lengths)) <= 2


class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        lengths = [round(edge.length, 3) for edge in self.edges]
        self.is_regular = len(set(lengths)) == 3
