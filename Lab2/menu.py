from model import Model
import time


class Menu:
    @staticmethod
    def mainmenu():
        check = True
        while check:
            print('''
             1 => One table
             2 => All tables
             3 => Insertion
             4 => Delete some inf
             5 => Updating
             6 => Selection
             7 => Random inf
             ...
             0 = > Exit
            ''')

            choice = input('Your choice is: ')
            if choice == '1':
                Model.outputonetable()
            elif choice == '2':
                Model.outputalltables()
            elif choice == '3':
                ins = True
                while ins:
                    Model.insertbyuser()
                    cont = True
                    while cont:
                        ch = input('1 => Continue insertion, 2 => Stop insertion => ')
                        if ch == '2':
                            ins = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '4':
                dele = True
                while dele:
                    gg = input('1 => delete one row;  2 => delete several rows; Your choice => ')
                    gg = int(gg)
                    if gg == 1:
                        Model.deletebyuser()
                    elif gg == 2:
                        Model.deletealot()
                    cont = True
                    while cont:
                        ch = input('1 => Continue delete, 2 => Stop delete => ')
                        if ch == '2':
                            dele = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '5':
                upd = True
                while upd:
                    choise = input('Update 1 column in 1 row => 1; Update all row => 2; Your choice: ')
                    choise = int(choise)
                    if choise == 1:
                        Model.updatebyuser()
                    elif choise == 2:
                        Model.updatebyuserallrow()
                    cont = True
                    while cont:
                        ch = input('1 => Continue update, 2 => Stop update => ')
                        if ch == '2':
                            upd = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '6':
                sel = True
                while sel:
                    Model.selection()
                    cont = True
                    while cont:
                        ch = input('1 => Continue selection, 2 => Stop selection => ')
                        if ch == '2':
                            sel = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '7':
                ra = True
                while ra:
                    Model.randomik()
                    cont = True
                    while cont:
                        ch = input('1 => Continue random, 2 => Stop random => ')
                        if ch == '2':
                            ra = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '0':
                check = False
            else:
                print('Try again')

            cont = True
            while cont:
                con = input('Continue to work with db => 1, stop => 2. Your choice =>')
                if con == '2':
                    check = False
                    cont = False
                elif con == '1':
                    cont = False
                    check = True
                else:
                    print('Try again')


