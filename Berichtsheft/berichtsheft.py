import argparse
import csv
import configparser
import datetime as dt
from pathlib import Path

import requests
import re
import io

DAY_RE = re.compile(r"\.\s+\d{2}\.\d{2}\.")

TIME_RE = re.compile(r"^\d{2}:\d{2}$")

from datetime import datetime

def duration_hours(start_str, end_str):
    fmt = "%H:%M"
    start = datetime.strptime(start_str, fmt)
    end   = datetime.strptime(end_str, fmt)
    return (end - start).total_seconds() / 3600


def is_slot_row(row):
    if len(row) < 4:
        return False
    return bool(
        TIME_RE.match((row[2] or "").strip()) and
        TIME_RE.match((row[3] or "").strip())
    )

    return

def is_week_header(row):
    if len(row) < 9:
        return False

    cells = row[4:9]
    return all(DAY_RE.search((c or "").strip()) for c in cells)


def monday_of_week(date: dt.date) -> dt.date:
    return date - dt.timedelta(days=date.weekday())

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--template", required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()

def load_config(path: Path):
    cfg = configparser.ConfigParser()
    read_files = cfg.read(path, encoding="utf-8")

    if not read_files:
        raise FileNotFoundError(f"Config-Datei nicht gefunden/lesbar: {path.resolve()}")

    if "berichtsheft" not in cfg:
        raise KeyError(
            f"Sektion [berichtsheft] fehlt in {path.resolve()}.\n"
            f"Gefundene Sektionen: {cfg.sections()}"
        )

    sec = cfg["berichtsheft"]
    return {
        "sheet_csv_url": sec.get("sheet_csv_url", "").strip(),
        "week_mode": sec.get("week_mode", "current").strip(),
        "manual_week_start": sec.get("manual_week_start", "").strip(),
    }
    

def resolve_week_start(cfg) -> dt.date:
    today = dt.date.today()
    if cfg["week_mode"] == "next":
        return monday_of_week(today) + dt.timedelta(days=7)
    if cfg["week_mode"] == "manual" and cfg["manual_week_start"]:
        return dt.date.fromisoformat(cfg["manual_week_start"])
    return monday_of_week(today)

def fetch_csv(url: str) -> str:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text
    
def main():
    args = parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    cfg = load_config(Path(args.config))
    week_start = resolve_week_start(cfg)
    week_end = week_start + dt.timedelta(days=4)

    week = {}
    header = []
    slot = []

    csv_text = fetch_csv(cfg["sheet_csv_url"])  
    DATE_RE = re.compile(r"\d{2}\.\d{2}\.")
    

    csv_reader = csv.reader(io.StringIO(csv_text), delimiter=",")

    for row in csv_reader:

        if is_week_header(row):
            current_days = current_days = [re.findall(r"\d{2}\.\d{2}\.", cell)[0] for cell in row[4:9]]
            header.append(current_days)
        
        
        if is_slot_row(row):  
            slot.append(row[4:9])
            # print(duration_hours(row[2],row[3]))
        
    print(header)
    print(slot)



    # print(tuple(week))

    # TODO: CSV parsen -> Mo-Fr aggregieren -> Excel-Maske befuellen (optional)
    # TODO: DOCX aus template erzeugen (Start/Enddatum + Tagespunkte + Stunden)

    # Platzhalter-Ausgabe, damit du siehst, dass alles wired ist:
    out_file = out_dir / f"Berichtsheft_{week_start.isoformat()}.docx"
    # TODO: echte docx schreiben
    out_file.write_bytes(b"")  # <- ersetzen

    print(f"OK: {out_file}")

if __name__ == "__main__":
    main()