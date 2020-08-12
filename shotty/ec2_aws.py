import sys
import boto3
import os
import click

#If .aws credentials file is in non standard location (~/.aws/credentials) uncomment and provide path
# os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '/home/ec2-user/environment/acg_py_code/.aws/credentials' 

session = boto3.Session()
ec2 = session.resource('ec2')

@click.command()

def list_instances():
    for i in ec2.instances.all():
        print (', '.join((i.id, i.instance_type, i.placement['AvailabilityZone'], i.state['Name'], i.public_dns_name, str(i.public_ip_address))))

#session = boto3.Session(profile_name='shotty')
if __name__ == '__main__':
    list_instances()

    
    