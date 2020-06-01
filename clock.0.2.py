class Clock:
    """A simple clock written in python"""
    def __init__(self):pass;

    def newAlarm(User,Alarm):pass;
    def deleteAlarm(User,Alarm):pass;
    def getAlarms(User):pass;

    def newUser(User):pass;
    def deleteUser(User):pass;
    def getUser(User):pass;

class Date:
    """ A simple date obj interface {hour,minute,second} """
    def __init__(self,month,day,year):pass;

    @staticmethod
	def checkMonth(month):pass;

	@staticmethod
	def checkDay(day):pass;

	@staticmethod
	def checkYear(year):pass;

class Time:
    """ A simple time obj interface {hour,minute,second}"""
    def __init__(self,hour,minute,second):pass;

    @staticmethod
	def checkHour(hour):pass;

	@staticmethod
	def checkMinute(minute):pass;

	@staticmethod
	def checkSecond(second):pass;

class Alarm:
    """ A simple alarm object interface {dateOBJ,timeOBJ} """
    def __init__(self,dateOBJ,timeOBJ):pass;

    @staticmethod
    def checkDateOBJ(dateOBJ):pass;

    @staticmethod
    def checkTimeOBJ(timeOBJ):pass;


class User:
    """ A simple user object interface {username,password} """
    def __init__(self,username,password):pass;

    @staticmethod
    def checkUsername(username):pass;

    @staticmethod
    def checkPassword(password):pass;