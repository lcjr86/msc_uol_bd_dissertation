from influxdb import InfluxDBClient

db_name = "edge_data"

client = InfluxDBClient('localhost', 8086, 'root', 'root', db_name)

client.drop_database(db_name)
