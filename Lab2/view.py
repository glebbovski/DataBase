import connection


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


    def perev(self):

        if self.table == 2:
            if self.datas[4] == 4:
                print('qweqwe')



    def output(self):
        print("***************************\n")
        if self.table == 1:
            print('gmailID      creator      name')
            for column in self.datas:
              #  print("gmailID = ", column[0])
               # print("creator = ", column[1])
               # print("name = ", column[2])
               print("{}            {}            {}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 2:
            print('foldID       Size      Colour      nameof      id_mainfolder')
            for column in self.datas:
            #    print("foldID = ", column[0])
             #   print("Size = ", column[1])
              #  print("Colour = ", column[2])
              #  print("nameof = ", column[3])
              #  print("id_mainfolder", column[4])
                print("{}            {}            {}            {}            {}".format(column[0], column[1], column[2], column[3], column[4]))
            print("***************************\n")
        elif self.table == 3:
            print('userID       adress     place      id_mail')
            for column in self.datas:
               # print("userID = ", column[0])
               # print("adress = ", column[1])
               # print("place = ", column[2])
               # print("id_mail = ", column[3])
                print("{}            {}            {}            {}".format(column[0], column[1], column[2],column[3]))
            print("***************************\n")
        elif self.table == 4:
            print('povID       text      addfiles      title      id_userfkey      id_sender')
            for column in self.datas:
              #  print("povID = ", column[0])
              #  print("text = ", column[1])
              #  print("addfiles = ", column[2])
              #  print("title = ", column[3])
              #  print("id_userfkey = ", column[4])
              #  print("id_sender = ", column[5])
              print("{}            {}            {}            {}            {}            {}".format(column[0], column[1], column[2],
                                                                                        column[3], column[4], column[5]))
            print("***************************\n")

        elif self.table == 5:
            print('ppID       notifications_ID     folders_ID')
            for column in self.datas:
              #  print("ppID = ", column[0])
               # print("notifications_ID = ", column[1])
               # print("folders_ID = ", column[2])
                print("{}            {}            {}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 6:
            print('pkID       notifications_ID     users_ID')
            for column in self.datas:
              #  print("pkID = ", column[0])
              #  print("notifications_ID", column[1])
              #  print("users_ID = ", column[2])
              print("{}            {}            {}".format(column[0], column[1], column[2]))
            print("***************************\n")

