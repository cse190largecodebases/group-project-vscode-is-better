# Project Title: TODO Tree Extension

## Team Members:
- Aman Singh Arora, A15977180, asa001@ucsd.edu
- Nathaniel Susabda, A17196946, nsusabda@ucsd.edu


## Project summary:
Motivation of this project: It is sometimes hard to see which part of the code that we need to fix, so a TODO tree will be beneficial in this case. Also, to be able to see which functions and class that needs to be fixed will help the programmer to focus on those stuffs first before moving on.

In this project, we would like to implement a TODO tree extension simillar with the one in VSCode. So the idea is we will add an option to show to do list then in the code, if the user have the following code:
```
213 class Tester:
214    ## TODO: 
215    def func ():
216        print("hello")
217    def func2():
218       print("vscode is better")
```
We will add a new option feature to show all the Todo List in one file. We will show it in terms of the function name and class (if the function has class). So after we clicked the option, it will show up in a new window/pyshell as
```
213 class Tester:
214     ## TODO:
215     def func()
```
Here, we would also want it to show the line number.

Also, we would like to try to implement so that if the user clicks the func on that window it will goes to the particular function in the file.

Process on how the user can use the feature:
- Open a .py file in IDLE
- Then add some ``## TODO:`` in the code
- Select the options
- In the drop down menu, there will be option to Show TODO Tree
- Then, it will shows up the list of TODO's in the new window
- If the user clicks a particular TODO's or function, the cursor will jump to that particular line of code


## Project outline/Feasibility analysis:

During the first two weeks, we will try to implement the whole TODO tree functionalities. It will also be able to printout the output to the python shell or some new output window.

The third week will be the implementation of clicking the the function and goes to the particular line.

The feature below is optional, if time permits, then:
The last week would be implementing the ToDO tree as a sidebar (like the one in VSCode). This might require a lot of time because we need to add a new sidebar for the TODO tree for each of the files that are opened.

Here is an example of such feature in VSCode:

[insert picture]

## Checkpoint deliverables:
- 1st Checkpoint:
  
Implemented the TODO tree functionalities as an extension. So that if the user selects opened a file that already has some TODO's comments, we already have an option to show the TODO list, and when that option is clicked, we already print it in a new window or pyshell.

- 2nd Checkpoint:

If in the first checkpoint we haven't print it in a new window, we would have this done by the second checkpoint. Also, we would like the clicking function feature to work properly by the second checkpoint. If time permits, we would also show that we already have a TODO sidebar that will show all the TODO's functions like the one that we have in VSCode


### - Since we are only a group of 2, we will be doing most of the work together, and hence there would not be a lot of work that would be split. We plan to meet up to work on the project, and then when required, individually divide up certain functions to work on.