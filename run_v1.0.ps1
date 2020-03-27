$userlist = @("name1familyname.companyname.com",
              "name2familyname.companyname.com",
              "name3familyname.companyname.com",
              "name4familyname.companyname.com"
	      )

# Get_info

foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user `
	-filepath c:\xxx\script\get_info.ps1 | Select-String -Pattern "=","Link-local", `
	"Secure Boot","Automatic","Adapter","Tunnel","Media","Configuration","Ethernet", `
	"Connection","Subnet","Default","Attempting","BitLocker","Copyright","Protectors", `
	"TPM:","PCR","0," -NotMatch | Out-File "c:\xxx\usr_file\info.txt" -Append -Verbose
	}

# Remote_encrypt

<#foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user -filepath c:\xxx\script\encrypt.ps1 | Select-String -Pattern "action","automatic","attempting","bitLocker","computer","copyright","data","encrypted","protectors","save","space","TPM:","PCR","0," -NotMatch | Out-File "c:\xxx\usr_file\key.txt" -Append -Verbose
	}#>

# Get_drive

foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user `
	-filepath c:\xxx\script\get_drive.ps1 | Select-String -Pattern "Attempting" `
	-NotMatch | Out-File c:\xxx\usr_file\drive.txt -Append -Verbose
	}

# Time_sync

foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user `
	-filepath c:\xxx\script\time_set.ps1 | Select-String -Pattern "Firewall","Attempting", `
	"powershell","c:","category","error" -NotMatch | Out-File "c:\xxx\usr_file\time.txt" -Append -Verbose
	}
