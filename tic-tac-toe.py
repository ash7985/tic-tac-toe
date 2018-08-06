print('\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tTIC-TAC-TOE')
print(' \n\n\t\t\t\t\t WELCOME! YOU BOTH HOPE YOU WILL ENJOY THIS GAME!\n\t\t\t\t\t\t\t SO BEST OF LUCK !!!!')
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def board():

    global li

    print('\n\n\t\t\t%s   |   %s   |   %s' % (li[0], li[1], li[2]))
    print('\t\t\t--------------------')
    print('\t\t\t%s   |   %s   |   %s' % (li[3], li[4], li[5]))
    print('\t\t\t--------------------')
    print('\t\t\t%s   |   %s   |   %s' % (li[6], li[7], li[8]))


def player(l, p):

    global li
    li[l-1] = p
    board()


def check():

    global li

    if li[0] == li[1] == li[2] or li[3] == li[4] == li[5] or li[6] == li[7] == li[8] :
        p = True
    elif li[0] == li[3] == li[6] or li[1] == li[4] == li[7] or li[2] == li[5] == li[8] :
        p = True
    elif li[0] == li[4] == li[8] or li[2] == li[4] == li[6] :
        p = True
    else:
        p = False
    return p


print("\n\n\t\tINSTRUCTIONS:")
print("\n\t\t\t1. Treat the board like a matrix.")
print("\n\t\t\t2. Enter the location according to the numbers present in your desired blocks.")
print("\n\t\t\t3. Use the symbols you want except the numbers from 1-9 ")

p1 = input('\n\t\t\tHEY PLAYER 1,Please enter your name =>   ')

s = input('\n\t\t\tand your symbol is ???  ')

p2 = input('\n\t\t\tHEY PLAYER 2,Please enter your name =>   ')

f = input("\n\t\t\tand your's is ???  ")

while s == f:
    f = input('\n\t\t\t\t\tThis symbol is already used by %s \n\t\t\t\t\tSo please choose another one => ' % p1)

board()

for i in range(0, 4):
   
   
   
   # global li
    print("\n\t\t%s's Turn!" % p1)
    loc = int(input('\n\t\tEnter the location.'))
    while li[loc-1] == s or li[loc-1] == f:
        loc = int(input('\n\t\t\tOOPS!! YOU HAVE ENTERED WRONG LOCATION | PLEASE ENTER THE VALID LOCATION =>  '))
    player(loc, s)
    t = check()
    if t is True:
        print('\n\t\t\t\t%s WINS' % p1)
        break
    print("\n\t\t\t%s's Turn!" % p2)
    loc = int(input('\n\t\tEnter the location.'))
    while li[loc - 1] == s or li[loc - 1] == f:
        loc = int(input('\n\t\t\t OOPS!! YOU HAVE ENTERED WRONG LOCATION | PLEASE ENTER THE VALID LOCATION =>  '))
    player(loc, f)
    t = check()
    if t is True:
        print('\n\t\t\t\t%s WINS' % p2)
        break
else:
    print("\n\t\t\t\tIT'S A DRAW\n\t\t\t\t WELL PLAYED BOTH OF YOU")
