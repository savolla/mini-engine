## mini-engine
* This project is made for **Data Structures** class.
* Currently runs on Linux (windows version is comming soon!)
* Uses **Boyer Moore Horspool** and **Levenshtein Distance** algorithms

### How to use it?
* run *main.py* in the repository
* it will ask you to select a file. Currently works on *pdf*, *doc & docx* and *plain text* files
* notice the file system navigator! you can access all you files within the program
* select one of those pdf,docx or text files from `sources/` 
* program will ask you to give some **strings** to search
* then it will show you lines that contain your string!

### How it works?
* it searches the entire text and looks for the *exact matching* string using **Boyer Moore Horspool**
* if it can't find that string then it looks for similar to given string using **Levenshtein Distance**
* then it shows *did you mean <string>* like phrase to the user
