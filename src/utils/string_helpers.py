"""String manipulation utilities."""


def reverse_string(s: str) -> str:
    """Reverse a string without using slicing."""
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case and spaces."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
