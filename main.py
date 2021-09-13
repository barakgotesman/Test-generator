import data as DataFile
import functions as fn


file = fn.getFile("quiz.txt")
dataFile = file.readlines()



for index, line in enumerate(dataFile):

    print(line, end="")

    # find questions
    # string that ends with question mark.
    # ANSWER MUST BE THE FIRST OPTION
    if(line.find("?") > -1 and line.find("?") == len(line)-2):
        questionAndCurrectAnswer = (
            fn.getString(line), fn.getString(dataFile[index+1]))
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
            options.append(fn.getString(option))
            nextIndex += 1
           
        # end scanning options of question that found
        DataFile.questionsAndOptions.append((fn.getString(line), options))


print("FOR DONE")
print("question and answer:")
print(DataFile.questionsAndAnswers)
print("all test:")
print(DataFile.questionsAndOptions)
