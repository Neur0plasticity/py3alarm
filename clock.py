"""This module is built with minimal code. Expect no security"""

class Clock:
	"""A simple clock written in python"""
	"""Only tells the time and is extensible"""
	def __init__(self):
		print("initialized Clock")


class Date: 
	""" A simple interface for date """
	def __init__(self, month,day,year):
		self.month 			= Date.checkMonth	(month);
		self.day   			= Date.checkDay		(day);
		self.year  			= Date.checkYear		(year);
	@staticmethod
	def checkMonth(month):	return month;
	@staticmethod
	def checkDay(day):		return day;
	@staticmethod
	def checkYear(year):	return year;

class Time:
	"""A simple interface for time"""
	def __init__(self,hour,minute,second):
		print("initialized time");
		self.hour 	 		= Time.checkHour	(hour);
		self.minute 		= Time.checkMinute	(minute);
		self.second			= Time.checkSecond	(second);
	
	@staticmethod
	def checkHour(hour):		return hour;
	@staticmethod
	def checkMinute(minute):	return minute;
	@staticmethod
	def checkSecond(second):	return second;
	

class Alarm:
	"""A simple interface for an alarm"""		
	
	def __init__(self,dateObj,timeObj):
		print("initialized alarm");
		self.date 	=	dateObj;
		self.time	= 	timeObj;
	
class User:
	"""A simple interface for user"""

	def __init__(self,username,password):
		print("initialized user");
		self.username 		= User.checkUserName(username);
		self.password 		= User.checkpassword(password);

	@staticmethod
	def checkUserName(username):	return username;
	@staticmethod
	def checkPassword(password):		return password;


d = Date(1,1,1);
t = Time(12,12,12);
a = Alarm(d,t);
u = User("bob","pwd");
Clock(a);