#!/bin/bash
set -e

echo "Running remediation steps..."
docker pull ubuntu:22.04
docker pull python:3.12
docker pull nginx:stable

echo "Rebuilding secure image..."
docker build -t ghcr.io/my-org/remediation-image:secure .

