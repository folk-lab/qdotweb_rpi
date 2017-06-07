#########################################
########## User Defined Imports #########
#########################################



##########################################
###### User Defined Global Variables #####
##########################################



#########################################
########## User Defined Devices #########
#########################################

DEVICE_NAMES = [""]

##########################################
####### Device object, do not alter ######
##########################################

class Device(object):
    def __init__(self, nm):
        self.name = nm
    def getName(self):
        return self.name
    def getData(self, cmd):
        return user_defined_data_method(self.name, cmd)

##########################################
## Device method, alter where necessary ##
##########################################

def user_defined_data_method(nm, cmd):
	if nm==DEVICE_NAMES[0] and cmd == "":
		return ""

#########################################
######### User Defined Interface ########
#########################################


