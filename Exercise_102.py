#A leap year is a year that is evenly divisible by 4, 100  and 400.
#A leap year can also be divisible by 4 and not divisible by both 100 and 400
def leap_year_checker(year): 
   
   if year % 4 == 0:
      
      if year % 100 == 0: 
         
         if year % 400 == 0:

            #True means that the year is a leap year
            return True
         
         else:

            return False
         
      else: 
         
         return True 
   
   else: 

       return False
   
    
def days_in_month(year, month):
   month_days = [31,28,31,30,31,30,31,31,30,31,30,31] 
   number = month_days[month]
   print(number)
   leap = leap_year_checker(year)
   if(leap == True):
      month_days[1] = 29
      number = month_days[1]

   return f"{year} on {month} has {number} days"


year = int(input("Enter the year you want to check: "))
month = int(input("Enter the month in number: "))

checker = days_in_month(year, month)
print(checker)

        