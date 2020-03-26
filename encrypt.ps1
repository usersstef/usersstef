
$env:computername
$env:username

#cmd /c manage-bde -on D: -rp -rk "C:\" -s; manage-bde -autounlock -enable D:          # encrypt full space on hdd/ssd
#cmd /c manage-bde -on C: -used -rp -rk "C:\" -s; manage-bde -autounlock -enable C:    # encrypt used space on hdd/ssd
attrib -h -r -s "C:\*.BEK"; Start-Sleep -s 1; Remove-Item "C:\*.BEK"

#cmd /c manage-bde -protectors -add -pw C:; cmd /c manage-bde -on C: -rp -rk "C:\" -s; # encrypt with password

ls c:\; attrib -h -r -s C:\*.BEK; ls c:\
