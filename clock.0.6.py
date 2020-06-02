class Clock:
    """A simple clock written in python"""
    def __init__(self):
        pass;
        # start clock
        # print time every second
        # check for alarm every interval

    def newAlarm(User,Alarm):
        pass;
        # use User Class
        # no duplicate users
        # use Alarm Class
        # merge-store/zipOBJ User & Alarm

    def deleteAlarm(User,Alarm):
        pass;
        # find alarm
        # exist-alarm   delete alarm
        # !exist:       report error

    def getAlarms(User):
        pass;
        # find alarms matching user
        # exist-alarmuser:  print found alarms
        # !exist-alarmuser: report error

    def newUser(User):
        pass;
        # use User class
        # exist-user:   create
        # user exist:   report error

    def deleteUser(User):
        pass;
        # find user
        # exist-user    : delete user
        # !exist-user   : report error

    def getUser(User):
        pass;
        # find user
        # exist-user    : print user
        # !exist-user   : report error

class Date:
    """ A simple date obj interface {hour,minute,second} """
    def __init__(self,month,day,year):
        pass;
        # mirror params to self


    @staticmethod
	def checkMonth(month):
        pass;
        # 12 >= month >= 1
        # true: return month;
        # false: raise error

	@staticmethod
	def checkDay(day):
        pass;
        # 31 >= day >= 1   # pretend all months have 31 days
        # true: return month;
        # false: raise error

	@staticmethod
	def checkYear(year):
        pass;
        # year >= actual year
        # true:     return year
        # false:    raise error

class Time:
    """ A simple time obj interface {hour,minute,second}"""
    def __init__(self,hour,minute,second):
        pass;
        # mirror params to self
        # check args

    @staticmethod
	def checkHour(hour):
        pass;
        # 23 >= hour >= 0
        # true:     return hour
        # false:    raise error

	@staticmethod
	def checkMinute(minute):
        pass;
        # 23 >= minute >= 0
        # true:     return minute
        # false:    raise error

	@staticmethod
	def checkSecond(second):
        pass;
        # 59 >= second >= 0
        # true:     return second
        # false:    raise error

class Alarm:
    """ A simple alarm object interface {dateOBJ,timeOBJ} """
    def __init__(self,dateOBJ,timeOBJ):
        self.dateOBJ = Alarm.checkDateOBJ(dateOBJ)
        self.timeOBJ = Alarm.checkTimeOBJ(timeOBJ)

    @staticmethod
    def checkDateOBJ(dateOBJ):
        a = "month" in dateOBJ
        b = "day"   in dateOBJ
        c = "year"  in dateOBJ
        
        if (a && b && c) return dateOBJ
        else raise Exception("unhandled exception")

    @staticmethod
    def checkTimeOBJ(timeOBJ):
        a = "hour"      in dateOBJ
        b = "minute"    in dateOBJ
        c = "second"    in dateOBJ
        
        if (a && b && c) return timeOBJ
        else raise Exception("unhandled exception")


class User:
    """ A simple user object interface {username,password} """
    def __init__(self,username,password):
        self.username = User.checkUsername(username)
        self.password = User.checkPassword(password)

    @staticmethod
    def checkUsername(username):
        r = empty(username)
        if (r == True) raise Exception("")
        elif (r === false) return username
        else            raise Exception("unhandled execption")

    @staticmethod
    def checkPassword(password):
        r = empty(password)
        if (r == True) raise Exception("")
        elif (r === false) return password
        else           raise Exception("unhandled execption")

def printMSG(msg):
    print(msg)

def exist(where,what):
    return what in where

def find(where,what,onNone,onFound):
    r = what in where
    if r == False:  return onNone()
    elif r == True: return onFound(where[what])
    else raise Exception("unhandled expection")

def delet(obj,key):
    r = what in where
    if r == False:  raise Exception("obj key not found")
    elif r == True: del obj[key]
    else raise Exception("unhandled exception")

def new(where,what,obj):
    r = what in where;
    if r == True:   raise Exception("where what exists")
    elif r == False: return where[what] = obj
    else raise Exception("unhandled exception")

def merge(c,a,b):
    # no defense against overwriting a key
    for k in a:
        c[k] = a[k]
    for k in b:
        c[k] = b[k]
    return c

def empty(str):
    r = len(str)
    if r == 0: return True
    elif r > 0: return False
    else raise Exception("unhandled exception")
    