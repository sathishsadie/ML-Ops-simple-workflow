#!/bin/bash

# Set project directory
projectDir="C:/Users/Sathish G/ML-Ops-simple-workflow"



# Change to the project directory
cd "$projectDir" || { echo "Failed to change directory to $projectDir"; exit 1; }

# Pull the latest changes from the repository
echo "Pulling the latest changes..."
git pull origin main

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run ingestion, transformation, and training scripts
echo "Running ingestion script..."
python3 src/ingestin.py

echo "Running transformation script..."
python3 src/transformation.py

echo "Running training script..."
python3 src/training.py

# Restart the application service (if needed)
# Example: Restart a Linux service
# echo "Restarting application service..."
# sudo systemctl restart your-app-service

echo "Deployment completed successfully!"
