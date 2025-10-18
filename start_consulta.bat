@echo off
cd /d "%~dp0"
if exist venv\Scripts\activate (
    call venv\Scripts\activate
) else (
    echo Ambiente virtual nao encontrado! Crie um com: python -m venv venv
    pause
    exit /b
)
python app.py
pause
