# Stack ML CPU compartido por labs/lab4 (CNN + LSTM) y labs/lab5 (embeddings/RAG) - Windows / PowerShell
# Idempotente - tambien sirve como script de reparacion: si torch/torchvision
# fallan o ves un error de SymInt, simplemente vuelve a ejecutar:
#   powershell -ExecutionPolicy Bypass -File labs\_install_torch_cpu.ps1

$ErrorActionPreference = "Stop"

$LabsDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Py = Join-Path $LabsDir ".venv\Scripts\python.exe"
$TorchCpuIndex = "https://download.pytorch.org/whl/cpu"
$TorchVersion = "2.5.1"
$TorchvisionVersion = "0.20.1"

if (-not (Test-Path $Py)) {
    Write-Host "[ERROR] No existe labs\.venv - ejecuta primero: powershell -ExecutionPolicy Bypass -File labs\setup.ps1" -ForegroundColor Red
    exit 1
}

Write-Host "-> sentence-transformers / transformers (Lab 5)..."
uv pip install --python $Py "sentence-transformers>=3.0.0,<4.0.0" "transformers>=4.41.0,<4.48.0"

Write-Host "-> Stack PyTorch CPU compartido (Labs 4-5): torch==$TorchVersion + torchvision==$TorchvisionVersion"
uv pip install --python $Py "torch==$TorchVersion" "torchvision==$TorchvisionVersion" --index-url $TorchCpuIndex --force-reinstall

Write-Host "-> Verificando imports compartidos..."
$checkScript = @"
import torch
import torchvision
from sentence_transformers import SentenceTransformer
assert hasattr(torch, 'SymInt'), 'torch sin SymInt - revisa el venv'
print('OK torch', torch.__version__, '| torchvision', torchvision.__version__, '| sentence-transformers OK')
"@
& $Py -c $checkScript
