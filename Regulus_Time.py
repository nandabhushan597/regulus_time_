"""
   A python class to represent time on the planet Regulus,
       as described in the lab assignment.

Examples:

>>> t1 = Time(03 + 60 * (25 + 60 * (01 + 24 * ((01-1) + 30 * ((04-1) + 12 * (12-1))))))
>>> print t1	# 04/01/12 01:25:03 AM RST     (or, if you like, 12-04-01 1:15:03 RST)
4/1/12 1:25:3 RST

>>> t1_original = deepcopy(t1)
>>> t1.add_minutes(-120)
>>> print t1					# 120 minutes before 04/01/12 01:25:03 AM RST
3/30/12 23:25:3 RST
>>> t1 = deepcopy(t1_original)

>>> t1.add_minutes(-60)
>>> print t1					#  60 minutes before 04/01/12 01:25:03 AM RST
4/1/12 0:25:3 RST
>>> t1 = deepcopy(t1_original)

>>> t1.add_minutes(60)
>>> print t1					#  60 minutes after  04/01/12 01:25:03 AM RST, i.e. into DST
4/1/12 3:25:3 RDT
>>> t1 = deepcopy(t1_original)


>>> Time(344775540).minutes_until(Time(344775900))  # from the assignment
6

# t2 is "10/01/12 01:55:57 AM RDT"
#  that's a total of 57 seconds plus 60*55 seconds ... minus 1 hour
>>> t2 = Time(57 + 60 * (55 + 60 * (01 + 24 * ((01-1) + 30 * ((10-1) + 12 * (12-1))))) - 3600)
>>> print t2  # "1:55:57 AM on October 1, year 12 prints as: "
10/1/12 1:55:57 RDT

>>> print t1.minutes_until(t2)	# 10/01/12 01:55:57 AM RDT   vs.   04/01/12 01:25:03 AM RST
259170
>>> print t2.minutes_until(t1)	# 04/01/12 01:25:03 AM RST   vs.   10/01/12 01:55:57 AM RDT  # note -259171 is fine too
-259170

>>> t2.add_minutes(60)
>>> print t2	# 1 hour  after "1:55:57 AM on October 1, year 12"
10/1/12 2:55:57 RDT
>>> t2.add_minutes(60)
>>> print t2	# 2 hours after "1:55:57 AM on October 1, year 12"
10/1/12 2:55:57 RST
>>> t2.add_minutes(60)
>>> print t2	# 3 hours after "1:55:57 AM on October 1, year 12"
10/1/12 3:55:57 RST

>>> t3 = deepcopy(t1)
>>> t3.add_minutes(  3)
>>> t1.minutes_until(t3)
3
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(-60)
>>> t1.minutes_until(t3)
-60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(-60)
>>> t3.minutes_until(t1)
60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(  0)
>>> t1.minutes_until(t3)
0
>>> t3 = deepcopy(t1)
>>> t3.add_minutes( 60)
>>> t1.minutes_until(t3)
60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(120)
>>> t1.minutes_until(t3)
120
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(180)
>>> t1.minutes_until(t3)
180

>>> t3 = deepcopy(t2)
>>> t3.add_minutes(  3)
>>> t2.minutes_until(t3)
3
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(-60)
>>> t2.minutes_until(t3)
-60
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(  0)
>>> t2.minutes_until(t3)
0
>>> t3 = deepcopy(t2)
>>> t3.add_minutes( 60)
>>> t2.minutes_until(t3)
60
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(120)
>>> t2.minutes_until(t3)
120
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(180)
>>> t2.minutes_until(t3)
180

"""
from copy import deepcopy
# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)

#collaborated with Sam Danish, Mikal Hayden-Gates, & Connie Chan 

class Time_represented_by_seconds:
    """Replace this with your definition of 'time' so that the test works"""
    def __init__(self, time):  #constructor that passes in time or the number of seconds the user inputs 
       # precondition(type(time)) == type(0)
        self.time = time   #defining instance variable 
        
    def add_minutes(self, min):  #method add_minutes that increments the number of minutes passed
        #precondition(type(self.time))== type(min.time)== type(1)
        self.time = self.time + (60 * min)  
        
    def minutes_until(self, other):  #method that calculates the difference between minutes 
       # precondition(type(self.time))== type(other.time) == type(1)
        answer = ((other.time - self.time)/60) 
        return answer 
    
    def __repr__(self): #__repr__ method that is used to print the date & time  
        
        #local variables seconds in a year, seconds in a month, seconds in a day,seconds in an hour, and seconds in a minute
        #they are passed into the the equations to calculate the output 
        seconds_year= 31104000 
        seconds_month= 2592000 
        seconds_day= 86400 
        seconds_hour = 3600 
        seconds_minutes = 60  
        
        #equation to calculate years from seconds 
        years = self.time/ seconds_year  
        
        #equation sec_left to calculate number of seconds left, will subsequently be updated  
        sec_left = self.time - (years * seconds_year)  
        
        #equation to calculate months from seconds left
        months= sec_left/seconds_month 
        sec_left = self.time - (years * seconds_year)-(months * seconds_month)  
        
        #equation to calculate days from seconds left 
        days= sec_left/seconds_day  
        sec_left = self.time - (years * seconds_year)- (months * seconds_month) - (days * seconds_day) 
        
        #equation to calculate hours from seconds left
        hours= sec_left/seconds_hour 
        sec_left = self.time - (years * seconds_year)- (months * seconds_month) - (days * seconds_day) - (hours * seconds_hour) 
        
        #equation to calculate number of minutes from seconds left 
        minutes= sec_left/seconds_minutes  
        sec_left = self.time - (years * seconds_year)- (months * seconds_month)- (days * seconds_day) - (hours * seconds_hour) - (minutes * seconds_minutes) 
        
        #final number of seconds left 
        seconds = sec_left   
        
        
        #seconds_left equation to use for daylight savings, need number of seconds left in terms of months 
        seconds_left = self.time-(years * seconds_year)  
        
        #calculates the number of seconds until daylight savings begins on April 1st 2AM 
        daylight_start = (3 * seconds_month) + (2 * seconds_hour) 
        
        #calculates the number of seconds until daylight savings ends on October 1st 3AM 
        daylight_end = daylight_start + (6 * seconds_month)  
        
        
        #an if statement that determines whether it is daylight savings time or not 
        #returns an added hour if fits restrictions 
        if (seconds_left >= daylight_start and seconds_left < daylight_end): 
           return str(months + 1) + "/" + str(days + 1)+ "/" + str(years + 1) + " " + str(hours + 1)+ ":" + str(minutes) + ":"+ str(seconds) + " RDT"  
       
        else:
            return str(months + 1) + "/" + str(days + 1)+ "/" + str(years + 1) + " " +  str(hours)+ ":" + str(minutes) + ":"+ str(seconds) + " RST" 
        
       
class Time_represented_by_clock_and_calendar:
    """Replace this with your definition of 'time' so that the test works"""
    def __init__(self,time):   
        #this class uses separate fields for years, months, days, hours, seconds 
        #constructor that passes in time or number of seconds user inputs 
        
        #define variables for seconds in a year, seconds in a month, seconds in a day, seconds in an hour, seconds in a minute 
        seconds_year= 31104000 
        seconds_month= 2592000 
        seconds_day= 86400 
        seconds_hour = 3600 
        seconds_minutes = 60 
        
        #equations that calculate years, months, days, hours, min, and seconds from time 
        self.year= time/seconds_year
        self.month= (time -(self.year * seconds_year))/(seconds_month)
        self.day= (time -(self.year * seconds_year)-(self.month * seconds_month))/(seconds_day) 
        self.hour= (time -(self.year * seconds_year)-(self.month * seconds_month)-(self.day * seconds_day))/(seconds_hour)
        self.min= (time -(self.year * seconds_year)-(self.month * seconds_month)-(self.day * seconds_day)-(self.hour * seconds_hour))/(seconds_minutes)
        self.sec= (time -(self.year * seconds_year)-(self.month * seconds_month)-(self.day * seconds_day)-(self.hour * seconds_hour)-(self.min * seconds_minutes))
         
    
    def add_minutes(self, min): #method that increments minutes 
        
        #variables for converting each measure of time into seconds 
        seconds_year= 31104000 
        seconds_month= 2592000 
        seconds_day= 86400 
        seconds_hour = 3600 
        seconds_minutes = 60    
         
        #calculate each measure of time back into seconds 
        self.year = self.year * seconds_year
        self.month = self.month * seconds_month  
        self.day= self.day * seconds_day
        self.hour= self.hour * seconds_hour
        self.min= self.min * seconds_minutes
        
        #calculate total number of seconds 
        #add or increment minutes by adding number of seconds in a min (60)  * min to total number of seconds 
        total_sec = (self.year + self.month + self.day + self.hour + self.min + self.sec)+(seconds_minutes * min) 
        
        #calculate the amount of time left in years, months, days, hours, minutes, seconds 
        self.year = total_sec/seconds_year
        self.month = (total_sec -((self.year * seconds_year)))/ seconds_month
        self.day = (total_sec -((self.year * seconds_year) + (self.month * seconds_month)))/ (seconds_day) 
        self.hour= (total_sec -((self.year * seconds_year) + (self.month * seconds_month) + (self.day * seconds_day)))/ seconds_hour
        self.min = (total_sec -((self.year * seconds_year) + (self.month * seconds_month) + (self.day * seconds_day) + (self.hour * seconds_hour)))/ seconds_minutes
        self.sec = (total_sec -((self.year * seconds_year) + (self.month * seconds_month) + (self.day * seconds_day) + (self.hour * seconds_hour) + (self.min * seconds_minutes)))
        
        
    def minutes_until(self,other):   #minutes until taking Time or "other" here because I have already used Time previously 
        seconds_year= 31104000 
        seconds_month= 2592000 
        seconds_day= 86400 
        seconds_hour = 3600 
        seconds_minutes = 60
        
        #convert the remaining time or amount of time left back into seconds and add all measures of time up 
        previous_min = ((self.year * seconds_year) + (self.month * seconds_month) + (self.day * seconds_day)+ (self.hour * seconds_hour) + (self.min * seconds_minutes)+ self.sec) 
        
        other_min= ((other.year * seconds_year) + (other.month * seconds_month) + (other.day * seconds_day)+ (other.hour * seconds_hour) + (other.min * seconds_minutes)+ other.sec) 
         
        #subtract the difference in minutes and divide by 60                                                                               
        min_until= ((other_min - previous_min)/(seconds_minutes)) 
        
        #return value of minutes until 
        return min_until 
         
    def __repr__(self): #__repr__ method that prints & formats date and time 
        
        #number of seconds in a year, month, day, hour, and minute for conversion 
        seconds_year= 31104000 
        seconds_month= 2592000 
        seconds_day= 86400 
        seconds_hour = 3600 
        seconds_minutes = 60
         
        #calculate seconds left up to months by adding the number of seconds for each measure of time but subtracting seconds in years 
        seconds_left = ((self.year * seconds_year)+(self.month * seconds_month) + (self.day * seconds_day) + (self.hour * seconds_hour)+ (self.min * seconds_minutes) + (self.sec)) -(self.year * seconds_year)
       
        #the number of seconds until daylight savings starts on April 1st 2AM 
        daylight_start = (3 * seconds_month) + (2 * seconds_hour) 
        
        #the number of seconds until daylight savings ends on October 1st 3AM 
        daylight_end = daylight_start + (6 * seconds_month) 
        
        #if statement that decides whether or note the date & time falls into daylight savings time period 
        if (seconds_left >= daylight_start and seconds_left < daylight_end): 
           return str(self.month + 1) + "/" + str(self.day + 1)+ "/" + str(self.year + 1) + " " + str(self.hour + 1)+ ":" + str(self.min) + ":"+ str(self.sec) + " RDT"  
       
        else:
            return str(self.month + 1) + "/" + str(self.day + 1)+ "/" + str(self.year + 1) + " " +  str(self.hour)+ ":" + str(self.min) + ":"+ str(self.sec) + " RST" 
        
# by default, use the first representation, but this is changed in DocTest below


# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    global Time
    Time = Time_represented_by_seconds
    result = doctest.testmod()
    print "Result of doctest for Time_represented_by_seconds is:",
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"

    print "\n\n\n\n"
    
    Time = Time_represented_by_clock_and_calendar
    result = doctest.testmod()
    print "Result of doctest for Time_represented_by_clock_and_calendar is:",
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"
    Time = Time_represented_by_seconds

if __name__ == "__main__":
    _test()
