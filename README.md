AWS SSM ParameterStore Manager
=========================
Automates the process of creating, modifying, and deleting Parameter Store parameters.

Example: `./param-manage edit test www`

Opens a YAML representation of your Parameter Store values in `vim` or the editor of your choice (`$EDITOR` environment variable). Changes to the file will be synced to AWS ParameterStore.

Constraints & Assumptions
-------------------------
- You are managing Parameters for one or more applications that have one or more environments (test, staging, live). These applications/environments have been granted proper permissions via IAM to access ParameterStore and the KMS keys used to encrypt secure ParameterStore values.
- Parameter names are pathed by Environment and Application. e.g. "/test/myapp/MY_SETTING"
- _One_ KMS Master Key exists for each Environment/Appliction combination (the same key can be used for multiple combinations). These keys are tagged as such. e.g. "Environment": "test", "Application": "myapp". 
- Your AWS User has permission to access these KMS keys as well as their Tags and to manage ParameterStore parameters.

Prerequisites:
--------------
- `pipenv` is [installed](https://docs.pipenv.org/)
- Your AWS keys are [properly configured](http://boto3.readthedocs.io/en/latest/guide/configuration.html) such that `boto3` can locate them.

Usage
-----
- Clone this repository
- `pipenv shell` to activate virtual env
- `./param-manage <environment_name> <application_name>` (Ex, `./param-manage test www`)
- Follow the instructions in the editor for modifying Parameters



