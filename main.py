import data as DataFile
import functions as fn

myTest = fn.createDataTest("quiz.txt")

print(fn.shuffleTest(DataFile.questionsAndOptions))
