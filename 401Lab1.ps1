# Script Name:                  Ops Lab 01: Powershell Screen Lock Automation
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/08/2024      
# Purpose:                      This PowerShell script is to automatically set up a screen lock on Windows 10 after a period of time.
# Resources:                    https://chat.openai.com/share/4bdb74cd-6d5d-4624-8b96-3fba3fd7e257

# This sets the time of inactivity in seconds before the screen locks 300 sec = 5 minutes.
$InactivityLimit = 300 

# The registry path where the screen lock settings are stored.
$regitstryPath = "HKCU:\SOFTWARE\Policies\Microsoft\Windows\Control Panel\Desktop"
$propertyName = "ScreenSaveTimeOut" # Name of the property to be set.
$propertyValue = $InactivityLimit # Value of the property (time limit).

# Checks if the registry path exists, if it does not, the script creates it.
If (!(Test-Path $registryPath)) {
    New-Item -Path $registryPath -Force | Out-Null
}

# Enables the screensaver, which is needed for the screen lock to activate after the specific time above.
Set-ItemProperty -Path $registryPath -Name "ScreenSaveActive" -Value "1" 

