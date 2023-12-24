#!/usr/bin/python3
"""
log parsing 0x03
"""

import sys
import re


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[(.*?)\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                date_str, code, file_size = match.groups()

                # File size
                log["file_size"] += int(file_size)

                # status code
                if code.isdecimal():
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        pass
    finally:
        output(log)
