import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import  datetime

engine = create_engine('postgresql://postgres:user@localhost')
connection = engine.connect()

query = ''' 
SELECT id ,"DateRegister"
  FROM "Sources"
  ORDER BY id
'''



result = connection.execute(query)
df = pd.DataFrame(result.fetchall())
df.columns = result.keys()
date = []
id = list(df['id'])

for i in df['DateRegister']:
    i = pd.to_datetime(i)
    date.append(i.date())


count = 0
for i in date:
    query = ''' 
    UPDATE "Sources" 
    SET "DateRegister1" = '{}'
    WHERE id = {}
    '''.format(i, id[count])
    connection.execute(query)
    count +=1
