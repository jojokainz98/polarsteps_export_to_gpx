import json
import datetime
import os

def json_to_gpx_sorted_by_day(json_file_path, output_dir="gpx_output_sorted"):
    """
    Konvertiert JSON-Datei in mehrere GPX-Dateien, eine pro Tag, sortiert nach Zeit.

    Args:
        json_file_path (str): Pfad zur JSON-Datei.
        output_dir (str): Name des Ausgabeverzeichnisses für GPX-Dateien.
    """

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Fehler: Datei '{json_file_path}' nicht gefunden.")
        return
    except json.JSONDecodeError:
        print(f"Fehler: Ungültiges JSON-Format in '{json_file_path}'.")
        return

    os.makedirs(output_dir, exist_ok=True)  # Ausgabeverzeichnis erstellen, falls nicht vorhanden

    locations_by_date = {}
    for location in data['locations']:
        timestamp = location['time']
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        if date not in locations_by_date:
            locations_by_date[date] = []
        locations_by_date[date].append(location)

    for date, locations in locations_by_date.items():
        locations.sort(key=lambda loc: loc['time'])  # Sortiere Standorte nach Zeit innerhalb des Tages

        gpx_file_path = os.path.join(output_dir, f"{date}.gpx")
        with open(gpx_file_path, 'w', encoding='utf-8') as gpx_file:
            gpx_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            gpx_file.write('<gpx version="1.1" creator="JSON to GPX Sorted by Day Converter">\n')
            gpx_file.write('  <trk>\n')
            gpx_file.write('    <trkseg>\n')

            for loc in locations:
                timestamp_str = datetime.datetime.fromtimestamp(loc['time']).strftime('%Y-%m-%dT%H:%M:%SZ')
                gpx_file.write(f'      <trkpt lat="{loc["lat"]}" lon="{loc["lon"]}">\n')
                gpx_file.write(f'        <time>{timestamp_str}</time>\n')
                gpx_file.write('      </trkpt>\n')

            gpx_file.write('    </trkseg>\n')
            gpx_file.write('  </trk>\n')
            gpx_file.write('</gpx>\n')

        print(f"GPX-Datei für {date} erstellt (nach Zeit sortiert): {gpx_file_path}")

# Beispielaufruf (ersetze 'deine_locations.json' durch deinen Dateinamen)
json_to_gpx_sorted_by_day('../locations.json')