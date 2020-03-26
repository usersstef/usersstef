
echo " "
$env:computername
echo " "
Get-Date -Format g #get_current_time
cmd /c net time \\server1 /set /y
echo *********************************************************
