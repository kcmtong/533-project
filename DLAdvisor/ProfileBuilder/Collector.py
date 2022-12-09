from .UserProfile import UserProfile

# make cross package call
# TODO (NOWSHABA) : introduce application purpose/guidance
def greeting():
    print("Greeting pending....Good day!")

# TODO (NOWSHABA) : add a few questions to confirm user's eligibility for BC DL (e.g. resident, no previous revoke of DL, pls google to find a few prerequisit bf applying BC DL
# return True if eligble for license
def passBasicEligibility():
    # Validation to be added?
    age = int(input("How old are you : "))
    if (age >= 16) :
        return True
    else :
        return False

# TODO (NOWSHABA) : (i) ask user for inputs, (ii) construct the UserProfile object
# call class modeule in the same pkg
# Return UserProfile object
def gatherProfile():
    # TODO : Just hardcoded for POC, to be changed to user input
    profile = UserProfile("roBOt",1,True,True,3)
    return profile

