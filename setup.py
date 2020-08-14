from setuptools import setup

setup(
    name="py-ec2-aws",
    version="0.1",
    author="A Campbell",
    description="A program to manage instances, snapshots, volumes",
    packages=['shotty'],
    url="https://github.com/alancam73/py-ec2-aws",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points={
        "console_scripts": [
            "ec2_aws=shotty.ec2_aws:cli"
        ]
    }
    
)