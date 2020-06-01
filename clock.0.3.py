class Clock:
    """A simple clock written in python"""
    def __init__(self):
        pass;
        # start clock
        # print time every second
        # check for alarm every interval
    def newAlarm():
        pass;
        # use Alarm object
    def deleteAlarm():pass;
    def getAlarm():pass;

    def newUser():pass;
    def deleteUser():pass;
    def getUser():pass;

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
    def checkDateOBJ(dataOBJ):pass;

    @staticmethod
    def checkTimeOBJ(timeOBJ):pass;


class User:
    """ A simple user object interface {username,password} """
    def __init__(self,username,password):pass;

    @staticmethod
    def checkUsername(username):pass;

    @staticmethod
    def checkPassword(password):pass;