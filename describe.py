#All information
'''import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
print(Myec2)

#Instances information
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
 print(pythonins)

#Instance ID
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
  for printout in pythonins['Instances']:
     print(printout['InstanceId'])
	 
#Instance ID,Instance Type	 
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
  for printout in pythonins['Instances']:
     print(printout['InstanceId'])
     print(printout['InstanceType'])

#Instance ID,Instance Type,Instance State
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
  for printout in pythonins['Instances']:
     print(printout['InstanceId'])
     print(printout['InstanceType']) 
     print(printout['State']['Name'])'''

#Instance ID,Instance Type,Instance State,Instance Name
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
  for printout in pythonins['Instances']:
   for printname in printout['Tags']:
     print(printout['InstanceId'])
     print(printout['InstanceType']) 
     print(printout['State']['Name'])
     print(printname['Value'])









        
