#!/bin/env python

import boto3
import csv
import sys

ssm = boto3.client('ssm')
params_file_name = sys.argv[1]
app_name = sys.argv[2]
env_name = sys.argv[3]
kms_key_arn = sys.argv[4]

with open(params_file_name) as param_file:
    rdr = csv.DictReader(param_file, fieldnames=['mode', 'name', 'value'])
    for row in rdr:
        if row['mode'] == 'E':
            kwargs = {
                'Type': 'SecureString',
                'KeyId': kms_key_arn
            }
        else:
            kwargs = {
                'Type': 'String',
            }

        name = '/{}/{}/{}'.format(env_name.lower(), app_name.lower(), row['name'])
        resp = ssm.put_parameter(
            Name=name,
            Value=row['value'],
            Overwrite=True,
            **kwargs
        )
        ssm.add_tags_to_resource(
            ResourceType='Parameter',
            ResourceId=name,
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': env_name
                },
                {
                    'Key': 'Application',
                    'Value': app_name
                }
            ]
        )
