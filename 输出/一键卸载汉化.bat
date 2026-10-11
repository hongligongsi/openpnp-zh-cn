@echo off
chcp 65001 >nul
setlocal

rem ============================================================
rem  OpenPnP 简体中文汉化 — 卸载还原（恢复到官方原版）
rem ============================================================

set "PS1=%~dp0安装汉化.ps1"

if not exist "%PS1%" (
    echo [错误] 找不到 %PS1%
    pause
    exit /b 1
)

echo.
echo ============================================
echo   OpenPnP 汉化卸载 — 还原官方原版
echo ============================================
echo.
echo   将从 安装备份\ 目录还原原始 JAR。
echo   需要管理员权限，若弹出 UAC 请点「是」。
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "Start-Process powershell -Verb RunAs -Wait -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-NoExit','-File','\"%PS1%\"','-uninstall'"

echo.
echo 按任意键关闭本窗口。
pause >nul
endlocal
