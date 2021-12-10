import sys
sys.path.append('.venv')
#sys.path.append('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Tesseract-OCR')
#yukaridaki satirlari eklemeden exe calismadi
import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--windowed',
  
])

#https://pyinstaller.readthedocs.io/en/latest/when-things-go-wrong.html?highlight=hidden%20import#listing-hidden-imports
#hidden imports kullanmak ne ise yariyor okumam lazim
#https://stackoverflow.com/questions/40716346/windows-pyinstaller-error-failed-to-execute-script-when-app-clicked
#https://pyinstaller.readthedocs.io/en/stable/usage.html
