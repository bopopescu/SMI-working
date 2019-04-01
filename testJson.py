from DBconnection import connection2, BankConnection, firebaseConnection
from datetime import datetime
import json
from pprint import pprint


'''profile_class = 'High'

#if profile_class in ('Medium', 'High'):
if (profile_class == 'Medium') or (profile_class == 'High'):
    print(profile_class)
else :
    print('Not found')

    # if (profile_class == 'Medium') or (profile_class == 'High'):
    # if profile_class in ('Medium', 'High'):'''

#cur1, db1, engine1 = connection2()#SMI_DB

'''cur1.execute("SELECT * FROM SMI_DB.Client")
    result = cur1.fetchall()

    for each in result:
        print(each[0])
        print(each[2])
        print('************')
        if each[2] == 'High':
            date_now = datetime.now()
            formatted_date = date_now.strftime('%Y-%m-%d %H:%M:%S')
            query = "INSERT INTO ClientCase (caseClassification, date, clientID) VALUES(%s,%s, %s)"
            val = (each[2], formatted_date, each[0])
            cur1.execute(query, val)'''

status, cur, db, engine = BankConnection()
cur.execute("SELECT * FROM Bank_DB.transaction LIMIT 1")



operands = ['==','not','or','in','and','<','>','<=','>=']


with open('Br_file/Br1.json') as f:
    data = json.load(f)

pprint(data)

if 'Rules' not in data:
    print('ERROR...your file is not well structured... please follow the file format in the sample')

firebase = firebaseConnection()
fb = firebase.database()



i=1
for each in data['Rules']:


   ### 1-check Key words structure #####
    if 'Rule{}'.format(i) not in data['Rules']:
        print('ERROR in your file structure in Rule{} please follow the format'.format(i))
        break
    else:
        print('Correct format')

    ### 2- check if all attriubtes in dataset ###

    if data['Rules']['Rule'+str(i)][0] not in cur.column_names:
        print('Rule{} attribute {} not found in the dataset'.format(i, data['Rules']['Rule{}'.format(i)][0]))
        break
    else:
        print('all attributes were found in dataset')

    ### 3- check if theres illegal operand ####

    if data['Rules']['Rule' + str(i)][1] not in operands:
        print('Illegal operand ({})in Rule{}'.format(data['Rules']['Rule{}'.format(i)][1], i))
        break
    else:
        print('all legal operand')

        #### 4- If there's rule for sanction, check if names are uploaded and get the names ####
    if data['Rules']['Rule' + str(i)][2] == 'sanctionList':
        print('Rule for sanction list')
        if ('sanctionList' not in data) :
            print('for Rule{} Please  upload the sanction list section to the file'.format(i))
        else:
            print('Sanction list is uploaded:')
            if len(data['sanctionList']) == 0 :
                print('Sanction List is empty please upload the names')
            print(data['sanctionList'])

    else :
        print('No Rule for sanction list ')

        #### 5- If there's rule for risk countries, check if countries are uploaded and get the countries ####
    if data['Rules']['Rule' + str(i)][2] == 'HighRiskCountries':
        print('Rule for Risk countries')
        if ('HighRiskCountries' not in data):
            print('for Rule{} Please  upload the HighRiskCountries list section to the file'.format(i))
        else:
            print('HighRiskCountries list is uploaded:')
            if len(data['HighRiskCountries']) == 0:
                print('HighRiskCountries is empty please upload the names')
            print(data['HighRiskCountries'])

    else:
        print('No Rule for HighRiskCountries ')

    print('*******************************')



    fb.child('Rules').child('Rule'+str(i)).set(data['Rules']['Rule'+str(i)])


    i= i+1

'''j=1
print('Number of rules',len(data['Rules']))
for each in data['Rules']:
    #print ('attrubite in file {}'.format(data[0][1]))
    if j> len(data['Rules']):
        break
    print('attrubite in file {}'.format(data['Rules']['Rule{}'.format(j)][0]))
    print ('Operand in dataset',data['Rules']['Rule{}'.format(j)][1])
    print('************')
    j = j + 1 '''


