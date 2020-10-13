import boto3
client = boto3.client('ec2',
         region_name = 'ap-south-1',
         aws_access_key_id = 'AKIAJASWTTYHG3RUNF4Q',
         aws_secret_access_key = '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')
myvpc = client.create_vpc(
        CidrBlock='192.168.0.0/16',
        InstanceTenancy='default',
        TagSpecifications=[{'ResourceType': 'vpc','Tags': [{'Key': 'Name','Value': 'Ktexperts-VPC'},]},])
print("My VPC ID :")
print(myvpc['Vpc']['VpcId'])   

mysubnet = client.create_subnet(
           CidrBlock='192.168.1.0/24',
	   VpcId=myvpc['Vpc']['VpcId'],
           AvailabilityZone='ap-south-1a',
           TagSpecifications=[{'ResourceType': 'subnet','Tags': [{'Key': 'Name','Value': 'MySubnet'},]},])
print("My Subnet ID :")
print(mysubnet['Subnet']['SubnetId'])

myroutetable=client.create_route_table(
             VpcId=myvpc['Vpc']['VpcId'],
	           TagSpecifications=[{'ResourceType': 'route-table','Tags': [{'Key': 'Name','Value': 'Ktexpers-RT'},]},])
print("My Route Table ID :")
print(myroutetable['RouteTable']['RouteTableId'])

myigw=client.create_internet_gateway(
      TagSpecifications=[{'ResourceType': 'internet-gateway', 'Tags': [{'Key': 'Name','Value': 'Ktexperts-IGW'},]},])
print("My Internet Gateway :")
print(myigw['InternetGateway']['InternetGatewayId'])

Mysubnetassociate=client.associate_route_table(
                  RouteTableId=myroutetable['RouteTable']['RouteTableId'],
                  SubnetId=mysubnet['Subnet']['SubnetId'])
print("Subnet Associated")

Myigwattach=client.attach_internet_gateway(
            InternetGatewayId=myigw['InternetGateway']['InternetGatewayId'],
            VpcId=myvpc['Vpc']['VpcId'])

Myrtentry = client.create_route(
            DestinationCidrBlock='0.0.0.0/0',
	    RouteTableId=myroutetable['RouteTable']['RouteTableId'],
            GatewayId=myigw['InternetGateway']['InternetGatewayId'])
print("Route entry entered")
