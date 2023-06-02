# Progress Report

Progress Report for Group: VSCode Is Better - Autocode

### 1. Progress Update

- Our group is currently making good progress on our Autocode feature extension.
-  We have a working implemenation of our autofill code snippet feature where once the user clicks on the menu option, a dialogue box appears which asks the user to select a code snippet to insert into their editor window, or the python shell depending on which one is selected. 
- The code is then successfully inserted into the file and is recognized by the window as executable code.
- We have also added another feature which allows the user to add custom code snippets which they might use often. However, these are only saved for the duration of the current session.
- Similarly, we added a feature which allows the user to delete any custom code snippets that they might have created for the current sesison. 
- We are working on adding more features to our extension, such as shortcuts for a particular code snippet, for easy access.
- We currently have a minor edge case we are trying to work on, which is that if the user inserts a code snippet from any position other than the start of the line, i.e. from an indented position, then if the user inserts a code snippet that has indentations inside it, then it does not match the proper indentation formatting. 

- #### Milestones
  - [x] Configured extension for autocode. [#5](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/5__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKnuRE2SA$ )
  - [x] Added menu option for Autocode. [#5](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/5__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKnuRE2SA$ )
  - [x] Implemented first version of user dialogue box. [#6](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/6__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKqsMphNI$ )
  - [x] Added common code snippet options for the user to choose from. [#6](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/6__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKqsMphNI$ )
  - [x] Implemented method to print to the editor window and python shell. [#6](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/6__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKqsMphNI$ )
  - [x] Tried to implement dropdown box displaying all possible code snippets for user to chose from (Not Working). - [#7](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/7__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKsdzA09S$ )
  - [x] Changed dialogue box popup and correctly implemented drowndown list for code snippets. [#8](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/8__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKoLFRQGU$ )
  - [x] Implemented feature to add and delete custom code snippets, and added keybinds. [#8](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/8__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKoLFRQGU$ )
  - [x] Added unit test for init. [#10](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/10__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKh3l5aSD$ )
  - [x] Added unit test for add custom snippet event, delete custom code snippet event, code fill event logic, custom code snippet code fill event logic. [#11](https://urldefense.com/v3/__https://github.com/cse190largecodebases/group-project-vscode-is-better/pull/11__;!!Mih3wA!G53bczMRnUUrTkFBP4EffX_gXZNpZi9RZtC2_4h42xtKWww4_zNG9GGDku41z1xjjKn_ee0FKl4rYjK6$ )
  - [x] Conducted code review for code so far to check for efficiency and any bugs/errors.
  - [ ] Add further unit tests to check for edge cases.
  - [ ] Implement a fix for edge case where user inserts a code snippet from an indented position, and so the inserted code snippet should follow proper indentation levels.
  - [ ] Implement keybinds for common code snippets to be inserted without having to access the dialogue box. 
  - [ ] Check for further edge cases.
  - [ ] Fix bugs as implementation continues. 
  - [ ] Solve world hunger with Super Secret Staff if time permits 


### 2. Challenges 
- After the code snippet was inserted into the window, the python shell was not recognizing the line as executable code. The line would get inserted into the python shell, and then the user would be unable to edit or run the line. This was later fixed when the implementation for the dialogue box was changed. It was fixed by using the insert method:
  ```
      def code_fill_event_logic(self, snippet):
        self.text.insert(tk.INSERT, snippet)
        self.text.see(tk.INSERT)
    ```

- Initially we were unable to implement a dropdown menu for the user to select from predefined code snippets. This was because we were using the `messagebox` library and `messagebox.askquestion` to display the pop up box to the user. This particular implementation did not allow for a dropdown menu since it was not part of the messagebox package. We changed our popup dialogue box to be a TkInter window, similar to how it is done in most of IDLE. This allowed us to have a dropdown menu for the user to be able to select from. 

- Unable to setup unit tests as we were getting an unexpected error while trying to import the modules from autocode. When trying to run the code below, we got an error which said it was unable to import the module AutoCode as it was not found. We fixed this error by removing the line 'from autocode import AutoCode, etc.' with just autocode.AutoCode wherever needed.
  ```
  from idlelib import autocode
  from autocode import AutoCode, etc.. 
  ```
    

- There were  times when some group members were unable to work on the project due to personal or family reasons, however, we made sure to stay on track with our checkpoint deliverable goals, and made sure to catch up whenever necessary. We made sure to communicate these challenges with each other so we weere all aware. Another member of the group always made sure to pick up the work to allow the other teammate to have time to deal with their challenges. 


### 3. Remaining Work

- Implement a fix for edge case where user inserts a code snippet from an indented position, and so the inserted code snippet should follow proper indentation levels.
  - Implement two new functions:
    - The `get_current_indentation` method retrieves the current indentation level at the cursor position in the editor. It gets the line of text at the current position and counts the number of leading spaces.
    - The `indent_code` method takes a code snippet and an indentation level as input. It indents each line of the code snippet by adding the specified number of spaces at the beginning.  
    - Implement these changes over the next 3-4 days and add unit tests for the same. Aman will primarily work on this.
- Implement keybinds for common code snippets to be inserted without having to access the dialogue box. 
  - Figure out which key bindings are open, and then how to execute the code fill event with a particular code snippet when key is pressed. 
  - Implement this in the next 2-3 days. Nathan will be primarily working on this
- Fix bugs as implementation continues. 
  - Continous code reviews as we implement new functions/small changes to ensure no new bugs are introduced, and to detect any errors. 
  - Check unit tests after any new addition to ensure functionality of the feature extension. 
- Solve world hunger with Super Secret Staff if time permits
  - Good question! I'll get back to you on that one.  
  



