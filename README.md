Parameter Manager
================

Automates the process of creating, modifying, and deleting Parameter Store parameters.

Opinions
-----------

- Parameters names are pathed by Environment and Application. e.g. "/test/myapp"
- KMS keys exist for each referenced Environment and Appliction, and are tagged as such. e.g. "Environment": "test", "Application": "myapp"
- One KMS key will be used to encrypt values for a particular path. 
