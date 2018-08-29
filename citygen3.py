# first we need to import the packages that we will be using
#we use random for the random generators and picking from lists
import random

numberofCities = int(input('How many cities? '))
numberofRegions = int(input('How many regions? '))

##This is some optional code that is used to generate the same random city each time
#random.seed(input('Pick a seed: '))
	
##------------IMPORTING------------##
#this is where it asks you what the name of the language is
langName = input('What is the name of your language?' )
if langName=='':
	langName='Koae'

#here we define a function to process the file
def readsplit(theFile):
	return theFile.read().splitlines()

def processline(line):
	rawLine = bigList[line]
	splitList = rawLine.split(', ')
	return splitList

#This is where we create the output file

outputFile = open('Cities.txt', 'w')

#This is where we access the language files
langFile = open('{}\{}.txt'.format(langName,langName), 'r', encoding='utf-8')
nameList = readsplit(langFile)
langFileNumLines = sum(1 for item in nameList)

langFileTrans = open('{}\{}_eng.txt'.format(langName,langName), 'r', encoding='utf-8')
translationList = readsplit(langFileTrans)
langFileTransNumLines = sum(1 for line in langFileTrans)

#This is where it processes the big file
bigFile = open('{}\{}_settings.txt'.format(langName,langName), 'r', encoding='utf-8')
bigList = readsplit(bigFile)
bigListNumLines = sum(1 for line in bigFile)


townList = processline(0)
directions = processline(1)
riverTypes = processline(2)
lakeTypes = processline(3)
landformTypes = processline	(4)
specialTypes = processline(5)
treeTypes = processline(6)
groveTypes = processline(7)
rockTypes = processline(8)
oreTypes = processline(9)
peopleNames = processline(10)
jobTypes = processline(11)
events = processline(12)
headofStateName = processline(13)
parliamentName = processline(14)
headofStateIdentity = processline(15)
electors = processline(16)



#def personwithjobmaker():
#	person = random.choice(peopleNames) + ' the' + random.choice(jobTypes)
#	return person

regionListInitial =[]
for i in range(0,numberofRegions):
	regionName = random.choice(nameList)
	regionListInitial.append(regionName.capitalize())

regionListFinal = regionListInitial
#for i in range(0,numberofCities):
#	regionListFinal.append(random.choice(regionListInitial))

regionsString = ', '.join(regionListInitial)
print(regionsString, file=outputFile)



for i in range(0,numberofCities):

	##------------NAME------------##
	cityNameList = []
	cityNameTranslationList =[]
	#now it gets either 1 or two words and adds them to the list
	cityNameLength = random.randint(1,2)
	for i in range(0,cityNameLength):
		namePartNumber = random.randint(0,int(langFileNumLines - 1))
		cityNameList.append(nameList[namePartNumber])
		cityNameTranslationList.append(translationList[namePartNumber])
	
	#now it chooses whether or not to add any town or village indicating suffixes to the end. 
	#It is twice as likely to select one if the name is only one word long
	if random.randint(1,3)/cityNameLength > 1:
		cityNameList.append(random.choice(townList))
	
	
	#now it joins the list into a string and capitalizes it. this is the city's name
	cityName = ''.join(cityNameList).capitalize()
	#now it joins the translation list into a string. this is the rough translation of the name.
	cityNameTranslation = ','.join(cityNameTranslationList)




	##------------REGION------------##
	cityRegion = random.choice(regionListFinal)
	regionListFinal.append(cityRegion)



	
	##------------POPULATION------------##
	#This is where the population of the city is determined. Most of the time the city populatioln is going to be small.
	#The number we generate hear isn't printed because of the rounding required for the racial composition estimates.
	#The final cityPop may be 1 or 2 off from citySize.
	citySize = int((.005 * (random.random()*10) ** 6 + 140) + random.randint(-50,30))
	#This is some optional code that will give bigger cities
	if citySize >= 4900:
		citySize = citySize + random.randint(-4000,24000)
	
	#This is where the city population is decided. 
	#First we get random numbers for genral sizes of each of the three races.
	popHuman = random.randint(1,1000)
	popGothe = random.randint(1,1000)
	popKobold = random.randint(1,100)
	
	#Now we take these random numbers and make them percents.
	popTempTotal = popHuman + popGothe + popKobold
	#Now we redefine the populations as percents and then as totals
	popHuman = int(popHuman/popTempTotal * citySize)
	popGothe = int(popGothe/popTempTotal * citySize)
	popKobold = int(popKobold/popTempTotal * citySize)
	cityPop = popHuman + popGothe + popKobold
	
	
	
	##------------AGE------------##
	#Now we generate the citie's age
	cityAge = int(random.betavariate(2,5) * 2000)
	
	
	
	##------------GEOGRAPHY------------##
	
	def namer():
		global nameList	
		return random.choice(nameList).capitalize() + ' '
	
	def direction():
		global directions
		return ' to the {}.'.format(random.choice(directions))
	



	##--WATER--##
	#First we decide the water source near the city. 0=lake, 1=river, 2=none
	water = random.randint(1,4)
	waterSourceChance = water % 3
	if waterSourceChance==0:
			waterString = 'The city has no major surface water source.' + '\n'
	else:
		waterStringList = ['Notable surface water:', '\n']
		for i in range(0,water):
			waterRandom = random.randint(1,3)
			if waterRandom==1:
				waterSource = random.choice(nameList).capitalize() + ' ' + random.choice(lakeTypes) + ' ' + 'to the {}'.format(random.choice(directions)) + '\n'
			else:
				waterSource = random.choice(nameList).capitalize() + ' ' + random.choice(riverTypes) + ' ' + 'to the {}'.format(random.choice(directions)) + '\n'
			waterStringList.append(waterSource)
		waterString = ' '.join(waterStringList)
	



	##--LAND--##
	#Now we decide the land features near the city
	#this decides how many the city gets (between 2 and 6)
	featureStringList=['Notable landmarks:', '\n']
	for i in range(0,random.randint(2,6)):
		#Now it picks a feature and formats it correctly before adding it to the list
		featureType = random.choice(landformTypes)
		if featureType=='Special':
			feature = random.choice(specialTypes) + direction() + '\n'
		elif featureType=='Forest':
			treesList = []
			for i in range(0,random.randint(1,5)):
				treesList.append(random.choice(treeTypes) + ' trees')
			trees = ', '.join(treesList)
			feature = featureType + ' of ' + trees + direction() + '\n'
		elif featureType=='Grove':
			feature = featureType + ' of ' + random.choice(groveTypes) + direction() + '\n'
		elif featureType=='Bare Rock Face of' or featureType=='Patch of Gravelled' or featureType=='Erratic':
			feature = featureType + ' ' + random.choice(rockTypes) + direction() + '\n'
		elif featureType=='Vein':
			feature = random.choice(oreTypes) + ' ' + featureType + direction() + '\n'
		elif featureType=='Dried':
			feature = featureType + ' ' + random.choice(riverTypes) + '\n'
		else:
			feature	= namer() + featureType	+ direction() + '\n'
		featureStringList.append(feature)
	featureString = ' '.join(featureStringList)
	



	##------------NOTABLE PEOPLE------------##
	#First it generates some last names/families for people to be a part of
	lastNames = ['newLastName']
	lastNameStringList = ['Notable Families: ', '\n']

	for i in range(int(cityPop/10),int(cityPop/5)):
		lastNameRandom = random.choice(lastNames)
		lastNameType = random.randint(1,2)
		if lastNameRandom=='newLastName' and lastNameType==1:
			protoLastName = random.choice(nameList)
			lastNames.append(protoLastName)
			lastNameStringList.append(protoLastName.capitalize() + '\n')
		elif lastNameRandom=='newLastName' and lastNameType==2:
			protoLastName = random.choice(jobTypes)
			lastNames.append(protoLastName)
			lastNameStringList.append(protoLastName.capitalize() + '\n')
		else:
			lastNames.append(lastNameRandom)
	lastNames.remove('newLastName')
	lastNames.append(random.choice(nameList))
	lastNameString = ''.join(lastNameStringList)

	def personmaker():
		person = random.choice(peopleNames) + ' ' + random.choice(lastNames).capitalize()
		return person

	#Now it generates some people and gives them first and last names
	peopleList = ['Notable people:', '\n']
	for i in range(0,random.randint(3,12)):
		person = personmaker() + ' the ' + random.choice(jobTypes) + '\n'
		peopleList.append(person)

	peopleString = ' '.join(peopleList)






	##------------GOVERNMENT------------##
	governmentStringList = ['Local Government:', '\n']
	parliamentList = []
	headofState = random.choice(headofStateName)
	parliament = random.choice(parliamentName)
	parliamentSize = random.randint(3,24)
	if headofState=='None' and parliament=='None' and cityPop < 1000:
		government = 'The locals have not formalized a government yet.'
	elif headofState=='None' and parliament=='None' and cityPop >= 1000:
		fallenGov = ['The city has fallen into a state of anarchy',"The city's government has collapsed",'Small gangs and alliances are fighting for control.']
		government = random.choice(fallenGov)
	elif headofState=='None':
		for i in range(0,parliamentSize):
			parliamentMember = personmaker()
			parliamentList.append(parliamentMember)
		parliamentMembers = ', '.join(parliamentList)
		government = 'The city is headed by a ' + str(parliamentSize) + ' member ' + parliament + ' of ' + random.choice(electors) + ' chosen by a ' + random.choice(electors) + '.' + '\n' + 'Its members are ' + parliamentMembers + '.'
	elif parliament=='None':
		government = 'The city is ruled by ' + headofState + ' who is ' + random.choice(headofStateIdentity) + ' named ' + personmaker() + ' and is answerable no one.'
	else:
		for i in range(0,parliamentSize):
			parliamentMember = personmaker()
			parliamentList.append(parliamentMember)
		parliamentMembers = ', '.join(parliamentList)
		government = 'The city is ruled by ' + headofState + ' named ' + personmaker() + ' who is ' + random.choice(headofStateIdentity) + ' chosen by ' + random.choice(electors) + '.' + '\n' + 'There is also a ' + str(parliamentSize) + ' member ' + parliament + ' of ' + random.choice(electors) + ' chosen by ' + random.choice(electors) + '.' + '\n' + 'Its members are ' + parliamentMembers + '.'
	governmentStringList.append(government)
	governmentString = ''.join(governmentStringList)
	##------------HISTORY (DEFUNCT)------------##
	#This is where the program generates historical people
	#numberPeople = random.randint(2,10)
	#historyStringList = ['History:', '\n']
	#peopleList = ['newperson']
	#yearIteration = 0
	#for i in range(0,cityAge):
	#	yearIteration += 1
	#	yearsAgo = str(cityAge - yearIteration)
	#	if random.random() < .05:
	#		figure = random.choice(peopleList)
	#		if figure=='newperson':
	#			figure = random.choice(nameList).capitalize()
	#			peopleList.append(figure)
	#			event = yearsAgo + ' years ago ' + figure + ' ' + random.choice(events) + '\n'
	#		else:
	#			event = yearsAgo + ' years ago ' + figure + ' ' + random.choice(events) + '\n'
	#		historyStringList.append(event)
	#		historyString = ' '.join(historyStringList)
	
	
	
	##------------PRINT STATEMENT------------##
	print(cityName, ' in the ', cityRegion, ' region', '\n',
		'Roughly translates to: ', cityNameTranslation, '\n',
		cityAge, ' years old', '\n',
	
		'------------------', '\n' +
		'Population: ',cityPop, '\n' + 
		'Humans: ',popHuman," Gothe: ",popGothe," Kobold: ",popKobold, '\n' +
		
		'------------------', '\n',
		waterString,
	
		'------------------', '\n',
		featureString,
	
		'------------------', '\n',
		peopleString,

		'------------------', '\n',
		lastNameString,
	
		'------------------', '\n',
		governmentString,
		
		'\n',
		'\n',
		sep="", file=outputFile)