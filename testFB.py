from DBconnection import firebaseConnection, connection2
import pandas as pd
from pandas import DataFrame



'''firebase = firebaseConnection()

fb = firebase.database()

isFB_Connected = fb.child().get().val()


print(isFB_Connected)'''

cur, db, engine = connection2()

clientIDs = []

ID = 644345897

q= "SELECT * FROM bank_db.transaction"
cur.execute(q)
recored = cur.fetchall()
df = DataFrame(recored)
df.columns = cur.column_names


for each in recored:
    clientIDs.append(each[7])

print(clientIDs)

client_df = df[df['clientID']==ID].drop_duplicates(keep='first')

print(client_df)