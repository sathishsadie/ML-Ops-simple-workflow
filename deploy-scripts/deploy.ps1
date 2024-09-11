# Set project directory
$projectDir = "C:\Users\Sathish G\ML-Ops-simple-workflow"

# Change to the project directory
Set-Location -Path $projectDir

# Pull the latest changes from the repository
Write-Output "Pulling the latest changes..."
git pull origin main

# Install dependencies
Write-Output "Installing dependencies..."
pip install -r requirements.txt

# Run ingestion, transformation, and training scripts
Write-Output "Running ingestion script..."
python src\ingestion.py

Write-Output "Running transformation script..."
python src\transformation.py

Write-Output "Running training script..."
python src\training.py

# Restart the application service (if needed)
# Example: Restart a Windows service
# Write-Output "Restarting application service..."
# Restart-Service -Name "YourAppService"

Write-Output "Deployment completed successfully!"
