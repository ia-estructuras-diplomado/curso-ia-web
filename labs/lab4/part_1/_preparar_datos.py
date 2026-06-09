"""Prepara subconjunto ligero del dataset Mendeley (grietas en hormigón).

- Si existe el RAR completo: extrae y muestrea 800 train + 200 val por clase.
- Si existe cracks_subset.zip: lo descomprime.
- Si cracks_subset/ ya está listo: no hace nada.
"""
from __future__ import annotations

import random
import shutil
import subprocess
import zipfile
from pathlib import Path

DIR = Path(__file__).parent
DATA = DIR / "data"
RAR = DATA / "Concrete Crack Images for Classification.rar"
SUBSET = DATA / "cracks_subset"
ZIP = DATA / "cracks_subset.zip"
TOOLS_UNRAR = DIR / "tools" / "unrar" / "unrar"

CLASSES = ("Negative", "Positive")
TRAIN_PER_CLASS = 800
VAL_PER_CLASS = 200
SAMPLES_PER_CLASS = TRAIN_PER_CLASS + VAL_PER_CLASS
SEED = 42


def find_unrar() -> str | None:
    for candidate in (
        shutil.which("unrar"),
        shutil.which("unar"),
        str(TOOLS_UNRAR) if TOOLS_UNRAR.is_file() else None,
    ):
        if candidate and Path(candidate).is_file():
            return candidate
    return None


def list_rar_images(unrar: str) -> dict[str, list[str]]:
    proc = subprocess.run(
        [unrar, "lb", str(RAR)],
        check=True,
        capture_output=True,
        text=True,
    )
    by_class: dict[str, list[str]] = {c: [] for c in CLASSES}
    for line in proc.stdout.splitlines():
        name = line.strip().replace("\\", "/")
        if not name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        for cls in CLASSES:
            prefix = f"{cls}/"
            if name.startswith(prefix):
                by_class[cls].append(name)
                break
    return by_class


def extract_files(unrar: str, names: list[str], dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    # unrar extrae conservando rutas relativas Positive/00001.jpg
    subprocess.run(
        [unrar, "x", "-o+", "-idq", str(RAR), *names, str(dest)],
        check=True,
    )


def build_subset_from_rar() -> None:
    unrar = find_unrar()
    if unrar is None:
        raise RuntimeError(
            "No se encontró unrar. En Codespaces usa cracks_subset.zip; "
            "en local instala unrar o compila labs/lab4/part_1/tools/unrar/unrar."
        )
    if not RAR.is_file():
        raise FileNotFoundError(f"No se encontró {RAR}")

    by_class = list_rar_images(unrar)
    for cls in CLASSES:
        n = len(by_class[cls])
        if n < SAMPLES_PER_CLASS:
            raise ValueError(f"Clase {cls}: solo {n} imágenes; se necesitan {SAMPLES_PER_CLASS}.")

    rng = random.Random(SEED)
    tmp = DATA / "_tmp_extract"
    if tmp.exists():
        shutil.rmtree(tmp)

    for cls in CLASSES:
        chosen = rng.sample(by_class[cls], SAMPLES_PER_CLASS)
        train_names = chosen[:TRAIN_PER_CLASS]
        val_names = chosen[TRAIN_PER_CLASS:]

        extract_files(unrar, train_names, tmp)
        for name in train_names:
            src = tmp / name
            dst = SUBSET / "train" / cls / src.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

        extract_files(unrar, val_names, tmp)
        for name in val_names:
            src = tmp / name
            dst = SUBSET / "val" / cls / src.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    if tmp.exists():
        shutil.rmtree(tmp, ignore_errors=True)

    print(
        f"✅ Subconjunto creado en {SUBSET} "
        f"({TRAIN_PER_CLASS} train + {VAL_PER_CLASS} val × {len(CLASSES)} clases)."
    )


def unzip_subset() -> None:
    if not ZIP.is_file():
        raise FileNotFoundError(
            f"No hay {ZIP} ni RAR para regenerar. Descarga el subconjunto del repo."
        )
    if SUBSET.exists():
        shutil.rmtree(SUBSET)
    with zipfile.ZipFile(ZIP, "r") as zf:
        zf.extractall(DATA)
    print(f"✅ Descomprimido {ZIP} → {SUBSET}")


def write_zip() -> None:
    if not SUBSET.is_dir():
        raise FileNotFoundError(f"No existe {SUBSET} para empaquetar.")
    if ZIP.is_file():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SUBSET.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(DATA))
    mb = ZIP.stat().st_size / (1024 * 1024)
    print(f"✅ Escrito {ZIP} ({mb:.1f} MB)")


def subset_ready() -> bool:
    for split in ("train", "val"):
        for cls in CLASSES:
            d = SUBSET / split / cls
            expected = TRAIN_PER_CLASS if split == "train" else VAL_PER_CLASS
            if not d.is_dir() or len(list(d.glob("*.jpg"))) != expected:
                return False
    return True


def main() -> None:
    if subset_ready():
        print(f"✅ {SUBSET} ya está listo.")
        return

    if RAR.is_file() and find_unrar():
        build_subset_from_rar()
        write_zip()
        return

    if ZIP.is_file():
        unzip_subset()
        if not subset_ready():
            raise RuntimeError("cracks_subset.zip incompleto tras descomprimir.")
        return

    raise FileNotFoundError(
        "Faltan datos: coloca cracks_subset.zip en data/ o el RAR completo con unrar."
    )


if __name__ == "__main__":
    main()
