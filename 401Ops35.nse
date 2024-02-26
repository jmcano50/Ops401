-- SimpleInfo.nse
-- Script Name:                  Ops Challenge: LUA-language script that gathers simple information about the target.
-- Author:                       Juan Miguel Cano 
-- Date of latest revision:      02/23/2024
-- Resource:                     Nmap Scripting Engine Documentation
-- Purpose:                      This script is designed to gather basic information about the target host, including its hostname, and uptime.

description = [[
Simple Information Gathering Script
]]

author = "Juan Miguel Cano"

categories = {"discovery", "safe"}

-- This function is called for each host scanned
portrule = function(host, port)
  return true
end

-- This function is called for each host that matches the portrule
action = function(host, port)
  -- Gather basic information
  local hostname = nmap.get_hostname()
  local uptime = nmap.get_uptime()
  
  -- Print the gathered information
  return string.format("Host: %s\nUptime: %s", hostname, uptime)
end
