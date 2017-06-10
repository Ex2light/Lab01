import os
import fnmatch
class LogParser:
	def parser(self,toSearch):
		if os.path.isfile("./parsing.txt"):
			os.unlink("./parsing.txt")
		results = open('parsing.txt','a')
		results.write(toSearch + "\n")
		listOfFileNames =  [x for x in os.listdir('.') if  fnmatch.fnmatch(x,'*.log')]
		for filename in listOfFileNames:
			file = open(filename,'r')
			self.counter = 0
			results.write("In File " + filename + " parsed string found\n" )
			for line in file:
				self.counter = self.counter + 1
				if toSearch in line:
					results.write("in line " + str(self.counter) + '\n')
			file.close()
		results.close()
		return None

log_parser = LogParser()
log_parser.parser("PrChecker.Downs")


