import logging
logger = logging.getLogger('log')
handler = logging.FileHandler('log.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


fileName = input("Enter the file name ")
file = open(fileName, 'r')
wordCount = 0
lineCounter = 0
n = 1
for line in file:
	lineCounter = lineCounter + 1
	for x in line.split(' '):
		wordCount = wordCount + 1
		if wordCount == n*100:
			n = n + 1
			logger.info(' File: %s Line: %d Word Count: %d', fileName, lineCounter, wordCount)
file.close()