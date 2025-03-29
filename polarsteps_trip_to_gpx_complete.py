import json
import datetime

def json_to_single_gpx_sorted(json_file_path, output_file_path="all_locations_sorted.gpx"):
    """
    Konvertiert JSON-Datei mit Location-Daten in eine einzelne, nach Zeit sortierte GPX-Datei.

    Args:
        json_file_path (str): Pfad zur JSON-Datei.
        output_file_path (str): Pfad für die Ausgabedatei.
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

    locations = data['locations']
    locations.sort(key=lambda loc: loc['time'])  # Sortiere nach Zeit

    with open(output_file_path, 'w', encoding='utf-8') as gpx_file:
        gpx_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        gpx_file.write('<gpx version="1.1" creator="JSON to Single Sorted GPX Converter">\n')
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

    print(f"GPX-Datei erstellt (nach Zeit sortiert): {output_file_path}")

# Beispielaufruf (ersetze 'deine_locations.json' durch deinen Dateinamen)
json_to_single_gpx_sorted('../locations.json')