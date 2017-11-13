print ('WELCOME TO THE KON BANEGA KAROR PATI SEASION 2017\n')
name = raw_input('WHAT IS YOUR NAME? ')
print ('\nHI THERE ' + name + '! LET''S PLAY KBC Season 2017!\n')
print ('I will ask you a  questions and give you four choices for each question.\n\nYou select which choice is the correct answer. Eg. 1, 2 , 3 or 4\n')
question = ['In which year of First World War Germany declared war on Russia and France?','ICAO stands for','indian has largest deposite of in the world.','how many lock sabha seat belongs to rajasthan?','who is the finace minister of india',' who is the speakr of loksabha', 'world yoga day is celebrated on','name the national flowerof india','who is the founder of facebook','name the national game of india','who won the 2011 icc cricket worlcup' ]

option_first = [' .1914','International Civil Aviation Organization','gold','32','rajnath singh',' partibha patil','25 december','lily','henery work','kabbadi','india']

option_second = ['.1915','Indian Corporation of Agriculture Organization','copper','25','m s nathan',' ismiriti irani',' 12 august','lotus', 'zone henery','hockey','australiya']

option_third = ['.1916','Indian Corporation of Agriculture Organization','mica','30',' ram vihari',' meera kumari','21 june','chameli','mark zekrberd',' hand ball','west indies']

option_fourth = ['1917',' none of the above','none of the above','17','atal vihari ji','sumitra mahajan',' 30 september','merigold',' none of the above',' football',' sri lanka']
correct_answer = [1,1,3,2,1,4,3,2,3, 2,1]
prizes = ['20000', '40000','80000','160000','320000','640000','1250000','2500000','5000000','10000000']

list_length = len(question)
index = 0
while index < list_length:
    print question[index]
    print '1.' +  option_first[index]
    print '2.' + option_second[index]
    print '3.' + option_third[index]
    print '4.' + option_fourth[index]
    user_input = int(raw_input("apna jabab btaiye"))
    if user_input == correct_answer[index]:
        print " congrats! aapka jabab sahi hai aapko diye jate h Rs " + str(prizes[index])

    else:
        print " sadly aapka jabab glat hai."
        
    if index== 3:
        print " aapka pehla padao khatm hota h"
    if index==6:
        print " aapka doosra padao khatm hota h"
    if index==9:
        print " aapka teesra padao khatm hota h "
    index = index+1
    if user_input != correct_answer[index]:
        print " aap kbc har chuke h aapko diye jate h Rs" + str(prizes[index])

        break
    

