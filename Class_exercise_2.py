NAME=[]
GRADE=[]
while True:
    INPUT=input("enter S for search or A for add:")


    if INPUT=='S':
        LENGTH=len(NAME)
        b1=int(input("Please enter the index or ID of student:"))

        if b1>LENGTH :
            print('Enter a correct number')
        else:
            print('The grade for',NAME[b1],'is',GRADE[b1] )
        
                  
    elif INPUT=='A':
        a1=input("Please enter your name  :")
        a2=input("Please enter your grade  :")
        NAME.append(a1)
        GRADE.append(a2)
       
    else: 
        print("Sorry, I did not understand that. Please try it again.")
        continue
    
