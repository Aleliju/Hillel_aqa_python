from pathlib import Path
import json
import logging

path = Path('/Users/o.bogachenko/PycharmProjects/aqa4/Data_for_test/')
files = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler(path / 'json_Bogachenko.log')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

for file in files:
    with open(path / file, 'r', encoding='utf-8') as q:
        try:
            data = json.load(q)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error in {file}: {e}")
