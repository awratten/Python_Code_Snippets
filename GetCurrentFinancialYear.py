__author__ = "Anthony Wratten"
__copyright__ = "Copyright 2017, Anthony Wratten"
__version__ = "1.0.0"


#
# Comments: Useful code snippet for getting the current financial year
# Returns: String eg. 2017/2018
# Inputs: user must change the LastMonth variable to the month (number) for your country
#

import time

def GetCurrentFinancialYear():
    LastMonth = 6 #Last month of the financial year eg. June would be : 6
    CurrentYear = int(time.strftime("%Y"))
    PreviousYear = int(time.strftime("%Y")) - 1
    NextYear = int(time.strftime("%Y")) + 1
    FinYear = ""
    if (int(time.strftime("%m")) > LastMonth):
        FinYear = str(CurrentYear) + "/" + str(NextYear)
    else:
        FinYear = str(PreviousYear) + "/" + str(CurrentYear)
    return FinYear
