# OpenEnv Customer Support Environment

## Overview
This environment simulates real-world customer support workflows where AI agents classify, respond, and resolve user issues.

## Tasks
- Easy: classification
- Medium: response generation
- Hard: multi-step resolution

## Action Space
- classify
- respond
- escalate
- request_info

## Observation Space
- ticket
- conversation_history
- status

## Setup
pip install -r requirements.txt  
uvicorn server:app  

## Docker
docker build -t support-env .  
docker run -p 7860:7860 support-env  

## Inference
python inference.py  