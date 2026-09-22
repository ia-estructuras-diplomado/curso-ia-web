# Entorno virtual centralizado para todos los labs (lab0, lab1, ...) - Windows / PowerShell
# Equivalente nativo de labs/setup.sh (para Linux/macOS).
# Uso:
#   powershell -ExecutionPolicy Bypass -File labs\setup.ps1

$ErrorActionPreference = "Stop"

$LabsDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $LabsDir
$PythonVersion = "3.12"

if (-not (Test-Path "requirements.txt")) {
    Write-Host "[ERROR] No se encontro labs\requirements.txt" -ForegroundColor Red
    exit 1
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "-> Instalando uv (instalador oficial de astral.sh)..."
    powershell -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
    $env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "[ERROR] uv no esta disponible ni se pudo instalar. Instalalo manualmente: https://astral.sh/uv" -ForegroundColor Red
    exit 1
}

Write-Host "-> uv: fijando interprete Python $PythonVersion"
uv python install $PythonVersion

$VenvPython = Join-Path $LabsDir ".venv\Scripts\python.exe"
if (Test-Path ".venv") {
    $VenvMinor = & $VenvPython -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null
    if ($VenvMinor -ne $PythonVersion) {
        Write-Host "-> Recreando labs\.venv ($VenvMinor -> $PythonVersion)"
        Remove-Item -Recurse -Force ".venv"
    }
}
if (-not (Test-Path ".venv")) {
    uv venv .venv --python $PythonVersion
}

Write-Host "-> Dependencias base (requirements.txt)..."
uv pip install --python $VenvPython -r requirements.txt

Write-Host "-> Stack ML CPU compartido (Lab 4 + Lab 5)..."
& (Join-Path $LabsDir "_install_torch_cpu.ps1")

Write-Host ""
Write-Host "[OK] Entorno centralizado listo (un solo labs\.venv, Python $PythonVersion, para todos los labs)." -ForegroundColor Green
Write-Host "   Activar:  .venv\Scripts\Activate.ps1"
Write-Host "   Jupyter:  cd labs\lab0; ..\.venv\Scripts\jupyter.exe notebook fundamentos_python_ia.ipynb"
