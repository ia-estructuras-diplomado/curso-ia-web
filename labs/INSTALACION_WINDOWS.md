# Instalar el entorno del curso en Windows

Todo se instala directamente desde **PowerShell**, sin necesidad de WSL ni
máquinas virtuales. Hay un script (`labs/setup.ps1`) que hace lo mismo que
`labs/setup.sh` hace en Linux/macOS, adaptado a herramientas nativas de
Windows.

## 1. Instalar Git para Windows (si no lo tienes)

Descarga e instala desde [git-scm.com/download/win](https://git-scm.com/download/win)
(acepta las opciones por defecto del instalador).

## 2. Clonar el repositorio del curso

Abre **PowerShell** (no hace falta modo administrador) y escribe:

```powershell
cd $HOME
git clone https://github.com/ia-estructuras-diplomado/curso-ia-web.git
cd curso-ia-web
```

## 3. Ejecutar el instalador del curso

```powershell
powershell -ExecutionPolicy Bypass -File labs\setup.ps1
```

> El parámetro `-ExecutionPolicy Bypass` solo aplica a esta ejecución (no
> cambia ninguna configuración permanente de tu sistema) — es necesario
> porque Windows bloquea scripts `.ps1` por defecto.

Esto hace todo automáticamente:

- Instala [`uv`](https://astral.sh/uv) (gestor de Python) si falta.
- Descarga Python 3.12 y crea el entorno virtual en `labs\.venv`.
- Instala todas las dependencias (`labs\requirements.txt`).
- Instala PyTorch CPU (para los labs de CNN/LSTM y embeddings).

Los Labs 5 y 6 usan además **Claude Code** (se instala aparte, ver la
Parte 0 de [`lab5/README.md`](lab5/README.md)).

## 4. Abrir un notebook

Sin necesidad de "activar" el entorno, puedes llamar directamente al
Jupyter del venv:

```powershell
cd labs\lab0
..\.venv\Scripts\jupyter.exe notebook fundamentos_python_ia.ipynb
```

Esto abre Jupyter en tu navegador.

Si prefieres activar el entorno (para no escribir la ruta completa cada vez):

```powershell
labs\.venv\Scripts\Activate.ps1
```

> 💡 **Tip:** también puedes abrir la carpeta `curso-ia-web` en **VS Code**
> e instalar la extensión "Jupyter" — selecciona como intérprete
> `labs\.venv\Scripts\python.exe` y ejecuta los notebooks directamente ahí.

## Si algo falla

| Problema | Solución |
|---|---|
| Falta `torchvision` o error `SymInt` | `powershell -ExecutionPolicy Bypass -File labs\_install_torch_cpu.ps1` |
| El entorno quedó roto | `Remove-Item -Recurse -Force labs\.venv` y vuelve a correr `labs\setup.ps1` |

## Alternativa: WSL2 (solo Labs 0-5)

Si el flujo de PowerShell no funciona en tu máquina (antivirus corporativo
bloqueando scripts, política de grupo restrictiva, etc.), puedes instalar
WSL2 (`wsl --install` desde PowerShell como administrador, requiere
reiniciar) y ahí usar `bash labs/setup.sh`.

> ⚠️ El **Lab 6 (ETABS)** no se puede hacer desde WSL2: ETABS y su servidor
> MCP son programas de Windows. Para ese lab necesitas Claude Code instalado
> en **Windows nativo** (PowerShell), en la misma PC donde está ETABS.
