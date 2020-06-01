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
        pass;
        # mirror params to self
        # check args

    @staticmethod
    def checkDateOBJ(dataOBJ):
        pass;
        # 23 >= hour >= 0
        # true:     return hour
        # false:    raise error

    @staticmethod
    def checkTimeOBJ(timeOBJ):pass;


class User:
    """ A simple user object interface {username,password} """
    def __init__(self,username,password):
        pass;
        # mirror params to self
        # check args

    @staticmethod
    def checkUsername(username):
        pass;
        # notEmpty-username:
        # true:    return username
        # false:   raise error

    @staticmethod
    def checkPassword(password):
        pass;
        # notEmpty-username:
        # true:    return username
        # false:   raise error


def printMSG():pass;
def check():pass;
def exist():pass;
def find():pass;
def delet():pass;
def new():pass;
def merge():pass;
def empty():pass;
    