# hw1 grading direction

## 1. How to use autograder:
- download a batch of students' submitted assignment from cms.
     - under hw1 group 
     - select the students' netids of your grading group
     - then click Files on the top right corner of the page, under [Select Group Operations:]
- scp this folder to your ugclinux server
- scp the autograder script folder to your ugclinux server as well
- all the four files should sit under the directory of Submissions 
     Your directories should look as follows:
     
     -- Submissions

     ----- hw1_edge.txt

     ----- hw1_norm.txt

     ----- hw1grader.py

     ----- standard_output.py

     ----- netid_1

     ---------- 'my screenshot.pdf'

     ---------- 'My source file.cpp'

     ----- netid_2

     ---------- 'my screenshot.pdf'

     ---------- 'My source file.cpp'

     ....

- run the autograder by calling `python hw1grader.py`
- after running the autograder, there is a grades.csv generated with the score of each student's code
     - grades == 3 means it passed
     - grades == 0 means the student's code didn't compile. In this case, please double check if their code file exist, and if you can manually compile. If not, 0 is the score the student get
     - grades == 2 means the code compile, but one of the test cases doesn't match. In this case, please double check with the grading rubric below, and assign score accordingly.


## 2. Grading rubric

-2 point [Functionality] if the code compile, but either doesn't printout anything, or doesn't take into user's input. Then it gets 1 points in total

-1 point [Format] if one of the following happen, they get 2 points in total (note that if more than one of the following is incorrect, please list them on the comments section on cms, so that the students know that they should change their code for hw2, which is the extended program):
  - The printout full name is incorrect
  - The letter counting is incorrect
  - The 30 blank spaces before letter, and the 10 blank spaces after ':' is incorrect
  - The ordering of A-Z, then A-z is incorrect
  - There is no single quotation marks between letter


Something not take points off, (in these cases, just comment in on the cms to remind them would be good)
  - if there are extra or less white spaces between 'a' and ':'
  - if there are extra or less white spaces between "Full user name: " and the name
  - if there are extra or less white spaces between "Please type your name: "
  - if there are mis-spelling of "Letter counts (with everything mapped to lower case):", or "Letter counts (upper case separate from lower case):"