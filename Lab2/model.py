import random
import connection
from view import View
import time

Tables = {
    1: 'email',
    2: 'folders',
    3: 'users',
    4: 'notifications',
    5: 'folders_notifications',
    6: 'notifications_users'
}

class Model:
    @staticmethod
    def existingtable():
        while True:
            table = input('Choose your table: ')
            table = int(table)
            if table == 1 or table == 2 or table == 3 or table == 4 or table == 5 or table == 6:
             return table
            else:
                print('Try again.')

    @staticmethod
    def outputonetable():
        View.listof()
        connect = connection.connection()
        cursor = connect.cursor()
        table = Model.existingtable()

        show = 'select * from public.{}'.format(Tables[table])

        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        datas = cursor.fetchall()
        obj = View(table, datas)
        obj.output()
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def outputalltables():
        connect = connection.connection()
        cursor = connect.cursor()
        for table in range(1, 7):
            show = 'select * from public.{}'.format(Tables[table])

            print("SQL query => ", show)
            print('')
            cursor.execute(show)
            datas = cursor.fetchall()
            obj = View(table, datas)
            obj.output()
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def insertbyuser():
        connect = connection.connection()
        cursor = connect.cursor()
        check = True
        while check:
            View.listof()
            table = Model.existingtable()

            if table == 1:
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
                    insert = 'DO $$ BEGIN if (1=1) and not exists (select gmailID from email where gmailID = {}) then INSERT INTO email(gmailID, creator, name) VALUES ({},{},{}); ' \
                         'raise notice {}; else raise notice {}; ' \
                         'end if; end $$;'.format(f, f, s, t, added, notice)
                    check = False
                else:
                    print('The values are wrong')


            elif table == 2:
                f = input('foldID = ')
                s = input('Size = ')
                t = input('Colour = ')
                fouth = input('nameof(str) = ')
                fifth = input('id_mainfolder = ')
                notice = 'gmailID = {} is not present in table or row with foldID = {} exists already'.format(fifth,f)
                notice = "'" + notice + "'"
                added = 'added'
                added = "'" + added + "'"

               # insert = 'INSERT INTO folders(foldID, Size, Colour, nameof, id_mainfolder) VALUES ({},{},{},{},{})'.format(f, s, t,fouth,fifth)
                if str(f).isdigit() and str(s).isdigit() and str(t).isdigit() and fouth.isalnum() and str(fifth).isdigit():
                    fouth = "'" + fouth + "'"
                    insert = 'DO $$	BEGIN IF EXISTS (select gmailID from email where gmailID = {}) and not exists (select foldId from folders where foldId = {}) THEN ' \
                         'INSERT INTO folders(foldID, Size, Colour, nameof, id_mainfolder) values ({}, {}, {}, {}, {}); ' \
                         'RAISE NOTICE {};' \
                         ' ELSE RAISE NOTICE {};' \
                         'END IF; ' \
                            'END $$;'.format(fifth,f, f, s, t, fouth, fifth, added, notice)
                    check = False
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
                    insert = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {}) and not exists (select userID from users where userID = {}) THEN ' \
                         'INSERT INTO users(userID, adress, place, id_mail) values ({}, {}, {}, {}); ' \
                         'RAISE NOTICE {};' \
                         ' ELSE RAISE NOTICE {};' \
                         'END IF; ' \
                        'END $$;'.format(fouth,f, f, s, t, fouth,added, notice)
                    check = False
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

              #  insert = 'INSERT INTO notifications(povID, text, addfiles, title, id_userfkey, id_sender) VALUES ({},{},{},{}, {}, {})'.format(
               #     f, s, t, fouth, fifth, sixth)
                if str(f).isdigit() and s.isalnum() and str(t).isdigit() and fouth.isalnum() and str(fifth).isdigit() and str(sixth).isdigit():
                    s = "'" + s + "'"
                    fouth = "'" + fouth + "'"

                    insert = 'DO $$	BEGIN IF EXISTS (select userID from users where userID = {}) and not exists (select povID from notifications where povID = {}) THEN ' \
                         'INSERT INTO notifications(povID, text, addfiles, title, id_userfkey, id_sender) values ({}, {}, {}, {}, {}, {}); ' \
                         'RAISE NOTICE {};' \
                         ' ELSE RAISE NOTICE {};' \
                         'END IF; ' \
                        'END $$;'.format(fifth, f, f, s, t, fouth, fifth, sixth, added, notice)
                    check = False
                else:
                    print('The values are wrong')


            elif table == 5:
                f = input('ppID = ')
                s = input('notifications_ID = ')
                t = input('folders_ID = ')
                notice = 'foldID = {} or povID = {} or both is not present in tables. Or ppId = {} exists already'.format(t, s, f)
                notice = "'" + notice + "'"
                added = 'added'
                added = "'" + added + "'"

               # insert = 'INSERT INTO folders_notifications(ppID, notifications_ID, folders_ID) VALUES ({},{},{})'.format(
                #    f, s, t)
                if str(f).isdigit() and str(s).isdigit() and str(t).isdigit():
                    insert = 'DO $$ BEGIN IF EXISTS (select foldID from folders where foldID = {}) and ' \
                         'EXISTS (select povID from notifications where povID = {}) and ' \
                             'not exists (select ppID from folders_notifications where ppID = {}) THEN ' \
                         'INSERT INTO folders_notifications(ppID, notifications_ID, folders_ID) VALUES ({},{},{}); ' \
                         'RAISE NOTICE {};' \
                         ' ELSE RAISE NOTICE {};' \
                         'END IF; ' \
                         'END $$;'.format(t,s, f, f,s,t, added, notice)
                    check = False
                else:
                    print('The values are wrong')

            elif table == 6:
                f = input('pkID = ')
                s = input('notifications_ID = ')
                t = input('users_ID = ')
                added = 'added'
                added = "'" + added + "'"
                notice = 'userID = {} or povID = {} is not present in tables. Or both.'.format(t, s)

                notice = "'" + notice + "'"

                #insert = 'INSERT INTO notifications_users(pkID, notifications_ID, users_ID) VALUES ({},{},{})'.format(
                 #   f, s, t)

                if str(f).isdigit() and str(s).isdigit() and str(t).isdigit():
                    insert = 'DO $$ BEGIN ' \
                         'IF EXISTS (select userID from users where userID = {}) and EXISTS (select povID from notifications where povID = {})' \
                             'and not exists (select pkID from notifications_users where pkID = {}) THEN ' \
                         'INSERT INTO notifications_users(pkID, notifications_ID, users_ID) VALUES ({},{},{}); ' \
                        'RAISE NOTICE {};' \
                         ' ELSE RAISE NOTICE {};' \
                         'END IF; ' \
                         'END $$;'.format(t,s, f, f,s,t, added, notice)
                    check = False
                else:
                    print('The values are wrong')



            else:
                print('Try again.')


        print(Tables[table])
        print('SQL query => ', insert)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def deletebyuser():
        connect = connection.connection()
        cursor = connect.cursor()
        check = True
        delete = 'deleted'
        delete = "'" + delete + "'"
        notice = 'something went wrong'
        notice = "'" + notice + "'"
        while check:
            View.listof()
            table = Model.existingtable()

            if table == 1:
                idk = input('Attribute to delete gmailID = ')
                idk = int(idk)

                #    'delete from notifications_users where notifications_ID = (select povID from notifications where id_userfkey = (select userID from users where id_mail = {}));' \
                #  'delete from folders_notifications where notifications_ID = (select povID from notifications where id_userfkey = (select userID from users where id_mail = {}));' \

                delete = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {}) then ' \
                         'delete from folders_notifications where folders_ID in (select foldID from folders where id_mainfolder = {});' \
                         'delete from folders_notifications where notifications_ID in (select povID from notifications where id_userfkey in (select userID from users where id_mail = {}));' \
                         'delete from notifications_users where notifications_ID in (select povID from notifications where id_userfkey in (select userID from users where id_mail = {}));' \
                         'delete from notifications_users where users_ID in (select userID from users where id_mail = {});' \
                         'delete from notifications where id_userfkey in (select userID from users where id_mail = {});' \
                         'delete from users where id_mail = {};' \
                         'delete from folders where id_mainfolder = {};' \
                         'delete from email where gmailID= {};' \
                         'raise notice {};' \
                         'else raise notice {};' \
                         'end if;' \
                         'end $$;'.format(idk, idk, idk, idk, idk, idk, idk, idk, idk, delete, notice)


                check = False
            elif table == 2:
                idk = input('Attribute to delete foldID = ')
                ddelete = 'DO $$ BEGIN if ' \
                             'exists (select foldID from folders where foldID = {}) then ' \
                             ' delete from folders_notifications where folders_ID in (select foldID from folders where id_mainfolder = {});' \
                             'delete from folders where foldID= {};' \
                             'raise notice {};' \
                             'else raise notice {};' \
                             'end if;' \
                             'end $$;'.format(idk, idk, idk, delete, notice)
                check = False
            elif table == 3:
                idk = input('Attribute to delete userID = ')
                delete = 'DO $$ BEGIN if ' \
                         'exists (select userID from users where userID = {}) then ' \
                         'delete from notifications_users where notifications_ID in (select povID from notifications ' \
                         'where id_userfkey in (select userID from users where userID = {}));' \
                         'delete from notifications_users where users_ID in (select povID from notifications ' \
                         'where id_userfkey = {});' \
                         'delete from notifications where id_userfkey = {};' \
                         'delete from users where userID = {};' \
                         'raise notice {};' \
                         'else raise notice {};' \
                         'end if;' \
                         'end $$;'.format(idk, idk, idk, idk, idk, delete, notice)
                check = False
            elif table == 4:
                idk = input('Attribute to delete povID = ')
                delete = 'DO $$ BEGIN if exists (select povID from notifications where povID = {}) then ' \
                         'delete from notifications_users where notifications_ID = {};' \
                         'delete from folders_notifications where notifications_ID = {};' \
                         'delete from notifications where povID= {};' \
                         'raise notice {};' \
                         'else raise notice {};' \
                         'end if;' \
                         'end $$;'.format(idk, idk, idk, idk, delete, notice)
                check = False
            elif table == 5:
                idk = input('Attribute to delete ppID = ')
                delete = 'DO $$ begin if exists (select ppID from folders_notifications where ppID = {}) then ' \
                         ' delete from folders_notifications where ppID= {};' \
                         'raise notice {};' \
                         'else raise notice {};' \
                         'end if;' \
                         'end $$;'.format(idk, idk, delete, notice)
                check = False
            elif table == 6:
                idk = input('Attribute to delete pkID = ')
                delete = 'do $$ begin if exists (select pkID from notifications_users where pkID = {}) then ' \
                         'delete from notifications_users where pkID= {};' \
                         'raise notice {};' \
                         'else raise notice {};' \
                         'end if;' \
                         'end $$;'.format(idk, idk, delete, notice)
                check = False
            else:
                print('Try again.')

        print(Tables[table])
        print("SQL query => ", delete)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def deletealot():
        connect = connection.connection()
        cursor = connect.cursor()
        delete = 'deleted'
        delete = "'" + delete + "'"
        notice = 'Something went wrong'
        notice = "'" + notice + "'"
        check = True
        while check:
            View.listof()
            table = Model.existingtable()
            start = input('From which number do you want to start? =>')
            stop = input('Number to stop? =>')
            start = int(start)
            stop = int(stop)
            if stop <= start:
                return 'Try again'
            if table == 1:
                while start != stop:
                    #                              'delete from folders_notifications where notifications_ID = (select povID from notifications where id_userfkey = (select userID from users where id_mail = {}));' \
                    #                             'delete from notifications_users where notifications_ID = (select povID from notifications where id_userfkey = (select userID from users where id_mail = {}));' \
                    #  'exists (select id_mainfolder from folders where id_mainfolder = {}) and ' \
                    #  'exists (select id_mail from users where id_mail = {}) and ' \
                    #  'exists (select id_userfkey from notifications where id_userfkey in (select userID from users where id_mail = {})) and ' \
                    #  'exists (select users_ID from notifications_users where users_ID in (select userID from users where id_mail = {})) and' \
                    #  'exists (select notifications_ID from notifications_users where notifications_ID in (select povID from notifications where id_userfkey in (select userID from users where id_mail = {}))) and ' \
                    #  'exists (select notifications_ID from folders_notifications where notifications_ID in (select povID from notifications where id_userfkey in (select userID from users where id_mail = {}))) and ' \
                    #   'exists (select folders_ID from folders_notifications where folders_ID in (select foldID from folders where id_mainfolder = {})) THEN ' \

                    delete = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {}) then ' \
                             'delete from folders_notifications where folders_ID in (select foldID from folders where id_mainfolder = {});' \
                             'delete from folders_notifications where notifications_ID in (select povID from notifications where id_userfkey in (select userID from users where id_mail = {}));' \
                             'delete from notifications_users where notifications_ID in (select povID from notifications where id_userfkey in (select userID from users where id_mail = {}));' \
                             'delete from notifications_users where users_ID in (select userID from users where id_mail = {});' \
                             'delete from notifications where id_userfkey in (select userID from users where id_mail = {});' \
                             'delete from users where id_mail = {};' \
                             'delete from folders where id_mainfolder = {};' \
                             'delete from email where gmailID= {};' \
                             'raise notice {};' \
                             'else raise notice {};' \
                             'end if;' \
                             'end $$;'.format(
                        start, start, start, start, start, start, start, start, start, delete, notice)
                    check = False
                    cursor.execute(delete)
                    start = start + 1
            elif table == 2:
                while start != stop:
                    delete = 'DO $$ BEGIN if ' \
                             'exists (select foldID from folders where foldID = {}) then ' \
                             ' delete from folders_notifications where folders_ID in (select foldID from folders where id_mainfolder = {});' \
                             'delete from folders where foldID= {};' \
                             'raise notice {};' \
                             'else raise notice {};' \
                             'end if;' \
                             'end $$;'.format(start, start, start, delete, notice)
                    check = False
                    cursor.execute(delete)
                    start = start + 1
            elif table == 3:
                while start != stop:
                    delete = 'DO $$ BEGIN if ' \
                             'exists (select userID from users where userID = {}) then ' \
                             'delete from notifications_users where notifications_ID in (select povID from notifications ' \
                             'where id_userfkey in (select userID from users where userID = {}));' \
                             'delete from notifications_users where users_ID in (select povID from notifications ' \
                             'where id_userfkey = {});' \
                             'delete from notifications where id_userfkey = {};' \
                             'delete from users where userID = {};' \
                             'raise notice {};' \
                             'else raise notice {};' \
                             'end if;' \
                             'end $$;'.format(start, start, start, start, start, delete, notice)
                    check = False
                    cursor.execute(delete)
                    start = start + 1
            elif table == 4:
                while start != stop:
                    delete = 'DO $$ BEGIN if exists (select povID from notifications where povID = {}) then ' \
                             'delete from notifications_users where notifications_ID = {};' \
                             'delete from folders_notifications where notifications_ID = {};' \
                             'delete from notifications where povID= {};' \
                             'raise notice {};' \
                             'else raise notice {};' \
                             'end if;' \
                             'end $$;'.format(start, start, start, start, delete, notice)
                    check = False
                    cursor.execute(delete)
                    start = start + 1
            elif table == 5:
                while start != stop:
                    delete = 'DO $$ begin if exists (select ppID from folders_notifications where ppID = {}) then ' \
                             ' delete from folders_notifications where ppID= {};' \
                             'raise notice {};' \
                             'else raise notice {};' \
                             'end if;' \
                             'end $$;'.format(start, start, delete, notice)
                    check = False
                    cursor.execute(delete)
                    start = start + 1
            elif table == 6:
                while start != stop:
                    delete = 'do $$ begin if exists (select pkID from notifications_users where pkID = {}) then ' \
                             'delete from notifications_users where pkID= {};' \
                             'raise notice {};' \
                             'else raise notice {};' \
                             'end if;' \
                             'end $$;'.format(start, start, delete, notice)
                    check = False
                    cursor.execute(delete)
                    start = start + 1
            else:
                print('Try again.')
        print(Tables[table])
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def updatebyuser():
        connect = connection.connection()
        cursor = connect.cursor()
        check = True

        updated = 'updated'
        updated = "'" + updated + "'"
        while check:
            View.listof()
            table = Model.existingtable()
            if table == 1:
                idk = input('Attribute to update(where) gmailID = ')
                notice = 'gmailID = {} is not present in table.'.format(idk)
                notice = "'" + notice + "'"
                View.listofdatatoupdate(1)
                checkin = True
                while checkin:
                    atnum = input('Number of attribute => ')
                    if(int(atnum) < 2 or int(atnum) > 3):
                        print('Try again')
                        continue
                    nval = input('New value = ')
                   # if atnum == '1':
                    #    set = 'gmailID = {}'.format(nval)
                     #   checkin = False
                    if atnum == '2':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'creator = {}'.format(nval)

                            update = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {})' \
                                     ' THEN ' \
                            'update email set {} where gmailID = {}; ' \
                            'RAISE NOTICE {};' \
                            ' ELSE RAISE NOTICE {};' \
                            'END IF; ' \
                            'END $$;'.format(idk, set, idk, updated, notice)

                            check = False
                            pass
                        else:
                            print('Column should contain only chars or numbers')
                    elif atnum == '3':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'name = {}'.format(nval)
                            update = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {}) THEN ' \
                                     'update email set {} where gmailID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format(idk, set, idk, updated, notice)
                            check = False
                            pass
                        else:
                            print('Column should contain only chars or numbers')
                    else:
                        print('Try again')
            elif table == 2:
                idk = input('Attribute to update(where) foldID = ')
                notice = 'foldID = {} is not present in table.'.format(idk)
                notice = "'" + notice + "'"
                View.listofdata(2)
                checkin = True
                while checkin:
                    atnum = input('Number of attribute => ')
                    if (int(atnum) < 2 or int(atnum) > 4):
                        print('Try again')
                        continue
                    nval = input('New value = ')

                   # if atnum == '1':
                    #    set = 'foldID = {}'.format(nval)
                    #    checkin = False
                    if atnum == '2':
                        set = 'Size = {}'.format(nval)
                        checkin = False
                        if (str(nval).isdigit() and str(idk).isdigit()):
                            update = 'DO $$ BEGIN IF EXISTS (select foldID from folders where foldID = {})' \
                                     ' THEN ' \
                                     'update folders set {} where foldID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format(idk, set, idk, updated, notice)
                            check = False

                        else:
                            print('Column should contain only numbers')
                    elif atnum == '3':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'colour = {}'.format(nval)
                            update = 'DO $$ BEGIN IF EXISTS (select foldID from folders where foldID = {}) ' \
                                     ' THEN ' \
                                     'update folders set {} where foldID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format(idk, set, idk, updated, notice)
                            check = False

                        else:
                            print('Column should contain only chars or numbers')
                    elif atnum == '4':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'nameof = {}'.format(nval)
                            update = 'DO $$ BEGIN IF EXISTS (select foldID from folders where foldID = {}) ' \
                                     ' THEN ' \
                                     'update folders set {} where foldID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format(idk, set, idk, updated, notice)
                            check = False

                        else:
                            print('Column should contain only chars or numbers')
                   # elif atnum == '5':
                    #    set = 'id_mainfolder = {}'.format(nval)
                     #   checkin = False
                    else:
                        print('Try again')
                pass
            elif table == 3:
                idk = input('Attribute to update(where) userID = ')
                notice = 'userID = {} is not present in table.'.format(idk)
                notice = "'" + notice + "'"
                View.listofdata(3)
                checkin = True
                while checkin:
                    atnum = input('Number of attribute => ')
                    if (int(atnum) < 2 or int(atnum) > 3):
                        print('Try again')
                        continue
                    nval = input('New value = ')
                    #if atnum == '1':
                     #   set = 'userID = {}'.format(nval)
                    #    checkin = False
                    if atnum == '2':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'adress = {}'.format(nval)

                            update = 'DO $$ BEGIN IF EXISTS (select userID from users where userID = {}) ' \
                                     ' THEN ' \
                                     'update users set {} where userID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format(idk, set, idk, updated, notice)
                            check = False
                        else:
                            print('Column should contain only chars or numbers')
                    elif atnum == '3':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'place = {}'.format(nval)
                            update = 'DO $$ BEGIN IF EXISTS (select userID from users where userID = {})' \
                                     '  THEN ' \
                                     'update users set {} where userID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format( idk, set, idk, updated, notice)
                            check = False
                        else:
                            print('Column should contain only chars or numbers')
                   # elif atnum == '4':
                    #    set = 'id_mail = {}'.format(nval)
                     #   checkin = False
                    else:
                        print('Try again')
                pass
            elif table == 4:
                idk = input('Attribute to update(where) povID = ')
                notice = 'povID = {} is not present in table.'.format( idk)
                notice = "'" + notice + "'"
                View.listofdata(4)
                checkin = True
                while checkin:
                    atnum = input('Number of attribute => ')
                    if (int(atnum) < 2 or int(atnum) > 6 or int(atnum) == 5):
                        print('Try again')
                        continue
                    nval = input('New value = ')
                    #if atnum == '1':
                     #   set = 'povID = {}'.format(nval)
                    #    checkin = False
                    if atnum == '2':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'text = {}'.format(nval)

                            update = 'DO $$ BEGIN IF EXISTS (select povID from notifications where povID = {}) ' \
                                     ' THEN ' \
                                     'update notifications set {} where povID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format( idk, set, idk, updated, notice)
                            check = False
                        else:
                            print('Column should contain only chars or numbers')
                    elif atnum == '3':
                        set = 'addfiles = {}'.format(nval)
                        checkin = False
                        if (str(nval).isdigit() and str(idk).isdigit()):
                            update = 'DO $$ BEGIN IF EXISTS (select povID from notifications where povID = {}) ' \
                                     ' THEN ' \
                                     'update notifications set {} where povID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format( idk, set, idk, updated, notice)
                            check = False
                        else:
                            print('Column should contain only numbers')
                    elif atnum == '4':
                        checkin = False
                        if (nval.isalnum() and str(idk).isdigit()):
                            nval = "'" + nval + "'"
                            set = 'title = {}'.format(nval)
                            update = 'DO $$ BEGIN IF EXISTS (select povID from notifications where povID = {}) ' \
                                     ' THEN ' \
                                     'update notifications set {} where povID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format( idk, set, idk, updated, notice)
                            check = False
                        else:
                            print('Column should contain only chars or numbers')
                    #elif atnum == '5':
                      #  set = 'id_userfkey = {}'.format(nval)
                     #   checkin = False
                    elif atnum == '6':

                        checkin = False
                        if (str(nval).isdigit() and str(idk).isdigit()):
                            set = 'id_sender = {}'.format(nval)
                            update = 'DO $$ BEGIN IF EXISTS (select povID from notifications where povID = {})' \
                                     ' THEN ' \
                                     'update notifications set {} where povID = {}; ' \
                                     'RAISE NOTICE {};' \
                                     ' ELSE RAISE NOTICE {};' \
                                     'END IF; ' \
                                     'END $$;'.format( idk, set, idk, updated, notice)
                            check = False
                        else:
                            print('Column should contain only chars or numbers')
                    else:
                        print('Try again')
                pass

          #  elif table == 5:
           #     idk = input('Attribute to update(where) ppID = ')
            #    View.listofdata(5)
             #   checkin = True
              #  while checkin:
               #     atnum = input('Number of attribute => ')
                #    nval = input('New value = ')
                 #   if atnum == '1':
                  #      set = 'ppID = {}'.format(nval)
                   #     checkin = False
                   # elif atnum == '2':
                    #    set = 'notifications_ID = {}'.format(nval)
                     #   checkin = False
                   # elif atnum == '3':
                    #    set = 'folders_ID = {}'.format(nval)
                     #   checkin = False

                   # else:
                   #     print('Try again')
                # update = 'update folders_notifications set {} where ppID = {}'.format(set, idk)
                # check = False
                # pass
            # elif table == 6:
             #   idk = input('Attribute to update(where) pkID = ')
              #  View.listofdata(6)
              #  checkin = True
              #  while checkin:
              #      atnum = input('Number of attribute => ')
              #      nval = input('New value = ')
              #      if atnum == '1':
              #          set = 'pkID = {}'.format(nval)
              #          checkin = False
              #      elif atnum == '2':
               #         set = 'notifications_ID = {}'.format(nval)
               #         checkin = False
                #    elif atnum == '3':
                #        set = 'users_ID = {}'.format(nval)
                #        checkin = False

                #    else:
                 #       print('Try again')
                #update = 'update notifications_users set {} where pkID = {}'.format(set, idk)
                #check = False
                #pass
            else:
                print('Try again.')
        print(Tables[table])
        print("SQL query => ", update)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)
        pass

    @staticmethod
    def updatebyuserallrow():
        connect = connection.connection()
        cursor = connect.cursor()
        check = True
        updated = 'updated'
        updated = "'" + updated + "'"
        while check:
            View.listof()
            table = Model.existingtable()
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

                    update = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {}) THEN ' \
                             'update email set creator = {}, name = {} where gmailID = {}; ' \
                             'RAISE NOTICE {};' \
                             ' ELSE RAISE NOTICE {};' \
                             'END IF; ' \
                             'END $$;'.format(idk, set2, set3, idk, updated, notice)
                    check = False
                    pass
                else:
                    print('The values are wrong')
            elif table == 2:
                idk = input('Row to update where foldID = ')
                notice = 'foldID = {} is not present in table.'.format( idk)
                notice = "'" + notice + "'"
                set1 = input('Size = ')
                set2 = input('Colour = ')
                set3 = input('nameof(str) = ')

                if str(idk).isdigit() and str(set1).isdigit() and str(set2).isdigit() and set3.isalnum():
                    set3 = "'" + set3 + "'"
                    update = 'DO $$ BEGIN IF EXISTS (select foldID from folders where foldID = {})' \
                             ' THEN ' \
                             'update folders set Size = {}, Colour = {}, nameof = {} where foldID = {}; ' \
                             'RAISE NOTICE {};' \
                             ' ELSE RAISE NOTICE {};' \
                             'END IF; ' \
                             'END $$;'.format( idk, set1, set2, set3, idk, updated, notice)
                    check = False
                    pass
                else:
                    print('The values are wrong')

            elif table == 3:
                idk = input('Row to update where userID = ')
                notice = 'userID = {} is not present in table.'.format( idk)
                notice = "'" + notice + "'"
                adress = input('adress(str) = ')

                place = input('place(str) = ')

                if str(idk).isdigit() and adress.isalnum() and place.isalnum():
                    adress = "'" + adress + "'"

                    place = "'" + place + "'"

                    update = 'DO $$ BEGIN IF EXISTS (select userID from users where userID = {}) ' \
                             ' THEN ' \
                             'update users set adress = {}, place = {} where userID = {}; ' \
                             'RAISE NOTICE {};' \
                             ' ELSE RAISE NOTICE {};' \
                             'END IF; ' \
                             'END $$;'.format(idk, adress, place, idk, updated, notice)
                    check = False
                    pass
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

                if str(idk).isdigit() and text.isalnum() and str(addfiles).isdigit() and title.isalnum() and str(sender).isdigit():
                    title = "'" + title + "'"
                    text = "'" + text + "'"

                    update = 'DO $$ BEGIN IF EXISTS (select povID from notifications where povID = {}) ' \
                             ' THEN ' \
                             'update notifications set text = {}, addfiles = {}, title = {}, id_sender = {} where povID = {}; ' \
                             'RAISE NOTICE {};' \
                             ' ELSE RAISE NOTICE {};' \
                             'END IF; ' \
                             'END $$;'.format( idk, text, addfiles, title, sender, idk, updated, notice)
                    check = False
                    pass
                else:
                    print('The values are wrong')
            else:
                print('Try again')
        print(Tables[table])
        print("SQL query => ", update)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)
        pass


    @staticmethod
    def selection():
        connect = connection.connection()
        cursor = connect.cursor()
        check = True
        while check:
            print('----------------------------------------')
            print('1 => Show size and colour of folders which created by *creator* '
                  'where name length is greater than *value* or equal')
            print('----------------------------------------')
            print('2 => Show text and addfiles of user message, where count of addfiles less than *value* on the mail *adress*')
            print('----------------------------------------')
            print('3 => Show size, colour and nameof of folders, which are stored on the *email*')
            print('----------------------------------------')
            choice = input('Your choice is ')
            choice = int(choice)

            if choice == 1:
                len = input('Enter the required length(int) = ')
                creator = input('Enter required creator(str) = ')
                select = """select size, colour, name, creator from (select c.size, c.colour, p.name, 
                                p.creator from 
                                    folders c left join email p
                                     on p.gmailID = c.id_mainfolder where length(p.name) >= {} and p.creator LIKE '{}' 
                                      group by c.size,
                                     c.colour, p.name, p.creator) as foo""".format(len, creator)
                check = False
            elif choice == 2:
                value = input('Enter required value(int) = ')
                adress = input('Enter required adress(str) = ')
                select = """select adress, addfiles, text from (select p.text, p.addfiles, c.adress from 
                                              notifications p right join users c on p.id_userfkey = c.userID
                                              where p.addfiles < {} and c.adress LIKE '{}' group by
                                              c.adress, p.addfiles, p.text) as foo
                """.format(value, adress)
                check = False
            elif choice == 3:
                title = input('Enter required email(str) = ')
                select = """select name, nameof, size, colour, name from (select c.name, p.nameof, p.size, p.colour from
                                             folders p left join email c on c.gmailID=p.id_mainfolder
                                             where c.name LIKE '{}' group by c.name, p.nameof, p.size, p.colour) as foo
                """.format(title)
                check = False
            else:
                print('Try again')
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        obj = View(choice, datas)
        obj.output_spec()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        connection.connectionlost(connect)



    @staticmethod
    def randomik():
            connect = connection.connection()
            cursor = connect.cursor()
            check = True
            while check:
                View.listof()
                table = Model.existingtable()
                kolvo = input('How much datas do you want to add => ')
                kolvo = int(kolvo)

                if table == 1:
                    res = 0
                    insert = "INSERT INTO email (Creator, Name) select chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int), " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int) " \
                             "from generate_series(1,{})".format(kolvo)
                    cursor.execute(insert)
                    check = False
                elif table == 2:
                    res = 0
                    while (True):
                        insert = "INSERT INTO folders(Size, Colour, Nameof, id_mainfolder) select random() * 256," \
                             "random() * 256," \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)," \
                             "(select gmailID from email order by random() limit 1)"\
                             "from generate_series(1,1)"
                        cursor.execute(insert)
                        res = res + 1
                        if(res == kolvo):
                            break
                    check = False
                elif table == 3:
                    res = 0
                    while (res != kolvo):
                        insert = "INSERT INTO users (adress, place, id_mail) select " \
                                 "chr(trunc(65 + random()*25)::int)||chr(trunc(65 + " \
                                 "random()*25)::int), " \
                                 "chr(trunc(65 + random()*25)::int)||chr(trunc(65 + random()*25)::int)," \
                                 "(select gmailID from email order by random() limit 1) " \
                                 "from generate_series(1,1)"
                        cursor.execute(insert)
                        res = res + 1

                    check = False
                elif table == 4:
                    res = 0
                    while (res != kolvo):
                        insert = "INSERT INTO notifications (text, addfiles, title, id_userfkey, id_sender) select " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int), random() * 256," \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)," \
                             "(select userID from users order by random() limit 1)," \
                             "random() * 256 " \
                             "from generate_series(1,1)"
                        cursor.execute(insert)
                        res = res + 1
                    check = False
                elif table == 5:
                    res = 0
                    while (res!=kolvo):

                         insert = "INSERT INTO folders_notifications (notifications_id, folders_id) select " \
                             "(select povID from notifications order by random() limit 1)," \
                             "(select foldID from folders order by random() limit 1) " \
                             "from generate_series(1,1)"
                         cursor.execute(insert)
                         res = res + 1
                    check = False
                elif table == 6:
                    res = 0
                    while (res!=kolvo):
                            insert = "INSERT INTO notifications_users (notifications_id, users_id) select " \
                             "(select povID from notifications order by random() limit 1)," \
                             "(select userID from users order by random() limit 1) " \
                             "from generate_series(1,1)"
                            cursor.execute(insert)
                            res = res + 1
                    check = False
                else:
                    print("Try again")
            print(Tables[table])
            print("SQL query => ", insert)
            connect.commit()
            print('Inserted randomly')
            cursor.close()
            connection.connectionlost(connect)