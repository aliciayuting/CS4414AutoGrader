import os
import subprocess
import shutil
from standard_output import *
import csv

OUTER_DIR= os.path.abspath(os.getcwd())

graded_netids = []
passed_netids = []
unpassed_netids = []
unpassed_netids_reasons = []

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
                    reason += output_list[i]
                    unpassed_netids_reasons.append(reason)
                    grades_file.append([str(netid), "2", reason])
                    return False
     return True
          


def main():
     subfolders = [ f.path for f in os.scandir(OUTER_DIR) if f.is_dir() ]
     for x in subfolders:
          netid = x[(x.rfind('/') + 1):]
          if(netid == "__pycache__"):
               continue
          try:
               print("- Grading: " + netid)
               dir = os.path.join(OUTER_DIR, x)
               mv_cmd = "mv 'My source file.cpp' hello.cpp"
               ps = subprocess.Popen(mv_cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, cwd=dir)
               (output, err) = ps.communicate()  
               p_status = ps.wait()

               p = subprocess.check_output(["g++", "-std=c++2a", "hello.cpp", "-o", "hello"], cwd=dir) 
               if(p):
                    graded_netids.append(netid)
                    unpassed_netids.append(netid)
                    unpassed_netids_reasons.append("Program unable to compile")
               cmd = "./hello < hw1_norm.txt"
               shutil.copy(os.path.join(OUTER_DIR,"hw1_norm.txt"), x)
               ps = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, cwd=dir)
               output = ps.communicate()[0]
               check = checkoutput(netid, output, hw1_norm_standard_output)
               if(not check):
                    continue

               cmd = "./hello < hw1_edge.txt"
               shutil.copy(os.path.join(OUTER_DIR,"hw1_edge.txt"), x)
               ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT, cwd=dir)
               output = ps.communicate()[0]
               check = checkoutput(netid, output, hw1_edge_standard_output)
               if(not check):
                    continue
               passed_netids.append(netid)
               grades_file.append([str(netid), "3", "Good work!"])
          except:
               graded_netids.append(netid)
               unpassed_netids.append(netid)
               unpassed_netids_reasons.append("Grader unable to run")
               print("Grader unable to run on netid: " + netid)
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
