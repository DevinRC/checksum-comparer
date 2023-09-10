@echo off
setlocal enabledelayedexpansion

set file1=%TEMP%\file1Path.txt
set "file2=%~1"

echo [Log] Checking if !file1! exists...
if exist "!file1!" (
    echo [Log] File 1 exists
    set /p file1=<"!file1!"
) else (
    echo [Log] File 1 does not exist
    set file1=None
)

echo [Log] File 1: !file1!
echo [Log] File 2: !file2!

echo Select an algorithm:
echo 1. MD2
echo 2. MD4
echo 3. MD5
echo 4. SHA1
echo 5. SHA256
echo 6. SHA384
echo 7. SHA512
choice /c 1234567 /n /m "Please select an option:"
set algorithm=
if %ERRORLEVEL%==1 set algorithm=MD2
if %ERRORLEVEL%==2 set algorithm=MD4
if %ERRORLEVEL%==3 set algorithm=MD5
if %ERRORLEVEL%==4 set algorithm=SHA1
if %ERRORLEVEL%==5 set algorithm=SHA256
if %ERRORLEVEL%==6 set algorithm=SHA384
if %ERRORLEVEL%==7 set algorithm=SHA512
echo You selected !algorithm!.

echo [info] Running checksum.py...
python "%~dp0checksum.py" "!file1!" "!file2!" "!algorithm!"

echo [info] Deleting %TEMP%\file1Path.txt...
del %TEMP%\file1Path.txt

endlocal
@pause
