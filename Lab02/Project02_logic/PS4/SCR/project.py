import copy
from enum import Enum
#                   ___________________________________________________________
#redefined class 
class Definition(Enum):
    OR_OPERATOR = ' OR '
    YES_OPERATOR = 'YES'
    NO_OPERATOR = 'NO'
    _SYMBOLEMPTY_CLAUSE = '{}'
    _SYMBOLNOT_OPERATOR = '-'
#                   ___________________________________________________________
#Class for checking the condition of clauses
class Checking(Enum):
    # is negative Clause, check if 2 clauses are opposite. eg A vs -A
    def Check_negative(clause):
        for literal in clause:
            if(-literal in clause): # It's opposite
                return True
        return False

    # Check if clause already exists in new clause list (before adding), which is existed in this loop and existed in (original KB and negative alpha)
    def Check_Exist(clause, list_clauses):
        if(clause in list_clauses):     # if existed 
            return True
        else:
            return False

    # check for null clause. eg A v B v -B is useless or A v A v C is useless, which is existed in many loops before
    def Check_List(clause, new_clauses):
        for new in new_clauses:
            if(Checking.Check_Exist(clause, new)):
                return True
        return False
    
    # check for all condition of clauses before adding to new_clauses for Data to write out 
    def Check_all(clause, list_clauses, origin_clauses, new_clause):
        return (not Checking.Check_negative(clause) and not Checking.Check_Exist(clause, list_clauses) and\
                not Checking.Check_Exist(clause, origin_clauses) and not Checking.Check_List(clause, new_clause))
        # not have all these conditions to be able to add 
#                   ___________________________________________________________
#class dealing with possible necessary work for clauses in KB and alpha
class Execute_problem(Enum):
    #Sorting clauses 
    def Alphabet_sort(clause: list):
            return sorted(list(set(copy.deepcopy(clause))), key=lambda kv:kv[-1])

    #num to character
    def convert_Literal(num):
        a_temp = ord('A') - 1   #just ord('A')(= 1) - 1 = 0
        if(num < 0):
            a_temp = Definition._SYMBOLNOT_OPERATOR.value + chr(-num)
        else:
            a_temp = chr(num)
        return a_temp           #return the character after converting 

    #character to num
    def convert_Number(literal):
        a_temp = ord('A') - 1   #just ord('A')(= 1) - 1 = 0
        if(len(literal) == 1):
            a_temp = ord(literal[0])
        else:
            a_temp = -(ord(literal[1]))
        return a_temp           #return the number after converting
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Read Data from input file
def Read_Data(filename_input: str):
    with open(filename_input, "r") as input:
        alpha = []
        arr = []
        for clause in input.readline()[:-1].rstrip("\n").split(Definition.OR_OPERATOR.value):
            arr.append(clause.strip())    
        arr = Execute_problem.Alphabet_sort(arr)    #Clauses're sorted 
        for al in arr:
            alpha.append(Execute_problem.convert_Number(al))    # convert to number to resolve easily
        # is empty file
        if(alpha == ""):
            return [], []

        read_num_KB = int(*input.readline()[:-1].rstrip("\n").splitlines())   #read the number that's number of clauses in KB
        # is number of KB < 0
        if(read_num_KB < 0):
            return [], []

        KB = []
        for i in range(read_num_KB):
            array = []
            arr = []
            for clause in input.readline().rstrip("\n").split(Definition.OR_OPERATOR.value):
                array.append(clause.strip())    # convert to number to resolve easily
            array = Execute_problem.Alphabet_sort(array)    #Clauses're sorted 
            for kb in array:
                arr.append(Execute_problem.convert_Number(kb))
            KB.append(arr)      
      
    input.close()
    return KB, alpha

#Write Data for output file
def Write_Data(filename_output, Data, isEntailalbe):
    with open(filename_output, "w") as output:
        for new_array in Data:
            output.write(str(len(new_array)) + '\n')    # write the number of clauses 
            for clause in new_array:
                if(clause != []):
                    write_Clause = []
                    for literal in clause:
                        write_Clause.append(Execute_problem.convert_Literal(literal))    #convert to literal before write clause 
                    output.write(Definition.OR_OPERATOR.value.join(write_Clause) + '\n')    #connect clause for write with ' OR ' after convert
                else:
                    output.write(Definition._SYMBOLEMPTY_CLAUSE.value + '\n')
                    #Not ended, still show all generated clause from Data in the last loop => don't break
           
        #write the result 
        if(isEntailalbe):
            output.write(Definition.YES_OPERATOR.value)
        else:
            output.write(Definition.NO_OPERATOR.value)

    output.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------
#returns the set of all possible clauses obtained by resolving its two input 
def PL_Resolve(Ci, Cj):
    clause_Ci = copy.deepcopy(Ci)
    clause_Cj = copy.deepcopy(Cj)
    isResolve = False           # flag for check it still resolved or not 
    
    for i in clause_Ci:         # remove literal v negative(literal), ex: A v -A
        if(-i in clause_Cj):
            isResolve = True
            clause_Ci.remove(i)
            clause_Cj.remove(-i)
            break
        for j in clause_Cj:
            if i == j:
                clause_Ci.remove(i)     # Reduce the same elements

    if(isResolve):
        clause_Ci.extend(clause_Cj)
        array = set(clause_Ci)          #create array 

        cloneCi = []
        sort_arr = []
        for literal in array:
            sort_arr.append(Execute_problem.convert_Literal(literal))    #convert to character for sorting
        sort_arr = Execute_problem.Alphabet_sort(sort_arr)                    #Clauses're sorted before return
        for new_literal in sort_arr:
            cloneCi.append(Execute_problem.convert_Number(new_literal))       #convert to number for continuing execute 

        return cloneCi
    else:
        return "none"

def PL_Resolution(KB, alpha):
    # the set of clauses in the CNF representation of KB ^ not(alpha)
    clauses = copy.deepcopy(KB) 
    for literal in alpha:
        clauses.append([-literal])  # append negative of each literal in form array (literal is number now)
    
    # consists of the result of clause after execute (KB and negative alpha)
    Data = []
    
    # Start loop
    while True:
        new_clauses = []
        clauses_pairs = []

        for i in range (len(clauses)):
            for j in range (i + 1, len(clauses)):
                clauses_pairs.append((clauses[i], clauses[j]))  # (Ci, Cj)

        for pair in clauses_pairs:
            if(pair[0] == pair[1]): #(Ci == Cj)
                continue
            resolvents = PL_Resolve(*pair)
            if(resolvents != "none" and Checking.Check_all(resolvents, new_clauses, clauses, Data)):
            # is resolved and drived into 1 clause
                new_clauses.append(resolvents)
        
        # first, add new even 
        Data.append(new_clauses)    # add the array of literal (clause)
        # then check if it's empty or contains [] to show the result
        if([] in new_clauses):
            return True, Data       # It has an empty clause
        if(len(new_clauses) == 0):
            return False, Data      # clause don't have anything (including literals)
        
        #add new_clauses back to clauses 
        clauses.extend(new_clauses)
