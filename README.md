# Serverless Web Application using AWS Lambda and API Gateway

This project contains a simple serverless API built with AWS Lambda, API Gateway, IAM, and CloudWatch. It is designed as a clean starting point for a portfolio-ready serverless web application.

## Skills Covered

- AWS Lambda
- Amazon API Gateway
- IAM execution roles
- CloudWatch logs
- Serverless architecture
- AWS SAM deployment

## Architecture

```text
Client -> API Gateway HTTP API -> Lambda function -> CloudWatch Logs
```

## Project Structure

```text
src/                  Lambda function code
events/               Local test events
scripts/              Deployment helper
template.yaml         AWS SAM template
```

## Local Test

```bash
sam build
sam local invoke HelloFunction -e events/sample-event.json
```

## Deploy

```bash
scripts/deploy.sh serverless-web-app-dev ap-south-1
```

## Cleanup

```bash
sam delete --stack-name serverless-web-app-dev
```
