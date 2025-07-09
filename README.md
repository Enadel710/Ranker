# Ranker

## Ranker program
This program allows users to rank a list of things of their choosing from best to worst. It asks the users the minimum number of required questions in order to gauge the exact position a new element should be placed in the list. It also allows for the following:
- Determine the remaining number of questions that will be asked (this feature is also in the standalone Calculator program)
- Save progress by writing the list of remaining entries to rank and the list of already ranked entries to a file
- Undo rankings as far back as desired
- Add more entries to rank even after the initial insert

When creating a file, it is recommended to make it a txt file. If no relative or absolute path is provided, the file is put in the directory the program was called from. A relative path can be provided when creating or reading an existing file. Once the program completes, it prints the ranked list both as an array and a more readable numbered list. It also saves a copy of the final ranked array in the file used to rank the list.

<br>

## Calculator program
This program allows the user to enter a number and it will print the minimum and maximum number of questions that can be asked if there are that many entries to rank. The average number of questions is also shown.
