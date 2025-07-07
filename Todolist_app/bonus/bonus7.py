filenames = ["1.raw data", "1.reports", "1.presentations"]
filenames = [filename.replace('.','-') + ".txt" for filename in filenames] #Concatenation #List Comprehension
print(filenames)
#["1-raw data.txt", "1-reports.txt", "1-presentations.txt"