# Script Name:                  Ops Lab 04: Systems Hardening with CIS Standards
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/12/2024      
# Purpose:                      This PowerShell script automates the configuration of the required settings in Windows Server 2019.
# Configure                     Automates CIS Benchmarks 1.1.5(L1) and 18.4.3(L1)
# Resources:                    https://chat.openai.com/share/c3e3e275-f601-47a9-a511-98e701fcaeba

# Configure 'Password must meet complexity requirements' (Benchmark 1.1.5 L1)
secedit /export /cfg "C:\SecConfig.cfg"
(Get-Content -path "C:\SecConfig.cfg").Replace("PasswordComplexity=0", "PasswordComplexity=1") | Set-Content -Path "C:\SecConfig.cfg"
secedit /configure /db "C:\Windows\security\local.sdb" /cfg "C:\SecConfig.cfg" /areas SECURITYPOLICY

# Configure 'Configure SMB v1 server' (Benchmark 18.4.3 L1)
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force

#Cleanup
Remove-Item -Path "C:\SecConfig.cfg"

# Output result
Write-Host "CIS Benchmark configurations for 1.1.5(L1) and 18.4.3(L1) applied."