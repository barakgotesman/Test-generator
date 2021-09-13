def getFile(fileName):
    file = open(fileName, "r")
    return file

def getString(line):
    return line.strip("\n")
