param(
    [string]$Package = (Join-Path $PSScriptRoot 'dist/PsychAIAuthorWorkbench'),
    [string]$Handbook = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path,
    [string]$Guide = (Join-Path (Split-Path $Handbook -Parent) 'psych-ai-start-guide')
)
$ErrorActionPreference = 'Stop'
$Package = (Resolve-Path -LiteralPath $Package).Path
$Handbook = (Resolve-Path -LiteralPath $Handbook).Path
$Guide = (Resolve-Path -LiteralPath $Guide).Path
$destination = Join-Path $env:LOCALAPPDATA 'Programs/PsychAIAuthorWorkbench'
$privateDirectory = Join-Path $env:LOCALAPPDATA 'PsychAI/AuthorWorkbench'
$registry = 'HKCU:\Software\Classes\psychauthor'
$executable = Join-Path $destination 'AuthorWorkbench.exe'
$expectedCommand = '"' + $executable + '" "%1"'
if (!(Test-Path -LiteralPath (Join-Path $Package 'AuthorWorkbench.exe'))) { throw '请先构建安装包。' }
foreach ($root in @($Handbook, $Guide)) {
    if (!(Test-Path -LiteralPath (Join-Path $root '_quarto.yml'))) { throw '项目目录不完整。' }
}
if (Test-Path -LiteralPath "$registry\shell\open\command") {
    $existing = (Get-Item -LiteralPath "$registry\shell\open\command").GetValue('')
    if ($existing -ne $expectedCommand) { throw 'psychauthor 协议已由其他程序使用，未覆盖。' }
}
if ((Test-Path -LiteralPath $destination) -and !(Test-Path -LiteralPath (Join-Path $destination 'installation.json'))) {
    throw '安装目录已有其他内容，未覆盖。'
}
if (Test-Path -LiteralPath (Join-Path $destination 'AuthorWorkbenchCLI.exe')) {
    & (Join-Path $destination 'AuthorWorkbenchCLI.exe') stop | Out-Null
    if ($LASTEXITCODE -ne 0) { throw '旧工作台未正常停止，请关闭后重试安装。' }
    Start-Sleep -Seconds 2
}
New-Item -ItemType Directory -Path $destination -Force | Out-Null
New-Item -ItemType Directory -Path $privateDirectory -Force | Out-Null
Copy-Item -Path (Join-Path $Package '*') -Destination $destination -Recurse -Force
# Existing private config and all author records survive updates.
$configPath = Join-Path $privateDirectory 'config.json'
if (!(Test-Path -LiteralPath $configPath)) {
    @{schema=1;projects=@{handbook=$Handbook;guide=$Guide}} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $configPath -Encoding utf8
}
New-Item -Path "$registry\shell\open\command" -Force | Out-Null
Set-Item -LiteralPath $registry -Value 'URL:PsychAI Author Workbench'
New-ItemProperty -LiteralPath $registry -Name 'URL Protocol' -Value '' -PropertyType String -Force | Out-Null
Set-Item -LiteralPath "$registry\shell\open\command" -Value $expectedCommand
$shortcutShell = New-Object -ComObject WScript.Shell
$shortcutPaths = @(
    (Join-Path ([Environment]::GetFolderPath('Desktop')) '心理学 AI 手册·作者工作台.lnk'),
    (Join-Path ([Environment]::GetFolderPath('Programs')) '心理学 AI 手册·作者工作台.lnk')
)
foreach ($path in $shortcutPaths) {
    $shortcut = $shortcutShell.CreateShortcut($path)
    $shortcut.TargetPath = $executable
    $shortcut.WorkingDirectory = $destination
    $shortcut.Description = '直接编辑、私人批注与下一轮待合并草稿'
    $shortcut.Save()
}
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'README.md') -Destination (Join-Path $destination '使用说明.md') -Force
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'uninstall.ps1') -Destination (Join-Path $destination 'uninstall.ps1') -Force
@{version='0.1.0';installed=(Get-Date).ToString('o');directory=$destination;shortcuts=$shortcutPaths;privateDirectory=$privateDirectory} |
    ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $destination 'installation.json') -Encoding utf8
Write-Output "已安装：$executable"
Write-Output "私人记录：$privateDirectory"
Write-Output '桌面和开始菜单入口已就绪。'
