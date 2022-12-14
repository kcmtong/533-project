from DLAdvisor.ProfileBuilder import Collector
from DLAdvisor.Analyzer import Resource

def advice(stage) :
    prepRes = populatePrepResources(stage)
    OLRes = populateOLResources(stage)
    if (stage == 1) :
        objective = "pass the ICBC Knowledge Test"
    elif (stage == 2) :
        objective = "pass the ICBC Road Test 5"
    elif (stage == 3) :
        objective = "pass the ICBC Road Test 7"
    else :
        objective = "apply exchanging for your license from Reciprocal countries"
        
    print(f'Here are your suggested resources to {objective}\n##########' )
    prepRes.display()
    print("")
    OLRes.display()
    print("########")
    
def populatePrepResources(stage):
    
    res1 = [
        ['Learn stage 1/Knowledge Test','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-L.aspx'],
        ['Book Appointment for Knowledge Test','https://appointments.servicebc.gov.bc.ca/appointment'],
        ['Practice Knowledge Test', 'https://www.icbc.com/driver-licensing/new-drivers/Pages/practice-knowledge-test.aspx'],
        ['Download ICBC Apps for iOS','https://apps.apple.com/ca/app/icbc-practice-knowledge-test/id438491857'],
        ['Download ICBC Apps for Android','https://play.google.com/store/apps/details?id=com.icbc.knowledge'],
        ['Learn to Drive Smart', 'https://www.icbc.com/driver-licensing/driving-guides/Pages/Learn-to-Drive-Smart.aspx'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res2 = [
        ['Learn stage 2/RoadTest7','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-N.aspx'],
        ['Book a Road Test','https://onlinebusiness.icbc.com/webdeas-ui/home'],
        ['Learn to Drive Smart', 'https://www.icbc.com/driver-licensing/driving-guides/Pages/Learn-to-Drive-Smart.aspx'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res3 = [
        ['Learn stage 3/RoadTest5','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-full-licence.aspx'],
        ['Book a Road Test','https://onlinebusiness.icbc.com/webdeas-ui/home'],
        ['Learn to Drive Smart', 'https://www.icbc.com/driver-licensing/driving-guides/Pages/Learn-to-Drive-Smart.aspx'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res4 = [
        ['Learn stage 4/RecipLic','https://www.icbc.com/driver-licensing/moving-bc/Pages/Moving-from-another-country.aspx'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]

    if (stage == 1) :
        res = res1
    elif (stage == 2) :
        res = res2
    elif (stage == 3) :
        res = res3
    else :
        res = res4
        
    return Resource.PrepResource(stage,res)


## Populate Online Resources (e.g. icbc application links to apply knowledge test/road test/reciprocal license exchange, knowledge test registration links, driving school registration link, etc) 

def populateOLResources(stage):

    res1 = [
        ['Learn stage 1/Knowledge Test OL','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-L.aspx'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
        ]
    
    res2 = [
        ['Learn stage 2/RoadTest7 OL','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-N.aspx'],
        ['Book Road Test','https://onlinebusiness.icbc.com/webdeas-ui/home'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
        ]
    
    res3 = [
        ['Learn stage 3/RoadTest5 OL','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-full-licence.aspx'],
        ['Book Road Test','https://onlinebusiness.icbc.com/webdeas-ui/home'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
    ]
    
    res4 = [
        ['Learn stage 4/RecipLic OL','https://www.icbc.com/driver-licensing/moving-bc/Pages/Moving-from-another-country.aspx'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
        ]

    if (stage == 1) :
        res = res1
    elif (stage == 2) :
        res = res2
    elif (stage == 3) :
        res = res3
    else :
        res = res4
        
    return Resource.OLResource(stage,res)
