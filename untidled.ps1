$wshell = New-Object -ComObject WScript.Shell

$wshell.Popup("Esse curso eh muito legal")

$wshell.Run("notepad")# Coloca o foco na janela do Notepad
$wshell.AppActivate("Notepad.exe")# Coloca o foco na janela do Notepad
Start-Sleep 1
$wshell.SendKeys("Curso de PowerShell - A melhor linguagem de script do mundo!")# Envia texto para o Notepad   