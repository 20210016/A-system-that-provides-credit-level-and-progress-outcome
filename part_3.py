
# inisialize variables
PASS = 0
DEFER = 0
FAIL = 0
progress = 0
Trailer= 0
Retriever = 0
Exclude = 0
progress_list = []
Trailer_list = []
Retriever_list  = []
Exclude_list = []
prog = 0
trai= 0
retr = 0
excl = 0
progress_input= []
Trailer_input= []
Retriever_input= []
Exclude_input= []
star = "  *  "


def main():
    global prog, trai, retr, excl
    credit=[0,20,40,60,80,100,120] 

            
#Getting inputs         
    try:
        PASS = int(input('Enter the credits at pass :'))
        if PASS not in credit:
            print('Out of range')
            print()
        
                    
        else:
            DEFER = int(input('Enter the credits at defer :'))
            if DEFER not in credit:
                print('Out of range')
                print()
            
            else:
                FAIL = int(input('Enter the credits at fail :'))
                if FAIL not in credit:
                    print('Out of range')
                    print()
#cheking errors
    except ValueError:
            print("integer required ")
    inputs=(PASS , DEFER , FAIL)            
    if PASS == 120 :
        print ("progress")
        prog += 1
        progress_list .append (star)
        progress_input.append (inputs)
    elif PASS == 100:
        print ("progress (module trailer)")
        trai += 1
        Trailer_list .append (star)
        Trailer_input.append (inputs)
        
    elif PASS == 80 and (DEFER == 0 or DEFER == 20 or DEFER == 40) and( FAIL== 40 or FAIL == 20 or FAIL == 0):
        print ("do not progress- module retriever")
        retr += 1
        Retriever_list .append (star)
        Retriever_input.append (inputs)
        
    elif PASS ==60 and (DEFER ==60 or DEFER==40 or DEFER== 20 or DEFER== 0) and (FAIL==0 or FAIL== 20 or FAIL== 40 or FAIL==60):
        print ("do not progress - module retriever")
        retr += 1
        Retriever_list .append (star)
        Retriever_input.append (inputs)
        
    elif PASS == 40 and (DEFER == 80 or DEFER== 60 or DEFER ==40 or DEFER== 20) and (FAIL == 0 or FAIL== 20 or FAIL == 40 or FAIL==60):
        print ("do not progress- module retriever")
        retr += 1
        Retriever_list .append (star)
        Retriever_input.append (inputs)
        
    elif PASS == 40 and DEFER== 0 and FAIL== 80:
        print ("exclude")
        excl += 1
        Exclude_list .append (star)
        Exclude_input.append(inputs)
        
    elif PASS== 20 and (DEFER== 100 or DEFER== 80 or DEFER== 60 or DEFER== 40 )and( FAIL==0 or FAIL== 20 or FAIL== 40 or FAIL==60):
        print ("do not progress- module retriever")
        retr += 1
        Retriever_list .append (star)
        Retriever_input.append (inputs)
        
    elif PASS== 20 and( DEFER == 20 or DEFER == 0) and (FAIL== 80 or FAIL== 100):
        print ("exclude")
        excl += 1
        Exclude_.append (star)
        Exclude_input.append(inputs)
        
    elif PASS==0 and (DEFER== 120 or DEFER== 100 or DEFER ==80 or DEFER==60) and (FAIL== 0 or FAIL==20 or FAIL== 40 or FAIL== 60):
        print ("Do not progress- module retriever :")
        retr += 1
        Retriever_list .append (star)
        Retriever_input.append (inputs)
        
    elif PASS ==0 and (DEFER== 40 or DEFER == 20 or DEFER == 0 )and( FAIL== 80 or FAIL== 100 or FAIL== 120):
        print ("exclude")
        excl += 1
        Exclude_list .append (star)
        Exclude_input.append(inputs)
        
    elif print ("invalid input"):
        print()

    if version.upper() == "SM":
            again()

#asking another round or exit    

def again():
        choice= input("Would you like to enter another set of data? Enter 'Y' for yes or 'Q' to quit and view result: ").upper()
        print()
        if choice == "Y":
            main()
        elif choice == "Q":
#Horizontal histogram
            print ("----------------------------------------------------------------------------")
            print ("Horizontal Histogram")
            print("progress  : ",len(progress_list ),":" , star * (int(len(progress_list ))))
            print("Trailer   : ",len(Trailer_list ),":",star *  (int(len(Trailer_list ))))
            print("Retriever : ",len(Retriever_list ),":",star *  (int(len(Retriever_list ))))
            print("Exclude   : ",len(Exclude_list ),":",star * (int(len(Exclude_list ))))
            print("\n",(int(len(progress_list )))+( int(len(Trailer_list )))+ (int(len(Retriever_list )))+ (int(len(Exclude_list ))),"out comes in total.")
            print("--------------------------------------------------------------------------------")
#Vertical histogram
            print('vertical histogram')
            print()

            print (' progress   '' Trailer   '' Retriever   '' Excluded')

            for x in range(max(prog,trai,retr,excl)):
                print("   {0}         {1}            {2}            {3}".format(
                    '*' if x < prog else ' ',
                    '*' if x < trai else ' ',
                    '*' if x < retr else ' ',
                    '*' if x < excl else ' '))
            print()
            print("\n",(len(progress_list ))+( len(Trailer_list ))+ (len(Retriever_list ))+ (len(Exclude_list )),"out comes in total.")
            print("-"*70)
#list of the outputs
            for a in progress_input:
                print ("progress",a)
            for b in Trailer_input:
                print ("Trailer",b)
            for c in Retriever_input:
                print("Retriever",c)
            for d in Exclude_input:
                print("Exclude",d)
#Asking the version
while True:
    version =input("If you are a staff member please enter SM ,\nIf you are a student please enter S: ") 

    main()
