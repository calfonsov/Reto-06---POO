"""
Shape package initialization file.
This allows importing all classes directly from the package.
"""

from .shapes import (
    Point,
    Line,
    Shape,
    Rectangle,
    Square,
    Triangle,
    Equilateral,
    Isosceles,
    Scalene,
    InvalidPointError,
    InvalidShapeError,
    MathComputationError
)

__all__ = [
    "Point",
    "Line",
    "Shape",
    "Rectangle",
    "Square",
    "Triangle",
    "Equilateral",
    "Isosceles",
    "Scalene",
    "InvalidPointError",
    "InvalidShapeError",
    "MathComputationError"
]
