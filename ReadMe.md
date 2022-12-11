# DATA 533 Project (Group 3) : BC Driver's License Advisor

## Structure and Module
The DLAdvisor package containers two subpackages, namely :
- ProfileBuilder : responsible for interacting with users, collect inputs, and constructing user profile objects
- Analyzer : responsible for gathering resources object, and present the recommendation to users

## Main Controller
`Main.py` (under DLAdvsior) is the main program which orchestrates all the modules and class in under the package.

## Call the Main Controller
Take reference to the `RunMe.ipynb`.

## How They Work
Keep track of the user profile, determine the user stage, populate various resources depending on user stage, and present to user.
