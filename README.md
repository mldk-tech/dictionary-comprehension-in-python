Here's an example one of dictionary comprehension in Python.

Dictionary comprehension provides a concise way to create dictionaries. The basic syntax is:

```python
{key_expression: value_expression for item in iterable if condition}
```

* `key_expression`: How to compute the key for each item.
* `value_expression`: How to compute the value for each item.
* `item`: The variable representing each element from the iterable during iteration.
* `iterable`: A sequence or collection to iterate over (like a list, tuple, range, or another dictionary's items).
* `if condition` (optional): A filter to include only items that satisfy the condition.

**Example 1: Creating a dictionary of numbers and their squares**

Let's say you want to create a dictionary where the keys are numbers from 1 to 5, and the values are their squares.

*Without comprehension (traditional loop):*
```python
squares_loop = {}
for number in range(1, 6):
  squares_loop[number] = number * number

print(f"Using a loop: {squares_loop}")
# Output: Using a loop: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

*With dictionary comprehension:*
```python
squares_comp = {number: number * number for number in range(1, 6)}

print(f"Using comprehension: {squares_comp}")
# Output: Using comprehension: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
In this comprehension:
* `number` is the `key_expression`.
* `number * number` is the `value_expression`.
* `number` is the loop `item`.
* `range(1, 6)` is the `iterable`.

**Example 2: Filtering an existing dictionary**

Suppose you have a dictionary of product prices and you want to create a new dictionary containing only the items that cost more than $50.

```python
prices = {'apple': 1.50, 'banana': 0.75, 'laptop': 1200.00, 'monitor': 300.50, 'keyboard': 75.00}

# Using dictionary comprehension with an if condition
expensive_items = {item: price for item, price in prices.items() if price > 50}

print(f"Original prices: {prices}")
print(f"Expensive items (> $50): {expensive_items}")
# Output:
# Original prices: {'apple': 1.5, 'banana': 0.75, 'laptop': 1200.0, 'monitor': 300.5, 'keyboard': 75.0}
# Expensive items (> $50): {'laptop': 1200.0, 'monitor': 300.5, 'keyboard': 75.0}
```
In this comprehension:
* `item` is the `key_expression`.
* `price` is the `value_expression`.
* `(item, price)` is the loop `item` (unpacking key-value pairs from `prices.items()`).
* `prices.items()` is the `iterable`.
* `price > 50` is the `condition`.

Dictionary comprehensions are often more readable and concise than equivalent `for` loops for creating dictionaries based on existing iterables.

Here's another example of dictionary comprehension in Python.

Let's say you want to create a dictionary mapping each character in a string to its corresponding ASCII value.

**Example 3: Character to ASCII value mapping**

*Without comprehension (traditional loop):*
```python
ascii_map_loop = {}
text = "abc"
for char in text:
  ascii_map_loop[char] = ord(char) # ord() gets the ASCII value

print(f"Using a loop: {ascii_map_loop}")
# Output: Using a loop: {'a': 97, 'b': 98, 'c': 99}
```

*With dictionary comprehension:*
```python
text = "abc"
ascii_map_comp = {char: ord(char) for char in text}

print(f"Using comprehension: {ascii_map_comp}")
# Output: Using comprehension: {'a': 97, 'b': 98, 'c': 99}
```

In this comprehension:
* `char` is the `key_expression`.
* `ord(char)` is the `value_expression`.
* `char` is the loop `item`.
* `text` (the string "abc") is the `iterable`.

This concisely creates a dictionary where each character from the string `text` is a key, and its ASCII value is the corresponding value.