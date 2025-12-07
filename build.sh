#!/bin/zsh

echo "🔧 Attivazione venv..."
source venv/bin/activate

echo "🧹 Pulizia build precedenti..."
rm -rf build dist tuttoCompreso.spec

echo "🚀 Generazione nuovo EXE..."

pyinstaller --onefile \
  --add-data "file/macro.xlsx:file" \
  --add-data "filePuliti:filePuliti" \
  --add-data "PagineHtml:PagineHtml" \
  --add-data "All:All" \
  --add-data "venv/lib/python3.9/site-packages/selenium_stealth/js:selenium_stealth/js" \
  tuttoCompreso.py

echo "✅ Compilazione completata!"
echo "📁 Il nuovo EXE è in: dist/tuttoCompreso"
