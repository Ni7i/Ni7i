"""Stack implementation."""


class Stack:
    """A simple stack data structure."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push item onto the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return top item."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"

def is_balanced_parentheses(expression: str) -> bool:
    """Check if parentheses in expression are balanced."""
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != matching[char]:
                return False
    return stack.is_empty()


def evaluate_postfix(expression: str) -> float:
    """Evaluate a postfix expression."""
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    for token in expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
        else:
            stack.push(float(token))
    return stack.pop()
