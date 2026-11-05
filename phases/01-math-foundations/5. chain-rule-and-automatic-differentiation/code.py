import math
import random


# STEP 1: Create the Value class
class Value:
    def __init__(self, data, children=(), operation=""):
        self.data = data
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(children)
        self._op = operation

    # STEP 2: Addition
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)

        result = Value(
            self.data + other.data,
            (self, other),
            "+"
        )

        def backward():
            self.grad += result.grad
            other.grad += result.grad

        result._backward = backward
        return result

    __radd__ = __add__
