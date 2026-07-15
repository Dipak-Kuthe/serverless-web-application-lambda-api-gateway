#!/usr/bin/env bash
set -euo pipefail

STACK_NAME="${1:-serverless-web-app-dev}"
REGION="${2:-ap-south-1}"

sam build
sam deploy \
  --stack-name "${STACK_NAME}" \
  --region "${REGION}" \
  --capabilities CAPABILITY_IAM \
  --guided
