import data as DataFile

def getFile(fileName):
    file = open(fileName, "r")
    return file

# clean \n from my string
def getString(line):
    return line.strip("\n")

# Extract all information from seouce file to create test
def createDataTest(source):
    file = getFile(source)
    dataFile = file.readlines()

    for index, line in enumerate(dataFile):

        print(line, end="")

        # find questions
        # string that ends with question mark.
        # ANSWER MUST BE THE FIRST OPTION
        if(line.find("?") > -1 and line.find("?") == len(line)-2):
            questionAndCurrectAnswer = (
                getString(line), getString(dataFile[index+1]))
            DataFile.questionsAndAnswers.append(questionAndCurrectAnswer)

            options = []  # list of options for the question
            option = True
            nextIndex = index+1
            # protect (out of range)
            while nextIndex < len(dataFile):
                option = dataFile[nextIndex]
                # new empty line means end of options
                if option == "\n":
                    break
                
                # append option to list
                options.append(getString(option))
                nextIndex += 1
            
            # end scanning options of question that found
            DataFile.questionsAndOptions.append((getString(line), options))