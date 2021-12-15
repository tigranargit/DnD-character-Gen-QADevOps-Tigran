# DnD-Character-Gen

This is a simple microservice application built using flask.

Application is designed so that users can enter the frontend service on port 5000 while leaving the other three services only accessible through the frontend.

## Requirements

| Service Name | Port |
| ------------ | ---- |
| frontend | 5000 |
| service1 | 5001 |
| service2 | 5002 |
| backend | 5003 |

'frontend' service needs environment variables named:

- MYSQL_USER
- MYSQL_PWD
- MYSQL_IP - endpoint of mysql database
- MYSQL_DB - schema name
- MYSQL_SK - random string of letters and numbers (genuinely doesn't matter)

Also need a mysql database with a blank schema initialised (flask app will create tables and dummy data)

Test
Test test