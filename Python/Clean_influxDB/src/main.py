### Import the influxdbClient from the influxdb library
from influxdb import InfluxDBClient

### Define the DataBase name
db_name = "edge_data"

### instantiate the InfluxClient, passing the address, port, user, password and the DataBase name
client = InfluxDBClient('localhost', 8086, 'root', 'root', db_name)

### Drop / Delete the DataBase specified at the variable 'db_name'
client.drop_database(db_name)
