from sqlalchemy.orm import relationship, backref
from db import Base, Session, engine
import psycopg2
from sqlalchemy import *
import time

metadata = MetaData()

s = Session()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class email(Base):
    __tablename__ = 'email'
    gmailID = Column(Integer, primary_key=True, nullable=False, unique=True)
    creator = Column(String, nullable=False)
    name = Column(String, nullable=False)
    users = relationship("users")
    folders = relationship("folders")

    #users -> child
  #  counter = relationship('users', cascade="all, delete, delete-orphan", backref='propperstrike')

    def __init__(self, gmailID, creator, name):
        self.gmailID = gmailID
        self.creator = creator
        self.name = name

    def __repr__(self):
        return "<email(gmailID={}, creator='{}', name='{}')>"\
    .format(self.gmailID, self.creator, self.name)

#Column('ppID', Integer, primary_key=True),

folders_notifications_association = Table(
    'folders_notifications', Base.metadata,
    Column('ppID', Integer, primary_key=True, nullable=False),
    Column('pov_ID', Integer, ForeignKey('notifications.povID', ondelete="CASCADE"), primary_key=True, nullable=False),
    Column('fold_ID', Integer, ForeignKey('folders.foldID', ondelete="cascade"), primary_key=True, nullable=False)
)
#   Column('pkID', Integer, primary_key=True),
users_notifications_association = Table(
   'users_notifications', Base.metadata,
    Column('pkID', Integer, primary_key=True, nullable=False),
    Column('pov_ID', Integer, ForeignKey('notifications.povID', ondelete="CASCADE"), nullable=False),
    Column('users_ID', Integer, ForeignKey('users.userID', ondelete="cascade"), nullable=False)
)

class folders(Base):
    __tablename__ = 'folders'
    foldID = Column(Integer, primary_key=True, nullable=False, unique=True)
    size = Column(Integer, nullable=False)
    colour = Column(Integer, nullable=False)
    nameof = Column(String, nullable=False)
    id_mainfolder = Column(Integer, ForeignKey('email.gmailID'), nullable=False)

    fol_not = relationship("notifications", secondary=folders_notifications_association, back_populates="not_fol",
        passive_deletes='all', lazy='dynamic')

    def __init__(self, foldID, size, colour, nameof, id_mainfolder):
        self.foldID = foldID
        self.size = size
        self.colour = colour
        self.nameof = nameof
        self.id_mainfolder = id_mainfolder


    def __repr__(self):
        return "<folders(foldID={} ,size={}, colour={}, nameof='{}', id_mainfolder={})>"\
    .format(self.foldID, self.size, self.colour, self.nameof, self.id_mainfolder)

class users(Base):
    __tablename__ = 'users'
    userID = Column(Integer, primary_key=True, nullable=False, unique=True)
    adress = Column(String, nullable=False)
    place = Column(String, nullable=False)
    id_mail = Column(Integer, ForeignKey('email.gmailID'), nullable=False)
  #  children = relationship("notifications", secondary=users_notifications_association, back_populates="pk", cascade = "all, delete")
    us_not = relationship("notifications", secondary=users_notifications_association, back_populates="not_us",
        passive_deletes='all', lazy='dynamic')
    #notifications -> child - one to many
    counter = relationship('notifications', cascade="all, delete",back_populates='propper', passive_deletes=True)
    #email -> parent
   # propper = relationship('email', backref=backref('counterstrike', cascade='all, delete'))


    def __init__(self, userID, adress, place, id_mail):
        self.userID = userID
        self.adress = adress
        self.place = place
        self.id_mail = id_mail

    def __repr__(self):
        return "<users(userID={}, adress='{}', place={}, id_mail={})>"\
    .format(self.userID, self.adress, self.place, self.id_mail)



class notifications(Base):
    __tablename__ = 'notifications'
    povID = Column(Integer, primary_key=True, nullable=False, unique=True)
    text = Column(String, nullable=False)
    addfiles = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    id_userFkey = Column(Integer, ForeignKey('users.userID', ondelete="CASCADE"), nullable=True)
    id_sender = Column(Integer, nullable=True)

    not_fol = relationship("folders", secondary=folders_notifications_association, back_populates="fol_not",
        passive_deletes='all', lazy='dynamic')

    not_us = relationship("users", secondary=users_notifications_association, back_populates="us_not",
        passive_deletes='all', lazy='dynamic')

    # users -> parent one to many
    propper = relationship('users', back_populates="counter")

    def __init__(self, povID, text, addfiles, title, id_userFkey, id_sender):
        self.povID = povID
        self.text = text
        self.addfiles = addfiles
        self.title = title
        self.id_userFkey = id_userFkey
        self.id_sender = id_sender

    def __repr__(self):
        return "<notifications(povID={}, text='{}', addfiles={}, title='{}', id_userFkey={}, id_sender={})>"\
    .format(self.povID, self.text, self.addfiles, self.title, self.id_userFkey, self.id_sender)



class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()
    @staticmethod
    def existingtable(table: int):
        if str(table).isdigit():
            table = int(table)
            if table >= 1 and table <= 6:
                return table
            else:
                error = f'table {table} does not exist in the database'
                print(error)
                return 0

    @staticmethod
    def deleteOrNot(table: int, id: int):
        if str(table).isdigit():
            table = int(table)
            if table == 1:
               f = bool(s.query(users).filter_by(id_mail = id).first())
               p = bool(s.query(folders).filter_by(id_mainfolder = id).first())
               if f == True:
                   print('There is dependence in users, you can not delete it')
                   return 0
               elif p == True:
                   print('There is dependence in folders, you can not delete it')
                   return 0
               else:
                   return 1
            elif table == 2:
                f = bool(s.query(folders_notifications_association).filter_by(fold_ID = id).first())
                if f == True:
                    print('There is dependence in folders_notifications, you can not delete it')
                    return 0
                else:
                    return 1
            elif table == 3:
                f = bool(s.query(notifications).filter_by(id_userFkey = id).first())
                if f == True:
                    print('There is dependence in notifications, you can not delete it')
                    return 0
                else:
                    return 1
            elif table == 4:
                f = bool(s.query(folders_notifications_association).filter_by(pov_ID=id).first())
                p = bool(s.query(users_notifications_association).filter_by(pov_ID = id).first())
                if f == True:
                    print('There is dependence in folders_notifications, you can not delete it')
                    return 0
                elif p == True:
                    print('There is dependence in users_notifications, you can not delete it')
                    return 0
                else:
                    return 1

            else:
                return 1


    @staticmethod
    def updateOrNot(table: int, id: int):
        if str(table).isdigit():
            table = int(table)
            if table == 1:
               f = bool(s.query(email).filter_by(gmailID = id).first())
               if f == True:
                   return 1
               else:
                   return 0
            elif table == 2:
                f = bool(s.query(folders).filter_by(foldID = id).first())
                if f == True:
                    return 1
                else:
                    return 0
            elif table == 3:
                f = bool(s.query(users).filter_by(userID = id).first())
                if f == True:
                    return 1
                else:
                    return 0
            elif table == 4:
                f = bool(s.query(notifications).filter_by(povID=id).first())
                if f == True:
                    return 1
                else:
                    return 0

            else:
                return 0

    @staticmethod
    def outputonetable(table: int):
        table = int(table)
        if table == 1:
            for class_instance in s.query(email).order_by(email.gmailID.asc()).all():
                print(class_instance)
        elif table == 2:
            for class_instance in s.query(folders).order_by(folders.foldID.asc()).all():
                print(class_instance)
        elif table == 3:
            for class_instance in s.query(users).order_by(users.userID.asc()).all():
                print(class_instance)
        elif table == 4:
            for class_instance in s.query(notifications).order_by(notifications.povID.asc()).all():
                print(class_instance)
        elif table == 5:
            for class_instance in s.query(folders_notifications_association).all():
                print(class_instance)
        elif table == 6:
            for class_instance in s.query(users_notifications_association).all():
                print(class_instance)
        else:
            print('Try again')



#insert
    @staticmethod
    def insertbyusertoEmail(gmailID: int, creator: str, name: str) -> None:
        var = email(gmailID = gmailID, creator = creator, name = name)
        s.add(var)
        s.commit()

    @staticmethod
    def insertbyusertoUsers(userID: int, adress: str, place: str, id_mail: int) -> None:
        var = users(userID = userID, adress=adress, place=place, id_mail=id_mail)
        s.add(var)
        s.commit()

    @staticmethod
    def insertbyusertoNotifications(povID: int, text: str, addfiles: int, title: str, id_userFkey: int, id_sender: int) -> None:
        var = notifications(povID = povID, text = text, addfiles = addfiles, title=title, id_userFkey=id_userFkey, id_sender=id_sender)
        s.add(var)
        s.commit()

    @staticmethod
    def insertbyusertoFolders(foldID: int, size: int, colour: int, nameof: str, id_mainfolder: int) -> None:
        var = folders(foldID=foldID, size=size, colour=colour, nameof=nameof,id_mainfolder=id_mainfolder)
        s.add(var)
        s.commit()
#delete
    @staticmethod
    def deleteEmail(gmailID) -> None:
        s.query(email).filter_by(gmailID=gmailID).delete()
        s.commit()

    @staticmethod
    def deleteUsers(userID) -> None:
        s.query(users).filter_by(userID=userID).delete()
        s.commit()

    @staticmethod
    def deleteNotifications(povID) -> None:
        s.query(notifications).filter_by(povID=povID).delete()
        s.commit()

    @staticmethod
    def deleteFolders(foldID) -> None:
        s.query(folders).filter_by(foldID=foldID).delete()
        s.commit()

    @staticmethod
    def deleteFoldNot(ppID) -> None:
        s.query(folders_notifications_association).filter_by(ppID=ppID).delete()
        s.commit()

    @staticmethod
    def deleteUsNot(pkID) -> None:
        s.query(users_notifications_association).filter_by(pkID=pkID).delete()
        s.commit()
#update
    @staticmethod
    def UpdateEmail(gmailID: int, creator: str, name: str) -> None:
        s.query(email).filter_by(gmailID=gmailID)\
            .update({email.creator: creator, email.name: name})
        s.commit()

    @staticmethod
    def UpdateUsers(userID: int, adress: str, place: str) -> None:
        s.query(users).filter_by(userID=userID)\
            .update({users.adress: adress, users.place: place})
        s.commit()

    @staticmethod
    def UpdateNotifications(povID: int, text: str, addfiles: int, title: str, id_sender: int) -> None:
        s.query(notifications).filter_by(povID=povID)\
            .update({notifications.text: text, notifications.addfiles: addfiles, notifications.title: title,
                    notifications.id_sender: id_sender})
        s.commit()

    @staticmethod
    def UpdateFolders(foldID: int, size: int, colour: int, nameof: str) -> None:
        s.query(folders).filter_by(foldID=foldID)\
            .update({folders.size: size, folders.colour: colour, folders.nameof: nameof})
        s.commit()







