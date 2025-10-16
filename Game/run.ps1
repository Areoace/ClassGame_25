# Run script for PowerShell: create venv (if missing) and run main.py
if (-not (Test-Path -Path .venv)) {
    python -m venv .venv
}
.\.venv\Scripts\Activate.ps1
python main.py
