import random
import connection
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
    def existingtable(table):
        if str(table).isdigit():
             table = int(table)
             cons = True
             while cons:
                if table == 1 or table == 2 or table == 3 or table == 4 or table == 5 or table == 6:
                   return table
                else:
                   print('///Try again.')
                   return 0
        else:
             print('Try again')
             return 0


    @staticmethod
    def outputonetable(table):
        connect = connection.connection()
        cursor = connect.cursor()
        show = 'select * from public.{}'.format(Tables[table])
        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        datas = cursor.fetchall()
        cursor.close()
        connection.connectionlost(connect)
        return datas

    @staticmethod
    def insertbyusertoEmail(f,s,t,added,notice):
        connect = connection.connection()
        cursor = connect.cursor()
        insert = 'DO $$ BEGIN if (1=1) and not exists (select gmailID from email where gmailID = {}) then INSERT INTO email(gmailID, creator, name) VALUES ({},{},{}); ' \
                 'raise notice {}; else raise notice {}; ' \
                 'end if; end $$;'.format(f, f, s, t, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def insertbyusertoFolders(f,s,t,fouth, fifth, added,notice):
        connect = connection.connection()
        cursor = connect.cursor()
        insert = 'DO $$	BEGIN IF EXISTS (select gmailID from email where gmailID = {}) and not exists (select foldId from folders where foldId = {}) THEN ' \
                 'INSERT INTO folders(foldID, Size, Colour, nameof, id_mainfolder) values ({}, {}, {}, {}, {}); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(fifth, f, f, s, t, fouth, fifth, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def insertbyusertoUsers(f,s,t,fouth,added,notice):
        connect = connection.connection()
        cursor = connect.cursor()
        insert = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {}) and not exists (select userID from users where userID = {}) THEN ' \
                 'INSERT INTO users(userID, adress, place, id_mail) values ({}, {}, {}, {}); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(fouth, f, f, s, t, fouth, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def insertbyusertoNotifications(f,s,t,fouth,fifth,sixth,added,notice):
        connect = connection.connection()
        cursor = connect.cursor()
        insert = 'DO $$	BEGIN IF EXISTS (select userID from users where userID = {}) and not exists (select povID from notifications where povID = {}) THEN ' \
                 'INSERT INTO notifications(povID, text, addfiles, title, id_userfkey, id_sender) values ({}, {}, {}, {}, {}, {}); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(fifth, f, f, s, t, fouth, fifth, sixth, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def deleteEmail(idk, delete, notice):
        connect = connection.connection()
        cursor = connect.cursor()
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
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def deleteFolders(idk, delete, notice):
        connect = connection.connection()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if ' \
                 'exists (select foldID from folders where foldID = {}) then ' \
                 ' delete from folders_notifications where folders_ID in (select foldID from folders where id_mainfolder = {});' \
                 'delete from folders where foldID= {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def deleteUsers(idk, delete, notice):
        connect = connection.connection()
        cursor = connect.cursor()
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
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def deleteNotifications(idk, delete, notice):
        connect = connection.connection()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if exists (select povID from notifications where povID = {}) then ' \
                 'delete from notifications_users where notifications_ID = {};' \
                 'delete from folders_notifications where notifications_ID = {};' \
                 'delete from notifications where povID= {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def UpdateEmail(idk, set2, set3, updated, notice):
        connect = connection.connection()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select gmailID from email where gmailID = {}) THEN ' \
                 'update email set creator = {}, name = {} where gmailID = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, set2, set3, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)


    @staticmethod
    def UpdateFolders(idk, set1, set2, set3, updated, notice):
        connect = connection.connection()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select foldID from folders where foldID = {})' \
                 ' THEN ' \
                 'update folders set Size = {}, Colour = {}, nameof = {} where foldID = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, set1, set2, set3, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def UpdateUsers(idk, adress, place, updated, notice):
        connect = connection.connection()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select userID from users where userID = {}) ' \
                 ' THEN ' \
                 'update users set adress = {}, place = {} where userID = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, adress, place, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)

    @staticmethod
    def UpdateNotifications(idk, text, addfiles, title, sender, updated, notice):
        connect = connection.connection()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select povID from notifications where povID = {}) ' \
                 ' THEN ' \
                 'update notifications set text = {}, addfiles = {}, title = {}, id_sender = {} where povID = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, text, addfiles, title, sender, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        connection.connectionlost(connect)


    @staticmethod
    def selectionone(len, creator):
        connect = connection.connection()
        cursor = connect.cursor()
        select = """select size, colour, name, creator from (select c.size, c.colour, p.name, 
                                        p.creator from 
                                            folders c left join email p
                                             on p.gmailID = c.id_mainfolder where length(p.name) >= {} and p.creator LIKE '{}' 
                                              group by c.size,
                                             c.colour, p.name, p.creator) as foo""".format(len, creator)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        connection.connectionlost(connect)
        return datas

    @staticmethod
    def selectiontwo(value, adress):
        connect = connection.connection()
        cursor = connect.cursor()
        select = """select adress, addfiles, text from (select p.text, p.addfiles, c.adress from 
                                                      notifications p right join users c on p.id_userfkey = c.userID
                                                      where p.addfiles < {} and c.adress LIKE '{}' group by
                                                      c.adress, p.addfiles, p.text) as foo
                        """.format(value, adress)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        connection.connectionlost(connect)
        return datas

    @staticmethod
    def selectionthree(title):
        connect = connection.connection()
        cursor = connect.cursor()
        select = """select name, nameof, size, colour, name from (select c.name, p.nameof, p.size, p.colour from
                                                     folders p left join email c on c.gmailID=p.id_mainfolder
                                                     where c.name LIKE '{}' group by c.name, p.nameof, p.size, p.colour) as foo
                        """.format(title)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        connection.connectionlost(connect)
        return datas




    @staticmethod
    def randomik(table, kolvo):
            connect = connection.connection()
            cursor = connect.cursor()
            check = True
            while check:
                if table == 1:
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
                    check = False
            print(Tables[table])
            print("SQL query => ", insert)
            connect.commit()
            print('Inserted randomly')
            cursor.close()
            connection.connectionlost(connect)