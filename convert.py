import json
from pathlib import Path
from os import listdir
import re

BASE_DIR = Path(__file__).resolve().parent
PLAYLIST_SYMBOLS_PATH = BASE_DIR / 'ya-music-playlist'
ALL_SYMBOLS = {}
RE_PATH = re.compile(r' d="(.*?)"')
files = list(filter(lambda x: x.endswith(".svg"), sorted(listdir(PLAYLIST_SYMBOLS_PATH))))
files_length = len(files)

i = 0
for symbol_file in files:
    i += 1
    symbol_name = symbol_file.rstrip('.svg')
    print(f'\r{i:4}/{files_length:4}: {symbol_name}', end='')
    symbol_file_path = PLAYLIST_SYMBOLS_PATH / symbol_file
    try:
        symbol_path_d = RE_PATH.findall(symbol_file_path.read_text())
    except UnicodeDecodeError as err:
        print(symbol_file_path)
        raise err
    try:
        ALL_SYMBOLS[symbol_name] = str(symbol_path_d[0])
    except Exception as err:
        print(f'\n\n{symbol_file_path}')
        raise err

print('\rDone!')

with open(BASE_DIR / 'ya-music-playlist.json', 'w') as file:
    json.dump(ALL_SYMBOLS, file, indent=2)

with open(BASE_DIR / 'ya-music-playlist.min.json', 'w') as file:
    json.dump(ALL_SYMBOLS, file)

with open(BASE_DIR / 'ya-music-playlist.raw.js', 'r') as raw, \
    open(BASE_DIR / 'ya-music-playlist.js', 'w') as res:
    res.write(
        raw.read().replace(
            "require('./ya-music-playlist.min.json')",
            json.dumps(ALL_SYMBOLS)
        )
    )
