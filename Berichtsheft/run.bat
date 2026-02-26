@echo off

setlocal EnableExtensions EnableDelayedExpansion

REM ====== KONFIG ======
set "WORKDIR=%~dp0work"
set "VENV=%WORKDIR%\venv"
set "PY=%VENV%\Scripts\python.exe"

set "SCRIPT=%~dp0berichtsheft.py"
set "REQ=%~dp0requirements.txt"

set "CONFIG=%~dp0config.ini"
set "EXPORT_DIR=%~dp0export"
set "TEMPLATE=%~dp0template.docx"

REM =====================

echo [1/6] Arbeitsordner vorbereiten...
if not exist "%WORKDIR%" mkdir "%WORKDIR%"
if not exist "%EXPORT_DIR%" mkdir "%EXPORT_DIR%"

echo [2/6] Python pruefen...
where python >nul 2>&1
if errorlevel 1 (
  echo FEHLER: Python wurde nicht gefunden.
  winget install -e --id Python.Python.3.14
)

echo [3/6] venv erstellen (falls noetig)...
if not exist "%VENV%" (
  python -m venv "%VENV%"
  if errorlevel 1 (
    echo FEHLER: venv konnte nicht erstellt werden.
    pause
    exit /b 1
  )
)

echo [4/6] Abhaengigkeiten installieren...
"%PY%" -m pip install --upgrade pip >nul
"%PY%" -m pip install -r "%REQ%"
if errorlevel 1 (
  echo FEHLER: pip install ist fehlgeschlagen.
  pause
  exit /b 1
)

echo [5/6] config.ini pruefen...
if not exist "%CONFIG%" (
  echo FEHLER: config.ini fehlt.
  echo Kopiere config.example.ini nach config.ini und trage deine CSV-URL ein.
  pause
  exit /b 1
)

echo [6/6] Berichtsheft erzeugen...
"%PY%" "%SCRIPT%" --config "%CONFIG%" --template "%TEMPLATE%" --out "%EXPORT_DIR%"
if errorlevel 1 (
  echo FEHLER: Script-Ausfuehrung fehlgeschlagen.
  pause
  exit /b 1
)

echo Fertig! Ausgabe liegt in: %EXPORT_DIR%
pause
exit /b 0
