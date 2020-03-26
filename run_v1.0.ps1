$userlist = @( #"abusereyaahmed.funlabs.com",
#"alexandrudinulescu.funlabs.com"
#"alexandruhotescu.funlabs.com",
#"alexandrustan.funlabs.com",
#"alexandruzaharia.funlabs.com",
#"alexdutu.funlabs.com",
#"alexlungeanu.funlabs.com"
#"andreiserpescu.funlabs.com" 
#"andreizoltan.funlabs.com"
#"biancabratu.funlabs.com"
#"bogdanmangri.funlabs.com",
#"calinbutoi.funlabs.com"
#"catalinbucur.funlabs.com",
#"ciprianstanciu.funlabs.com",
#"costindumitru.funlabs.com",
#"cristiangherman.funlabs.com",
#"cristianpredo.funlabs.com",
#"cristipaun.funlabs.com"
#"danschiopu.funlabs.com",
#"danielverban.funlabs.com"
#"dianadrumea.funlabs.com"
#"dianamarinache.funlabs.com"
#"dorinzicu.funlabs.com",
#"dragosababei.funlabs.com",
#"enedaniel.funlabs.com",
#"fabiofilip.funlabs.com"
#"gabrielvisan.funlabs.com",
#"georgemihalascu.funlabs.com",
#"ileanagh1.funlabs.com",
#"ileanagh2.funlabs.com",
#"ioanadumitriu.funlabs.com",
#"ionutcioara.funlabs.com"
#"laurentiumarin.funlabs.com",
#"liviuion.funlabs.com",
#"lucaminca.funlabs.com"
#"mariansandru.funlabs.com",
#"mariuspetre.funlabs.com",
#"mariusrachiteanu.funlabs.com",
#"mihaelaionda.funlabs.com",
#"mihaelanichifor.funlabs.com",
#"mihaiiordache.funlabs.com",
#"mihaipreda.funlabs.com",
#"mihaivlada.funlabs.com",
#"mirceaiancu.funlabs.com"
#"mujdabasegel.funlabs.com",
#"petrutilie.funlabs.com"
#"radustanut.funlabs.com",
#"razvanmatache.funlabs.com",
#"razvanserban.funlabs.com",
#"roberttataru.funlabs.com"
#"sergiugrigoras.funlabs.com"
#"silviuiliescu.funlabs.com"
#"stefantataru.funlabs.com"
#"tomaherciu.funlabs.com"
#"tudornimara.funlabs.com"
#"vladcirstoiu.funlabs.com",
    )

# Get_info

foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user -filepath c:\xxx\script\get_info.ps1 | Select-String -Pattern "=","Link-local","Secure Boot","Automatic","Adapter","Tunnel","Media","Configuration","Ethernet","Connection","Subnet","Default","Attempting","BitLocker","Copyright","Protectors","TPM:","PCR","0," -NotMatch | Out-File "c:\xxx\usr_file\info.txt" -Append -Verbose
	}

# Remote_encrypt

<#foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user -filepath c:\xxx\script\encrypt.ps1 | Select-String -Pattern "action","automatic","attempting","bitLocker","computer","copyright","data","encrypted","protectors","save","space","TPM:","PCR","0," -NotMatch | Out-File "c:\xxx\usr_file\key.txt" -Append -Verbose
	}#>

# Get_drive

foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user -filepath c:\xxx\script\get_drive.ps1 | Select-String -Pattern "Attempting" -NotMatch | Out-File c:\xxx\usr_file\drive.txt -Append -Verbose
	}

# Time_sync

foreach ($user in $userlist) {
	powershell -ExecutionPolicy bypass -command Invoke-Command -ComputerName $user -filepath c:\xxx\script\time_set.ps1 | Select-String -Pattern "Firewall","Attempting","powershell","c:","category","error" -NotMatch | Out-File "c:\xxx\usr_file\time.txt" -Append -Verbose
	}
