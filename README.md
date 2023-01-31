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
     - Submissions

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
     - grades == 1 means one of the test cases doesn't match. In this case, please double check with the grading rubric below, and assign score accordingly.


## 2. Grading rubric

-1 point if one of the following happen, do not double count each issue(since we have two test cases), max points off is -2:
  - The printout full name is incorrect
  - The letter counting is incorrect
  - The 30 blank spaces before letter, and the 10 blank spaces after ':' is incorrect
  - The ordering of A-Z, then A-z is incorrect