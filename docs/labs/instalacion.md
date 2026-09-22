# Instalación del entorno

Todos los labs se trabajan **en tu computadora**, con un único entorno
Python compartido (`labs/.venv`).

## Windows (recomendado: PowerShell, sin WSL)

1. Instala [Git para Windows](https://git-scm.com/download/win) (opciones por defecto).
2. En **PowerShell**:

    ```powershell
    cd $HOME
    git clone https://github.com/ia-estructuras-diplomado/curso-ia-web.git
    cd curso-ia-web
    powershell -ExecutionPolicy Bypass -File labs\setup.ps1
    ```

3. Abre un notebook:

    ```powershell
    cd labs\lab0
    ..\.venv\Scripts\jupyter.exe notebook fundamentos_python_ia.ipynb
    ```

Guía completa y solución de problemas:
[`labs/INSTALACION_WINDOWS.md`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/INSTALACION_WINDOWS.md).

## macOS / Linux

```bash
git clone https://github.com/ia-estructuras-diplomado/curso-ia-web.git
cd curso-ia-web
bash labs/setup.sh
source labs/.venv/bin/activate
```

## Labs 5 y 6 — Claude Code

Los Labs 5 y 6 no usan notebooks: se trabajan con **Claude Code** y
servidores MCP. La instalación está en la Parte 0 del [Lab 5](lab5.md).

!!! warning "Lab 6 = Windows nativo + ETABS"
    El Lab 6 conecta Claude Code con **ETABS 21+**, que solo corre en
    Windows. Instala Claude Code desde **PowerShell** en la misma PC donde
    está ETABS — no desde WSL2 ni macOS.

[← Laboratorios](index.md)
