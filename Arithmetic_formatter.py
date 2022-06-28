def arithmetic_arranger(arithmetic_problems,optional_display= False):
    # Maximum 5 arithmetic problems can be given
    if len(arithmetic_problems) > 5:
        return print('Error: Too many problems')
        
    #Acceptable operators
    operators=['+','-']
    
    #We define 3 lists; one for each line we will split
    
    list_1=[]
    list_2=[]
    list_3=[]
    list_4=[]
    
    #We set the condition for acceptable operators
    for values in arithmetic_problems:
         problem_operator = values.split(" ")
        
         if problem_operator[1] not in operators:
             return print("Error: Operator must be '+' or '-'.")
        
         #Now, we assign the numbers 
         number_1=problem_operator[0]
         number_2=problem_operator[2]
        
         #Those numbers should be only digit
         if number_1.isdigit()== False or number_2.isdigit()==False:
             return print(print("Error: Numbers must only contain digits"))
        
        
        #In addition, each operand must contain up to 4 digits
         if len(number_1) > 4 or len(number_2) > 4:
            return print("Error: Numbers cannot be more than four digits.")
       
         #Now we have to identify the longest operand and adjust the problem to feet the criteria in the exercise
         maximum_filling_space=max(len(length) for length in problem_operator)
         dash='-'
         space=''
        
         #Append each first operand and we add 4 spaces between each operation
         list_1.append(number_1.rjust(maximum_filling_space+2)+space*4)
         #Append the operator, space and second number
         list_2.append(problem_operator[1]+space + number_2.rjust(maximum_filling_space+1)+space*4)
         #Append the dash line
         list_3.append(dash * (maximum_filling_space+2)+space*4)
         #Append the result in case the optional display is True
         result=str(eval(values))
         list_4.append(result.rjust(maximum_filling_space+2)+space*4)
        
         # We also have to transform each list to a string before we display it
         list_1=''.join(map(str, list_1))
         list_2 =''.join(map(str, list_2))
         list_3 =''.join(map(str, list_3))
         list_4 =''.join(map(str, list_4))
        
         #Finally we have to take into account if the optional _display is True
         if optional_display == True:
             final_result = list_1 + "\n" + list_2 + "\n"+ list_3+ "\n"+ list_4
         # If second argument false, only print operation
         if optional_display == False:
             final_result = list_1 + "\n" + list_2 + "\n"+ list_3
         print(final_result)
         return final_result
        
 #Let's check if the function works
arithmetic_arranger( ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)   
