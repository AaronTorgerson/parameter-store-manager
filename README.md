AWS SSM Parameter Manager
=========================
Automates the process of creating, modifying, and deleting Parameter Store parameters.


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


Constraints
-----------

- Parameters names are pathed by Environment and Application. e.g. "/test/myapp"
- KMS keys exist for each referenced Environment and Appliction, and are tagged as such. e.g. "Environment": "test", "Application": "myapp"
- One KMS key will be used to encrypt values for a particular path. 


