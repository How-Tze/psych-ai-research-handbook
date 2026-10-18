$ErrorActionPreference = 'Stop'
$expectedDirectory = [IO.Path]::GetFullPath((Join-Path $env:LOCALAPPDATA 'Programs/PsychAIAuthorWorkbench'))
if (!(Test-Path -LiteralPath $expectedDirectory)) { Write-Output '程序尚未安装。'; exit }
$directory = (Resolve-Path -LiteralPath $expectedDirectory).Path
$manifest = Get-Content -LiteralPath (Join-Path $directory 'installation.json') -Raw | ConvertFrom-Json
if ($directory -ne $expectedDirectory -or $manifest.directory -ne $directory) { throw '安装位置核验失败，未删除任何内容。' }
if ((Get-Item -LiteralPath $directory).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw '安装目录是链接，未删除。' }
$executable = Join-Path $directory 'AuthorWorkbench.exe'
& (Join-Path $directory 'AuthorWorkbenchCLI.exe') stop | Out-Null
if ($LASTEXITCODE -ne 0) { throw '服务未停止，请稍后重试。' }
Start-Sleep -Seconds 2
$registry = 'HKCU:\Software\Classes\psychauthor'
$expectedCommand = '"' + $executable + '" "%1"'
if (Test-Path -LiteralPath "$registry\shell\open\command") {
    if ((Get-Item -LiteralPath "$registry\shell\open\command").GetValue('') -eq $expectedCommand) {
        Remove-Item -LiteralPath $registry -Recurse
    }
}
$shortcutShell = New-Object -ComObject WScript.Shell
foreach ($folder in @([Environment]::GetFolderPath('Desktop'),[Environment]::GetFolderPath('Programs'))) {
    $path = Join-Path $folder '心理学 AI 手册·作者工作台.lnk'
    if (Test-Path -LiteralPath $path) {
        if ($shortcutShell.CreateShortcut($path).TargetPath -eq $executable) { Remove-Item -LiteralPath $path }
    }
}
# The resolved absolute path and installation ownership were checked above.
Remove-Item -LiteralPath $directory -Recurse
Write-Output '程序与快捷入口已移除。私人草稿、备份和项目源码全部保留。'
