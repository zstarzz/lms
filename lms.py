import os
import getpass
import csv
import time
import isbnlib
import string


os.system('mode con: cols=155 lines=55')
dir = os.path.dirname(os.path.realpath(__file__))
ndir = dir.replace("\\", "/")
bpath = ndir + '/books.csv'
bpath1 = ndir + '/books1.csv'
ppath = ndir + '/pass.txt'

###################################################
#----------------Formating------------------------#
barsp = 140
isbnsp = 10
titlesp = 71
authorsp = 37

headsp = 60

dynamicWsT = 75
dynamicWsA = 42


def dynamicWS(line, static):
    linelen = len(line)
    x = ' '
    y = static - linelen
    sp = x * y
    line = line + sp
    return line


#----------------Formating------------------------#
###################################################

def login():
    os.system('cls')
    pin = getpass.getpass(' Please enter the 4-digit pin to continue:  ')
    f = open(ppath)
    ptxt = f.read()
    if pin == ptxt:
        welcome()

    else:
        print(' Incorrect pin, try again')
        print('\n')
        time.sleep(0.5)
        login()


def viewbooks():
    os.system("cls")
    print('\n')
    print(' ' * headsp,'View Books')
    print(' ' * headsp ,'----------')
    print('\n')
    f = open(bpath)
    k = 0
    for row in csv.reader(f):
        k += 1
    f.close()

    if k != 0:

        print(' ISBN', ' '*isbnsp , 'TITLE', ' '*titlesp, 'AUTHOR', ' '*authorsp, 'QTY')
        print('\n')
        print('', '-' * barsp)
        f = open(bpath)
        for row in csv.reader(f):

            isbn = row[0]
            title = dynamicWS(row[1], dynamicWsT)
            author = dynamicWS(row[2], dynamicWsA)
            qty = row[3]

            print('', isbn,' ', title,' ', author,' ', qty)
            print('', '-' * barsp)

        f.close()

        ret = input('\n Press Enter to go back... ')
        if ret == "b":
            welcome()
        else:
            welcome()

    else:
        print("\n"' No books found!')
        print("\n"' Taking you back to the home screen')
        time.sleep(2)
        welcome()



def searchbooks():
    os.system("cls")
    print('\n')
    print(' ' * headsp,'Search Books')
    print(' ' * headsp,'------------')
    print('\n')
    print('\n')
    print(' Search by:')
    print('\n')
    print(' 1. ISBN ')
    print(' 2. Title')
    print(' 3. Author')
    print('\n')

    key = input(' Choose an option: ')

    if key == '1':
        print('\n')
        ss = input(' Enter ISBN: ').replace('-', '')

    elif key == '2':
        print('\n')
        ss = string.capwords(input(' Enter Title: '))

    elif key == '3':

        print('\n')
        ss = string.capwords(input(' Enter Author: '))

    else:
        welcome()

    ikey = int(key) - 1
    result = False

    inp = open(bpath, 'r')
    k = 0
    for row in csv.reader(inp):
        if row[ikey] == ss.strip():
            k += 1

    if k > 0 :
        print('\n')
        print(' ISBN', ' ' * isbnsp, 'TITLE', ' ' * titlesp, 'AUTHOR', ' ' * authorsp, 'QTY')
        print('', '-' * barsp)
    inp.close()
    inp = open(bpath, 'r')

    for row in csv.reader(inp):
        if row[ikey] == ss.strip():
            result = True

            isbn = row[0]
            title = dynamicWS(row[1], dynamicWsT)
            author = dynamicWS(row[2], dynamicWsA)
            qty = row[3]

            print('', isbn, ' ', title, ' ', author, ' ', qty)
            print('', '-' * barsp)

    print('\n')

    if result is False:
        print(' No results matched your search...')

    print('\n')
    sagain = input(' Search again? (y/n): ')

    if sagain == 'y':
        searchbooks()
    else:
        time.sleep(1)
        welcome()




def insertbook():
    os.system("cls")
    print('\n')
    print(' ' * headsp, 'Insert Book')
    print(' ' * headsp, '-----------')
    print('\n')
    print('\n')

    books = []

    while True:
        isbn = input("\n"' Enter ISBN: ').replace('-', '')
        ilength = len(isbn)
        digit = str.isdigit(isbn)
        if ilength == 13 and digit is True:

            try:
                book = isbnlib.meta(isbn)
                title = book['Title']
                author = book['Authors'][0]

                print('\n')
                print(' Title: ', title)
                print('\n')
                print(' Author: ', author)
                print('\n')
            except:
                print('\n')
                print(' ISBN number not found in Database')
                print('\n')
                man = input(' Would you like to enter the book details manually?(y/n): ')
                if man == 'y':
                    print('\n')
                    print('ISBN:',isbn)
                    print('\n')
                    title = string.capwords(input(' Title: '))
                    print('\n')
                    author = string.capwords(input(' Author: '))
                    print('\n')

                else:
                    welcome()


            print(' Insert with these details?')
            print('\n')
            decsion = input(' Yes(Enter), No(n): ')

            if decsion == '':

                #inp = open(bpath, 'r')
                #for row in csv.reader(inp):
                #   if row[0] == isbn:

                qty = 1

                books.append(isbn)
                books.append(title)
                books.append(author)
                books.append(qty)

                with open(bpath, 'a', newline='\n') as csv_b:
                    writer = csv.writer(csv_b)
                    writer.writerow(books)

                print('\n')
                print(' Successfully inserted...')
                time.sleep(1)
                welcome()
            else:
                print('\n')
                print(' Returning to Home Screen')
                time.sleep(2)
                welcome()

            break
        else:
            if isbn != '':
                if ilength != 13:
                    print(' ISBN number must be 13 digits long')
                    if digit is False:
                        print(' ISBN must only contain numbers')
                else:
                    if digit is False:
                        print(' ISBN must only contain numbers')
            else:
                welcome()
                break


def deletebook():
    os.system("cls")
    print('\n')
    print(' ' * headsp, 'Delete Books')
    print(' ' * headsp, '------------')
    print('\n')
    print('\n')

    isbn = input(' Enter ISBN: ')
    isbn = isbn.strip()
    ilength = len(isbn)
    digit = str.isdigit(isbn)
    if ilength == 13 and digit is True:

        result = False
        inp = open(bpath, 'r')
        for row in csv.reader(inp):
            if row[0] == isbn:
                result = True
                print('\n')
                print(' ISBN', ' ' * isbnsp, 'TITLE', ' ' * titlesp, 'AUTHOR', ' ' * authorsp, 'QTY')
                print('', '-' * barsp)

                isbn = row[0]
                title = dynamicWS(row[1], dynamicWsT)
                author = dynamicWS(row[2], dynamicWsA)
                qty = row[3]

                print('', isbn, ' ', title, ' ', author, ' ', qty)
                print('', '-' * barsp)
                print('\n')

        if result is True:

            delete = input(' Delete book? (y/n): ')

            if delete == 'y':
                inp = open(bpath, 'r')
                output = open(bpath1, 'w+', newline='')
                writer = csv.writer(output)
                for row in csv.reader(inp):
                    if row[0] != isbn:
                        writer.writerow(row)

                inp.close()
                output.close()


                inp = open(bpath1, 'r')
                output = open(bpath, 'w+', newline='')
                writer = csv.writer(output)
                for row in csv.reader(inp):
                    writer.writerow(row)

                inp.close()
                output.close()

                os.remove(bpath1)

                print(' Successfully deleted')
                time.sleep(1)
                welcome()
            else:
                welcome()

        else:
            opt = input("\n"' ISBN number not found, would you like to search again? (Yes(enter) / No(n)):  ')
            if opt == '':
                deletebook()
            else:
                print("\n"' You are being directed back to the home screen')
                time.sleep(2)
                welcome()


    elif isbn != '':
        if ilength != 13:
            print(' ISBN number must be 13 digits long')
            if digit is False:
                print(' ISBN must only contain numbers')
        else:
            if digit is False:
                print(' ISBN must only contain numbers')
        time.sleep(1)
        deletebook()
    else:
        welcome()



def loan():
    os.system("cls")
    print(' Loan to user is still in progress')
    print(' You will be directed to the Home Screen in 2 seconds')

    time.sleep(2)
    welcome()



def welcome():
    os.system('cls')
    print('\n')
    print(' ' * headsp, 'Home Page')
    print(' ' * headsp, '---------')
    print('\n')
    print('\n')
    print(' ***********************************************************')
    print(" * Welcome to Zain's library management system.            *")
    print(' *                                                         *')
    print(' * Please select one of the following options              *')
    print(' *                                                         *')
    print(' * 1. View all books                                       *')
    print(' * 2. Search books                                         *')
    print(' * 3. Insert book                                          *')
    print(' * 4. Delete book                                          *')
    print(' * 5. Loan to user                                         *')
    print(' *                                                         *')
    print(' ***********************************************************')

    key = input(' Choose an option: ')

    if key == '1':
        viewbooks()
    elif key == '2':
        searchbooks()
    elif key == '3':
        insertbook()
    elif key == '4':
        deletebook()
    elif key == '5':
        loan()
    else:
        welcome()



def signup():
    os.system('cls')
    if os.path.exists(bpath) and os.path.exists(ppath) :
        login()
    else:
        print('\n')
        print(' Welcome... please enter a pin you would like to use to login (minimum 4 digits)')
        passcode = getpass.getpass(' Pin:  ')
        cpasscode = getpass.getpass(' Confirm pin:  ')
        if passcode == cpasscode:

            ln = len(str(passcode))
            if ln > 3:
                f = open(bpath, 'w+')
                f.close()
                f = open(ppath, 'w+')
                f.write(passcode)
                f.close()
                login()

            else:
                print(' Pin needs to be at least 4 digits')
                time.sleep(2)
                signup()

        else:
            print(' Pin numbers do not match... please try again')
            time.sleep(2)
            signup()


signup()