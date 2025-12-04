#!/bin/bash
set -e

echo "Building normal image..."
docker build -t ghcr.io/my-org/remediation-image:latest .

echo "Pushing image..."
docker push ghcr.io/my-org/remediation-image:latest

