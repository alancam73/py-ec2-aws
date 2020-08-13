import sys
import boto3
import os
import click

#If .aws credentials file is in non standard location (~/.aws/credentials) uncomment and provide path
# os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '/home/ec2-user/environment/acg_py_code/.aws/credentials' 

session = boto3.Session()
ec2 = session.resource('ec2')


def filter_instances(project):
    instances = []
    
    if project:
        print(project)
        filters = [{'Name': 'tag:Name', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
        
    return instances
    

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')    
@click.option('--project', default=None, help="Only instances for project tag Name ")
def list_instances(project):
    "List EC2 instances"
    
    instances = filter_instances(project)
    
    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print (', '.join((i.id, i.instance_type, i.placement['AvailabilityZone'], i.state['Name'], i.public_dns_name, str(i.public_ip_address), tags.get('Name', '<no nametag>'))))


@instances.command('stop')
@click.option('--project', default=None, help="Only instances for project tag Name ")
def stop_instances(project):
    "Stop EC2 instances"
    
    instances = filter_instances(project)
    
    for i in instances:
        print ("Stopping...{0}".format(i.id))
        i.stop()
        
    return


@instances.command('start')
@click.option('--project', default=None, help="Only instances for project tag Name ")
def start_instances(project):
    "Start EC2 instances"
    
    instances = filter_instances(project)
    
    for i in instances:
        print ("Starting...{0}".format(i.id))
        i.start()
        
    return



#session = boto3.Session(profile_name='shotty')
if __name__ == '__main__':
    instances()

    
    