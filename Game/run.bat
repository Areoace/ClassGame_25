@echo off
if not exist .venv (python -m venv .venv)
.\.venv\Scripts\activate.bat
python main.py
