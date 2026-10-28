"""A small vector implementation for practicing linear algebra."""

from __future__ import annotations

from math import fsum, sqrt
from typing import Iterable


class Vector:
    """An immutable, non-empty vector of real numbers."""

    def __init__(self, components: Iterable[float]) -> None:
        values = tuple(float(value) for value in components)
        if not values:
            raise ValueError("a vector must have at least one component")
        self._components = values

    @property
    def components(self) -> tuple[float, ...]:
        """Return the vector's components as an immutable tuple."""
        return self._components

    def dot(self, other: Vector) -> float:
        """Return the dot product, requiring vectors of equal dimension."""
        if not isinstance(other, Vector):
            raise TypeError("dot product requires another Vector")
        if len(self) != len(other):
            raise ValueError("dot product requires vectors of equal dimension")
        return fsum(a * b for a, b in zip(self, other))

    def magnitude(self) -> float:
        """Return the Euclidean length: sqrt(sum(component ** 2))."""
        return sqrt(fsum(component * component for component in self))

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self) -> str:
        return f"Vector({self._components!r})"


if __name__ == "__main__":
    first = Vector([3, 4])
    second = Vector([1, 2])

    print(f"{first}.dot({second}) = {first.dot(second)}")
    print(f"magnitude({first}) = {first.magnitude()}")
