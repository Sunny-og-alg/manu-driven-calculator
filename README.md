# manu-driven-calculator

# Menu-Driven Calculator (PS 28)

A simple terminal calculator written in Python 3. It runs in a continuous loop so you can do multiple math operations without restarting the script.

## What it does

Supports six operations:
- **1. Add (`+`)**
- **2. Subtract (`-`)**
- **3. Multiply (`*`)**
- **4. Divide (`/`)**
- **5. Power (`^`)**
- **6. Modulus (`%`)**

Instead of writing a big `if/elif` block, the menu choices are mapped directly to functions in a dictionary (`OPERATIONS`). It also handles common errors—like dividing by zero, typing letters instead of numbers, or trying to calculate a complex number like `-4 ^ 0.5`—so the program won't crash on bad input.

## How to run it

Make sure you have Python 3 installed, then run the file from your terminal:

```bash
python3 calculator.py
```

*(Note: Change `calculator.py` to whatever you named the file.)*

## Example

```text
===== MENU-DRIVEN CALCULATOR =====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulus
7. Exit
Enter your choice (1-7): 5
Enter first number: 3
Enter second number: 4
3 ^ 4 = 81.00

===== MENU-DRIVEN CALCULATOR =====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulus
7. Exit
Enter your choice (1-7): 4
Enter first number: 8
Enter second number: 0
Error: Division by zero is not allowed.

===== MENU-DRIVEN CALCULATOR =====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulus
7. Exit
Enter your choice (1-7): 7
Thank you for using the calculator. Exiting...
```
