#requires -Version 5.1
<#
.SYNOPSIS
    OpenPnP 简体中文汉化 — 一键安装 / 卸载 / 校验脚本

.DESCRIPTION
    将本目录下 输出\class补丁\openpnp-gui-final.jar（含 properties + class 常量池
    两层汉化）安装到 OpenPnP 安装目录，替换 openpnp-gui-*.jar。

    功能：
      -install   安装汉化（自动备份原版）
      -uninstall 卸载，还原到官方原版
      -verify    只校验当前已安装 JAR 的 SHA256
      -status    显示当前状态（不修改任何文件）

.PARAMETER InstallDir
    OpenPnP 安装目录，默认 C:\Program Files\openpnp

.EXAMPLE
    # 以管理员身份运行
    powershell -ExecutionPolicy Bypass -File .\安装汉化.ps1 -install

.NOTES
    需要管理员权限（写入 Program Files）。
#>
[CmdletBinding(DefaultParameterSetName = 'Status')]
param(
    [Parameter(ParameterSetName = 'Install')]   [switch]$Install,
    [Parameter(ParameterSetName = 'Uninstall')] [switch]$Uninstall,
    [Parameter(ParameterSetName = 'Verify')]    [switch]$Verify,
    [Parameter(ParameterSetName = 'Status')]    [switch]$Status,
    [string]$InstallDir = 'C:\Program Files\openpnp',
    [switch]$Force      # 跳过 OpenPnP 运行检查（仅用于自动化测试）
)

$ErrorActionPreference = 'Stop'

# ---------- 常量 ----------
$ScriptDir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$SrcJar     = Join-Path $ScriptDir 'class补丁\openpnp-gui-final.jar'
$BackupDir  = Join-Path $ScriptDir '安装备份'
$JarPattern = 'openpnp-gui-*.jar'

# 期望的 SHA256（与 输出\class补丁\SHA256.txt 一致）
$ExpectSha  = '7b3cddfccd81da7c0bf82c50c3817b44eb412776544835e0cb62d9fd1fd2cc65'

function Write-Title($t) { Write-Host ''; Write-Host "=== $t ===" -ForegroundColor Cyan }
function Write-Ok($t)    { Write-Host "  [OK]   $t" -ForegroundColor Green }
function Write-Warn2($t) { Write-Host "  [警告] $t" -ForegroundColor Yellow }
function Write-Err($t)   { Write-Host "  [错误] $t" -ForegroundColor Red }

function Assert-Admin {
    $id = [Security.Principal.WindowsIdentity]::GetCurrent()
    $p  = New-Object Security.Principal.WindowsPrincipal($id)
    if (-not $p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Err '需要管理员权限。请右键 PowerShell → 以管理员身份运行，或：'
        Write-Host '         Start-Process powershell -Verb RunAs -ArgumentList "-ExecutionPolicy Bypass -File `"$PSCommandPath`" -install"'
        exit 1
    }
}

function Get-TargetJar {
    if (-not (Test-Path $InstallDir)) { throw "找不到安装目录：$InstallDir" }
    $jars = @(Get-ChildItem -Path $InstallDir -Filter $JarPattern -File -ErrorAction SilentlyContinue)
    if ($jars.Count -eq 0) { throw "安装目录中没有 $JarPattern" }
    # 排除我们自己的临时文件
    $jars = @($jars | Where-Object { $_.Name -notlike '*.tmp' })
    return $jars | Sort-Object Length -Descending | Select-Object -First 1
}

function Assert-NotRunning {
    if ($Force) { return }
    $proc = Get-Process -Name 'OpenPnP' -ErrorAction SilentlyContinue
    if ($proc) {
        Write-Err "OpenPnP 正在运行（PID $($proc.Id -join ',')），请先完全退出。"
        exit 1
    }
}

function Get-Sha256($path) {
    return (Get-FileHash -Path $path -Algorithm SHA256).Hash.ToLower()
}

# ============================================================
#  STATUS
# ============================================================
function Do-Status {
    Write-Title 'OpenPnP 汉化状态'
    Write-Host "  安装目录 : $InstallDir"

    try { $jar = Get-TargetJar } catch { Write-Err $_ ; return }
    if (-not $jar) { Write-Err '未找到目标 JAR'; return }

    Write-Host "  目标 JAR : $($jar.Name)"
    Write-Host "  当前大小 : $([math]::Round($jar.Length/1MB,2)) MB ($($jar.Length) 字节)"
    $sha = Get-Sha256 $jar.FullName
    Write-Host "  当前 SHA256: $sha"

    if ($sha -eq $ExpectSha) {
        Write-Ok '已安装汉化版（与发布版一致）'
    } else {
        $bak = Join-Path $BackupDir "$($jar.Name).bak"
        if ((Test-Path $bak) -and (Get-Sha256 $bak) -eq $sha) {
            Write-Warn2 '当前为官方原版（未汉化）'
        } else {
            Write-Warn2 '当前 JAR 与发布版 / 官方原版均不一致（可能被其他补丁修改过）'
        }
    }

    # 统计中文条目
    Write-Host ''
    Write-Host '  正在统计常量池中文条目…' -ForegroundColor DarkGray
    $py = Get-Python
    $counter = Join-Path $ScriptDir '统计中文条目.py'
    if ($py -and (Test-Path $counter)) {
        try {
            $cnt = & $py $counter $jar.FullName 2>$null
            if ($cnt) { Write-Host "  含中文常量池条目: $cnt" }
        } catch { }
    }
    Write-Host ''
}

function Get-Python {
    $cands = @(
        "$env:USERPROFILE\.workbuddy\binaries\python\versions\3.13.12\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe"
    )
    foreach ($c in $cands) { if (Test-Path $c) { return $c } }
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    return $null
}

# ============================================================
#  VERIFY
# ============================================================
function Do-Verify {
    Write-Title '校验已安装 JAR'
    try { $jar = Get-TargetJar } catch { Write-Err $_; exit 1 }
    $sha = Get-Sha256 $jar.FullName
    Write-Host "  文件 : $($jar.FullName)"
    Write-Host "  大小 : $($jar.Length) 字节"
    Write-Host "  SHA256: $sha"
    Write-Host ''
    if ($sha -eq $ExpectSha) {
        Write-Ok '与发布版 SHA256 完全一致'
        exit 0
    } else {
        Write-Err "与发布版不一致（期望 $ExpectSha）"
        exit 2
    }
}

# ============================================================
#  INSTALL
# ============================================================
function Do-Install {
    Assert-Admin
    Write-Title 'OpenPnP 汉化安装'

    if (-not (Test-Path $SrcJar)) { Write-Err "找不到汉化 JAR：$SrcJar"; exit 1 }
    Assert-NotRunning
    Write-Ok 'OpenPnP 未在运行'

    $jar = Get-TargetJar
    Write-Host "  目标: $($jar.FullName)"

    # 1) 备份
    if (-not (Test-Path $BackupDir)) { New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null }
    $bak = Join-Path $BackupDir "$($jar.Name).bak"
    if (-not (Test-Path $bak)) {
        Copy-Item $jar.FullName $bak -Force
        Write-Ok "[1/4] 已备份原版 → $bak"
    } else {
        Write-Warn2 "[1/4] 备份已存在，跳过（$bak）"
    }

    # 2) 源 JAR 校验
    $srcSha = Get-Sha256 $SrcJar
    if ($srcSha -eq $ExpectSha) {
        Write-Ok "[2/4] 源 JAR SHA256 校验通过"
    } else {
        Write-Warn2 "[2/4] 源 JAR SHA256 与预期不符（实际 $srcSha）"
        $ans = Read-Host '        仍要继续安装吗？(y/N)'
        if ($ans -notmatch '^[yY]') { Write-Host '已取消'; exit 0 }
    }

    # 3) 复制
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $stage = Join-Path $InstallDir "openpnp-gui-$stamp.new"
    Copy-Item $SrcJar $stage -Force
    Copy-Item $stage $jar.FullName -Force
    Remove-Item $stage -Force -ErrorAction SilentlyContinue
    Write-Ok "[3/4] 已替换 $($jar.Name)"

    # 4) 回读校验
    $nowSha = Get-Sha256 $jar.FullName
    if ($nowSha -eq $srcSha) {
        Write-Ok "[4/4] 安装后 SHA256 校验一致"
    } else {
        Write-Err "[4/4] 安装后校验失败！正在回滚…"
        Copy-Item $bak $jar.FullName -Force
        Write-Warn2 '已回滚到备份版本'
        exit 3
    }

    Write-Host ''
    Write-Host '  安装完成！' -ForegroundColor Green
    Write-Host '  启动 OpenPnP 即可看到中文界面。' -ForegroundColor Gray
    Write-Host '  （若界面仍为英文，请检查菜单 Language → Chinese (Simplified)）' -ForegroundColor DarkGray
    Write-Host ''
}

# ============================================================
#  UNINSTALL
# ============================================================
function Do-Uninstall {
    Assert-Admin
    Write-Title 'OpenPnP 汉化卸载'
    Assert-NotRunning
    Write-Ok 'OpenPnP 未在运行'

    $jar = Get-TargetJar
    $bak = Join-Path $BackupDir "$($jar.Name).bak"
    if (-not (Test-Path $bak)) {
        Write-Err "找不到备份：$bak"
        Write-Host '        无法自动还原。可从 备份\ 目录手动复制官方原版。'
        exit 1
    }

    Copy-Item $bak $jar.FullName -Force
    Write-Ok "已还原为官方原版（来自 $bak）"
    Write-Host "  还原后 SHA256: $(Get-Sha256 $jar.FullName)"
    Write-Host ''
}

# ============================================================
#  入口
# ============================================================
switch ($PSCmdlet.ParameterSetName) {
    'Install'   { Do-Install }
    'Uninstall' { Do-Uninstall }
    'Verify'    { Do-Verify }
    default     { Do-Status }
}
