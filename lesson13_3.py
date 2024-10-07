from pathlib import Path
import logging
import xml.etree.ElementTree as ET

path = Path('/Users/o.bogachenko/PycharmProjects/aqa4/Data_for_test/')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

tree = ET.parse(path / 'groups.xml')
root = tree.getroot()

for child in root:
    log_data = [child.tag, child.attrib]
    timing_exbytes = child.find("timingExbytes")
    if timing_exbytes is not None:
        for subchild in child:
            if subchild.tag == "timingExbytes":
                for subsubchild in subchild:
                    if subsubchild.tag == "incoming":
                        log_data.append(subsubchild.tag)
                        log_data.append(subsubchild.text)
    if len(log_data) > 2:
        logger.info(log_data)

