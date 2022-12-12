from .UserProfile import UserProfile
import datetime
from datetime import date

# This fuction will greet the applicant based onthe time of the day
def greeting():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12 :
        print('Good morning!')
    elif 12 <= currentTime.hour < 18 :
         print('Good afternoon!')
    else:
         print('Good evening!')

#Calculate no. of years from current date based on a date input (like, age, driving license yrs, etc.)
def calculateAge(dateEntry):
    days_in_year = 365.2425  
    age = int((date.today() - dateEntry).days / days_in_year)
    return age
       
# This function takes input from user to create profile and check eligibility
# This returns True if eligible for license
def passBasicEligibility():
    # Validation to be added?
    bcres = input("Are you a BC resident?[Yes/No]")#BC resident
    if (bcres == "No") :
        print("Only BC residents are eligible to get a BC Driving License")
        return False
    name = input("What is your full name?")# Full Name
    dob = input("Enter your date of birth?[DD/MM/YYYY]") #Date of birth
    birthday_list = dob.split("/")
    day=int(birthday_list[0])
    month=int(birthday_list[1])
    year=int(birthday_list[2])
    age = calculateAge(date(year, month, day)) #applicant age
    if (age < 16) :
        print("Your age is",age,"which is below 16 yrs, so you are not eligible for BC Driving license")
        return False
    haveICBCLicence = input("Do you have ICBC driver licence? [Yes/No]")
    wantToExchange =("Do you want to exchnage your licence? [Yes/No]")
    #country = input("Where are you from? Canada/Your Country Name/Others")# Full Name
    if haveICBCLicence == "Yes":
        reciprocal = input("Are you from a reciprocal country? [Yes/No]")
    haveDriveLic = input("Do you have a driving license from your country? [Yes/No]")# Have exiting license?
    if haveDriveLic == "Yes":
        drivingLicDate=input("Driving license date [DD/MM/YYYY]:")# country type
        driveDate = drivingLicDate.split("/")
        day=int(driveDate[0])
        month=int(driveDate[1])
        year=int(driveDate[2])
        drivingYears = calculateAge(date(year, month, day)) #driving years
    else:
        drivingYears = 0 #driving years
    
    #defines the stages
    #1=No driving experince (Learner's License)
    #2=from 1 upto 2 years driving (Novice License)
    #3=greater than 2 years driving expericense (Full License)

        
    print(name,"'s profile:\n Age:",age,"\nFrom:",country,"\nReciprocal Country:",reciprocal,"\nHave License:",haveDriveLic,"\nDriving years:",drivingYears)
    return True

# After taking input from user in passBasicEligibility() it then constructs the UserProfile object
# call class modeule in the same pkg
# Return UserProfile object
def gatherProfile():
    # TODO : Just hardcoded for POC, to be changed to user input
    #UserProfile(self,name,current_icbc_lic,is_dl_exchange,is_recip_country,stage)
    profile = UserProfile(name,haveDrivingLic,haveDrivingLic,reciprocal,3)
    return profile

