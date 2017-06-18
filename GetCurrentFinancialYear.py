__author__ = "Anthony Wratten"
__copyright__ = "Copyright 2017, Anthony Wratten"
__version__ = "1.0.0"

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
