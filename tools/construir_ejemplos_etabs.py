"""Construye los dos modelos de referencia del Lab 6 y los guarda en labs/lab6/ejemplos/.

Arranca su propia instancia de ETABS 21 (no se conecta a un ETABS ya abierto)
y la cierra al terminar. Requiere Windows, ETABS 21+ con licencia y comtypes:

    py -3 -m pip install comtypes
    py -3 tools/construir_ejemplos_etabs.py

Unidades del modelo: kN, m, C. El peso sísmico sale solo de los patrones de
carga (no de la masa de los elementos): PP×1 + CM×1 + CV×0.25.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ETABS_EXE = Path(r"C:\Program Files\Computers and Structures\ETABS 21\ETABS.exe")
OUT_DIR = Path(__file__).resolve().parents[1] / "labs" / "lab6" / "ejemplos"
KN_M = 6  # eUnits.kN_m_C
SHELL_THIN_ETABS21 = 1  # en ETABS 21.2, ShellType=0 deja el tipo vacío
XS = (0.0, 5.0, 10.0)
YS = (0.0, 5.0, 10.0)
VOID = ((5.0, 10.0), (5.0, 10.0))  # paño sin losa en el ejemplo irregular


def ret_of(value) -> int:
    if isinstance(value, (tuple, list)):
        return int(value[-1])
    return int(value)


def check(value, what: str):
    code = ret_of(value)
    if code != 0:
        raise RuntimeError(f"{what}: ret={code} raw={value!r}")
    return value


def start_etabs():
    import comtypes.client

    if not ETABS_EXE.is_file():
        raise SystemExit(f"No está ETABS en {ETABS_EXE}")
    helper = comtypes.client.CreateObject("ETABSv1.Helper")
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    etabs = helper.CreateObject(str(ETABS_EXE))
    check(etabs.ApplicationStart(), "ApplicationStart")
    return etabs


def stories_of(model) -> list[dict]:
    raw = model.Story.GetStories()
    names = list(raw[1])
    measured = []
    for name in names:
        elev = round(float(model.Story.GetElevation(name)[0]), 4)
        measured.append({"name": name, "elevation_m": elev})
    measured.sort(key=lambda row: row["elevation_m"])
    rows = []
    previous = 0.0
    for row in measured:
        if row["name"].lower() == "base" or row["elevation_m"] <= 0:
            continue
        rows.append(
            {
                "name": row["name"],
                "height_m": round(row["elevation_m"] - previous, 4),
                "elevation_m": row["elevation_m"],
                "z_bottom_m": round(previous, 4),
            }
        )
        previous = row["elevation_m"]
    return rows


def read_table(model, table: str) -> list[dict]:
    raw = model.DatabaseTables.GetTableForDisplayArray(table, [], "All", 0, [], 0, [])
    fields = [field for field in list(raw[2]) if field]
    n_rows = int(raw[3])
    flat = list(raw[4])
    if ret_of(raw) != 0 or not fields or n_rows == 0:
        return []
    width = len(fields)
    return [
        dict(zip(fields, flat[i * width : (i + 1) * width]))
        for i in range(n_rows)
    ]


def add_frame(model, x1, y1, z1, x2, y2, z2, section: str) -> None:
    # Name va antes de PropName. Pasar la sección en el puesto del nombre
    # deja el frame en la sección por defecto (acero W14X500).
    check(
        model.FrameObj.AddByCoord(x1, y1, z1, x2, y2, z2, "", section),
        f"frame {section} ({x1},{y1},{z1})-({x2},{y2},{z2})",
    )


def add_area(model, xs, ys, zs, section: str) -> str:
    created = check(
        model.AreaObj.AddByCoord(4, list(xs), list(ys), list(zs), "", section),
        f"area {section}",
    )
    names = [item for item in created[:-1] if isinstance(item, str)]
    if not names:
        raise RuntimeError(f"area sin nombre: {created!r}")
    return names[-1]


def define_common(model) -> None:
    check(model.SetPresentUnits(KN_M), "SetPresentUnits")
    check(model.PropMaterial.SetMaterial("C21", 2), "SetMaterial C21")
    check(model.PropMaterial.SetMPIsotropic("C21", 2.15e7, 0.2, 9.9e-6), "SetMPIsotropic")
    check(
        model.PropMaterial.SetOConcrete_1("C21", 21000.0, False, 0.0, 2, 1, 0.003, 0.005, -0.1),
        "SetOConcrete_1",
    )
    check(model.PropMaterial.SetWeightAndMass("C21", 1, 24.0), "SetWeightAndMass")
    check(model.PropFrame.SetRectangle("COL40X40", "C21", 0.40, 0.40), "COL40X40")
    check(model.PropFrame.SetRectangle("VIGA30X50", "C21", 0.50, 0.30), "VIGA30X50")
    # ETABS 21.2: ShellType=1 produce Shell-Thin. El 0 deja el tipo vacío.
    check(model.PropArea.SetSlab("LOSA15", 0, SHELL_THIN_ETABS21, "C21", 0.15), "LOSA15")
    check(model.LoadPatterns.Add("PP", 1, 1.0, True), "pattern PP")
    check(model.LoadPatterns.Add("CM", 2, 0.0, True), "pattern CM")
    check(model.LoadPatterns.Add("CV", 3, 0.0, True), "pattern CV")
    check(model.LoadPatterns.SetSelfWTMultiplier("PP", 1.0), "SW PP")
    check(model.LoadPatterns.SetSelfWTMultiplier("CM", 0.0), "SW CM")
    check(model.LoadPatterns.SetSelfWTMultiplier("CV", 0.0), "SW CV")
    # Opción 2: solo desde cargas. No sumar además la masa de los elementos.
    check(model.PropMaterial.SetMassSource(2, 3, ["PP", "CM", "CV"], [1.0, 1.0, 0.25]), "MassSource")
    check(model.LoadCases.ModalEigen.SetCase("Modal"), "Modal")
    check(model.LoadCases.ModalEigen.SetNumberModes("Modal", 12, 1), "NumberModes")


def draw(model, stories: list[dict], irregular: bool) -> dict:
    slab_names: list[str] = []
    for story in stories:
        z0 = story["z_bottom_m"]
        z1 = story["elevation_m"]
        for x in XS:
            for y in YS:
                add_frame(model, x, y, z0, x, y, z1, "COL40X40")
        for x0, x1 in zip(XS, XS[1:]):
            for y in YS:
                add_frame(model, x0, y, z1, x1, y, z1, "VIGA30X50")
        for y0, y1 in zip(YS, YS[1:]):
            for x in XS:
                add_frame(model, x, y0, z1, x, y1, z1, "VIGA30X50")
        for x0, x1 in zip(XS, XS[1:]):
            for y0, y1 in zip(YS, YS[1:]):
                if irregular and (x0, x1) == VOID[0] and (y0, y1) == VOID[1]:
                    continue
                slab_names.append(
                    add_area(
                        model,
                        [x0, x1, x1, x0],
                        [y0, y0, y1, y1],
                        [z1, z1, z1, z1],
                        "LOSA15",
                    )
                )
        if irregular:
            add_area(model, [0, 0, 0, 0], [0, 10, 10, 0], [z0, z0, z1, z1], "MURO20")
    for area in slab_names:
        # Dir 6 = Z global. Negativo = hacia abajo.
        check(model.AreaObj.SetLoadUniform(area, "CM", -3.0, 6), f"CM {area}")
        check(model.AreaObj.SetLoadUniform(area, "CV", -2.0, 6), f"CV {area}")

    points = model.PointObj.GetNameList()
    fixed = 0
    for point in list(points[1]):
        coord = model.PointObj.GetCoordCartesian(point)
        if abs(float(coord[2])) < 1e-6:
            check(
                model.PointObj.SetRestraint(point, [True, True, True, True, True, True]),
                f"restraint {point}",
            )
            fixed += 1

    # Un diafragma rígido por piso, solo en las losas de ese nivel.
    by_level: dict[float, list[str]] = {}
    for area in slab_names:
        points_of_area = model.AreaObj.GetPoints(area)
        # [n, (nombres,), ret]
        names = list(points_of_area[1])
        zs = [float(model.PointObj.GetCoordCartesian(point)[2]) for point in names]
        level = round(sum(zs) / len(zs), 4)
        by_level.setdefault(level, []).append(area)
    diaphragms = []
    existing = model.Diaphragm.GetNameList()
    existing_names = list(existing[1]) if existing[0] else []
    for index, level in enumerate(sorted(by_level), start=1):
        diaphragm = f"D{index}"
        if diaphragm not in existing_names:
            created = model.Diaphragm.SetDiaphragm(diaphragm, False)
            if ret_of(created) != 0:
                raise RuntimeError(
                    f"diaphragm {diaphragm}: ret={ret_of(created)} existentes={existing_names}"
                )
        for area in by_level[level]:
            check(model.AreaObj.SetDiaphragm(area, diaphragm), f"assign {diaphragm} {area}")
        diaphragms.append({"name": diaphragm, "elevation_m": level, "slabs": len(by_level[level])})

    frames = list(model.FrameObj.GetNameList()[1])
    sections: dict[str, int] = {}
    wrong = []
    for frame in frames:
        section = model.FrameObj.GetSection(frame)[0]
        sections[section] = sections.get(section, 0) + 1
        if section not in ("COL40X40", "VIGA30X50"):
            wrong.append(f"{frame}={section}")
    if wrong:
        raise RuntimeError(f"Frames fuera de sección: {wrong[:6]}")
    areas = list(model.AreaObj.GetNameList()[1])
    area_sections: dict[str, int] = {}
    for area in areas:
        prop = model.AreaObj.GetProperty(area)[0]
        area_sections[prop] = area_sections.get(prop, 0) + 1
    return {
        "base_points_fixed": fixed,
        "diaphragms": diaphragms,
        "slabs": len(slab_names),
        "frame_sections": sections,
        "area_sections": area_sections,
    }


def build_one(model, path: Path, irregular: bool) -> dict:
    check(model.InitializeNewModel(KN_M), "InitializeNewModel")
    # NumberLinesX/Y antes de SpacingX/Y: 3 líneas → 2 vanos de 5 m.
    check(model.File.NewGridOnly(3, 3.0, 3.0, 3, 3, 5.0, 5.0), "NewGridOnly")
    check(model.SetPresentUnits(KN_M), "SetPresentUnits after grid")
    define_common(model)
    if irregular:
        check(model.PropArea.SetWall("MURO20", 0, SHELL_THIN_ETABS21, "C21", 0.20), "MURO20")
    story_rows = stories_of(model)
    if len(story_rows) != 3 or any(abs(row["height_m"] - 3.0) > 0.01 for row in story_rows):
        raise RuntimeError(f"La grilla no quedó en 3 pisos de 3 m: {story_rows}")
    drawn = draw(model, story_rows, irregular)
    path.parent.mkdir(parents=True, exist_ok=True)
    check(model.File.Save(str(path)), f"Save {path.name}")
    check(model.Analyze.RunAnalysis(), f"RunAnalysis {path.name}")
    check(model.File.Save(str(path)), f"Save results {path.name}")
    mass = read_table(model, "Mass Source")
    slab = read_table(model, "Slab Property Definitions")
    patterns = read_table(model, "Load Pattern Definitions")
    return {
        "file": path.name,
        "irregular": irregular,
        "stories": story_rows,
        "drawn": drawn,
        "mass_source_table": mass,
        "slab_table": slab,
        "load_patterns": patterns,
        "get_slab_LOSA15": list(model.PropArea.GetSlab("LOSA15")),
        "get_mass_source": list(model.PropMaterial.GetMassSource()),
    }


def main() -> None:
    etabs = start_etabs()
    model = etabs.SapModel
    summary = []
    try:
        summary.append(build_one(model, OUT_DIR / "regular.edb", irregular=False))
        summary.append(build_one(model, OUT_DIR / "irregular.edb", irregular=True))
    finally:
        etabs.ApplicationExit(False)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
