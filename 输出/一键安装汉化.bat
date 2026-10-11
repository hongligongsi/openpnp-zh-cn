@echo off
chcp 65001 >nul
setlocal

rem ============================================================
rem  OpenPnP 简体中文汉化 — 一键安装
rem  双击本文件即可（会自动请求管理员权限）
rem ============================================================

set "PS1=%~dp0安装汉化.ps1"

if not exist "%PS1%" (
    echo [错误] 找不到 %PS1%
    pause
    exit /b 1
)

echo.
echo ============================================
echo   OpenPnP 简体中文汉化 一键安装
echo ============================================
echo.
echo   即将安装汉化包到 C:\Program Files\openpnp
echo   安装前会自动备份原版（可随时卸载还原）
echo.
echo   需要管理员权限，若弹出 UAC 请点「是」。
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "Start-Process powershell -Verb RunAs -Wait -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-NoExit','-File','\"%PS1%\"','-install'"

echo.
echo 安装流程已结束。按任意键关闭本窗口。
pause >nul
endlocal
