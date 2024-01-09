# Script Name:                  Ops Lab 01: Powershell Screen Lock Automation
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/08/2024      
# Purpose:                      This PowerShell script is to automatically set up a screen lock on Windows 10 after a period of time.
# Resources:                    https://chat.openai.com/share/4bdb74cd-6d5d-4624-8b96-3fba3fd7e257

# This sets the time of inactivity in seconds before the screen locks 300 sec = 5 minutes.
$InactivityLimit = 300 

# The registry path where the screen lock settings are stored.
$registryPath = "HKCU:\SOFTWARE\Policies\Microsoft\Windows\Control Panel\Desktop"
$propertyName = "ScreenSaveTimeOut" # Name of the property to be set.
$propertyValue = $InactivityLimit # Value of the property (time limit).

# Starts a 'Try' block to handle potential errors.
Try {

# Checks if the registry path exists, if it does not, the script creates it.
If (!(Test-Path $registryPath)) {
    New-Item -Path $registryPath -Force | Out-Null
}

# Sets the screen save timeout value in the registry.
Set-ItemProperty -Path $registryPath -Name $propertyName -Value $propertyValue 

# Activates the screen saver feature.
Set-ItemProperty -Path $registryPath -Name "ScreenSaveActive" -Value "1"

# Prints a message confirming successful registry update.
Write-Host "Registry updated successfully."

# Initiates a Catch clock for handling exceptions.
} Catch {
    Write-Host "Error: $_"
}
#Prints any error encountered during the execution of the Try block.