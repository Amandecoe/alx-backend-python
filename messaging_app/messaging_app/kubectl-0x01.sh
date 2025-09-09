#!/bin/bash

# Scale the deployment to 3 replicas
echo "Scaling Django app deployment to 3 replicas..."
kubectl scale deployment messaging-app-deployment --replicas=3

# Wait a few seconds for pods to be created
echo "Waiting for pods to be ready..."
sleep 10

# Verify multiple pods are running
echo "Listing all pods..."
kubectl get pods -l app=messaging-app

# Perform load testing using wrk (make sure wrk is installed)
# Replace http://<service-ip>:<port> with your actual service URL inside cluster
SERVICE_IP=$(kubectl get svc messaging-app-service -o jsonpath='{.spec.clusterIP}')
SERVICE_PORT=$(kubectl get svc messaging-app-service -o jsonpath='{.spec.ports[0].port}')
URL="http://${SERVICE_IP}:${SERVICE_PORT}/"

echo "Performing load test using wrk on $URL..."
wrk -t2 -c10 -d10s "$URL"

# Monitor resource usage of pods
echo "Displaying pod resource usage..."
kubectl top pods -l app=messaging-app