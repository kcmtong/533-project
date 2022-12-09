from DLAdvisor.ProfileBuilder import Collector, UserProfile

def execute():
    Collector.greeting()
#    if (!Collector.passBasicEligiblity()) :
#        print("Sorry, not eligible! Bye!")
#        return
    if (not Collector.passBasicEligibility()) :
        print("Sorry, too young!")
        return
    print("Great! You can proceed2")
    user = Collector.gatherProfile()    
    user.formatName()
    print("Returned User Profile ....." + str(user))
    
    # TODO BY KENNY