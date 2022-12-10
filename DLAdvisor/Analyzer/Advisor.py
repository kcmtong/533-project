from DLAdvisor.ProfileBuilder import Collector
from DLAdvisor.Analyzer import Resource

# TEST ONLY
def kttest1():
    Collector.greeting()

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
        objectove = "apply exchanging for your license from Reciprocal countries"
        
    print(f'Here are your suggested resources to {objective}\n##########' )
    prepRes.display()
    print("")
    OLRes.display()
    print("########")
    
## TODO : Provide Resources
def populatePrepResources(stage):
    
    res1 = [
        ['Learn stage 1/Knowledge Test','http://www.stage1.com'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res2 = [
        ['Learn stage 2/RoadTest7','http://www.stage2.com'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res3 = [
        ['Learn stage 3/RoadTest5','http://www.stage3.com'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res4 = [
        ['Learn stage 4/RecipLic','http://www.stage4.com'],
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


# TODO : Provide Resources
def populateOLResources(stage):

    res1 = [
        ['Learn stage 1/Knowledge Test OL','http://www.stage1.com']
        ]
    
    res2 = [
        ['Learn stage 2/RoadTest7 OL','http://www.stage2.com'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc']
        ]
    
    res3 = [
        ['Learn stage 3/RoadTest5 OL','http://www.stage3.com']
    ]
    
    res4 = [
        ['Learn stage 4/RecipLic OL','http://www.stage4.com']
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
