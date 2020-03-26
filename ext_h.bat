
@ECHO OFF
REM  QBFC Project Options Begin
REM  HasVersionInfo: yes > updated at 11.05.2019
REM  Companyname: 
REM  Productname: 
REM  Filedescription: 
REM  Copyrights: 
REM  Trademarks: 
REM  Originalname: 
REM  Comments: current script is compiled in dynamic/globally mode; for direct path switch comments in code;
REM  Productversion:
REM  Fileversion:  0.2
REM  Internalname: script
REM  Appicon: 
REM  AdministratorManifest: No
REM  QBFC Project Options End

@ECHO ON
@echo off
title Hide_file_extension
echo.
echo 	*** Input ***
echo.
SETLOCAL
:re
SET "request="
set /p request=Select 1(print) or 2(unprint): %=%
IF NOT DEFINED request GOTO :eof
  echo.%request%| findstr /R "[^1]" >nul 2>&1
  if ErrorLevel 1 (
    echo %request% - OK
    rem goto :switch-case-request-1
	attrib "G:\miscellaneous\Images\avatars\temp\*.*" -r -s -h
) else (
    echo.%request%| findstr /R "[^2]" >nul 2>&1
    IF NOT DEFINED request GOTO :eof
    if ErrorLevel 1 (
      echo %request% - OK
      rem goto :switch-case-request-2
	  attrib "G:\miscellaneous\Images\avatars\temp\*.*" +r +s +h
) else (
  echo.
  echo %request% - Invalid input. Please select just 1 or 2!
  echo.
  goto :re
	   )
)
exit
  :switch-case-request-1
  echo.
  echo You are in the print section.
  echo.
  goto :unprint
  :switch-case-request-2
  echo.
  echo You are in the unprint section.
  echo.
  goto :print
SETLOCAL
:unprint
set "ext="
  set /p ext=Type one, two or three alpha chars: %=%
IF NOT DEFINED ext GOTO :eof
  echo.%ext%| findstr /R "[^*^a-zA-Z]" >nul 2>&1
if ErrorLevel 1 (
  echo %ext% - OK
  rem attrib *.%ext% +r +s +h
  attrib "G:\miscellaneous\Images\avatars\temp\*.%ext%" +r +s +h
) else (
  echo.
  echo %ext% - Invalid input, insert just alpha chars.
  echo.
  goto :hide
)
exit
SETLOCAL
:print
set "ext="
  set /p ext=Type one, two or three alpha chars: %=%
IF NOT DEFINED ext GOTO :eof
  echo.%ext%| findstr /R "[^*^a-zA-Z]" >nul 2>&1
if ErrorLevel 1 (
  echo %ext% - OK
  rem attrib *.%ext% -r -s -h
  attrib "G:\miscellaneous\Images\avatars\temp\*.%ext%" -r -s -h
) else (
  echo.
  echo %ext% - Invalid input, type just alpha chars.
  echo.
  goto :unhide
)
exit


