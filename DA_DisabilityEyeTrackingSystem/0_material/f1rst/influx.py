import struct
import os
import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

 
token = 'KM_EpPlR-r6klw-0PUWmtiw3viJlLtLh5lLTdkghxxPdA91onSh6Ewvo986oxDeSUQT2ZDP-F_aIJc-nqJaXtQ=='
org = "HTL Hollabrunn"
url = "http://projects-et.htl-hl.ac.at:8086"
 
bucket = 'Test5AHET'

def writeInflux(value):
	write_client = InfluxDBClient(url=url, token=token, org=org)
	write_api = write_client.write_api(write_options=SYNCHRONOUS)
 
	point = [
		Point("5AHET").tag("name", "Machal").field("Groesse", value),
        ]
	write_api.write(bucket=bucket, org="HTL Hollabrunn", record=point)
 
def main():
    #print("hello")
    writeInflux(1.82)

 
if __name__ == '__main__':
	main()