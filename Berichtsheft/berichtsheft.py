import argparse
import configparser
import datetime as dt
from pathlib import Path

import requests

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

    csv_text = fetch_csv(cfg["sheet_csv_url"])

    # TODO: CSV parsen -> Mo-Fr aggregieren -> Excel-Maske befuellen (optional)
    # TODO: DOCX aus template erzeugen (Start/Enddatum + Tagespunkte + Stunden)

    # Platzhalter-Ausgabe, damit du siehst, dass alles wired ist:
    out_file = out_dir / f"Berichtsheft_{week_start.isoformat()}.docx"
    # TODO: echte docx schreiben
    out_file.write_bytes(b"")  # <- ersetzen

    print(f"OK: {out_file}")

if __name__ == "__main__":
    main()