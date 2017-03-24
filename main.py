from allDayIndicators import allDayIndicators
from dateIteration import dateIteration, dateRange
from sortData import sortData
from removeDuplicates import removeDuplicates
from divideData import divideData

def main():
	try:
		while True:
			i = 5
			l = {
				1:dateIteration,
				2:sortData,
				3:removeDuplicates,
				4:divideData
				}
				
			print ('\n----------------------\n        MENU\n----------------------\n1.Add historical data\n2.Sort data\n3.Remove duplicates\n4.Apply split/Divident/etc\n5.Exit')
			try:
				i = int(raw_input('\nInput: '))
			except Exception, e:
				print 'Invalid input!!\n\n'
			if i == 5:
				break
			elif i < 6 and i > 0 :
				l[i]()

	except Exception, e:
		print 'Exception :', str(e)
	
main()
	
	