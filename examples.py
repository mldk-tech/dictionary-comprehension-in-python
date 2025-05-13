# {key_expression: value_expression for item in iterable if condition}

squares_loop = {}
for number in range(1, 6):
  squares_loop[number] = number * number

print(f"Using a loop: {squares_loop}")
# Output: Using a loop: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squares_comp = {number: number * number for number in range(1, 6)}

print(f"Using comprehension: {squares_comp}")
# Output: Using comprehension: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Filtering an existing dictionary

prices = {'apple': 1.50, 'banana': 0.75, 'laptop': 1200.00, 'monitor': 300.50, 'keyboard': 75.00}

# Using dictionary comprehension with an if condition
expensive_items = {item: price for item, price in prices.items() if price > 50}

print(f"Original prices: {prices}")
print(f"Expensive items (> $50): {expensive_items}")
# Output:
# Original prices: {'apple': 1.5, 'banana': 0.75, 'laptop': 1200.0, 'monitor': 300.5, 'keyboard': 75.0}
# Expensive items (> $50): {'laptop': 1200.0, 'monitor': 300.5, 'keyboard': 75.0}

# Example 3: Character to ASCII value mapping

ascii_map_loop = {}
text = "abc"
for char in text:
  ascii_map_loop[char] = ord(char) # ord() gets the ASCII value

print(f"Using a loop: {ascii_map_loop}")
# Output: Using a loop: {'a': 97, 'b': 98, 'c': 99}

text = "abc"
ascii_map_comp = {char: ord(char) for char in text}

print(f"Using comprehension: {ascii_map_comp}")
# Output: Using comprehension: {'a': 97, 'b': 98, 'c': 99}