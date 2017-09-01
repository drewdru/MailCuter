# *.vcf to txt
#f = open('contacts.vcf', 'r')
#sEmailList = ''
#for line in f:
#	try:
#		email = line.split('EMAIL:')[1]
#		sEmailList += email + ',\n'
#	except:
#		pass
#f.close()
#
#print(sEmailList)
#
#f = open('emails.txt', 'w')
#f.write(sEmailList)
#f.close()
import re


#all mails to one file with out duplicate

filesName = ('ЕКАТЕРЕНБУРГ3.txt',)
res = []
for fName in filesName:
	f = open(fName, 'r')
	text = f.read()
	emails = text.split(',')
	for email in emails:	
		e = email.lower()
		if e not in res:
			res.append(e)
	f.close()

#write emails
f3 = open('ВСЕ ЕКАТЕРЕНБУРГ3.txt', 'w+')
counter = 0
for mail in res:
	f3.write(re.sub(r'\s', '', mail)+', ')
	if(counter==29):
		f3.write('\n')
		counter = 0
	else:
		counter += 1
f3.close


#delete emails from file
#f = open('ВСЕ.txt', 'r')
#text = f.read()
#emails = text.split(',')
#f.close()
#f2 = open('Адреса - ОБРОЗОВАНИЕ.txt', 'r')
#text = f2.read()
#deletemails = text.split(',')
#f2.close()
#res = [] 
#for email in emails:
#	e2 = email.lower()
#	e2 = re.sub(r'\s', '', e2)
#	res.append(e2)
#for deletemail in deletemails:	
#	#print('test')
#	e = deletemail.lower()
#	e = re.sub(r'\s', '', e)
#	for email in emails:		
#		e2 = email.lower()
#		e2 = re.sub(r'\s', '', e2)
#		if e == e2:
#			print('test')
#			try:
#				#print(e)
#				res.remove(e2)
#				#print('test')
#			except ValueError:
#				#print(ValueError)
#				pass
#f3 = open('ВСЕ без образования.txt', 'w+')
#counter = 0
#for mail in res:
#	f3.write(re.sub(r'\s', '', mail)+', ')
#	if(counter==29):
#		f3.write('\n')
#		counter = 0
#	else:
#		counter += 1
#f3.close

#res = []
#for item in src:
#  if item not in res:
#    res.append(item)
