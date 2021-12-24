import tarantool
import pandas as pd
from clickhouse_driver import Client

connection = tarantool.connect("localhost", 3301, user='admin', password='pass')

tarantoolDB = connection.space('userlog')
client = Client(host='localhost')
client.execute('SHOW DATABASES')

data = tarantoolDB.select()

#client.execute('INSERT INTO testdb.tarantool_table(Day, TickTime, Speed) VALUES',
#        [{
    #    'Day': data[0][0],
   #     'TickTime': data[0][1],
     #   'Speed': data[0][2]
    #}])

for count, row in enumerate(data):
    client.execute('INSERT INTO testdb.tarantool_table(Day, TickTime, Speed) VALUES',
        [{
        'Day': data[count][0],
        'TickTime': data[count][1],
        'Speed': data[count][2]
    }])
