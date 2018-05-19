#!/bin/env python

import boto3
import sys

ssm = boto3.client('ssm')
path = sys.argv[1]

next_token = None
param_names = []
while True:
    kwargs = {'NextToken': next_token} if next_token is not None else {}
    params_resp = ssm.get_parameters_by_path(Path=path, **kwargs)

    for p in params_resp['Parameters']:
        param_names.append(p['Name'])

    next_token = params_resp.get('NextToken')
    if next_token is None:
        break

for n in param_names:
    ssm.delete_parameter(Name=n)

