from workplace import nearestAirport
import sys

# dont touch this stuff

numtasks = 4
variables = {}
perfect = True

for i in range(1, numtasks+1):
  testCase = open(("TestCases/testCase" + str(i) + ".py"), "r").read().splitlines()
  testCase = [[int(i.split()[0]), int(i.split()[1])] for i in testCase]

  print("---------- test" + str(i) + " ----------")
  variables["t{0}t".format(i)] = open(("TaskResults/task" + str(i) + "Test.py"), "r").read()

  variables["t{0}a".format(i)] = nearestAirport(testCase[0], testCase[1], testCase[2], testCase[3])

  if variables["t{0}t".format(i)] == variables["t{0}a".format(i)]:
    print("|         Success         |")
  else:
    print("|       You failed.       |")
    perfect = False
  
print("---------------------------")

if perfect == True:
  print("\nCongratulations! You successfully completed PPSC_task_2")
  
