# OpenPnP 汉化替换脚本
# 用法：关闭 OpenPnP 后，在 PowerShell 中运行本脚本（需管理员权限）
# PowerShell: Start-Process powershell -Verb RunAs -ArgumentList "-File `"$PWD\替换汉化.ps1`""

$ErrorActionPreference = "Stop"

$InstallDir = "C:\Program Files\openpnp"
$JarName    = "openpnp-gui-0.0.1-alpha-SNAPSHOT.jar"
$JarPath    = Join-Path $InstallDir $JarName
$NewJar     = Join-Path $InstallDir "openpnp-gui-new.jar.tmp"
$NewFile    = "C:\Users\hongliwang\Desktop\open PNP\输出\translations_zh_CN.properties"
$BackupDir  = "C:\Users\hongliwang\Desktop\open PNP\备份"

Write-Host "=== OpenPnP 汉化替换 ===" -ForegroundColor Cyan

# 1. 检查 OpenPnP 是否在运行
$proc = Get-Process -Name "OpenPnP" -ErrorAction SilentlyContinue
if ($proc) {
    Write-Host "错误：OpenPnP 正在运行（PID $($proc.Id)），请先关闭它。" -ForegroundColor Red
    exit 1
}
Write-Host "[1/5] OpenPnP 未运行，可以继续" -ForegroundColor Green

# 2. 备份原始 jar
if (-not (Test-Path $BackupDir)) { New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null }
$BackupFile = Join-Path $BackupDir "$JarName.bak"
if (-not (Test-Path $BackupFile)) {
    Copy-Item $JarPath $BackupFile -Force
    Write-Host "[2/5] 已备份原始 jar 到 $BackupFile" -ForegroundColor Green
} else {
    Write-Host "[2/5] 备份已存在，跳过" -ForegroundColor Yellow
}

# 3. 构建新 jar（若 tmp 不存在则重新生成）
if (-not (Test-Path $NewJar)) {
    Write-Host "[3/5] 临时 jar 不存在，正在重新生成..." -ForegroundColor Yellow
    $py = "C:\Users\hongliwang\.workbuddy\binaries\python\versions\3.13.12\python.exe"
    $code = @"
import zipfile, os
SRC = r'$JarPath'
TMP = r'$NewJar'
TARGET = 'org/openpnp/translations_zh_CN.properties'
NEWFILE = r'$NewFile'
newdata = open(NEWFILE,'rb').read()
zin = zipfile.ZipFile(SRC,'r')
zout = zipfile.ZipFile(TMP,'w',zipfile.ZIP_DEFLATED)
for item in zin.infolist():
    data = zin.read(item.filename)
    if item.filename == TARGET:
        data = newdata
    zi = zipfile.ZipInfo(item.filename, date_time=item.date_time)
    zi.compress_type = item.compress_type
    zi.external_attr = item.external_attr
    zi.internal_attr = item.internal_attr
    zi.create_system = item.create_system
    zout.writestr(zi, data)
zout.close(); zin.close()
print('OK')
"@
    $code | Out-File -FilePath "$env:TEMP\build_openpnp_jar.py" -Encoding UTF8
    & $py "$env:TEMP\build_openpnp_jar.py"
} else {
    Write-Host "[3/5] 临时 jar 已就绪" -ForegroundColor Green
}

# 4. 替换
Copy-Item $NewJar $JarPath -Force
Write-Host "[4/5] 已替换 $JarName" -ForegroundColor Green

# 5. 校验
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($JarPath)
$entry = $zip.Entries | Where-Object { $_.FullName -eq "org/openpnp/translations_zh_CN.properties" }
Write-Host "[5/5] 校验：条目大小 $($entry.Length) 字节（预期 240251）" -ForegroundColor Green
$zip.Dispose()

Remove-Item $NewJar -Force -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "完成！启动 OpenPnP，在菜单 Language 中选择 Chinese (Simplified)" -ForegroundColor Cyan
