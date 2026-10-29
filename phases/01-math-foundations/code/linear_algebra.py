"""Runnable, dependency-free examples for the Linear Algebra Intuition lesson."""

from __future__ import annotations

from math import acos, degrees, fsum, sqrt
from typing import Iterable


class Vector:
    def __init__(self, components: Iterable[float]) -> None:
        self.components = tuple(float(x) for x in components)
        if not self.components:
            raise ValueError("a vector must have at least one component")

    def _check(self, other: Vector) -> None:
        if len(self.components) != len(other.components):
            raise ValueError("vectors must have the same dimension")

    def __add__(self, other: Vector) -> Vector:
        self._check(other)
        return Vector(a + b for a, b in zip(self.components, other.components))

    def __sub__(self, other: Vector) -> Vector:
        self._check(other)
        return Vector(a - b for a, b in zip(self.components, other.components))

    def dot(self, other: Vector) -> float:
        self._check(other)
        return fsum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self) -> float:
        return sqrt(self.dot(self))

    def normalize(self) -> Vector:
        length = self.magnitude()
        if length == 0:
            raise ValueError("cannot normalize the zero vector")
        return Vector(x / length for x in self.components)

    def angle_between(self, other: Vector) -> float:
        denominator = self.magnitude() * other.magnitude()
        if denominator == 0:
            raise ValueError("angle is undefined for the zero vector")
        cosine = max(-1.0, min(1.0, self.dot(other) / denominator))
        return degrees(acos(cosine))

    def __repr__(self) -> str:
        return f"Vector({list(self.components)})"


class Matrix:
    def __init__(self, rows: Iterable[Iterable[float]]) -> None:
        self.rows = tuple(tuple(float(x) for x in row) for row in rows)
        if not self.rows or not self.rows[0]:
            raise ValueError("a matrix must have at least one row and column")
        if any(len(row) != len(self.rows[0]) for row in self.rows):
            raise ValueError("matrix rows must have equal lengths")

    def __matmul__(self, vector: Vector) -> Vector:
        if len(self.rows[0]) != len(vector.components):
            raise ValueError("matrix columns must match vector dimension")
        return Vector(fsum(a * b for a, b in zip(row, vector.components)) for row in self.rows)

    def rank(self, tolerance: float = 1e-10) -> int:
        """Compute rank by Gaussian elimination with partial pivoting."""
        rows = [list(row) for row in self.rows]
        pivot_row = 0
        for col in range(len(rows[0])):
            pivot = max(range(pivot_row, len(rows)), key=lambda r: abs(rows[r][col]), default=pivot_row)
            if pivot_row == len(rows) or abs(rows[pivot][col]) <= tolerance:
                continue
            rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
            divisor = rows[pivot_row][col]
            rows[pivot_row] = [x / divisor for x in rows[pivot_row]]
            for r in range(len(rows)):
                if r != pivot_row:
                    factor = rows[r][col]
                    rows[r] = [x - factor * y for x, y in zip(rows[r], rows[pivot_row])]
            pivot_row += 1
            if pivot_row == len(rows):
                break
        return pivot_row

    def __repr__(self) -> str:
        return f"Matrix({[list(row) for row in self.rows]})"


def project(a: Vector, b: Vector) -> Vector:
    """Return the component of a that points along b."""
    denominator = b.dot(b)
    if denominator == 0:
        raise ValueError("cannot project onto the zero vector")
    return Vector((a.dot(b) / denominator) * x for x in b.components)


def gram_schmidt(vectors: Iterable[Vector]) -> list[Vector]:
    """Build an orthonormal basis for the span of the input vectors."""
    basis: list[Vector] = []
    for vector in vectors:
        residual = vector
        for unit in basis:
            residual = residual - project(residual, unit)
        if residual.magnitude() > 1e-10:
            basis.append(residual.normalize())
    return basis


def main() -> None:
    a, b = Vector([1, 2, 3]), Vector([4, 5, 6])
    print(f"a + b = {a + b}")
    print(f"a dot b = {a.dot(b):.1f}")
    print(f"|a| = {a.magnitude():.4f}")
    print(f"angle(a, b) = {a.angle_between(b):.2f} degrees")

    scale = Matrix([[2, 0], [0, 3]])
    print(f"scale [1, 1] = {scale @ Vector([1, 1])}")
    print(f"projection [3, 4] onto [1, 0] = {project(Vector([3, 4]), Vector([1, 0]))}")

    orthonormal = gram_schmidt([Vector([1, 0, 0]), Vector([1, 1, 0]), Vector([1, 1, 1])])
    print(f"Gram-Schmidt vectors = {orthonormal}")
    print(f"lengths = {[round(v.magnitude(), 6) for v in orthonormal]}")
    print(f"pairwise dots = {[round(orthonormal[i].dot(orthonormal[j]), 6) for i in range(3) for j in range(i + 1, 3)]}")

    rank_two = Matrix([[1, 2, 3], [2, 4, 6], [0, 1, 1]])
    print(f"rank of {rank_two} = {rank_two.rank()}")
    print("The columns span a plane through the origin (rank 2).")


if __name__ == "__main__":
    main()
