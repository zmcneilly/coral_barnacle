#CharyPass - Password Generation Service
API generates random passwords. It uses the Serverless application framework.

## Usage
### Deploy
On changes to the `serverless.yml` file:
```bash
serverless deploy --stage [dev|prod] [-v]
```
On changes to the the `gen` function:
```bash
serverless deploy function --stage [dev|prod] [-v] -f gen
```
### Invoking Lambda
To simulate running lambda locally:
```bash
serverless invoke local -f gen -p invoke_event.json
```
To invoke the remote Lambda function:
```bash
serverless invoke -f gen -p invoke_event.json
```
## TODO
- CI/CD