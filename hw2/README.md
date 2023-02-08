# hw2 grading direction

## 1. How to use autograder:
- download a batch of students' submitted assignment from cms.
     - under hw2 group 
     - select the students' netids of your grading group
     - then click Files on the top right corner of the page, under [Select Group Operations:]
- scp this folder to your ugclinux server
- scp the autograder script folder to your ugclinux server as well
- all the four files should sit under the directory of Submissions 
     Your directories should look as follows:
     
     -- Submissions

     ----- hw2_edge.txt

     ----- hw2_norm.txt

     ----- hw2grader.py

     ----- standard_output.py

     ----- netid_1

     ---------- 'My output file.txt'

     ---------- 'My solution.cpp'

     ----- netid_2

     ---------- 'My output file.txt'

     ---------- 'My solution.cpp'

     ....

- run the autograder by calling `python3 hw2grader.py`
- you may notice the autograder getting stuck on a submission. in this, press ctrl-c and it will move on to grading the next student. please manually check the student's submission if this happens.
- after running the autograder, there is a grades.csv generated with the score of each student's code
     - grades == 3 means it passed
     - grades == 2 means the code compiled, but one of the test cases doesn't match. In this case, please double check with the grading rubric below, and assign score accordingly.
     - grades == 0 means the student's code didn't compile. In this case, please double check if their code file exist, and if you can manually compile. If not, 0 is the score the student get
     


## 2. Grading rubric

- 3 points if code compiles and both test cases pass
- 2 points if the code compiles, but one of the following happens:
     - The printout full name is incorrect
     - The full name is split incorrectly (e.g., more/fewer lines than parts of the name. remember the name should be split among as many lines as there are parts to it.)
     - The letter counting is incorrect
     - The 10 spaces before "Name 1:..." or the 30 blank spaces before letter under letter counts or the 10 blank spaces after ':' under letter counts is incorrect
     - The output doesn't end with a way to continue inputting names (e.g., "Please type your name: ")
- 1 point if the code compiles but either doesn't print out anything, or doesn't take user input, then it gets only 1 point in total.

Do not take points off if: 
  - There is no single quotation marks between letter
  - if there are extra or less white spaces between 'a' and ':'
  - if there are extra or less white spaces between "Full user name: " and the name
  - if there are extra or less white spaces between "Please type your name: "
  - if there are mis-spelling or varied capitalizations of "Letter counts (with everything mapped to lower case):", or "Letter counts (upper case separate from lower case):"

_in these cases, just comment on the submission to remind them would be good_