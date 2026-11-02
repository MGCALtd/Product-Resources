# Free local prerequisite discovery. No cloud calls or system changes.
$PSVersionTable.PSVersion.ToString()
foreach ($supportCommand in @('python','python3','py')) { $located=Get-Command $supportCommand -ErrorAction SilentlyContinue; if ($located) { Write-Output ($supportCommand+': '+$located.Source) } }
Write-Output 'Run your selected Python command with --version; the free Python helpers require Python 3.10 or later.'
