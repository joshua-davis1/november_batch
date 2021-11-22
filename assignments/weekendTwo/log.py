import logging

def logStart():
    logging.basicConfig(filename='report.log', level=logging.DEBUG)
    logging.debug('Starting py analysis using pandas.')


def closeFile():
    logging.debug("File closed")

def openFile(fName):
    logging.debug("Analysing %s" % fName)

def dfLenErr(data):
    logging.error("Entry Count Discrepancy\n%s entries: %i\n%s entries: %i\nSkipping file" % (data["file"][0],data["dataframe"][0],data["file"][1],data["dataframe"][1]))

def offset(offset):
    logging.debug("offset: %i" % offset)

def alreadyPrc(fName):
    logging.error("File Already Processed\nfile: %s" % fName)

def invalidPhNum(i,col):
    logging.error("Invalid Phone Number in column: %s @ %i" % (col,i))

def invalidSts(i,col):
    logging.error("Invalid State found in column: %s @ %i" % (col,i))

def invalidEmail(i,col):
    logging.error("Invalid Email found in column: %s @ %i" % (col,i))
