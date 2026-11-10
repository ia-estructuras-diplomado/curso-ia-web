"""Create a searchable OCR copy of the scanned E.030 PDF.

The source PDF is left untouched.  Each source page is copied as-is and its
OCR text is embedded invisibly at the detected positions, so visual citations
continue to refer to the original page layout.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR


def add_ocr_layer(source: Path, output: Path, dpi: int, first: int, last: int | None, split_dir: Path | None) -> None:
    source_pdf = pymupdf.open(source)
    result_pdf = pymupdf.open()
    engine = RapidOCR()
    scale = dpi / 72

    last = min(last or len(source_pdf), len(source_pdf))
    for number in range(first, last + 1):
        page_output = split_dir / f"E030_{number:03}.pdf" if split_dir else None
        if page_output and page_output.exists():
            print(f"OCR ya existe: página {number}/{len(source_pdf)}", flush=True)
            continue
        source_page = source_pdf[number - 1]
        page_pdf = pymupdf.open()
        page_pdf.insert_pdf(source_pdf, from_page=number - 1, to_page=number - 1)
        target_page = page_pdf[-1]
        pixmap = source_page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
        recognized, _elapsed = engine(pixmap.tobytes("png"))

        if recognized:
            for polygon, text, confidence in recognized:
                if confidence < 0.35 or not text.strip():
                    continue
                xs = [point[0] / scale for point in polygon]
                ys = [point[1] / scale for point in polygon]
                # render_mode=3 writes invisible text, preserving the scan visually.
                target_page.insert_text(
                    pymupdf.Point(min(xs), max(ys)),
                    text.strip(),
                    fontsize=3,
                    fontname="helv",
                    render_mode=3,
                    overlay=True,
                )

        if page_output:
            page_output.parent.mkdir(parents=True, exist_ok=True)
            page_pdf.save(page_output, garbage=4, deflate=True)
        else:
            result_pdf.insert_pdf(page_pdf)
        page_pdf.close()
        print(f"OCR completado: página {number}/{len(source_pdf)}", flush=True)

    if not split_dir:
        output.parent.mkdir(parents=True, exist_ok=True)
        result_pdf.save(output, garbage=4, deflate=True)
    source_pdf.close()
    result_pdf.close()


def merge_pages(parts_dir: Path, output: Path) -> None:
    pages = sorted(parts_dir.glob("E030_*.pdf"))
    if len(pages) != 68:
        raise SystemExit(f"Faltan páginas OCR: hay {len(pages)} de 68 en {parts_dir}")
    merged = pymupdf.open()
    for page_file in pages:
        part = pymupdf.open(page_file)
        merged.insert_pdf(part)
        part.close()
    output.parent.mkdir(parents=True, exist_ok=True)
    merged.save(output, garbage=4, deflate=True)
    merged.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--first", type=int, default=1, help="Primera página, base 1")
    parser.add_argument("--last", type=int, help="Última página, inclusive")
    parser.add_argument("--split-dir", type=Path, help="Carpeta de páginas OCR reanudables")
    parser.add_argument("--merge-from", type=Path, help="Une las páginas OCR ya procesadas")
    args = parser.parse_args()
    if args.merge_from:
        merge_pages(args.merge_from, args.output)
    else:
        add_ocr_layer(args.source, args.output, args.dpi, args.first, args.last, args.split_dir)


if __name__ == "__main__":
    main()
