@echo off
title Jenkins Server
echo ========================================================
echo Starting Jenkins with OpenJDK 21 on http://localhost:8080
echo Keep this window open while using Jenkins.
echo ========================================================
"C:\Users\777em\jdk-21\bin\java.exe" -jar "C:\Users\777em\Downloads\jenkins.war" --httpPort=8080
pause
