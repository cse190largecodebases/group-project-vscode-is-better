# Project title: Autofill Your Code

##  Team members: 
- Aman Singh Arora, A15977180, asa001@ucsd.edu
- Nathaniel Susabda, A17196946 , nsusabda@ucsd.edu

## Project summary: 

One really helpful tool that a lot of IDEs such as VSCode or Pycharm have is the ability to autofill code snippets. Code snippets are basically pre-defined pieces of code which are usually very commmonly used, and can  help the programmer/user save a lot of time by not having to write down these trivial pieces of code. This feature is also very helpful for new and novice programmers as it helps them avoid minor errors in syntaxing which might break their code. 

We can implement this autofill feature as an extension to the IDLE ide. The option to autofill code can be enabled by the user when they are inside a editor window. The user will navigate to the `options` menu bar, which will then show an option to `autofill snippets`. Once the user clicks on this, it will open a dialogue box with different commonly use code snippets. The user can select one of the choices, after which the snippet will be pasted into the editor window where the user's cursor is present. The feature will also accomodate for syntaxing, for example if the user selects "for loop" from the code snippet options, then it will paste the format for a for loop in the editor window, and then place the user's cursor at the correct spot with indentation. 

With each code snippet, the feature will also include comments which mention where the user should make their desired changes or add their code. 

Some possible code snippets that we can add:
Here are some examples of code snippets that could be useful in IDLE IDE:

- File I/O: A code snippet that quickly sets up file input/output operations. This could include opening a file, reading from a file, writing to a file, and closing a file.
- Looping constructs: Code snippets that quickly generate for loops, while loops, and other common looping constructs. These could include customizable parameters such as loop index variables and step sizes.
- Conditional statements: Code snippets that quickly generate if/else statements, switch statements, and other common conditional constructs. These could include customizable conditions and branching logic.
- Function definitions: Code snippets that quickly generate function definitions, including input and output parameters, function names, and function bodies.
- Import statements: Code snippets that quickly generate import statements for commonly used libraries and modules.
- Error handling: Code snippets that quickly generate try/catch blocks and other error handling constructs, including customizable error messages and handling logic.


For example, here are some possible code snippets

```
# For loop
for i in range(start, stop, step):
    # Loop body
    (this is where the user's cursor would be set)
    pass

# While loop
while condition:
    # Loop body
    (this is where the user's cursor would be set)
    pass


# Try/catch block
try:
    # Code that may raise an exception
    pass
except Exception as e:
    # Handle the exception
    pass

```



## Project outline/Feasibility analysis: 

- This is the proposed or target timeline for the project:
    - By Week 2: 
      - implement and configure the new extension so that the option is displayed in the menu bar, and define event functions and Class structure
      - Have a set of code snippets defined inside a seperate file that the user can choose from. These code snippts would include the options mentioned above such as File I/O, Looping Constructs, Error Handling, Conditional Statements, Function definitions, import statements, etc. 
      - implement menthod to display dialogue box, or pop-up window, which will be displayed when the user clicks on the menu option.
    - By Week 3: 
      - Implement method to select the appropriate code snippet, from the option that the user selects to be pasted into the editor window.
      - Once the code snippet is selected, implement method to paste this code snippet into the editor window.
    - During Week 4 (and also continousally):
      - Debug and continous improvements

- This feature is feasible to implement as it relies on building upon existing pieces of code, and using existing methods to obtain the information we need. This feature can extend or modify methods used in goto_line for example to set the new cursor position, or to open diaogue boxes, etc.

- One extension to this project which would be feasible given time constraints, would be to be able to give the user a prompt for certain codes. For example, if the user selects a for loop, then allowing them to enter the values for the variable they want to loop through, the start and end index, etc., or if they want to import a module, then allowing them to enter the name of the module in a popup and then filling in the rest of the code with the module name in the correct position. 

## Checkpoint deliverables: There will be two checkpoints before the final due date (presentation) of your project. You should write down what you expect will be completed by each checkpoint.
  - Checkpoint 1:
    - Show option to autofill code snippets in the menu bar
    - Have a list of useful code snippets 
    - implement those code snippets and store them in a file which the paste function would be able to access
    - Display dialogue box when user clicks on autofill code snippet menu option.
    - Checkpoint 2:
      - Implement function to correctly select the appropriate code snippet based on the users choice from the pop-up window or dialogue box
      - Implement method to paste the selected code snippet into the editor window at the user's current cursor position.
      - In the process of debugging
  

### - Since we are only a group of 2, we will be doing most of the work together, and hence there would not be a lot of work that would be split. We plan to meet up to work on the project, and then when required, individually divide up certain functions to work on. 