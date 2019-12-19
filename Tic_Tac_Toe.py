a=['1','2','3','4','5','6','7','8','9']
n=["",""]
flag=i=0
##########################################################################################################################
def Display():
    #print('   |   |   ')
    print(' {} | {} | {} '.format(a[0],a[1],a[2]))
    #print('   |   |   ')
    print('---|---|---')
    #print('   |   |   ')
    print(' {} | {} | {} '.format(a[3], a[4], a[5]))
    #print('   |   |   ')
    print('---|---|---')
    #print('   |   |   ')
    print(' {} | {} | {} '.format(a[6], a[7], a[8]))
    #print('   |   |   ')
##########################################################################################################################
def ListInitializer():
    i=0
    for i in range(0,9):
        a[i]= str(i+1)
    i=0
##########################################################################################################################
def Details():
    print("--:TIC TAC TOE:--\n\n")
    n[0]=raw_input("Enter name of Player 1:- ")
    n[1]=raw_input("Enter name of Player 2:- ")
    print("\n\nCROSS :- X FOR {}".format(n[0]))
    print("OVAL :- O FOR {}".format(n[1]))
    print("\n\n")
    print("# KEY-POSITION # FOR PLACING X or O ")
    Display()
    print("\n\n")
    return n
##########################################################################################################################
def Play():
    j=0
    for j in range(0,7,3):
        if(a[j]==a[j+1] and a[j+1]==a[j+2]):
            return(1)
    j=0
    for j in range(0,3):
        if(a[j]==a[j+3] and a[j]==a[j+6]):
            print("true")
            return(1)
    if(a[0]==a[4] and a[0]==a[8]):
        return(1)
    if(a[2]==a[4] and a[4]==a[6]):
        return(1)
    return 0
###########################################################################################################################
ch=1
#Details()
while(ch==1):
    ListInitializer()
    n=Details()
    flag=0
    i=0
    for i in range(0,9):
        k=1
        if(i%2==0):
            while (k==1):
                pos = int(raw_input("Enter position no :-"))
                if (a[pos - 1] == str(pos)):
                    a[pos - 1] = 'x'
                    k = 0
                else:
                    print("Place already taken, try another position ")

        else:
            while (k == 1):
                pos = int(raw_input("Enter position no :-"))
                if (a[pos - 1] == str(pos)):
                    a[pos - 1] = 'o'
                    k = 0
                else:
                    print("Place already taken, try another position ")
        Display()
        flag=Play()
        if(flag==1):
            if(i%2==0):
                print("     **CONGRATULATIONS**")
                print("   {} WINS THE GAME \n".format(n[0]))
            else:
                print("     **CONGRATULATIONS**")
                print("   {} WINS THE GAME \n".format(n[1]))
            break
    if(flag==0):
        print("**OOPS**")
        print("ITS A DRAW\n")
    flag=0
    c=raw_input("**DO YOU WANT TO CONTINUE** - [YES/NO] ")
    if(c=="YES"):
        ch=1
    else:
        ch=0
