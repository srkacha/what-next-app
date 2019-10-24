#Module for file manipualtion utility funtions

def readLinesFromFile(fileDestination, fileEncoding):
    try:
        file = open(fileDestination, encoding=fileEncoding, mode="r")
        lines = file.readlines()
        return lines
    except:
        return UnicodeError

