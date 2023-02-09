import os
import subprocess
import shutil
import time
from standard_output import *
import csv

OUTER_DIR= os.path.abspath(os.getcwd())

graded_netids = []
passed_netids = []
unpassed_netids = []
unpassed_netids_reasons = []
manual_check_netid = []

fields = ['netid', 'pass/fail', 'reason']
grades_file = []


def checkoutput(netid, output, expected_list):
     output_list = str(output.decode()).splitlines()
     for i in range(len(expected_list)):
          for j in range(len(expected_list[i])):
               if(not expected_list[i][j] in output_list[i] ):
                    graded_netids.append(netid)
                    unpassed_netids.append(netid)
                    reason = "output miss match\n"
                    reason += "\nYour output:"
                    reason += str(output.decode())
                    unpassed_netids_reasons.append(reason)
                    grades_file.append([str(netid), "2", reason]) # award 2 points because code compiled, but output mismatch
                    return False
     return True


def main():
     subfolders = [ f.path for f in os.scandir(OUTER_DIR) if f.is_dir() ]
     for x in subfolders:
          netid = x[(x.rfind('/') + 1):]
          if(netid == "__pycache__"):
               continue
          try:
               # 1. copy cpp file which we will use to compile
               print("\nGrading: " + netid +":") 
               dir = os.path.join(OUTER_DIR, x)
               mv_cmd = "cp 'My solution.cpp' solution_copy.cpp"
               ps = subprocess.Popen(mv_cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, cwd=dir)
               (output, err) = ps.communicate()  
               p_status = ps.wait()

               # 2. compile file
               p = subprocess.check_output(["g++", "-std=c++2a", "solution_copy.cpp", "-o", "solution_copy"], cwd=dir) 
               if(p):
                    graded_netids.append(netid)
                    unpassed_netids.append(netid)
                    unpassed_netids_reasons.append("Program unable to compile")
               
               # 3. check normal case for hw2
               cmd = "./solution_copy < hw2_norm.txt"
               shutil.copy(os.path.join(OUTER_DIR,"hw2_norm.txt"), x)
               print(f'checking normal case for {netid} (press ctrl-c if it gets stuck here to move on to next student)')
               ps = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, cwd=dir)
               output = ps.communicate()[0]
               ps.kill() # kill process after completed
               print(str(netid), ': output[0] -->', output, 'len output ==', str(output))
               check = checkoutput(netid, output, hw2_norm_standard_output)
               if(not check):
                    print(f'skipping edge case because {netid} didn\'t pass normal case')
                    continue

               # 4. check edge case for hw2
               cmd = "./solution_copy < hw2_edge.txt"
               shutil.copy(os.path.join(OUTER_DIR,"hw2_edge.txt"), x)
               print('checking edge case (press ctrl-c if it gets stuck here to move on to next student)')
               ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT, cwd=dir)
               output = ps.communicate()[0]
               ps.kill() # kill process after completed
               check = checkoutput(netid, output, hw2_edge_standard_output)
               if(not check):
                    continue
               
               # award full points to netid if reached till here
               passed_netids.append(netid)
               grades_file.append([str(netid), "3", "Good work!"])
          except:
               graded_netids.append(netid)
               unpassed_netids.append(netid)
               unpassed_netids_reasons.append("Grader unable to run. Check manually!")
               print(f"Grader unable to run on netid: " + netid +". Please check {netid}'s submission manually.")
               time.sleep(1)
               grades_file.append([str(netid), "0", "Grader unable to run"])
     print("-passed netids:", passed_netids)
     print("-unpassed netids:",unpassed_netids)
     print("-unpassed reasons: ",unpassed_netids_reasons)




if __name__ == "__main__":
     main()
     with open('grades.csv', 'w') as f:  
          # using csv.writer method from CSV package
          write = csv.writer(f)     
          write.writerow(fields)
          write.writerows(grades_file)