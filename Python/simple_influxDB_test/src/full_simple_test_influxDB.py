### Import influxDBClient from influxdb library
from influxdb import InfluxDBClient

### Define the data that will be loaded to InfluxDB
### More details for the json structure could be find here: 
### https://docs.influxdata.com/influxdb/v1.7/introduction/getting-started/

json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T22:00:00Z",
        "fields": {
            "value": 0.65
        }
    }
]

### Create the InfluxDB Client passing the db address, port, user, password and db_name
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')

#client.drop_database('example')

### Create the database named 'example'
client.create_database('example')

### Insert the data from 'json_body'
client.write_points(json_body)

### Get the result running the query indicated below
result = client.query('select value from cpu_load_short;')

### Print the result of the query
print("Result: {0}".format(result))