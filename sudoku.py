#!/usr/bin/python3

import sys, getopt
#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
# num_hours_i_spent_on_this_assignment = 20
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
# Everything is OK.
"""

"""
#####################################################
#####################################################

def main(argv):
   inputfile = ''
   N=0
   try:
      opts, args = getopt.getopt(argv,"hn:i:",["N=","ifile="])
   except getopt.GetoptError:
      print ('sudoku.py -n <size of Sodoku> -i <inputputfile>')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('sudoku.py  -n <size of Sodoku> -i <inputputfile>')
           sys.exit()
       elif opt in ("-n", "--N"):
           N = int(arg)
       elif opt in ("-i", "--ifile"):
           inputfile = arg
   instance = readInstance(N, inputfile)
   toCNF(N,instance,inputfile+str(N)+".cnf")




def readInstance (N, inputfile):
    if inputfile == '':
        return [[0 for j in range(N)] for i in range(N)]
    with open(inputfile, "r") as input_file:
        instance =[]
        for line in input_file:
            number_strings = line.split() # Split the line on runs of whitespace
            numbers = [int(n) for n in number_strings] # Convert to integers
            if len(numbers) == N:
                instance.append(numbers) # Add the "row" to your list.
            else:
                print("Invalid Sudoku instance!")
                sys.exit(3)
        return instance # a 2d list: [[1, 3, 4], [5, 5, 6]]




def makeMapping(N):
  literal = 1
  literalDict = {}
  for i in range(1, N+1):
    for j in range(1, N+1):
      for k in range(1, N+1):
        key = (i, j, k)
        literalDict[key] = literal
        literal = literal + 1
  return literalDict




""" Question 1 """
def toCNF (N, instance, outputfile):
    """ Constructs the CNF formula C in Dimacs format from a sudoku grid."""
    """ OUTPUT: Write Dimacs CNF to output_file """
    output_file = open(outputfile, "w")
    "*** YOUR CODE HERE ***"

    #Display input values
    print("Converting to .cnf")
    print("N is: %d" % N)
    print("Instance is: %s" % instance)
    print("Output file name is: %s" % outputfile)

    #Create literal map for clause printing
    litDict = makeMapping(N)

    #Write CNF file header
    output_file.write("c\t%s\n" % outputfile)
    output_file.write("c\n")
    #number of literals is N^3 --> in python N**3 
    numLit = N**3
    output_file.write("p cnf %d " % numLit)

    #Initialize count of number of clauses
    clauseCount = 0

    C_1 = []

    #generate clause 1
    for i in range(1, N+1):
      for j in range(1, N+1):
        #C_1 has a unique clause for each i, j
        clause = []
        for k in range(1, N+1):
          #literal[1] is 1 if NOT is desired; and 0 otherwise
          literal = [(i, j, k), 0]
          clause.append(literal)
        C_1.append(clause)
        clauseCount = clauseCount + 1

    C_2 = []

    for i in range(1, N+1):
      for j in range(1, N+1):
        for k in range(1, N+1):
          for l in range(k+1, N+1):
            leftLit = [(i, j, k), 1]
            rightLit = [(i, j, l), 1]
            clause = [leftLit, rightLit]
            C_2.append(clause)
            clauseCount = clauseCount + 1

    C_3 = []

    for i in range(1, N+1):
      for j1 in range(1, N+1):
        for j2 in range(j1+1, N+1):
          for k in range(1, N+1):
            leftLit = [(i, j1, k), 1]
            rightLit = [(i, j2, k), 1]
            clause = [leftLit, rightLit]
            C_3.append(clause)
            clauseCount = clauseCount + 1

    C_4 = []

    for j in range(1, N+1):
      for i1 in range(1, N+1):
        for i2 in range(i1+1, N+1):
            for k in range(1, N+1):
              leftLit = [(i1, j, k), 1]
              rightLit = [(i2, j, k), 1]
              clause = [leftLit, rightLit]
              C_4.append(clause)
              clauseCount = clauseCount + 1

    C_5 = []

    for i in range(0, N):
      for j in range(0, N):
          if instance[i][j] != 0:
            #since i and j in the puzzle start at 1, must increment these indicies by 1
            C_5.append([[(i+1, j+1, instance[i][j]), 0]])
            clauseCount = clauseCount + 1

    C_Total = []
    C_Total.extend(C_1)
    C_Total.extend(C_2)
    C_Total.extend(C_3)
    C_Total.extend(C_4)
    C_Total.extend(C_5)

    #OUTPUT LOGIC
    output_file.write("%d\n" % clauseCount)

    for i in range(0, len(C_Total)):
      for j in range(0, len(C_Total[i])):
        if C_Total[i][j][1] == 0:
          output_file.write("%d " % litDict[C_Total[i][j][0]])
        else:
          output_file.write("%d " % -litDict[C_Total[i][j][0]])
      output_file.write("0\n")

    "*** YOUR CODE ENDS HERE ***"
    output_file.close()




if __name__ == "__main__":
   main(sys.argv[1:])
