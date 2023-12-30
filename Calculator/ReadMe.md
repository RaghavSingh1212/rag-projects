# Calculator Project

## Introduction
This GitHub repository, developed by Raghav Singh, contains the source code for an advanced calculator application. It's capable of performing basic arithmetic operations and is implemented in Python. Notably, it offers both a command-line interface and a graphical user interface (GUI) using Tkinter.

## Repository Structure
The repository comprises several key components:
- `calculator.py`: This is the heart of the application, responsible for parsing and evaluating mathematical expressions.
- `stack.py`: Implements the Stack class, essential for expression evaluation in `calculator.py`.
- `tree.py`: Contains implementations of binary and expression trees, crucial for arithmetic operations.
- `calculatorGUI.py`: Provides a GUI, crafted using the Tkinter library, enhancing user interaction.

## Detailed Explanation of Each Component

### calculator.py
**Purpose**: Core logic for interpreting and computing arithmetic expressions.
1. **Imports**:
   - `stack`: For the Stack class, facilitating data storage and retrieval.
   - `tree`: For the ExpTree class, instrumental in building expression trees from arithmetic expressions.
2. **Key Functions**:
   - `infix_to_postfix(infix)`: Transforms an infix expression (normal arithmetic format) to postfix (Reverse Polish Notation) using two stacks for operators and output.
   - `calculate(infix)`: Converts infix to postfix, constructs an expression tree, and evaluates this tree.

### stack.py
**Purpose**: Defines a Stack class used in `calculator.py`.
1. **Class Stack**:
   - Implements fundamental stack operations like `push`, `pop`, `peek`, `isEmpty`, and `size`.
   - Essential for managing data in a LIFO method, crucial for both the infix-to-postfix conversion and the construction of expression trees.

### tree.py
**Purpose**: Establishes a binary tree structure and extends it to an expression tree.
1. **Class BinaryTree**:
   - Basic operations like `insertLeft`, `insertRight`, and getters and setters for child nodes and root value.
2. **Class ExpTree (extends BinaryTree)**:
   - `make_tree(postfix)`: Converts postfix expressions to expression trees.
   - Tree traversal methods: `preorder`, `inorder`, `postorder`.
   - `evaluate(tree)`: Computes the result of the expression tree.

### calculatorGUI.py
**Purpose**: Delivers a Graphical User Interface using Tkinter.
1. **Main Functions**:
   - `calculator(gui)`: Establishes the calculator layout and buttons.
   - `addButton(gui, entrybox, value)`: Assists in creating calculator buttons.
   - `clickButton(entrybox, value)`: Defines button click actions, including calculations and UI updates.

### Features
- **Arithmetic Operations**: Manages basic arithmetic like addition, subtraction, multiplication, division, and exponentiation.
- **Expression Handling**: Evaluates expressions, respecting the correct order of operations.
- **Graphical User Interface**: An intuitive GUI for easier operation.

## Usage Instructions
1. **Command-Line Calculator**:
   - Execute `calculator.py`, input expressions when prompted. Use 'quit' or 'q' to exit.
2. **Graphical Calculator**:
   - Run `calculatorGUI.py` to launch the GUI. Input expressions using buttons and view results on the display.

## Installation
1. Clone the repository.
2. Ensure Python is installed.
3. `calculator.py` requires no external libraries. For `calculatorGUI.py`, Tkinter is necessary (usually included in Python distributions).

## Running the Tests
- Test cases are included in `calculator.py`, `stack.py`, and `tree.py`. Execute these files to run the tests.

## Dependencies
- Python 3.x
- Tkinter for GUI (typically included in Python)

## Contributing
We welcome contributions, bug reports, and feature requests. Please see the contribution guidelines for more details.

## License
This project is open-source under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
- **Author**: Raghav Singh
- **Email**: [raghav.world1212@gmail.com](mailto:raghav.world1212@gmail.com)
- **GitHub**: [github.com/RaghavSingh](https://github.com/RaghavSingh)

