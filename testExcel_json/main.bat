@echo off 
echo 当前盘符和路径：%~dp0

start python  %~dp0/ExcelToJson.py 
REM exit 
pause