import connection
from model import Model



class View:
    def __init__(self, table, datas):
        self.table = table
        self.datas = datas


    @staticmethod
    def listof():
        print('''
        1                 => email
        2                 => folders
        3                 => users
        4                 => notifications 
        5                 => folders_notifications
        6                 => notifications_users
        ''')

    @staticmethod
    def listofdata(choice):
        if choice == 1:
            print('''
            1 => gmailID
            2 => creator
            3 => name
            ''')
        elif choice == 2:
            print('''
            1 => foldID
            2 => Size
            3 => Colour
            4 => nameof
            5 => id_mainfolder
            ''')
        elif choice == 3:
            print('''
            1 => userID
            2 => adress
            3 => place
            4 => id_mail
            ''')
        elif choice == 4:
            print('''
            1 => povID
            2 => text
            3 => addfiles
            4 => title
            5 => id_userfkey
            6 => id_sender
            ''')
        elif choice == 5:
            print('''
            1 => ppID
            2 => notifications_ID
            3 => folders_ID
            ''')
        elif choice == 6:
            print('''
            1 => pkID
            2 => notifiations_ID
            3 => users_ID
            ''')

    @staticmethod
    def listofdatatoupdate(choice):
        if choice == 1:
            print('''
                2 => creator
                3 => name
                ''')
        elif choice == 2:
            print('''
                2 => Size
                3 => Colour
                4 => nameof
                ''')
        elif choice == 3:
            print('''
                2 => adress
                3 => place
                ''')
        elif choice == 4:
            print('''
                2 => text
                3 => addfiles
                4 => title
                6 => id_sender
                ''')

    @staticmethod
    def spis(choice):
        if choice == 1:
            print('''
             gmailID
             creator
             name
                ''')
        elif choice == 2:
            print('''
                foldID
                Size
                Colour
                nameof
                id_mainfolder
                ''')
        elif choice == 3:
            print('''
                userID
                adress
                place
                id_mail
                ''')
        elif choice == 4:
            print('''
                povID
                text
                addfiles
                title
                id_userfkey
                id_sender
                ''')
        elif choice == 5:
            print('''
                ppID
                notifications_ID
                folders_ID
                ''')
        elif choice == 6:
            print('''
                pkID
                notifiations_ID
                users_ID
                ''')


    def output_spec(self):
        if self.table == 1:
            print("***************************\n")
            print('size       colour           name           creator')
            for column in self.datas:
                print(
                    "{}            {}            {}            {}".format(column[0], column[1], column[2],
                                                                                        column[3]))
            print("***************************\n")
        elif self.table == 2:
            print("***************************\n")
            print('adress           addfiles           text')
            for column in self.datas:
                print(
                    "{}            {}            {}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 3:
            print("***************************\n")
            print('name           nameof           size           colour')
            for column in self.datas:
                print(
                    "{}            {}            {}            {}".format(column[0], column[1], column[2],
                                                                                        column[3]))
            print("***************************\n")
        else:
            print('Something gone wrong')




    def output(self):
        print("***************************\n")
        if self.table == 1:
            print('gmailID      creator      name')
            for column in self.datas:
               print("{}            {}            {}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 2:
            print('foldID       Size      Colour      nameof      id_mainfolder')
            for column in self.datas:
                print("{}            {}            {}            {}            {}".format(column[0], column[1], column[2], column[3], column[4]))
            print("***************************\n")
        elif self.table == 3:
            print('userID       adress     place      id_mail')
            for column in self.datas:
                print("{}            {}            {}            {}".format(column[0], column[1], column[2],column[3]))
            print("***************************\n")
        elif self.table == 4:
            print('povID       text      addfiles      title      id_userfkey      id_sender')
            for column in self.datas:
              print("{}            {}            {}            {}            {}            {}".format(column[0], column[1], column[2],
                                                                                        column[3], column[4], column[5]))
            print("***************************\n")

        elif self.table == 5:
            print('ppID       notifications_ID     folders_ID')
            for column in self.datas:
                print("{}            {}            {}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 6:
            print('pkID       notifications_ID     users_ID')
            for column in self.datas:
              print("{}            {}            {}".format(column[0], column[1], column[2]))
            print("***************************\n")




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
                View.listof()
                table = input('Choose your table:')
                table = Model.existingtable(table)
                if table == 0:
                    continue
                datas = Model.outputonetable(table)
                obj = View(table, datas)
                obj.output()
            elif choice == '2':
                for table in range(1, 7):
                    datas = Model.outputonetable(table)
                    obj = View(table, datas)
                    obj.output()
            elif choice == '3':
                ins = True
                while ins:
                    View.listof()
                    table = input('Choose your table: ')
                    table = int(table)
                    table = Model.existingtable(table)
                    if table == 0:
                        continue
                    elif table == 1:
                        f = input('gmailID = ')
                        s = input('creator(str) = ')
                        t = input('name(str) = ')
                        added = 'added'
                        added = "'" + added + "'"
                        notice = 'wrong way, the row with gmailID = {} exists'.format(f)
                        notice = "'" + notice + "'"
                        if str(f).isdigit() and s.isalnum() and t.isalnum():
                            s = "'" + s + "'"
                            t = "'" + t + "'"
                            Model.insertbyusertoEmail(f, s, t, added, notice)
                        else:
                            print('The values are wrong')
                    elif table == 2:
                        f = input('foldID = ')
                        s = input('Size = ')
                        t = input('Colour = ')
                        fouth = input('nameof(str) = ')
                        fifth = input('id_mainfolder = ')
                        notice = 'gmailID = {} is not present in table or row with foldID = {} exists already'.format(
                            fifth, f)
                        notice = "'" + notice + "'"
                        added = 'added'
                        added = "'" + added + "'"
                        if str(f).isdigit() and str(s).isdigit() and str(t).isdigit() and fouth.isalnum() and str(
                                fifth).isdigit():
                            fouth = "'" + fouth + "'"
                            Model.insertbyusertoFolders(f, s, t, fouth, fifth, added, notice)
                        else:
                            print('The values are wrong')

                    elif table == 3:
                        f = input('userID = ')
                        s = input('adress(str) = ')
                        t = input('place(str) = ')

                        fouth = input('id_mail = ')
                        notice = 'gmailID = {} is not present in table or userID = {} exists already'.format(fouth, f)
                        notice = "'" + notice + "'"
                        added = 'added'
                        added = "'" + added + "'"

                        if str(f).isdigit() and s.isalnum() and t.isalnum() and str(fouth).isdigit():
                            s = "'" + s + "'"
                            t = "'" + t + "'"
                            Model.insertbyusertoUsers(f,s,t,added,notice)
                        else:
                            print('The values are wrong')
                    elif table == 4:
                        f = input('povID = ')
                        s = input('text(str) = ')
                        t = input('addfiles = ')
                        fouth = input('title(str) = ')
                        fifth = input('id_userfkey = ')
                        sixth = input('id_sender = ')
                        notice = 'userID = {} is not present in table or povID = {} exists already'.format(fifth, f)
                        notice = "'" + notice + "'"
                        added = 'added'
                        added = "'" + added + "'"
                        if str(f).isdigit() and s.isalnum() and str(t).isdigit() and fouth.isalnum() and str(
                                fifth).isdigit() and str(sixth).isdigit():
                            s = "'" + s + "'"
                            fouth = "'" + fouth + "'"
                            Model.insertbyusertoNotifications(f,s,t,fouth,fifth,sixth)
                        else:
                            print('The values are wrong')
                    else:
                        print('Something gone wrong')
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
                delete = 'deleted'
                delete = "'" + delete + "'"
                notice = 'something went wrong'
                notice = "'" + notice + "'"
                dele = True
                while dele:
                    View.listof()
                    table = input('Choose your table:')

                    table = Model.existingtable(table)
                    if table == 1:
                            idk = input('Attribute to delete gmailID = ')
                            if str(idk).isdigit():
                                Model.deleteEmail(idk,delete,notice)
                            else:
                                print('The value are wrong')
                    elif table == 2:
                            idk = input('Attribute to delete foldID = ')
                            if str(idk).isdigit():
                                Model.deleteFolders(idk,delete,notice)
                            else:
                                print('The value are wrong')
                    elif table == 3:
                            idk = input('Attribute to delete userID = ')
                            if str(idk).isdigit():
                                Model.deleteUsers(idk,delete,notice)
                            else:
                                print('The value are wrong')
                    elif table == 4:
                            idk = input('Attribute to delete povID = ')
                            if str(idk).isdigit():
                                Model.deleteNotifications(idk,delete,notice)
                            else:
                                print('The value are wrong')

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
                updated = 'updated'
                updated = "'" + updated + "'"
                upd = True
                while upd:
                    View.listof()
                    table = input('Choose your table:')
                    table = Model.existingtable(table)
                    table = int(table)
                    View.listofdatatoupdate(table)

                    if table == 1:
                        idk = input('Row to update where gmailID = ')
                        notice = 'gmailID = {} is not present in table.'.format(idk)
                        notice = "'" + notice + "'"
                        set2 = input('creator(str) = ')

                        set3 = input('name(str) = ')

                        if set2.isalnum() and set3.isalnum() and str(idk).isdigit():
                            set2 = "'" + set2 + "'"
                            set3 = "'" + set3 + "'"
                            Model.UpdateEmail(idk, set2, set3, updated, notice)
                        else:
                            print('The values are wrong')
                    elif table == 2:
                        idk = input('Row to update where foldID = ')
                        notice = 'foldID = {} is not present in table.'.format(idk)
                        notice = "'" + notice + "'"
                        set1 = input('Size = ')
                        set2 = input('Colour = ')
                        set3 = input('nameof(str) = ')

                        if str(idk).isdigit() and str(set1).isdigit() and str(set2).isdigit() and set3.isalnum():
                            set3 = "'" + set3 + "'"
                            Model.UpdateFolders(idk, set1, set2, set3, updated, notice)
                        else:
                            print('The values are wrong')
                    elif table == 3:
                        idk = input('Row to update where userID = ')
                        notice = 'userID = {} is not present in table.'.format(idk)
                        notice = "'" + notice + "'"
                        adress = input('adress(str) = ')
                        place = input('place(str) = ')
                        if str(idk).isdigit() and adress.isalnum() and place.isalnum():
                            adress = "'" + adress + "'"
                            place = "'" + place + "'"
                            Model.UpdateUsers(idk, adress, place, updated, notice)
                        else:
                            print('The values are wrong')
                    elif table == 4:
                        idk = input('Row to update where povID = ')
                        notice = 'povID = {} is not present in table.'.format(idk, idk)
                        notice = "'" + notice + "'"
                        text = input('text(str) = ')
                        addfiles = input('addfiles = ')
                        title = input('title(str) = ')
                        sender = input('id_sender = ')

                        if str(idk).isdigit() and text.isalnum() and str(
                                addfiles).isdigit() and title.isalnum() and str(sender).isdigit():
                            title = "'" + title + "'"
                            text = "'" + text + "'"
                            Model.UpdateNotifications(idk, text, addfiles, title, sender, updated, notice)
                        else:
                            print('The values are wrong')
                    else:
                        print('Something went wrong')
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
                    print('----------------------------------------')
                    print('1 => Show size and colour of folders which created by *creator* '
                          'where name length is greater than *value* or equal')
                    print('----------------------------------------')
                    print(
                        '2 => Show text and addfiles of user message, where count of addfiles less than *value* on the mail *adress*')
                    print('----------------------------------------')
                    print('3 => Show size, colour and nameof of folders, which are stored on the *email*')
                    print('----------------------------------------')
                    choice = input('Your choice is ')
                    choice = int(choice)
                    if choice == 1:
                        len = input('Enter the required length(int) = ')
                        creator = input('Enter required creator(str) = ')
                        datas = Model.selectionone(len, creator)
                        obj = View(choice, datas)
                        obj.output_spec()
                    elif choice == 2:
                        value = input('Enter required value(int) = ')
                        adress = input('Enter required adress(str) = ')
                        datas = Model.selectiontwo(value, adress)
                        obj = View(choice, datas)
                        obj.output_spec()
                    elif choice == 3:
                        title = input('Enter required email(str) = ')
                        datas = Model.selectionthree(title)
                        obj = View(choice, datas)
                        obj.output_spec()
                    else:
                        print('Try again')
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
                    View.listof()
                    table = input("Choose your table (only from 1 to 4!!!!): ")
                    table = Model.existingtable(table)
                    if table == 0:
                        print('Something went wrong')
                        continue
                    kolvo = input('How much datas do you want to add => ')
                    if not str(kolvo).isdigit():
                        print('Something wrong')
                        continue
                    Model.randomik(table, kolvo)
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

