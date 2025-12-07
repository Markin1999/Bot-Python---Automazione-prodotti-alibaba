#!/bin/zsh

echo "🔧 Attivazione venv..."
source venv/bin/activate

echo "🧹 Pulizia build precedenti..."
rm -rf build dist tuttoCompreso.spec

echo "🚀 Generazione nuovo EXE..."

pyinstaller --onefile \
  --add-data "file/macro.xlsx:file" \
  --add-data "TopAziende:TopAziende" \
  --add-data "PagineHtml:PagineHtml" \
  --add-data "All:All" \
  tuttoCompreso.py

echo "✅ Compilazione completata!"
echo "📁 Il nuovo EXE è in: dist/tuttoCompreso"
