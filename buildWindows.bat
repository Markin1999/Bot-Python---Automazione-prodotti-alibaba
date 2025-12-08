@echo off
REM --------------------------------------
REM Build script Windows per tuttoCompreso.py
REM --------------------------------------

echo 🔧 Controllo se venv esiste...
if not exist "venv\Scripts\activate.bat" (
    echo ❌ venv non trovato! Creo nuovo venv...
    python -m venv venv
)

echo 🔧 Attivazione venv...
call venv\Scripts\activate.bat

echo 🧹 Pulizia build precedenti...
if exist build rmdir /S /Q build
if exist dist rmdir /S /Q dist
if exist tuttoCompreso.spec del /Q tuttoCompreso.spec

echo 📦 Installazione dipendenze...
pip install --upgrade pip
pip install selenium pandas beautifulsoup4 openpyxl selenium-stealth pyinstaller

echo 🚀 Generazione nuovo EXE...
pyinstaller --onefile ^
  --add-data "file\macro.xlsx;file" ^
  --add-data "filePuliti;filePuliti" ^
  --add-data "PagineHtml;PagineHtml" ^
  --add-data "All;All" ^
  --add-data "venv\Lib\site-packages\selenium_stealth\js;selenium_stealth/js" ^
  tuttoCompreso.py

echo.
echo ✅ Compilazione completata!
echo 📁 Il nuovo EXE è in: dist\tuttoCompreso.exe
pause
