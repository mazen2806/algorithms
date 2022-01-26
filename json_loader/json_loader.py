import json
import logging

from typing import Iterator
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class log:
    def __init__(self, each=5):
        self.each = each
        self.log_count = 0

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            value = f(*args, **kwargs)
            self.log_count += 1
            if self.log_count == self.each:
                self.log_count = 0
                logger.info(f'Function {f} was called with params {args}')
            return value
        return wrapper


def get_records_from_json() -> Iterator[dict]:
    with open("2gb_file.json") as fp:
        file_str = fp.readline()
        while file_str != ']':
            json_record = fp.readline()
            yield from process_json_record(json_record)


def process_json_record(s):
    len_s = len(s)
    if len_s > 1:
        obj_str = s[0:len_s - 2] if s.endswith(',\n') else s
        try:
            obj = json.loads(obj_str)
            yield from update_record_info(obj)
        except json.JSONDecodeError as err:
            logger.exception("Incorrect JSON record")


@log(each=2)
def update_record_info(obj):
    obj["date_read"] = datetime.utcnow()
    yield obj


if __name__ == '__main__':
    for row in get_records_from_json():
        print(row['date_read'])
