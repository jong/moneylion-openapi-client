#!/usr/bin/env bash

SPEC_FILE="https://even-api-reference.s3.amazonaws.com/releases/branches/public@1.58.0/latest/open-api/public/spec.json"
curl -s -o spec.json ${SPEC_FILE}
openapi-generator generate -i spec.json -g python
