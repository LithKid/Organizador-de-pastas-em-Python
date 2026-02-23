# Limpa a tela do console
Clear-Host

# Lista os comandos do módulo PSScheduledJob ordenados por substantivo
Get-Command -Module PSScheduledjob | Sort-Object Noun

# Cria um gatilho de job diário às 14:00
$diario = New-JobTrigger -daily -at 2pm

# Cria um gatilho de job que executa uma vez, daqui a 1 hora
$umavez = New-JobTrigger -Once -at (Get-Date).AddHours(1)

# Cria um gatilho de job semanal às segundas-feiras às 18:00
$semanal = New-JobTrigger -weekly -daysOfWeek Monday -at 6pm

# Registra um job agendado chamado 'backup' com gatilho diário, executando um bloco de script
Register-ScheduledJob -Name backup -Trigger $diario -ScriptBlock {
    # Copia o diretório C:\Daniel recursivamente para o arquivo .\AFERJ-VPNX.ovpn
    Copy-Item C:\Daniel -Recurse -Force .\AFERJ-VPNX.ovpn
}

# Lista os jobs agendados
Get-ScheduledJob